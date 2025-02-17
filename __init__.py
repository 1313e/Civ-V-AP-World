# world/mygame/__init__.py

# import settings
from typing import List, Optional
from .Tech_Array import list_of_tech_keys
from .options import CivVOptions  # the options we defined earlier
from .items import CivVItem, item_table  # data used below to add items to the World
from .locations import CivVLocation, location_table_data  # same as above
from .regions import region_data_table
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess

base_id = 1
offset = 140319

def run_client(url: Optional[str] = None):
    print("Running CivV Client")
    from .CivVClient import main
    launch_subprocess(main, name="CivV Client")

components.append(
    Component("CivV Client", func=run_client, component_type=Type.CLIENT)
)


class CivVWorld(World):
    """Insert description of the world/game here."""
    game = "Civilization V"  # name of the game/world
    options_dataclass = CivVOptions  # options the player can set
    options: CivVOptions  # typing hints for option results
    # settings: typing.ClassVar[MyGameSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = {name: id for
                       id, name in enumerate(item_table.keys(), base_id + offset)}
    location_name_to_id = {name: id for
                           id, name in enumerate(location_table_data.keys(), base_id + offset)}
    
    item_name_groups = {
        "Column 1" : {"Pottery", "Animal Husbandry", "Archery", "Mining"},
        "Column 2" : {"Sailing", "Calendar", "Writing", "Trapping", "The Wheel", "Masonry", "Bronze Working"},
        "Column 3" : {"Optics", "Horseback Riding", "Mathematics", "Construction"},
        "Column 4" : {"Philosophy", "Drama", "Currency", "Engineering", "Iron Working"},
        "Column 5" : {"Theology", "Civil Service", "Guilds", "Metal Casting"},
        "Column 6" : {"Compass", "Education", "Chivalry", "Machinery", "Physics", "Steel"},
        "Column 7" : {"Astronomy", "Acoustics", "Banking", "Printing Press", "Gunowder"},
        "Column 8" : {"Navigation", "Architecture", "Economics", "Metallurgy", "Chemistry"},
        "Column 9" : {"Archaeology", "Scientific Theory", "Industrialization", "Rifling", "Military Science", "Fertilizer"},
        "Column 10" : {"Biology", "Electricity", "Steam Power", "Dynamite"},
        "Column 11" : {"Refrigeration", "Radio", "Replaceable Parts", "Flight", "Railroad"},
        "Column 12" : {"Plastics", "Electronics", "Ballistics", "Combustion"},
        "Column 13" : {"Penicillin", "Atomic Theory", "Radar", "Combined Arms"},
        "Column 14" : {"Ecology", "Nuclear Fission", "Rocketry", "Computers"},
        "Column 15" : {"Telecommunications", "Mobile Tactics", "Advanced Ballistics", "Satellites", "Robotics", "Lasers"},
        "Column 16" : {"The Internet", "Globalization", "Particle Physics", "Nuclear Fusion", "Nanatechnology", "Stealth"}
    }
    
    def create_item(self, name) -> CivVItem:
        return CivVItem(name, item_table[name][1], self.item_name_to_id[name], self.player)
    
    def create_items(self) -> None:
        item_pool: List[CivVItem] = []
        for name, item in item_table.items():
            item_pool.append(self.create_item(name))
        self.multiworld.itempool += item_pool
    
    def create_regions(self) -> None:
        menu_reigion = Region("Menu", self.player, self.multiworld)
        column1_region = Region("Column 1", self.player, self.multiworld)
        column2_region = Region("Column 2", self.player, self.multiworld)
        column3_region = Region("Column 3", self.player, self.multiworld)
        column4_region = Region("Column 4", self.player, self.multiworld)
        column5_region = Region("Column 5", self.player, self.multiworld)
        column6_region = Region("Column 6", self.player, self.multiworld)
        column7_region = Region("Column 7", self.player, self.multiworld)
        column8_region = Region("Column 8", self.player, self.multiworld)
        column9_region = Region("Column 9", self.player, self.multiworld)
        column10_region = Region("Column 10", self.player, self.multiworld)
        column11_region = Region("Column 11", self.player, self.multiworld)
        column12_region = Region("Column 12", self.player, self.multiworld)
        column13_region = Region("Column 13", self.player, self.multiworld)
        column14_region = Region("Column 14", self.player, self.multiworld)
        column15_region = Region("Column 15", self.player, self.multiworld)
        column16_region = Region("Column 16", self.player, self.multiworld)

        self.multiworld.regions.append(menu_reigion)

        main_region = Region("Main", self.player, self.multiworld)
        for location, id in location_table_data.items():
            if id[1] == 1:
                column1_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 2:
                column2_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 3:
                column3_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 4:
                column4_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 5:
                column5_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 6:
                column6_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 7:
                column7_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 8:
                column8_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 9:
                column9_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 10:
                column10_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 11:
                column11_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 12:
                column12_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 13:
                column13_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 14:
                column14_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 15:
                column15_region.add_locations({location : id[0] + offset}, CivVLocation)
            if id[1] == 16:
                column16_region.add_locations({location : id[0] + offset}, CivVLocation)
        self.multiworld.regions.append(column1_region)
        self.multiworld.regions.append(column2_region)
        self.multiworld.regions.append(column3_region)
        self.multiworld.regions.append(column4_region)
        self.multiworld.regions.append(column5_region)
        self.multiworld.regions.append(column6_region)
        self.multiworld.regions.append(column7_region)
        self.multiworld.regions.append(column8_region)
        self.multiworld.regions.append(column9_region)
        self.multiworld.regions.append(column10_region)
        self.multiworld.regions.append(column11_region)
        self.multiworld.regions.append(column12_region)
        self.multiworld.regions.append(column13_region)
        self.multiworld.regions.append(column14_region)
        self.multiworld.regions.append(column15_region)
        self.multiworld.regions.append(column16_region)


        menu_reigion.connect(column1_region)
        column1_region.add_exits({"Column 2" : "To Column 2"}, {"Column 2": lambda state: state.has_group("Column 1", self.player)})
        column2_region.add_exits({"Column 3" : "To Column 3"}, {"Column 3": lambda state: state.has_group("Column 2", self.player)})
        column3_region.add_exits({"Column 4" : "To Column 4"}, {"Column 4": lambda state: state.has_group("Column 3", self.player)})
        column4_region.add_exits({"Column 5" : "To Column 5"}, {"Column 5": lambda state: state.has_group("Column 4", self.player)})
        column5_region.add_exits({"Column 6" : "To Column 6"}, {"Column 6": lambda state: state.has_group("Column 5", self.player)})
        column6_region.add_exits({"Column 7" : "To Column 7"}, {"Column 7": lambda state: state.has_group("Column 6", self.player)})
        column7_region.add_exits({"Column 8" : "To Column 8"}, {"Column 8": lambda state: state.has_group("Column 7", self.player)})
        column8_region.add_exits({"Column 9" : "To Column 9"}, {"Column 9": lambda state: state.has_group("Column 8", self.player)})
        column9_region.add_exits({"Column 10" : "To Column 10"}, {"Column 10": lambda state: state.has_group("Column 9", self.player)})
        column10_region.add_exits({"Column 11" : "To Column 11"}, {"Column 11": lambda state: state.has_group("Column 10", self.player)})
        column11_region.add_exits({"Column 12" : "To Column 12"}, {"Column 12": lambda state: state.has_group("Column 11", self.player)})
        column12_region.add_exits({"Column 13" : "To Column 13"}, {"Column 13": lambda state: state.has_group("Column 12", self.player)})
        column13_region.add_exits({"Column 14" : "To Column 14"}, {"Column 14": lambda state: state.has_group("Column 13", self.player)})
        column14_region.add_exits({"Column 15" : "To Column 15"}, {"Column 15": lambda state: state.has_group("Column 14", self.player)})
        column15_region.add_exits({"Column 16" : "To Column 16"}, {"Column 16": lambda state: state.has_group("Column 15", self.player)})
        return