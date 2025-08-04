# %% IMPORTS
import itertools
from collections.abc import Callable

from BaseClasses import Region, ItemClassification, CollectionState
from worlds.AutoWorld import World

from .constants import GAME_NAME
from .items import (
    ITEMS_DATA,
    ITEMS_DATA_BY_ID,
    ITEM_GROUPS,
    POLICY_ITEMS,
    PROGRESSIVE_ERA_ITEM,
    PROGRESSIVE_TECH_ITEMS,
    TECH_ITEMS,
    CivVItem,
)
from .locations import LOCATIONS_DATA, CivVLocation, CivVLocationData
from .options import CivVOptions
from .regions import ERA_REGIONS, REGIONS_DATA, CivVRegionData

# All declaration
__all__ = ["CivVWorld"]


# %% WORLD CLASS DEFINITION
class CivVWorld(World):
    """
    APWorld for Civilization V.

    """

    # Class attributes
    game = GAME_NAME
    options_dataclass = CivVOptions
    options: CivVOptions
    topology_present = True
    item_name_to_id = {item_data.name: item_data.ap_id for item_data in ITEMS_DATA}
    location_name_to_id = {location_data.name: location_data.ap_id for location_data in LOCATIONS_DATA}
    item_name_groups = ITEM_GROUPS

    def create_item(self, name: str) -> CivVItem:
        item_data = ITEMS_DATA_BY_ID[self.item_name_to_id[name]]
        return CivVItem(
            name=item_data.name,
            classification=item_data.classification,
            code=item_data.ap_id,
            player=self.player,
        )

    def create_items(self) -> None:
        # Create list of items to use for this seed
        items_data = [PROGRESSIVE_ERA_ITEM]

        # Pick which items lists to use based on options
        items_data.extend(POLICY_ITEMS)
        items_data.extend(PROGRESSIVE_TECH_ITEMS if self.options.progressive_techs.value else TECH_ITEMS)

        # Add the items to the multiworld
        self.multiworld.itempool.extend(itertools.chain.from_iterable(
            ([self.create_item(item_data.name) for _ in range(item_data.count)] for item_data in items_data)))

    def create_access_rule(self, data: CivVRegionData | CivVLocationData) -> Callable[[CollectionState], bool]:
        """
        Creates the access rule function for the given region or location `data` and returns it.

        This function can be used as the access rule when creating :class:`Region` and :class:`Location` instances.

        """

        # Create rule function that uses the CollectionState to determine if region/location is reachable
        def rule(state: CollectionState) -> bool:
            return all((state.has(name, self.player, count) for name, count in data.requirements.items()))

        # Return created rule
        return rule

    def create_regions(self) -> None:
        # Add the origin region
        self.multiworld.regions.append(
            Region(name=self.origin_region_name, player=self.player, multiworld=self.multiworld)
        )

        # Create and register all defined regions
        self.multiworld.regions.extend(
            [Region(name=region_data.name, player=self.player, multiworld=self.multiworld)
             for region_data in REGIONS_DATA]
        )

        # Add connections and rules to all regions
        for region_data in REGIONS_DATA:
            # Retrieve region and parent region
            region = self.multiworld.get_region(region_name=region_data.name, player=self.player)
            parent_region = self.multiworld.get_region(
                region_name=region_data.parent.name if region_data.parent is not None else self.origin_region_name,
                player=self.player
            )

            # Make connection between parent region and this region
            parent_region.connect(
                connecting_region=region,
                rule=self.create_access_rule(region_data),
            )

        # Add all locations to the multiworld
        for location_data in LOCATIONS_DATA:
            # Create location and add it to its region
            region = self.multiworld.get_region(
                region_name=location_data.region.name if location_data.region is not None else self.origin_region_name,
                player=self.player
            )
            location = CivVLocation(
                player=self.player,
                name=location_data.name,
                address=location_data.ap_id,
                parent=region,
            )
            region.locations.append(location)

            # Add accessibility rule to this location
            location.access_rule = self.create_access_rule(location_data)

        # Add victory to the multiworld
        victory_region = self.multiworld.get_region(ERA_REGIONS[self.options.era_goal.value].name, self.player)
        victory_location = CivVLocation(
            player=self.player,
            name="Victory",
            address=None,
            parent=victory_region
        )
        victory_location.place_locked_item(CivVItem("Victory", ItemClassification.progression, None, self.player))
        victory_region.locations.append(victory_location)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
