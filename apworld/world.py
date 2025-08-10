# %% IMPORTS
import itertools

from BaseClasses import Region, ItemClassification
from worlds.AutoWorld import World

from .constants import GAME_NAME
from .enums import CivVLocationType
from .items import (
    FILLER_ITEMS,
    ITEMS_DATA,
    ITEMS_DATA_BY_ID,
    ITEM_GROUPS,
    POLICY_ITEMS,
    PROGRESSIVE_ERA_ITEM,
    PROGRESSIVE_TECH_ITEMS,
    TECH_ITEMS,
    TRAP_ITEMS,
    CivVFillerItemData,
    CivVItem,
    CivVUsefulItemData,
)
from .locations import (
    LOCATIONS_DATA,
    LOCATIONS_DATA_BY_TYPE_ID,
    NATIONAL_WONDER_LOCATIONS,
    POLICY_BRANCH_LOCATIONS,
    POLICY_LOCATIONS,
    TECH_LOCATIONS,
    WORLD_WONDER_LOCATIONS,
    CivVLocation,
    CivVLocationData,
)
from .options import CivVOptions
from .regions import ERA_REGIONS, REGIONS_DATA

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

    def get_useful_items_data(self) -> list[CivVUsefulItemData]:
        """
        Returns the list of `CivVUsefulItemData` instances to use for this seed, according to the options.

        """

        # Create list with items that are always included
        items_data = [PROGRESSIVE_ERA_ITEM, *POLICY_ITEMS.values()]

        # Pick which items lists to use based on options
        items_data.extend(
            PROGRESSIVE_TECH_ITEMS.values() if self.options.progressive_techs else TECH_ITEMS.values()
        )

        # Return items data
        return items_data

    def get_filler_items_data(self, n: int) -> list[CivVFillerItemData]:
        """
        Returns a list of `n` `CivVFillerItemData` instances to use for this seed, according to the options.

        """

        # Create list with filler items
        n_filler = len(FILLER_ITEMS)
        items_data = []

        # If traps are enabled and not all blacklisted, create both filler and trap items
        traps_list = [item_data for item_data in TRAP_ITEMS if item_data.name not in self.options.trap_blacklist]
        if self.options.enable_traps and traps_list:
            # Generate n filler items
            n_traps = len(traps_list)
            trap_chance = self.options.trap_filler_chance / 100
            for _ in range(n):
                # Determine if filler item or trap should be chosen
                if self.random.random() <= trap_chance:
                    # Pick random trap item
                    items_data.append(traps_list[self.random.randint(0, n_traps - 1)])
                else:
                    # Pick random filler item
                    items_data.append(FILLER_ITEMS[self.random.randint(0, n_filler - 1)])

        # Else, create n filler items
        else:
            items_data.extend((FILLER_ITEMS[self.random.randint(0, n_filler - 1)] for _ in range(n)))

        # Return items data
        return items_data

    def create_items(self) -> None:
        # Create list of all progression and useful items to be added to the multiworld
        useful_items = list(itertools.chain.from_iterable(
            ([self.create_item(item_data.name) for _ in range(item_data.count)] for item_data in
             self.get_useful_items_data())))

        # Calculate number of filler items required
        # Extra minus 1 here because victory location already has an item placed
        n_filler = len(list(self.multiworld.get_locations(self.player))) - len(useful_items) - 1

        # Create list of all filler and trap items to be added to the multiworld
        filler_items = (self.create_item(item_data.name) for item_data in self.get_filler_items_data(n_filler))

        # Add the items to the multiworld
        self.multiworld.itempool.extend(useful_items)
        self.multiworld.itempool.extend(filler_items)

    def get_locations_data(self) -> list[CivVLocationData]:
        """
        Returns the list of `CivVLocationData` instances to use for this seed, according to the options.

        """

        # Create list with locations that are always included
        locations_data = [*POLICY_BRANCH_LOCATIONS, *POLICY_LOCATIONS, *TECH_LOCATIONS]

        # Add wonder locations if corresponding wonder sanity is enabled
        if self.options.national_wonder_sanity:
            locations_data.extend(NATIONAL_WONDER_LOCATIONS)
        if self.options.world_wonder_sanity:
            locations_data.extend(WORLD_WONDER_LOCATIONS)

        # Return locations data
        return locations_data

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
                rule=region_data.requirements.create_access_rule(self.player, self.options),
            )

        # Add all locations to the multiworld
        for location_data in self.get_locations_data():
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
            location.access_rule = location_data.requirements.create_access_rule(self.player, self.options)

        # Add victory to the multiworld
        victory_region = self.multiworld.get_region(ERA_REGIONS[self.options.era_goal_logic.value].name, self.player)
        victory_location = CivVLocation(
            player=self.player,
            name="Victory",
            address=None,
            parent=victory_region
        )
        victory_region.locations.append(victory_location)

        # If specific victory goal was set in the options, add its requirements access rule to the location
        if self.options.victory_goal_logic.value:
            victory_requirements = LOCATIONS_DATA_BY_TYPE_ID[
                (CivVLocationType.victory, self.options.victory_goal_logic.value)].requirements
            victory_location.access_rule = victory_requirements.create_access_rule(self.player, self.options)

        # Place dummy Victory item at this location and add completion condition to the multiworld
        victory_location.place_locked_item(CivVItem("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
