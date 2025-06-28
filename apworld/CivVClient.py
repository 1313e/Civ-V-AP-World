# %% IMPORTS
import traceback

import Utils
import asyncio
import socket
from .tuner import Tuner
from .items import CivVItemData
from typing import Dict

from CommonClient import ClientCommandProcessor, CommonContext, get_base_parser, logger, server_loop, gui_enabled
from NetUtils import ClientStatus
from .tuner import TunerErrorException, TunerRuntimeException, TunerConnectionException, TunerTimeoutException
from .constants import ADDRESS, GAME_NAME, GAME_READY, GAME_NOT_READY, ITEM_OFFSET, MOD_READY, MOD_NOT_READY, PORT


# %% GLOBALS
GAME_IS_READY: bool = False
"Bool indicating whether game is currently ready"
MOD_IS_READY: bool = False
"Bool indicating whether mod is currently ready"


# %% CLIENT CLASS DEFINITION
class CivVCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx: CommonContext):
        super().__init__(ctx)

class CivVContext(CommonContext):
    game = GAME_NAME
    items_handling = 0b111
    command_processor = CivVCommandProcessor
    tuner: Tuner
    firetuner_task = None
    processing_multiple_items = False
    item_id_to_civ_item: Dict[int, CivVItemData] = {}
    current_index = 0
    current_location_index = 0
    item_offset = ITEM_OFFSET
    logger = logger
    loc_list = []
    locations_to_send = []

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.tuner = Tuner(logger)

    async def server_auth(self, password_requested = False):
        if password_requested and not self.password:
            await super(CivVContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def run_gui(self):
        from kvui import GameManager

        class CivVManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = f"Archipelago {GAME_NAME} Client"
        self.ui = CivVManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            self.slot_data = args["slot_data"]
            logger.info("Connected:")

async def firetuner_task(ctx: CivVContext):
    while True:
        if ctx.exit_event.is_set():
            break

        if not ctx.slot:
            await asyncio.sleep(3)
            continue

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        loop = asyncio.get_event_loop()
        try:
            await loop.sock_connect(sock, (ADDRESS, PORT))
            sock.setblocking(False)
        except ConnectionRefusedError:
            log_game_ready(False)
            await asyncio.sleep(3)
            continue

        while not ctx.exit_event.is_set():
            try:
                if not ctx.slot:
                    continue
                if not GAME_IS_READY and not await game_is_ready(ctx, sock, loop):
                    continue
                if await mod_is_ready(ctx, sock, loop):
                    if not ctx.processing_multiple_items:
                        await perform_firetuner_step(ctx, sock, loop)
                elif not await game_is_ready(ctx, sock, loop):
                    continue
            except TunerConnectionException as e:
                logger.debug(str(e))
                break
            except Exception:
                logger.debug(traceback.format_exc())
            finally:
                await asyncio.sleep(3)
        sock.close()

async def game_is_ready(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop) -> bool:
    try:
        await ctx.tuner.send_init_command(sock, loop)
    except TunerTimeoutException:
        log_game_ready(False)
        return False
    else:
        log_game_ready(True)
        return True


async def mod_is_ready(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop) -> bool:
    try:
        ready = await ctx.tuner.send_command("ModIsReady()", sock, loop, size=1024*100) == "True"
    except (TunerRuntimeException, TunerTimeoutException):
        log_mod_ready(False)
        return False
    else:
        log_mod_ready(ready)
        return ready


def log_game_ready(ready: bool):
    global GAME_IS_READY
    if ready and not GAME_IS_READY:
        logger.info(GAME_READY)
        GAME_IS_READY = True
    elif not ready:
        GAME_IS_READY = False
        logger.info(GAME_NOT_READY)


def log_mod_ready(ready: bool):
    global MOD_IS_READY
    if ready and not MOD_IS_READY:
        logger.info(MOD_READY)
        MOD_IS_READY = True
    elif not ready:
        MOD_IS_READY = False
        logger.info(MOD_NOT_READY)

async def perform_firetuner_step(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    if ctx.server:
        await handle_checked_location(ctx, sock, loop)
        await handle_receive_items(ctx, sock, loop)
        await handle_goal_complete(ctx, sock, loop)

async def handle_receive_items(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    print("Executing: 'handle_receive_items'")
    try:
        if len(ctx.items_received) - ctx.current_index > 1:
            ctx.processing_multiple_items = True

        for index, network_item in enumerate(ctx.items_received):

            if index >= ctx.current_index:
                current_item = ctx.items_received[ctx.current_index]
                await ctx.tuner.send_command(f"AddTech({current_item[0] - ctx.item_offset + 81})", sock, loop)
                await asyncio.sleep(0.02)
                ctx.current_index += 1
            await asyncio.sleep(0.02)
        
    finally:
        ctx.processing_multiple_items = False
    print("Finishing: 'handle_receive_items'")


async def handle_checked_location(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    print("Executing: 'handle_checked_location'")
    result : str
    result = await ctx.tuner.send_command("GetItemsToSend()", sock, loop)
    result_list = result.split(",")
    for index in range(0, len(result_list)):
        location = result_list[index]
        if location == '0' or location == '':
            continue
        elif location == 'True' or location == 'False':
            continue
        elif location in ctx.loc_list:
            continue
        else:
            ctx.loc_list.append(location)

    for index in range(0, len(ctx.loc_list)):
        if index >= ctx.current_location_index:
            loc = int(ctx.loc_list[index])
            if loc == False:
                loc = 1
            ctx.locations_to_send.append(loc + ctx.item_offset)
            await ctx.send_msgs([{"cmd": "LocationChecks", "locations": ctx.locations_to_send}])
            ctx.current_location_index += 1
    print("Finishing: 'handle_checked_location'")


async def handle_goal_complete(ctx: CivVContext, sock: socket.socket, loop: asyncio.AbstractEventLoop):
    print("Executing: 'handle_goal_complete'")
    goal_complete = await ctx.tuner.send_command("IsVictory()", sock, loop)
    if goal_complete == "True":
        await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
    print("Finishing: 'handle_goal_complete'")

def main(connect=None, password=None, name=None):
    Utils.init_logging(f"{GAME_NAME} Client")
    

    async def _main(connect, password, name):
        ctx = CivVContext(connect, password)
        ctx.auth = name
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")
        
        if gui_enabled:
            ctx.run_gui()
        await asyncio.sleep(1)

    
        ctx.firetuner_task = asyncio.create_task(firetuner_task(ctx), name="FireTuner")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.shutdown()

        if ctx.firetuner_task:
            await asyncio.sleep(3)
            await ctx.firetuner_task

        print("I am done")

    import colorama

    colorama.init()
    asyncio.run(_main(connect, password, name))
    colorama.deinit()
    
    