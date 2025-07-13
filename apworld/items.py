# %% IMPORTS
from collections import defaultdict
from dataclasses import dataclass, field

from BaseClasses import ItemClassification, Item

from .enums import CivVItemGroup, CivVItemType
from .constants import GAME_NAME, ID_OFFSET

# All declaration
__all__ = ["CivVItem", "ITEMS_DATA", "ITEMS_DATA_BY_ID", "ITEM_GROUPS"]


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
    game_id: int
    "ID of this item with this item type within Civ V"
    classification: ItemClassification
    "Classification of this item"
    groups: set[CivVItemGroup | CivVItemType] = field(default_factory=set)
    "Set of groups this item belongs to. The type of this item is always part of this set"
    ap_id: int = field(init=False)
    "ID of this item within AP"

    def __post_init__(self):
        # Add the item type as a prefix to the item name
        self.name = f"{self.type.capitalize()} - {self.name}"

        # Set AP ID for this item
        self.ap_id = len(ITEMS_DATA) + ID_OFFSET

        # Make sure the item type is part of this item's groups set
        self.groups.add(self.type)

        # Add self to the ITEMS_DATA; ITEMS_DATA_BY_ID; and ITEM_GROUPS dicts
        ITEMS_DATA.append(self)
        ITEMS_DATA_BY_ID[self.ap_id] = self
        for group in self.groups:
            ITEM_GROUPS[str(group)].append(self.name)


# %% ITEM DECLARATIONS
TECH_ITEMS = [
    CivVItemData(
        name="Pottery",
        type=CivVItemType.tech,
        game_id=82,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Animal Husbandry",
        type=CivVItemType.tech,
        game_id=83,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Archery",
        type=CivVItemType.tech,
        game_id=84,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Mining",
        type=CivVItemType.tech,
        game_id=85,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Sailing",
        type=CivVItemType.tech,
        game_id=86,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Calendar",
        type=CivVItemType.tech,
        game_id=87,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Writing",
        type=CivVItemType.tech,
        game_id=88,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Trapping",
        type=CivVItemType.tech,
        game_id=89,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="The Wheel",
        type=CivVItemType.tech,
        game_id=90,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Masonry",
        type=CivVItemType.tech,
        game_id=91,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Bronze Working",
        type=CivVItemType.tech,
        game_id=92,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    CivVItemData(
        name="Optics",
        type=CivVItemType.tech,
        game_id=93,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Horseback Riding",
        type=CivVItemType.tech,
        game_id=94,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Mathematics",
        type=CivVItemType.tech,
        game_id=95,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Construction",
        type=CivVItemType.tech,
        game_id=96,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Philosophy",
        type=CivVItemType.tech,
        game_id=97,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Drama and Poetry",
        type=CivVItemType.tech,
        game_id=98,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Currency",
        type=CivVItemType.tech,
        game_id=99,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Engineering",
        type=CivVItemType.tech,
        game_id=100,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Iron Working",
        type=CivVItemType.tech,
        game_id=101,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    CivVItemData(
        name="Theology",
        type=CivVItemType.tech,
        game_id=102,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Civil Service",
        type=CivVItemType.tech,
        game_id=103,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Guilds",
        type=CivVItemType.tech,
        game_id=104,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Metal Casting",
        type=CivVItemType.tech,
        game_id=105,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Compass",
        type=CivVItemType.tech,
        game_id=106,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Education",
        type=CivVItemType.tech,
        game_id=107,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Chivalry",
        type=CivVItemType.tech,
        game_id=108,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Machinery",
        type=CivVItemType.tech,
        game_id=109,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Physics",
        type=CivVItemType.tech,
        game_id=110,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Steel",
        type=CivVItemType.tech,
        game_id=111,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    CivVItemData(
        name="Astronomy",
        type=CivVItemType.tech,
        game_id=112,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Acoustics",
        type=CivVItemType.tech,
        game_id=113,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Banking",
        type=CivVItemType.tech,
        game_id=114,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Printing Press",
        type=CivVItemType.tech,
        game_id=115,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Gunpowder",
        type=CivVItemType.tech,
        game_id=116,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Navigation",
        type=CivVItemType.tech,
        game_id=117,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Architecture",
        type=CivVItemType.tech,
        game_id=118,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Economics",
        type=CivVItemType.tech,
        game_id=119,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Metallurgy",
        type=CivVItemType.tech,
        game_id=120,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Chemistry",
        type=CivVItemType.tech,
        game_id=121,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    CivVItemData(
        name="Archaeology",
        type=CivVItemType.tech,
        game_id=122,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Scientific Theory",
        type=CivVItemType.tech,
        game_id=123,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Industrialization",
        type=CivVItemType.tech,
        game_id=124,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Rifling",
        type=CivVItemType.tech,
        game_id=125,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Military Science",
        type=CivVItemType.tech,
        game_id=126,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Fertilizer",
        type=CivVItemType.tech,
        game_id=127,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Biology",
        type=CivVItemType.tech,
        game_id=128,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Electricity",
        type=CivVItemType.tech,
        game_id=129,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Steam Power",
        type=CivVItemType.tech,
        game_id=130,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Dynamite",
        type=CivVItemType.tech,
        game_id=131,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    CivVItemData(
        name="Refrigeration",
        type=CivVItemType.tech,
        game_id=132,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Radio",
        type=CivVItemType.tech,
        game_id=133,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Replaceable Parts",
        type=CivVItemType.tech,
        game_id=134,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Flight",
        type=CivVItemType.tech,
        game_id=135,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Railroad",
        type=CivVItemType.tech,
        game_id=136,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Plastics",
        type=CivVItemType.tech,
        game_id=137,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Electronics",
        type=CivVItemType.tech,
        game_id=138,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Ballistics",
        type=CivVItemType.tech,
        game_id=139,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Combustion",
        type=CivVItemType.tech,
        game_id=140,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    CivVItemData(
        name="Penicillin",
        type=CivVItemType.tech,
        game_id=141,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Atomic Theory",
        type=CivVItemType.tech,
        game_id=142,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Radar",
        type=CivVItemType.tech,
        game_id=143,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Combined Arms",
        type=CivVItemType.tech,
        game_id=144,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Ecology",
        type=CivVItemType.tech,
        game_id=145,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Nuclear Fission",
        type=CivVItemType.tech,
        game_id=146,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Rocketry",
        type=CivVItemType.tech,
        game_id=147,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Computers",
        type=CivVItemType.tech,
        game_id=148,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    CivVItemData(
        name="Telecommunications",
        type=CivVItemType.tech,
        game_id=149,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Mobile Tactics",
        type=CivVItemType.tech,
        game_id=150,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Advanced Ballistics",
        type=CivVItemType.tech,
        game_id=151,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Satellites",
        type=CivVItemType.tech,
        game_id=152,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Robotics",
        type=CivVItemType.tech,
        game_id=153,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Lasers",
        type=CivVItemType.tech,
        game_id=154,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="The Internet",
        type=CivVItemType.tech,
        game_id=155,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Globalization",
        type=CivVItemType.tech,
        game_id=156,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Particle Physics",
        type=CivVItemType.tech,
        game_id=157,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Nuclear Fusion",
        type=CivVItemType.tech,
        game_id=158,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Nanotechnology",
        type=CivVItemType.tech,
        game_id=159,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    CivVItemData(
        name="Stealth",
        type=CivVItemType.tech,
        game_id=160,
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
]
"List of all technologies within Civ V"
