# %% IMPORTS
from BaseClasses import Region
from worlds.AutoWorld import World

from .constants import GAME_NAME
from .items import ITEMS_DATA, ITEMS_DATA_BY_ID, ITEM_GROUPS, CivVItem
from .locations import LOCATIONS_DATA, CivVLocation
from .options import CivVOptions
from .regions import REGIONS_DATA

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
        self.multiworld.itempool.extend([self.create_item(item_data.name) for item_data in ITEMS_DATA])

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
                region_name=region_data.parent if region_data.parent is not None else self.origin_region_name,
                player=self.player
            )

            # Make connection between parent region and this region
            parent_region.connect(
                connecting_region=region,
                rule=lambda state: region_data.rule(state) if region_data.rule is not None else True,
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
            location.access_rule = lambda state: location_data.rule(state) if location_data.rule is not None else True
