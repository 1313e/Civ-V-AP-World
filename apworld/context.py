# %% IMPORTS
import asyncio
import typing

from CommonClient import CommonContext

from .command_processor import CivVCommandProcessor
from .constants import GAME_NAME, ID_OFFSET
from .dataclasses import CivVSlotData
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
    queued_death_links: list[str] = []
    "List of queued death links"
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
            slot_data = args["slot_data"]
            self.slot_data = CivVSlotData(
                output_file_id=slot_data["output_file_id"],
                death_link=slot_data["death_link"],
            )

    def on_deathlink(self, data: typing.Dict[str, typing.Any]) -> None:
        self.queued_death_links.append(data.get("cause", f"Received from {data['source']}"))
        super().on_deathlink(data)
