# %% IMPORTS
from collections import defaultdict
from dataclasses import dataclass, field

from BaseClasses import ItemClassification, Item

from .enums import CivVItemGroup, CivVItemType
from .constants import GAME_NAME, ID_OFFSET

# All declaration
__all__ = [
    "CivVItem",
    "CivVItemData",
    "ITEMS_DATA",
    "ITEMS_DATA_BY_ID",
    "ITEM_GROUPS",
    "PROGRESSIVE_ERA_ITEM",
    "PROGRESSIVE_TECH_ITEMS",
    "TECH_ITEMS",
]


# %% GLOBALS
ITEMS_DATA: list["CivVItemData"] = []
"List of all defined items"
ITEMS_DATA_BY_ID: dict[int, "CivVItemData"] = {}
"Dict of all defined items, separated by AP ID"
ITEM_GROUPS: defaultdict[str, list[str]] = defaultdict(list)
"Dict of all defined item names per item group. Used by the CivVWorld"


# %% ITEM CLASS DEFINITION
class CivVItem(Item):
    game: str = GAME_NAME


# %% ITEM_DATA CLASS DEFINITION
@dataclass
class CivVItemData:
    """
    Dataclass used for specifying an item within Civ V.

    """

    name: str
    "Name of this item"
    type: CivVItemType
    "Type of this item"
    game_ids: list[int]
    "ID(s) of this item with this item type within Civ V. If multiple, this item exists that many times"
    classification: ItemClassification
    "Classification of this item"
    count: int = field(init=False)
    "Number of times this item exists within Civ V"
    groups: set[CivVItemGroup | CivVItemType] = field(default_factory=set)
    "Set of groups this item belongs to. The type of this item is always part of this set"
    ap_id: int = field(init=False)
    "ID of this item within AP"

    def __post_init__(self):
        # Add the item type as a prefix to the item name
        self.name = f"{self.type.capitalize()} - {self.name}"

        # Set count for this item
        self.count = len(self.game_ids)

        # Set AP ID for this item
        self.ap_id = len(ITEMS_DATA) + ID_OFFSET

        # Make sure the item type is part of this item's groups set
        self.groups.add(self.type)

        # Add self to the dicts
        ITEMS_DATA.append(self)
        ITEMS_DATA_BY_ID[self.ap_id] = self
        for group in self.groups:
            ITEM_GROUPS[str(group)].append(self.name)


# %% ITEM DECLARATIONS
PROGRESSIVE_ERA_ITEM = CivVItemData(
    name="Progressive",
    type=CivVItemType.era,
    game_ids=[169, 170, 171, 172, 173, 174, 175],
    classification=ItemClassification.progression,
)
"Progressive era item within Civ V"

TECH_ITEMS = [
    CivVItemData(
        name="Pottery",
        type=CivVItemType.tech,
        game_ids=[1],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Animal Husbandry",
        type=CivVItemType.tech,
        game_ids=[2],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Archery",
        type=CivVItemType.tech,
        game_ids=[3],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Mining",
        type=CivVItemType.tech,
        game_ids=[4],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Sailing",
        type=CivVItemType.tech,
        game_ids=[5],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Calendar",
        type=CivVItemType.tech,
        game_ids=[6],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Writing",
        type=CivVItemType.tech,
        game_ids=[7],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Trapping",
        type=CivVItemType.tech,
        game_ids=[8],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="The Wheel",
        type=CivVItemType.tech,
        game_ids=[9],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Masonry",
        type=CivVItemType.tech,
        game_ids=[10],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Bronze Working",
        type=CivVItemType.tech,
        game_ids=[11],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Optics",
        type=CivVItemType.tech,
        game_ids=[12],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Horseback Riding",
        type=CivVItemType.tech,
        game_ids=[13],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Mathematics",
        type=CivVItemType.tech,
        game_ids=[14],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Construction",
        type=CivVItemType.tech,
        game_ids=[15],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Philosophy",
        type=CivVItemType.tech,
        game_ids=[16],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Drama and Poetry",
        type=CivVItemType.tech,
        game_ids=[17],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Currency",
        type=CivVItemType.tech,
        game_ids=[18],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Engineering",
        type=CivVItemType.tech,
        game_ids=[19],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Iron Working",
        type=CivVItemType.tech,
        game_ids=[20],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Theology",
        type=CivVItemType.tech,
        game_ids=[21],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Civil Service",
        type=CivVItemType.tech,
        game_ids=[22],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Guilds",
        type=CivVItemType.tech,
        game_ids=[23],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Metal Casting",
        type=CivVItemType.tech,
        game_ids=[24],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Compass",
        type=CivVItemType.tech,
        game_ids=[25],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Education",
        type=CivVItemType.tech,
        game_ids=[26],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Chivalry",
        type=CivVItemType.tech,
        game_ids=[27],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Machinery",
        type=CivVItemType.tech,
        game_ids=[28],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Physics",
        type=CivVItemType.tech,
        game_ids=[29],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Steel",
        type=CivVItemType.tech,
        game_ids=[30],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Astronomy",
        type=CivVItemType.tech,
        game_ids=[31],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Acoustics",
        type=CivVItemType.tech,
        game_ids=[32],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Banking",
        type=CivVItemType.tech,
        game_ids=[33],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Printing Press",
        type=CivVItemType.tech,
        game_ids=[34],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Gunpowder",
        type=CivVItemType.tech,
        game_ids=[35],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Navigation",
        type=CivVItemType.tech,
        game_ids=[36],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Architecture",
        type=CivVItemType.tech,
        game_ids=[37],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Economics",
        type=CivVItemType.tech,
        game_ids=[38],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Metallurgy",
        type=CivVItemType.tech,
        game_ids=[39],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Chemistry",
        type=CivVItemType.tech,
        game_ids=[40],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Archaeology",
        type=CivVItemType.tech,
        game_ids=[41],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Scientific Theory",
        type=CivVItemType.tech,
        game_ids=[42],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Industrialization",
        type=CivVItemType.tech,
        game_ids=[43],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Rifling",
        type=CivVItemType.tech,
        game_ids=[44],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Military Science",
        type=CivVItemType.tech,
        game_ids=[45],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Fertilizer",
        type=CivVItemType.tech,
        game_ids=[46],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Biology",
        type=CivVItemType.tech,
        game_ids=[47],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Electricity",
        type=CivVItemType.tech,
        game_ids=[48],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Steam Power",
        type=CivVItemType.tech,
        game_ids=[49],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Dynamite",
        type=CivVItemType.tech,
        game_ids=[50],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Refrigeration",
        type=CivVItemType.tech,
        game_ids=[51],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Radio",
        type=CivVItemType.tech,
        game_ids=[52],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Replaceable Parts",
        type=CivVItemType.tech,
        game_ids=[53],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Flight",
        type=CivVItemType.tech,
        game_ids=[54],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Railroad",
        type=CivVItemType.tech,
        game_ids=[55],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Plastics",
        type=CivVItemType.tech,
        game_ids=[56],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Electronics",
        type=CivVItemType.tech,
        game_ids=[57],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Ballistics",
        type=CivVItemType.tech,
        game_ids=[58],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Combustion",
        type=CivVItemType.tech,
        game_ids=[59],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Penicillin",
        type=CivVItemType.tech,
        game_ids=[60],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Atomic Theory",
        type=CivVItemType.tech,
        game_ids=[61],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Radar",
        type=CivVItemType.tech,
        game_ids=[62],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Combined Arms",
        type=CivVItemType.tech,
        game_ids=[63],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Ecology",
        type=CivVItemType.tech,
        game_ids=[64],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Nuclear Fission",
        type=CivVItemType.tech,
        game_ids=[65],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Rocketry",
        type=CivVItemType.tech,
        game_ids=[66],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Computers",
        type=CivVItemType.tech,
        game_ids=[67],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Telecommunications",
        type=CivVItemType.tech,
        game_ids=[68],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Mobile Tactics",
        type=CivVItemType.tech,
        game_ids=[69],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Advanced Ballistics",
        type=CivVItemType.tech,
        game_ids=[70],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Satellites",
        type=CivVItemType.tech,
        game_ids=[71],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Robotics",
        type=CivVItemType.tech,
        game_ids=[72],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Lasers",
        type=CivVItemType.tech,
        game_ids=[73],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="The Internet",
        type=CivVItemType.tech,
        game_ids=[74],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Globalization",
        type=CivVItemType.tech,
        game_ids=[75],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Particle Physics",
        type=CivVItemType.tech,
        game_ids=[76],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Nuclear Fusion",
        type=CivVItemType.tech,
        game_ids=[77],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Nanotechnology",
        type=CivVItemType.tech,
        game_ids=[78],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Stealth",
        type=CivVItemType.tech,
        game_ids=[79],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
]
"List of all technologies within Civ V"

PROGRESSIVE_TECH_ITEMS = [
    CivVItemData(
        name="Progressive Growth",
        type=CivVItemType.tech,
        game_ids=[1, 19, 22, 46, 47, 60],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Production",
        type=CivVItemType.tech,
        game_ids=[4, 10, 24, 43, 64],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Science",
        type=CivVItemType.tech,
        game_ids=[7, 26, 42, 56, 66, 70, 71, 76, 78],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Culture",
        type=CivVItemType.tech,
        game_ids=[16, 17, 32, 41, 52, 68, 74],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Gold",
        type=CivVItemType.tech,
        game_ids=[2, 18, 23, 33, 38, 48],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Happiness",
        type=CivVItemType.tech,
        game_ids=[6, 8, 15, 34, 51],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Exploration",
        type=CivVItemType.tech,
        game_ids=[5, 12, 25, 31],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Melee Unit",
        type=CivVItemType.tech,
        game_ids=[11, 13, 20, 27, 30, 35, 39, 44, 45, 49, 53, 59, 63, 67, 69, 73, 77],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Ranged Unit",
        type=CivVItemType.tech,
        game_ids=[3, 28, 36, 54, 57, 58, 62, 72, 79],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Siege Unit",
        type=CivVItemType.tech,
        game_ids=[14, 29, 40, 50],
        classification=ItemClassification.progression,
    ),
    CivVItemData(
        name="Progressive Misc",
        type=CivVItemType.tech,
        game_ids=[9, 21, 37, 55, 61, 65, 75],
        classification=ItemClassification.progression,
    ),
]
"List of all progressive technologies within Civ V"
