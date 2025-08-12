# %% IMPORTS
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

from BaseClasses import CollectionState, ItemClassification, Item
from Options import PerGameCommonOptions

from .constants import GAME_NAME, ID_OFFSET
from .enums import CivVFillerType, CivVItemGroup, CivVItemType
from .helpers import to_title

# All declaration
__all__ = [
    "CivVFillerItemData",
    "CivVItem",
    "CivVItemData",
    "CivVUsefulItemData",
    "FILLER_ITEMS",
    "ItemRequirements",
    "ITEMS_DATA",
    "ITEMS_DATA_BY_ID",
    "ITEM_GROUPS",
    "POLICY_ITEMS",
    "PROGRESSIVE_ERA_ITEM",
    "PROGRESSIVE_TECH_ITEMS",
    "TECH_ITEMS",
    "TRAP_ITEMS",
]


# %% GLOBALS
ITEMS_DATA: list["CivVItemData|CivVUsefulItemData|CivVFillerItemData"] = []
"List of all defined items"
ITEMS_DATA_BY_ID: dict[int, "CivVItemData|CivVUsefulItemData|CivVFillerItemData"] = {}
"Dict of all defined items, separated by AP ID"
ITEMS_DATA_BY_NAME: dict[str, "CivVItemData|CivVUsefulItemData|CivVFillerItemData"] = {}
"Dict of all defined items, separated by name"
ITEM_GROUPS: defaultdict[str, list[str]] = defaultdict(list)
"Dict of all defined item names per item group. Used by the CivVWorld"
FILLER_ITEMS: list["CivVFillerItemData"] = []
"List of all defined filler items"
TRAP_ITEMS: list["CivVFillerItemData"] = []
"List of all defined trap items"


# %% ITEM CLASS DEFINITION
class CivVItem(Item):
    game: str = GAME_NAME


# %% ITEM_REQUIREMENTS CLASS DEFINITION
@dataclass
class ItemRequirements:
    """
    Dataclass used for specifying the item requirements of a region or location.

    """

    always_requirements: dict[str, int] = field(default_factory=dict)
    "Dict of requirements that always apply"
    option_requirements: list[tuple[dict[str, int | str], dict[str, int]]] = field(default_factory=list)
    "Dict of requirements that only apply when specific options are used"

    @classmethod
    def create(cls, items: dict[str, int], when: dict[str, int | str] | None = None) -> "ItemRequirements":
        """
        Creates a new item requirements object.

        Args:
            items: Dict of required items names and their count to access this region or location.
            when: If set, only use these requirements when the given option names have the provided values

        """

        # Check that all items requested exist and are marked as progression
        for item_name in items.keys():
            if item_name not in ITEMS_DATA_BY_NAME:
                raise ValueError(f"Required item with name {item_name!r} does not exist")
            if ITEMS_DATA_BY_NAME[item_name].classification != ItemClassification.progression:
                raise ValueError(f"Required item with name {item_name!r} is not a progression item")

        # Create object according to the 'when' clause
        if when is None:
            return cls(always_requirements=items)
        else:
            return cls(option_requirements=[(when, items)])

    def __or__(self, other: "ItemRequirements") -> "ItemRequirements":
        # Combine the two requirements together
        return ItemRequirements(
            always_requirements=self.always_requirements|other.always_requirements,
            option_requirements=[*self.option_requirements, *other.option_requirements],
        )

    def create_access_rule(self, player: int, options: PerGameCommonOptions) -> Callable[[CollectionState], bool]:
        """
        Creates the access rule function for this instance and returns it.

        This function can be used as the access rule when creating :class:`Region` and :class:`Location` instances.

        """

        # Determine all the requirements that must be satisfied
        requirements = self.always_requirements
        for options_dct, requirements_dct in self.option_requirements:
            # Check if this options requirements applies and add it to the dict of requirements if so
            if all((getattr(options, name, None) == value for name, value in options_dct.items())):
                requirements = requirements | requirements_dct

        # Create rule function that uses the CollectionState to determine if region/location is reachable
        def rule(state: CollectionState) -> bool:
            return all((state.has(name, player, count) for name, count in requirements.items()))

        # Return created rule
        return rule


# %% ITEM_DATA CLASS DEFINITION
@dataclass
class CivVItemData:
    """
    Dataclass used for specifying an item.

    """

    name: str
    "Name of this item"
    type: CivVItemType
    "Type of this item"
    game_ids: list[int] | None
    "IDs of this item with this item type. If None, this item has no defined count"
    classification: ItemClassification
    "Classification of this item"
    count: int | None = field(init=False)
    "Number of times this item exists. If None, this item has no defined count"
    groups: set[CivVItemGroup | CivVItemType] = field(default_factory=set)
    "Set of groups this item belongs to. The type of this item is always part of this set"
    prefix: str | None = None
    "Prefix to use for this item's name. By default, the item type is used"
    ap_id: int = field(init=False)
    "ID of this item within AP"

    def __post_init__(self):
        # Add the item type as a prefix to the item name
        self.name = f"{self.prefix or to_title(self.type)} - {self.name}"

        # Set count for this item
        self.count = len(self.game_ids) if self.game_ids is not None else None

        # Set AP ID for this item
        self.ap_id = len(ITEMS_DATA) + ID_OFFSET

        # Make sure the item type is part of this item's groups set
        self.groups.add(self.type)

        # Add self to the dicts
        ITEMS_DATA.append(self)
        ITEMS_DATA_BY_ID[self.ap_id] = self
        ITEMS_DATA_BY_NAME[self.name] = self
        for group in self.groups:
            ITEM_GROUPS[str(group)].append(self.name)


@dataclass
class CivVUsefulItemData(CivVItemData):
    """
    Dataclass used for specifying an item.

    """

    game_ids: list[int]
    "IDs of this item with this item type"
    classification: Literal[ItemClassification.progression, ItemClassification.useful]
    "Classification of this item"
    count: int = field(init=False)
    "Number of times this item exists"


@dataclass
class CivVFillerItemData(CivVItemData):
    """
    Dataclass used for specifying a filler item.

    """

    game_ids: None = field(default=None, init=False)
    classification: Literal[ItemClassification.filler, ItemClassification.trap]
    weight: int = 1
    "Weight of this filler item"
    action: dict[CivVFillerType, int] = field(default_factory=dict)
    "Action to perform when this filler item is granted to the player"

    def __post_init__(self):
        # Call super method
        super().__post_init__()

        # Add self to proper filler item dict
        if self.classification == ItemClassification.filler:
            FILLER_ITEMS.extend([self] * self.weight)
        else:
            TRAP_ITEMS.extend([self] * self.weight)


# %% ITEM DECLARATIONS
PROGRESSIVE_ERA_ITEM = CivVUsefulItemData(
    name="Progressive",
    type=CivVItemType.era,
    game_ids=[169, 170, 171, 172, 173, 174, 175],
    classification=ItemClassification.progression,
)
"Progressive era item"


TECH_ITEMS = {
    "Pottery": CivVUsefulItemData(
        name="Pottery",
        type=CivVItemType.tech,
        game_ids=[1],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Animal Husbandry": CivVUsefulItemData(
        name="Animal Husbandry",
        type=CivVItemType.tech,
        game_ids=[2],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Archery": CivVUsefulItemData(
        name="Archery",
        type=CivVItemType.tech,
        game_ids=[3],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Mining": CivVUsefulItemData(
        name="Mining",
        type=CivVItemType.tech,
        game_ids=[4],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Sailing": CivVUsefulItemData(
        name="Sailing",
        type=CivVItemType.tech,
        game_ids=[5],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Calendar": CivVUsefulItemData(
        name="Calendar",
        type=CivVItemType.tech,
        game_ids=[6],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Writing": CivVUsefulItemData(
        name="Writing",
        type=CivVItemType.tech,
        game_ids=[7],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Trapping": CivVUsefulItemData(
        name="Trapping",
        type=CivVItemType.tech,
        game_ids=[8],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "The Wheel": CivVUsefulItemData(
        name="The Wheel",
        type=CivVItemType.tech,
        game_ids=[9],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Masonry": CivVUsefulItemData(
        name="Masonry",
        type=CivVItemType.tech,
        game_ids=[10],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Bronze Working": CivVUsefulItemData(
        name="Bronze Working",
        type=CivVItemType.tech,
        game_ids=[11],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Optics": CivVUsefulItemData(
        name="Optics",
        type=CivVItemType.tech,
        game_ids=[12],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Horseback Riding": CivVUsefulItemData(
        name="Horseback Riding",
        type=CivVItemType.tech,
        game_ids=[13],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Mathematics": CivVUsefulItemData(
        name="Mathematics",
        type=CivVItemType.tech,
        game_ids=[14],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Construction": CivVUsefulItemData(
        name="Construction",
        type=CivVItemType.tech,
        game_ids=[15],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Philosophy": CivVUsefulItemData(
        name="Philosophy",
        type=CivVItemType.tech,
        game_ids=[16],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Drama and Poetry": CivVUsefulItemData(
        name="Drama and Poetry",
        type=CivVItemType.tech,
        game_ids=[17],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Currency": CivVUsefulItemData(
        name="Currency",
        type=CivVItemType.tech,
        game_ids=[18],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Engineering": CivVUsefulItemData(
        name="Engineering",
        type=CivVItemType.tech,
        game_ids=[19],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Iron Working": CivVUsefulItemData(
        name="Iron Working",
        type=CivVItemType.tech,
        game_ids=[20],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Theology": CivVUsefulItemData(
        name="Theology",
        type=CivVItemType.tech,
        game_ids=[21],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Civil Service": CivVUsefulItemData(
        name="Civil Service",
        type=CivVItemType.tech,
        game_ids=[22],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Guilds": CivVUsefulItemData(
        name="Guilds",
        type=CivVItemType.tech,
        game_ids=[23],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Metal Casting": CivVUsefulItemData(
        name="Metal Casting",
        type=CivVItemType.tech,
        game_ids=[24],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Compass": CivVUsefulItemData(
        name="Compass",
        type=CivVItemType.tech,
        game_ids=[25],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Education": CivVUsefulItemData(
        name="Education",
        type=CivVItemType.tech,
        game_ids=[26],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Chivalry": CivVUsefulItemData(
        name="Chivalry",
        type=CivVItemType.tech,
        game_ids=[27],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Machinery": CivVUsefulItemData(
        name="Machinery",
        type=CivVItemType.tech,
        game_ids=[28],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Physics": CivVUsefulItemData(
        name="Physics",
        type=CivVItemType.tech,
        game_ids=[29],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Steel": CivVUsefulItemData(
        name="Steel",
        type=CivVItemType.tech,
        game_ids=[30],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Astronomy": CivVUsefulItemData(
        name="Astronomy",
        type=CivVItemType.tech,
        game_ids=[31],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Acoustics": CivVUsefulItemData(
        name="Acoustics",
        type=CivVItemType.tech,
        game_ids=[32],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Banking": CivVUsefulItemData(
        name="Banking",
        type=CivVItemType.tech,
        game_ids=[33],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Printing Press": CivVUsefulItemData(
        name="Printing Press",
        type=CivVItemType.tech,
        game_ids=[34],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Gunpowder": CivVUsefulItemData(
        name="Gunpowder",
        type=CivVItemType.tech,
        game_ids=[35],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Navigation": CivVUsefulItemData(
        name="Navigation",
        type=CivVItemType.tech,
        game_ids=[36],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Architecture": CivVUsefulItemData(
        name="Architecture",
        type=CivVItemType.tech,
        game_ids=[37],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Economics": CivVUsefulItemData(
        name="Economics",
        type=CivVItemType.tech,
        game_ids=[38],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Metallurgy": CivVUsefulItemData(
        name="Metallurgy",
        type=CivVItemType.tech,
        game_ids=[39],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Chemistry": CivVUsefulItemData(
        name="Chemistry",
        type=CivVItemType.tech,
        game_ids=[40],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Archaeology": CivVUsefulItemData(
        name="Archaeology",
        type=CivVItemType.tech,
        game_ids=[41],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Scientific Theory": CivVUsefulItemData(
        name="Scientific Theory",
        type=CivVItemType.tech,
        game_ids=[42],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Industrialization": CivVUsefulItemData(
        name="Industrialization",
        type=CivVItemType.tech,
        game_ids=[43],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Rifling": CivVUsefulItemData(
        name="Rifling",
        type=CivVItemType.tech,
        game_ids=[44],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Military Science": CivVUsefulItemData(
        name="Military Science",
        type=CivVItemType.tech,
        game_ids=[45],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Fertilizer": CivVUsefulItemData(
        name="Fertilizer",
        type=CivVItemType.tech,
        game_ids=[46],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Biology": CivVUsefulItemData(
        name="Biology",
        type=CivVItemType.tech,
        game_ids=[47],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Electricity": CivVUsefulItemData(
        name="Electricity",
        type=CivVItemType.tech,
        game_ids=[48],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Steam Power": CivVUsefulItemData(
        name="Steam Power",
        type=CivVItemType.tech,
        game_ids=[49],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Dynamite": CivVUsefulItemData(
        name="Dynamite",
        type=CivVItemType.tech,
        game_ids=[50],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Refrigeration": CivVUsefulItemData(
        name="Refrigeration",
        type=CivVItemType.tech,
        game_ids=[51],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Radio": CivVUsefulItemData(
        name="Radio",
        type=CivVItemType.tech,
        game_ids=[52],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Replaceable Parts": CivVUsefulItemData(
        name="Replaceable Parts",
        type=CivVItemType.tech,
        game_ids=[53],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Flight": CivVUsefulItemData(
        name="Flight",
        type=CivVItemType.tech,
        game_ids=[54],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Railroad": CivVUsefulItemData(
        name="Railroad",
        type=CivVItemType.tech,
        game_ids=[55],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Plastics": CivVUsefulItemData(
        name="Plastics",
        type=CivVItemType.tech,
        game_ids=[56],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Electronics": CivVUsefulItemData(
        name="Electronics",
        type=CivVItemType.tech,
        game_ids=[57],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Ballistics": CivVUsefulItemData(
        name="Ballistics",
        type=CivVItemType.tech,
        game_ids=[58],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Combustion": CivVUsefulItemData(
        name="Combustion",
        type=CivVItemType.tech,
        game_ids=[59],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Penicillin": CivVUsefulItemData(
        name="Penicillin",
        type=CivVItemType.tech,
        game_ids=[60],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Atomic Theory": CivVUsefulItemData(
        name="Atomic Theory",
        type=CivVItemType.tech,
        game_ids=[61],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Radar": CivVUsefulItemData(
        name="Radar",
        type=CivVItemType.tech,
        game_ids=[62],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Combined Arms": CivVUsefulItemData(
        name="Combined Arms",
        type=CivVItemType.tech,
        game_ids=[63],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Ecology": CivVUsefulItemData(
        name="Ecology",
        type=CivVItemType.tech,
        game_ids=[64],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Nuclear Fission": CivVUsefulItemData(
        name="Nuclear Fission",
        type=CivVItemType.tech,
        game_ids=[65],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Rocketry": CivVUsefulItemData(
        name="Rocketry",
        type=CivVItemType.tech,
        game_ids=[66],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Computers": CivVUsefulItemData(
        name="Computers",
        type=CivVItemType.tech,
        game_ids=[67],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Telecommunications": CivVUsefulItemData(
        name="Telecommunications",
        type=CivVItemType.tech,
        game_ids=[68],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Mobile Tactics": CivVUsefulItemData(
        name="Mobile Tactics",
        type=CivVItemType.tech,
        game_ids=[69],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Advanced Ballistics": CivVUsefulItemData(
        name="Advanced Ballistics",
        type=CivVItemType.tech,
        game_ids=[70],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Satellites": CivVUsefulItemData(
        name="Satellites",
        type=CivVItemType.tech,
        game_ids=[71],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Robotics": CivVUsefulItemData(
        name="Robotics",
        type=CivVItemType.tech,
        game_ids=[72],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Lasers": CivVUsefulItemData(
        name="Lasers",
        type=CivVItemType.tech,
        game_ids=[73],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "The Internet": CivVUsefulItemData(
        name="The Internet",
        type=CivVItemType.tech,
        game_ids=[74],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Globalization": CivVUsefulItemData(
        name="Globalization",
        type=CivVItemType.tech,
        game_ids=[75],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Particle Physics": CivVUsefulItemData(
        name="Particle Physics",
        type=CivVItemType.tech,
        game_ids=[76],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Nuclear Fusion": CivVUsefulItemData(
        name="Nuclear Fusion",
        type=CivVItemType.tech,
        game_ids=[77],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Nanotechnology": CivVUsefulItemData(
        name="Nanotechnology",
        type=CivVItemType.tech,
        game_ids=[78],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Stealth": CivVUsefulItemData(
        name="Stealth",
        type=CivVItemType.tech,
        game_ids=[79],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
}
"Dict of all technologies"


PROGRESSIVE_TECH_ITEMS = {
    "Progressive Growth": CivVUsefulItemData(
        name="Progressive Growth",
        type=CivVItemType.tech,
        game_ids=[1, 19, 22, 46, 47, 60],
        classification=ItemClassification.progression,
    ),
    "Progressive Production": CivVUsefulItemData(
        name="Progressive Production",
        type=CivVItemType.tech,
        game_ids=[4, 10, 24, 43, 64],
        classification=ItemClassification.progression,
    ),
    "Progressive Science": CivVUsefulItemData(
        name="Progressive Science",
        type=CivVItemType.tech,
        game_ids=[7, 26, 42, 56, 66, 70, 71, 76, 78],
        classification=ItemClassification.progression,
    ),
    "Progressive Culture": CivVUsefulItemData(
        name="Progressive Culture",
        type=CivVItemType.tech,
        game_ids=[17, 32, 41, 52, 68, 74],
        classification=ItemClassification.progression,
    ),
    "Progressive Gold": CivVUsefulItemData(
        name="Progressive Gold",
        type=CivVItemType.tech,
        game_ids=[2, 18, 23, 33, 38, 48, 75],
        classification=ItemClassification.progression,
    ),
    "Progressive Happiness": CivVUsefulItemData(
        name="Progressive Happiness",
        type=CivVItemType.tech,
        game_ids=[6, 8, 15, 34, 51],
        classification=ItemClassification.progression,
    ),
    "Progressive Exploration": CivVUsefulItemData(
        name="Progressive Exploration",
        type=CivVItemType.tech,
        game_ids=[5, 12, 25, 31],
        classification=ItemClassification.progression,
    ),
    "Progressive Melee Unit": CivVUsefulItemData(
        name="Progressive Melee Unit",
        type=CivVItemType.tech,
        game_ids=[11, 13, 20, 27, 30, 35, 39, 44, 45, 49, 53, 59, 63, 67, 69, 73, 77],
        classification=ItemClassification.progression,
    ),
    "Progressive Ranged Unit": CivVUsefulItemData(
        name="Progressive Ranged Unit",
        type=CivVItemType.tech,
        game_ids=[3, 28, 36, 54, 57, 58, 62, 72, 79],
        classification=ItemClassification.progression,
    ),
    "Progressive Siege Unit": CivVUsefulItemData(
        name="Progressive Siege Unit",
        type=CivVItemType.tech,
        game_ids=[14, 29, 40, 50, 61, 65],
        classification=ItemClassification.progression,
    ),
    "Progressive Misc": CivVUsefulItemData(
        name="Progressive Misc",
        type=CivVItemType.tech,
        game_ids=[9, 16, 21, 37, 55],
        classification=ItemClassification.progression,
    ),
}
"Dict of all progressive technologies"


POLICY_ITEMS = {
    "Liberty": CivVUsefulItemData(
        name="Liberty",
        type=CivVItemType.policy,
        game_ids=[0],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Collective Rule": CivVUsefulItemData(
        name="Collective Rule",
        type=CivVItemType.policy,
        game_ids=[1],
        classification=ItemClassification.useful,
    ),
    "Citizenship": CivVUsefulItemData(
        name="Citizenship",
        type=CivVItemType.policy,
        game_ids=[2],
        classification=ItemClassification.useful,
    ),
    "Republic": CivVUsefulItemData(
        name="Republic",
        type=CivVItemType.policy,
        game_ids=[3],
        classification=ItemClassification.useful,
    ),
    "Representation": CivVUsefulItemData(
        name="Representation",
        type=CivVItemType.policy,
        game_ids=[4],
        classification=ItemClassification.useful,
    ),
    "Meritocracy": CivVUsefulItemData(
        name="Meritocracy",
        type=CivVItemType.policy,
        game_ids=[5],
        classification=ItemClassification.useful,
    ),
    "Tradition": CivVUsefulItemData(
        name="Tradition",
        type=CivVItemType.policy,
        game_ids=[6],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Aristocracy": CivVUsefulItemData(
        name="Aristocracy",
        type=CivVItemType.policy,
        game_ids=[7],
        classification=ItemClassification.useful,
    ),
    "Oligarchy": CivVUsefulItemData(
        name="Oligarchy",
        type=CivVItemType.policy,
        game_ids=[8],
        classification=ItemClassification.useful,
    ),
    "Legalism": CivVUsefulItemData(
        name="Legalism",
        type=CivVItemType.policy,
        game_ids=[9],
        classification=ItemClassification.useful,
    ),
    "Landed Elite": CivVUsefulItemData(
        name="Landed Elite",
        type=CivVItemType.policy,
        game_ids=[10],
        classification=ItemClassification.useful,
    ),
    "Monarchy": CivVUsefulItemData(
        name="Monarchy",
        type=CivVItemType.policy,
        game_ids=[11],
        classification=ItemClassification.useful,
    ),
    "Honor": CivVUsefulItemData(
        name="Honor",
        type=CivVItemType.policy,
        game_ids=[12],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Warrior Code": CivVUsefulItemData(
        name="Warrior Code",
        type=CivVItemType.policy,
        game_ids=[13],
        classification=ItemClassification.useful,
    ),
    "Discipline": CivVUsefulItemData(
        name="Discipline",
        type=CivVItemType.policy,
        game_ids=[14],
        classification=ItemClassification.useful,
    ),
    "Military Tradition": CivVUsefulItemData(
        name="Military Tradition",
        type=CivVItemType.policy,
        game_ids=[15],
        classification=ItemClassification.useful,
    ),
    "Military Caste": CivVUsefulItemData(
        name="Military Caste",
        type=CivVItemType.policy,
        game_ids=[16],
        classification=ItemClassification.useful,
    ),
    "Professional Army": CivVUsefulItemData(
        name="Professional Army",
        type=CivVItemType.policy,
        game_ids=[17],
        classification=ItemClassification.useful,
    ),
    "Piety": CivVUsefulItemData(
        name="Piety",
        type=CivVItemType.policy,
        game_ids=[18],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Organized Religion": CivVUsefulItemData(
        name="Organized Religion",
        type=CivVItemType.policy,
        game_ids=[19],
        classification=ItemClassification.useful,
    ),
    "Mandate of Heaven": CivVUsefulItemData(
        name="Mandate of Heaven",
        type=CivVItemType.policy,
        game_ids=[20],
        classification=ItemClassification.useful,
    ),
    "Theocracy": CivVUsefulItemData(
        name="Theocracy",
        type=CivVItemType.policy,
        game_ids=[21],
        classification=ItemClassification.useful,
    ),
    "Reformation": CivVUsefulItemData(
        name="Reformation",
        type=CivVItemType.policy,
        game_ids=[22],
        classification=ItemClassification.useful,
    ),
    "Religious Tolerance": CivVUsefulItemData(
        name="Religious Tolerance",
        type=CivVItemType.policy,
        game_ids=[23],
        classification=ItemClassification.useful,
    ),
    "Patronage": CivVUsefulItemData(
        name="Patronage",
        type=CivVItemType.policy,
        game_ids=[24],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Philanthropy": CivVUsefulItemData(
        name="Philanthropy",
        type=CivVItemType.policy,
        game_ids=[25],
        classification=ItemClassification.progression,
    ),
    "Consulates": CivVUsefulItemData(
        name="Consulates",
        type=CivVItemType.policy,
        game_ids=[26],
        classification=ItemClassification.progression,
    ),
    "Scholasticism": CivVUsefulItemData(
        name="Scholasticism",
        type=CivVItemType.policy,
        game_ids=[27],
        classification=ItemClassification.useful,
    ),
    "Cultural Diplomacy": CivVUsefulItemData(
        name="Cultural Diplomacy",
        type=CivVItemType.policy,
        game_ids=[28],
        classification=ItemClassification.useful,
    ),
    "Merchant Confederacy": CivVUsefulItemData(
        name="Merchant Confederacy",
        type=CivVItemType.policy,
        game_ids=[29],
        classification=ItemClassification.useful,
    ),
    "Commerce": CivVUsefulItemData(
        name="Commerce",
        type=CivVItemType.policy,
        game_ids=[30],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Trade Unions": CivVUsefulItemData(
        name="Trade Unions",
        type=CivVItemType.policy,
        game_ids=[31],
        classification=ItemClassification.useful,
    ),
    "Entrepreneurship": CivVUsefulItemData(
        name="Entrepreneurship",
        type=CivVItemType.policy,
        game_ids=[32],
        classification=ItemClassification.useful,
    ),
    "Mercantilism": CivVUsefulItemData(
        name="Mercantilism",
        type=CivVItemType.policy,
        game_ids=[33],
        classification=ItemClassification.useful,
    ),
    "Caravans": CivVUsefulItemData(
        name="Caravans",
        type=CivVItemType.policy,
        game_ids=[34],
        classification=ItemClassification.useful,
    ),
    "Protectionism": CivVUsefulItemData(
        name="Protectionism",
        type=CivVItemType.policy,
        game_ids=[35],
        classification=ItemClassification.useful,
    ),
    "Rationalism": CivVUsefulItemData(
        name="Rationalism",
        type=CivVItemType.policy,
        game_ids=[36],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Secularism": CivVUsefulItemData(
        name="Secularism",
        type=CivVItemType.policy,
        game_ids=[37],
        classification=ItemClassification.useful,
    ),
    "Humanism": CivVUsefulItemData(
        name="Humanism",
        type=CivVItemType.policy,
        game_ids=[38],
        classification=ItemClassification.useful,
    ),
    "Free Thought": CivVUsefulItemData(
        name="Free Thought",
        type=CivVItemType.policy,
        game_ids=[39],
        classification=ItemClassification.useful,
    ),
    "Sovereignty": CivVUsefulItemData(
        name="Sovereignty",
        type=CivVItemType.policy,
        game_ids=[40],
        classification=ItemClassification.useful,
    ),
    "Scientific Revolution": CivVUsefulItemData(
        name="Scientific Revolution",
        type=CivVItemType.policy,
        game_ids=[41],
        classification=ItemClassification.useful,
    ),
    "Tradition Finisher": CivVUsefulItemData(
        name="Tradition Finisher",
        type=CivVItemType.policy,
        game_ids=[42],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Liberty Finisher": CivVUsefulItemData(
        name="Liberty Finisher",
        type=CivVItemType.policy,
        game_ids=[43],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Honor Finisher": CivVUsefulItemData(
        name="Honor Finisher",
        type=CivVItemType.policy,
        game_ids=[44],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Piety Finisher": CivVUsefulItemData(
        name="Piety Finisher",
        type=CivVItemType.policy,
        game_ids=[45],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Patronage Finisher": CivVUsefulItemData(
        name="Patronage Finisher",
        type=CivVItemType.policy,
        game_ids=[46],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Commerce Finisher": CivVUsefulItemData(
        name="Commerce Finisher",
        type=CivVItemType.policy,
        game_ids=[47],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Rationalism Finisher": CivVUsefulItemData(
        name="Rationalism Finisher",
        type=CivVItemType.policy,
        game_ids=[48],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Aesthetics": CivVUsefulItemData(
        name="Aesthetics",
        type=CivVItemType.policy,
        game_ids=[49],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Cultural Centers": CivVUsefulItemData(
        name="Cultural Centers",
        type=CivVItemType.policy,
        game_ids=[50],
        classification=ItemClassification.useful,
    ),
    "Fine Arts": CivVUsefulItemData(
        name="Fine Arts",
        type=CivVItemType.policy,
        game_ids=[51],
        classification=ItemClassification.useful,
    ),
    "Flourishing of the Arts": CivVUsefulItemData(
        name="Flourishing of the Arts",
        type=CivVItemType.policy,
        game_ids=[52],
        classification=ItemClassification.useful,
    ),
    "Artistic Genius": CivVUsefulItemData(
        name="Artistic Genius",
        type=CivVItemType.policy,
        game_ids=[53],
        classification=ItemClassification.useful,
    ),
    "Cultural Exchange": CivVUsefulItemData(
        name="Cultural Exchange",
        type=CivVItemType.policy,
        game_ids=[54],
        classification=ItemClassification.progression,
    ),
    "Aesthetics Finisher": CivVUsefulItemData(
        name="Aesthetics Finisher",
        type=CivVItemType.policy,
        game_ids=[55],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Exploration": CivVUsefulItemData(
        name="Exploration",
        type=CivVItemType.policy,
        game_ids=[56],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Maritime Infrastructure": CivVUsefulItemData(
        name="Maritime Infrastructure",
        type=CivVItemType.policy,
        game_ids=[57],
        classification=ItemClassification.useful,
    ),
    "Naval Tradition": CivVUsefulItemData(
        name="Naval Tradition",
        type=CivVItemType.policy,
        game_ids=[58],
        classification=ItemClassification.useful,
    ),
    "Merchant Navy": CivVUsefulItemData(
        name="Merchant Navy",
        type=CivVItemType.policy,
        game_ids=[59],
        classification=ItemClassification.useful,
    ),
    "Navigation School": CivVUsefulItemData(
        name="Navigation School",
        type=CivVItemType.policy,
        game_ids=[60],
        classification=ItemClassification.useful,
    ),
    "Treasure Fleets": CivVUsefulItemData(
        name="Treasure Fleets",
        type=CivVItemType.policy,
        game_ids=[61],
        classification=ItemClassification.useful,
    ),
    "Exploration Finisher": CivVUsefulItemData(
        name="Exploration Finisher",
        type=CivVItemType.policy,
        game_ids=[62],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
}
"Dict of all policies"


# %% FILLER ITEM DEFINITIONS
GOLD_FILLER_ITEMS = {
    "Minor Gold": CivVFillerItemData(
        name="Minor Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_gold: 100,
        }
    ),
    "Gold": CivVFillerItemData(
        name="Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_gold: 250,
        }
    ),
    "Major Gold": CivVFillerItemData(
        name="Major Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_gold: 1000,
        }
    ),
}
"Dict of all gold filler items"


CULTURE_FILLER_ITEMS = {
    "Minor Culture": CivVFillerItemData(
        name="Minor Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_culture: 100,
        }
    ),
    "Culture": CivVFillerItemData(
        name="Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_culture: 250,
        }
    ),
    "Major Culture": CivVFillerItemData(
        name="Major Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_culture: 1000,
        }
    ),
}
"Dict of all culture filler items"


FAITH_FILLER_ITEMS = {
    "Minor Faith": CivVFillerItemData(
        name="Minor Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_faith: 50,
        }
    ),
    "Faith": CivVFillerItemData(
        name="Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_faith: 125,
        }
    ),
    "Major Faith": CivVFillerItemData(
        name="Major Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_faith: 500,
        }
    ),
}
"Dict of all faith filler items"


FREE_FILLER_ITEMS = {
    "Free Great Person": CivVFillerItemData(
        name="Free Great Person",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_great_people: 1,
        }
    ),
    "Free Policy": CivVFillerItemData(
        name="Free Policy",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_policies: 1,
        }
    ),
    "Free Tech": CivVFillerItemData(
        name="Free Tech",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_techs: 1,
        }
    ),
}
"Dict of free reward filler items"


ALL_CITY_POPULATION_FILLER_ITEMS = {
    "All City Population +1": CivVFillerItemData(
        name="All City Population +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_all_city_population: 1,
        }
    ),
    "All City Population +2": CivVFillerItemData(
        name="All City Population +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_all_city_population: 2,
        }
    ),
}
"Dict of city population filler items"


NEW_CITY_EXTRA_POPULATION_FILLER_ITEMS = {
    "New City Extra Population +1": CivVFillerItemData(
        name="New City Extra Population +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_new_city_extra_population: 1,
        }
    ),
    "New City Extra Population +2": CivVFillerItemData(
        name="New City Extra Population +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_new_city_extra_population: 2,
        }
    ),
}
"Dict of extra population in newly founded cities filler items"


EXTRA_HAPPINESS_PER_CITY_FILLER_ITEM = CivVFillerItemData(
    name="Extra Happiness Per City",
    type=CivVItemType.bonus,
    classification=ItemClassification.filler,
    weight=2,
    action={
        CivVFillerType.change_extra_happiness_per_city: 1,
    }
)
"Extra happiness per city filler item"


GOLDEN_AGE_FILLER_ITEM = CivVFillerItemData(
    name="Golden Age",
    type=CivVItemType.bonus,
    classification=ItemClassification.filler,
    weight=1,
    action={
        CivVFillerType.start_golden_age: 1,
    }
)
"Golden age filler item"


# %% TRAP ITEM DEFINITIONS
GOLD_TRAP_ITEMS = {
    "Minor Gold": CivVFillerItemData(
        name="Minor Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_gold: -50,
        }
    ),
    "Gold": CivVFillerItemData(
        name="Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_gold: -100,
        }
    ),
    "Major Gold": CivVFillerItemData(
        name="Major Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_gold: -250,
        }
    ),
}
"Dict of all gold trap items"


CULTURE_TRAP_ITEMS = {
    "Minor Culture": CivVFillerItemData(
        name="Minor Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_culture: -50,
        }
    ),
    "Culture": CivVFillerItemData(
        name="Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_culture: -100,
        }
    ),
    "Major Culture": CivVFillerItemData(
        name="Major Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_culture: -250,
        }
    ),
}
"Dict of all culture trap items"


FAITH_TRAP_ITEMS = {
    "Minor Faith": CivVFillerItemData(
        name="Minor Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_faith: -25,
        }
    ),
    "Faith": CivVFillerItemData(
        name="Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_faith: -50,
        }
    ),
    "Major Faith": CivVFillerItemData(
        name="Major Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_faith: -125,
        }
    ),
}
"Dict of all faith trap items"


ALL_CITY_POPULATION_TRAP_ITEMS = {
    "All City Population -1": CivVFillerItemData(
        name="All City Population -1",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=5,
        action={
            CivVFillerType.change_all_city_population: -1,
        }
    ),
    "All City Population -2": CivVFillerItemData(
        name="All City Population -2",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=2,
        action={
            CivVFillerType.change_all_city_population: -2,
        }
    ),
}
"Dict of city population trap items"


DENOUNCE_TRAP_ITEM = CivVFillerItemData(
    name="Denounce",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=2,
    action={
        CivVFillerType.denounce_random: 1,
    }
)
"Denounce trap item"


WAR_TRAP_ITEM = CivVFillerItemData(
    name="War",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=1,
    action={
        CivVFillerType.declare_war_random: 1,
    }
)
"War trap item"
