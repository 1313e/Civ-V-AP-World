# %% IMPORTS
import asyncio
import functools
import traceback
import socket

import colorama

from CommonClient import gui_enabled, logger, server_loop
from NetUtils import ClientStatus
from Utils import init_logging

from .context import CivVContext
from .constants import ADDRESS, GAME_NAME, GAME_READY, GAME_NOT_READY, MOD_READY, MOD_NOT_READY, PORT
from .enums import CivVLocationType, CivVItemType
from .exceptions import TunerConnectionException
from .items import ITEMS_DATA_BY_ID
from .locations import LOCATIONS_DATA_BY_ID, LOCATIONS_DATA_BY_TYPE_ID
from .tuner import Tuner

# All declaration
__all__ = ["CivVClient"]


# %% CLIENT CLASS DEFINITION
class CivVClient:
    """
    Client class for Civ V AP.

    """

    def __init__(self, ctx: CivVContext):
        # Define instance attributes
        self.ctx: CivVContext = ctx
        "The Civ V context to use for this instance of AP"
        self.tuner: Tuner = Tuner()
        "Tuner instance to use for communicating with the game"

        # Define state variables
        self._game_is_ready: bool = False
        "Bool indicating whether game is currently ready"
        self._mod_is_ready: bool = False
        "Bool indicating whether AP mod is currently ready"

    @property
    def game_is_ready(self) -> bool:
        """
        Bool indicating whether game is currently ready

        """

        return self._game_is_ready

    @game_is_ready.setter
    def game_is_ready(self, ready: bool):
        # If the game is ready and was not ready before, store and send this to the client's console
        if ready and not self.game_is_ready:
            logger.info(GAME_READY)
            self._game_is_ready = True

        # If the game is not ready, store and send this to the client's console
        elif not ready:
            logger.info(GAME_NOT_READY)
            self._game_is_ready = False

    @property
    def mod_is_ready(self) -> bool:
        """
        Bool indicating whether AP mod is currently ready

        """

        return self._mod_is_ready

    @mod_is_ready.setter
    def mod_is_ready(self, ready: bool):
        # If the mod is ready and was not ready before, store and send this to the client's console
        if ready and not self.mod_is_ready:
            logger.info(MOD_READY)
            self._mod_is_ready = True

        # If the mod is not ready, store and send this to the client's console
        elif not ready:
            logger.info(MOD_NOT_READY)
            self._mod_is_ready = False

    @staticmethod
    def update_func(func):
        """
        Simple decorator that marks the given `func` as an update cycle function.

        """

        function_name: str = func.__name__

        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            logger.debug(f"Executing: {function_name}")
            result = await func(*args, **kwargs)
            logger.debug(f"Finished: {function_name}")
            return result

        return wrapper

    @classmethod
    def run_client(cls):
        """
        Creates a new instance of this client with associated context, and runs it.

        Automatically cleans up used resources once the client exits.

        """

        # Log that we are setting up the client
        init_logging(f"{GAME_NAME} Client")

        # Define async function to execute in a coroutine
        async def _main():
            """
            Runs the client asynchronously in a spawn task until it exits.

            """

            # Create context and add it as a task to the AP server loop
            ctx = CivVContext()
            ctx.server_task = asyncio.create_task(server_loop(ctx), name="ServerLoop")

            # Run the GUI for the client if GUIs are enabled
            if gui_enabled:
                ctx.run_gui()
            await asyncio.sleep(1)

            # Create client and add it as a task
            ctx.client_task = asyncio.create_task(cls(ctx).run(), name="CivVClient")

            # Wait until the context has given the exit signal
            await ctx.exit_event.wait()

            # Wait until the context has shut down completely
            ctx.server_address = None
            await ctx.shutdown()

            # Wait until the client has also shut down completely
            if ctx.client_task:
                await asyncio.sleep(3)
                await ctx.client_task

        # Execute the coroutine
        colorama.init()
        asyncio.run(_main())
        colorama.deinit()

    async def run(self) -> None:
        """
        Runs this client until an exit signal is received from the context.

        """

        # Run this client indefinitely
        while True:
            # If the context has given the exit signal, exit the loop
            if self.ctx.exit_event.is_set():
                break

            # If the context has not provided us with a slot yet, try again later
            if not self.ctx.slot:
                await asyncio.sleep(3)
                continue

            # Try to set up a socket connection for the Tuner
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                await asyncio.get_event_loop().sock_connect(sock, (ADDRESS, PORT))

            # If the connection cannot be set up, try again later. This also means that the game is not ready
            except ConnectionRefusedError:
                self.game_is_ready = False
                await asyncio.sleep(3)
                continue

            # Make sure the socket is not blocking and set it on the Tuner
            sock.setblocking(False)
            self.tuner.sock = sock

            # Start running the game update loop
            await self.run_update_loop()

            # If the game update loop ended, properly close the socket such that we can set it up again in the outer
            # loop
            sock.close()

    async def run_update_loop(self) -> None:
        """
        Runs the loop required for keeping Civ V updated with changes in the multiworld.

        This loop ends when either an exit signal is received from the context or when the connection to the game is
        lost.

        """

        # Perform game updates while a proper connection has been established
        while not self.ctx.exit_event.is_set():
            # Try to perform a game update cycle
            try:
                # If the client has lost connection to the slot, try again later
                if not self.ctx.slot:
                    continue

                # If the game is currently not ready to receive any commands, try again later
                if not self.game_is_ready and not await self.check_game_ready():
                    continue

                # If the AP mod is ready, perform a game update cycle
                if await self.check_mod_ready():
                    await self.perform_update_cycle()

                # If the AP mod was not ready, Make sure the game itself still is
                else:
                    _ = await self.check_game_ready()
                    await asyncio.sleep(4)

            # If we lost connection to the game at any point, break out of the game update loop to set it up again
            except TunerConnectionException as e:
                logger.debug(str(e))
                break

            # If any other exception occurred, we simply log the entire traceback and keep going
            except Exception:
                logger.debug(traceback.format_exc())

            # Wait a bit before performing the next update cycle
            finally:
                await asyncio.sleep(1)

    async def check_game_ready(self) -> bool:
        """
        Checks whether the game is currently ready and returns the result.

        """

        # Send ready check to the game and return the result
        self.game_is_ready = await self.tuner.send_ready_check()
        return self.game_is_ready

    async def check_mod_ready(self) -> bool:
        """
        Checks whether the AP mod is currently loaded and ready, and returns the result.

        """

        # Send mod ready check to the game and return the result
        self.mod_is_ready = await self.tuner.is_mod_ready()
        return self.mod_is_ready

    async def perform_update_cycle(self) -> None:
        """
        Performs a game update cycle.

        """

        # If a connection to the server is currently established, perform an update cycle
        if self.ctx.server:
            # Process checked locations and received items
            await self.process_push_table()
            await self.process_received_items()

    @update_func
    async def process_push_table(self) -> None:
        """
        Processes requests pushed by the APMod to the client and acts upon them.

        """

        # Retrieve the push table and process its contents
        for key, value in (await self.tuner.get_push_table()).items():
            match key:
                # If a full game sync was requested
                case "sync":
                    # Grant all checked locations as items
                    await self.tuner.grant_technologies(
                        *(LOCATIONS_DATA_BY_ID[x].game_id for x in self.ctx.checked_locations))
                    self.ctx.sent_locations[CivVLocationType.tech].update(self.ctx.checked_locations)

                    # Reset received_items to resend all items received
                    self.ctx.received_item_ids.clear()

                # If victory was achieved
                case "victory":
                    # Send message that player has goaled their game
                    await self.ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    self.ctx.has_achieved_victory = True

                # All other cases are location types
                case _:
                    # Send the locations of this location type that have not been sent yet
                    locations_to_send = set(value).difference(self.ctx.sent_locations[key])
                    await self.ctx.send_msgs(
                        [{"cmd": "LocationChecks",
                          "locations": [LOCATIONS_DATA_BY_TYPE_ID[(key, x)].ap_id for x in locations_to_send]},
                         ]
                    )
                    self.ctx.sent_locations[key].update(locations_to_send)

    @update_func
    async def process_received_items(self) -> None:
        """
        Processes items that have been received by the player from the multiworld and grants them to the player.

        """

        # Grant all items that have not been received by the player yet
        techs_to_send = []
        items_ids_to_receive = [x.item for x in self.ctx.items_received[len(self.ctx.received_item_ids):]]
        for id_to_receive in items_ids_to_receive:
            # Retrieve the data on this item
            item = ITEMS_DATA_BY_ID[id_to_receive]

            # Retrieve the ID to send to the player according to its item type
            match item.type:
                case CivVItemType.tech | CivVItemType.era:
                    techs_to_send.append(item.game_ids[self.ctx.received_item_ids.count(id_to_receive)])

            # Add ID to list of received IDs to account for multiple progressive items being sent at once
            self.ctx.received_item_ids.append(id_to_receive)

        # Grant all techs at once, as it is far more efficient
        if techs_to_send:
            await self.tuner.grant_technologies(*techs_to_send)
