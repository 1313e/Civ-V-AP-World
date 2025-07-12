# %% IMPORTS
import asyncio

from CommonClient import CommonContext
from NetUtils import NetworkItem

from .command_processor import CivVCommandProcessor
from .constants import GAME_NAME, ITEM_OFFSET

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
    item_offset: int = ITEM_OFFSET
    "Item offset to use for conversion from internal IDs to multiworld IDs"
    sent_locations: dict[str, set[int]] = {"techs": set()}
    "Dict of locations originating from this game that have been sent to the multiworld already, split by location type"
    received_items: set[NetworkItem] = set()
    "Set of items originating from the multiworld that have been received by this game already"
    has_achieved_victory: bool = False
    "Whether the player has achieved victory yet"

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
