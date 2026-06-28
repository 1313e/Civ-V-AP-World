# %% IMPORTS
import asyncio
import itertools
import typing

from CommonClient import CommonContext
from NetUtils import NetworkItem

from .command_processor import CivVCommandProcessor
from .constants import GAME_NAME, ID_OFFSET
from .dataclasses import CivVSlotData
from .death_link import DEATH_LINK_EFFECTS_BY_NAME, CivVDeathLinkEffect
from .enums import CivVLocationType

# All declaration
__all__ = ["CivVContext"]


# %% CONTEXT CLASS DEFINITION
class CivVContext(CommonContext):
    """
    AP context for Civ V.

    """

    # Class attributes
    game = GAME_NAME
    items_handling = 0b111
    command_processor = CivVCommandProcessor

    # Additional class attributes
    client_task: asyncio.Task
    "The asyncio task that contains the Civ V AP Client"
    item_offset: int = ID_OFFSET
    "Item offset to use for conversion from internal IDs to multiworld IDs"
    sent_locations: dict[CivVLocationType, set[int]] = {location_type: set() for location_type in CivVLocationType}
    "Dict of locations originating from this game that have been sent to the multiworld already, split by location type"
    received_item_ids: list[int] = []
    "IDs of items originating from the multiworld that have been received by this game already"
    queued_sent_items: list[tuple[NetworkItem, int]] = []
    "List of queued items and their receiver that this game sent to them"
    queued_death_links: list[str] = []
    "List of queued death links"
    death_link_effect_list: list[CivVDeathLinkEffect] = []
    "List of possible death link effects"
    n_death_links_effects: int = 0
    "Number of death link effects"
    has_achieved_victory: bool = False
    "Whether the player has achieved victory yet"
    slot_data: CivVSlotData
    "Slot data received from the server"

    async def server_auth(self, password_requested = False):
        if password_requested and not self.password:
            await super(CivVContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def make_gui(self):
        from kvui import GameManager

        class CivVManager(GameManager):
            logging_pairs = [("Client", "Archipelago")]
            base_title = f"Archipelago {GAME_NAME} Client"

        return CivVManager

    def on_package(self, cmd, args):
        if cmd == "Connected":
            # Retrieve the slot data from this slot
            self.slot_data = CivVSlotData(**args["slot_data"])

            # Pre-calculate the weighted death link effects list
            self.death_link_effect_list = list(itertools.chain.from_iterable(
                [[DEATH_LINK_EFFECTS_BY_NAME[x]]*y for x, y in self.slot_data.death_link_effect_weights.items()]
            ))
            self.n_death_links_effects = len(self.death_link_effect_list)

    def on_print_json(self, args: dict):
        # If an item was sent by this slot, queue the details regarding that item
        if args["type"] == "ItemSend" and args["item"].player == self.slot:
            self.queued_sent_items.append((args["item"], args["receiving"]))
        super().on_print_json(args)

    def on_deathlink(self, data: typing.Dict[str, typing.Any]) -> None:
        self.queued_death_links.append(data.get("cause", f"Received from {data['source']}"))
        super().on_deathlink(data)
