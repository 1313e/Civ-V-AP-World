# %% IMPORTS
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field

from BaseClasses import CollectionState, ItemClassification, Item

from .constants import GAME_NAME, ID_OFFSET
from .enums import CivVItemGroup, CivVItemType
from .helpers import to_title
from .options import CivVOptions

# All declaration
__all__ = [
    "CivVItem",
    "CivVItemData",
    "ItemRequirements",
    "ITEMS_DATA",
    "ITEMS_DATA_BY_ID",
    "ITEM_GROUPS",
    "POLICY_ITEMS",
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


# %% ITEM_REQUIREMENTS CLASS DEFINITION
@dataclass
class ItemRequirements:
    """
    Dataclass used for specifying the item requirements of a region or location within Civ V.

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

    def create_access_rule(self, player: int, options: CivVOptions) -> Callable[[CollectionState], bool]:
        """
        Creates the access rule function for this instance and returns it.

        This function can be used as the access rule when creating :class:`Region` and :class:`Location` instances.

        """

        # Determine all the requirements that must be satisfied
        requirements = self.always_requirements
        for options_dct, requirements_dct in self.option_requirements:
            # Check if this options requirements applies and add it to the dict of requirements if so
            if all((getattr(options, name, None) == value for name, value in options_dct.items())):
                requirements |= requirements_dct

        # Create rule function that uses the CollectionState to determine if region/location is reachable
        def rule(state: CollectionState) -> bool:
            return all((state.has(name, player, count) for name, count in requirements.items()))

        # Return created rule
        return rule


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
    prefix: str | None = None
    "Prefix to use for this item's name. By default, the item type is used"
    ap_id: int = field(init=False)
    "ID of this item within AP"

    def __post_init__(self):
        # Add the item type as a prefix to the item name
        self.name = f"{self.prefix or to_title(self.type)} - {self.name}"

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

TECH_ITEMS = {
    "Pottery": CivVItemData(
        name="Pottery",
        type=CivVItemType.tech,
        game_ids=[1],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Animal Husbandry": CivVItemData(
        name="Animal Husbandry",
        type=CivVItemType.tech,
        game_ids=[2],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Archery": CivVItemData(
        name="Archery",
        type=CivVItemType.tech,
        game_ids=[3],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Mining": CivVItemData(
        name="Mining",
        type=CivVItemType.tech,
        game_ids=[4],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Sailing": CivVItemData(
        name="Sailing",
        type=CivVItemType.tech,
        game_ids=[5],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Calendar": CivVItemData(
        name="Calendar",
        type=CivVItemType.tech,
        game_ids=[6],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Writing": CivVItemData(
        name="Writing",
        type=CivVItemType.tech,
        game_ids=[7],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Trapping": CivVItemData(
        name="Trapping",
        type=CivVItemType.tech,
        game_ids=[8],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "The Wheel": CivVItemData(
        name="The Wheel",
        type=CivVItemType.tech,
        game_ids=[9],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Masonry": CivVItemData(
        name="Masonry",
        type=CivVItemType.tech,
        game_ids=[10],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Bronze Working": CivVItemData(
        name="Bronze Working",
        type=CivVItemType.tech,
        game_ids=[11],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.ancient_era},
    ),
    "Optics": CivVItemData(
        name="Optics",
        type=CivVItemType.tech,
        game_ids=[12],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Horseback Riding": CivVItemData(
        name="Horseback Riding",
        type=CivVItemType.tech,
        game_ids=[13],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Mathematics": CivVItemData(
        name="Mathematics",
        type=CivVItemType.tech,
        game_ids=[14],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Construction": CivVItemData(
        name="Construction",
        type=CivVItemType.tech,
        game_ids=[15],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Philosophy": CivVItemData(
        name="Philosophy",
        type=CivVItemType.tech,
        game_ids=[16],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Drama and Poetry": CivVItemData(
        name="Drama and Poetry",
        type=CivVItemType.tech,
        game_ids=[17],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Currency": CivVItemData(
        name="Currency",
        type=CivVItemType.tech,
        game_ids=[18],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Engineering": CivVItemData(
        name="Engineering",
        type=CivVItemType.tech,
        game_ids=[19],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Iron Working": CivVItemData(
        name="Iron Working",
        type=CivVItemType.tech,
        game_ids=[20],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.classical_era},
    ),
    "Theology": CivVItemData(
        name="Theology",
        type=CivVItemType.tech,
        game_ids=[21],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Civil Service": CivVItemData(
        name="Civil Service",
        type=CivVItemType.tech,
        game_ids=[22],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Guilds": CivVItemData(
        name="Guilds",
        type=CivVItemType.tech,
        game_ids=[23],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Metal Casting": CivVItemData(
        name="Metal Casting",
        type=CivVItemType.tech,
        game_ids=[24],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Compass": CivVItemData(
        name="Compass",
        type=CivVItemType.tech,
        game_ids=[25],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Education": CivVItemData(
        name="Education",
        type=CivVItemType.tech,
        game_ids=[26],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Chivalry": CivVItemData(
        name="Chivalry",
        type=CivVItemType.tech,
        game_ids=[27],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Machinery": CivVItemData(
        name="Machinery",
        type=CivVItemType.tech,
        game_ids=[28],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Physics": CivVItemData(
        name="Physics",
        type=CivVItemType.tech,
        game_ids=[29],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Steel": CivVItemData(
        name="Steel",
        type=CivVItemType.tech,
        game_ids=[30],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.medieval_era},
    ),
    "Astronomy": CivVItemData(
        name="Astronomy",
        type=CivVItemType.tech,
        game_ids=[31],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Acoustics": CivVItemData(
        name="Acoustics",
        type=CivVItemType.tech,
        game_ids=[32],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Banking": CivVItemData(
        name="Banking",
        type=CivVItemType.tech,
        game_ids=[33],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Printing Press": CivVItemData(
        name="Printing Press",
        type=CivVItemType.tech,
        game_ids=[34],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Gunpowder": CivVItemData(
        name="Gunpowder",
        type=CivVItemType.tech,
        game_ids=[35],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Navigation": CivVItemData(
        name="Navigation",
        type=CivVItemType.tech,
        game_ids=[36],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Architecture": CivVItemData(
        name="Architecture",
        type=CivVItemType.tech,
        game_ids=[37],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Economics": CivVItemData(
        name="Economics",
        type=CivVItemType.tech,
        game_ids=[38],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Metallurgy": CivVItemData(
        name="Metallurgy",
        type=CivVItemType.tech,
        game_ids=[39],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Chemistry": CivVItemData(
        name="Chemistry",
        type=CivVItemType.tech,
        game_ids=[40],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.renaissance_era},
    ),
    "Archaeology": CivVItemData(
        name="Archaeology",
        type=CivVItemType.tech,
        game_ids=[41],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Scientific Theory": CivVItemData(
        name="Scientific Theory",
        type=CivVItemType.tech,
        game_ids=[42],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Industrialization": CivVItemData(
        name="Industrialization",
        type=CivVItemType.tech,
        game_ids=[43],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Rifling": CivVItemData(
        name="Rifling",
        type=CivVItemType.tech,
        game_ids=[44],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Military Science": CivVItemData(
        name="Military Science",
        type=CivVItemType.tech,
        game_ids=[45],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Fertilizer": CivVItemData(
        name="Fertilizer",
        type=CivVItemType.tech,
        game_ids=[46],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Biology": CivVItemData(
        name="Biology",
        type=CivVItemType.tech,
        game_ids=[47],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Electricity": CivVItemData(
        name="Electricity",
        type=CivVItemType.tech,
        game_ids=[48],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Steam Power": CivVItemData(
        name="Steam Power",
        type=CivVItemType.tech,
        game_ids=[49],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Dynamite": CivVItemData(
        name="Dynamite",
        type=CivVItemType.tech,
        game_ids=[50],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.industrial_era},
    ),
    "Refrigeration": CivVItemData(
        name="Refrigeration",
        type=CivVItemType.tech,
        game_ids=[51],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Radio": CivVItemData(
        name="Radio",
        type=CivVItemType.tech,
        game_ids=[52],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Replaceable Parts": CivVItemData(
        name="Replaceable Parts",
        type=CivVItemType.tech,
        game_ids=[53],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Flight": CivVItemData(
        name="Flight",
        type=CivVItemType.tech,
        game_ids=[54],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Railroad": CivVItemData(
        name="Railroad",
        type=CivVItemType.tech,
        game_ids=[55],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Plastics": CivVItemData(
        name="Plastics",
        type=CivVItemType.tech,
        game_ids=[56],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Electronics": CivVItemData(
        name="Electronics",
        type=CivVItemType.tech,
        game_ids=[57],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Ballistics": CivVItemData(
        name="Ballistics",
        type=CivVItemType.tech,
        game_ids=[58],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Combustion": CivVItemData(
        name="Combustion",
        type=CivVItemType.tech,
        game_ids=[59],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.modern_era},
    ),
    "Penicillin": CivVItemData(
        name="Penicillin",
        type=CivVItemType.tech,
        game_ids=[60],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Atomic Theory": CivVItemData(
        name="Atomic Theory",
        type=CivVItemType.tech,
        game_ids=[61],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Radar": CivVItemData(
        name="Radar",
        type=CivVItemType.tech,
        game_ids=[62],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Combined Arms": CivVItemData(
        name="Combined Arms",
        type=CivVItemType.tech,
        game_ids=[63],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Ecology": CivVItemData(
        name="Ecology",
        type=CivVItemType.tech,
        game_ids=[64],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Nuclear Fission": CivVItemData(
        name="Nuclear Fission",
        type=CivVItemType.tech,
        game_ids=[65],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Rocketry": CivVItemData(
        name="Rocketry",
        type=CivVItemType.tech,
        game_ids=[66],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Computers": CivVItemData(
        name="Computers",
        type=CivVItemType.tech,
        game_ids=[67],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.atomic_era},
    ),
    "Telecommunications": CivVItemData(
        name="Telecommunications",
        type=CivVItemType.tech,
        game_ids=[68],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Mobile Tactics": CivVItemData(
        name="Mobile Tactics",
        type=CivVItemType.tech,
        game_ids=[69],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Advanced Ballistics": CivVItemData(
        name="Advanced Ballistics",
        type=CivVItemType.tech,
        game_ids=[70],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Satellites": CivVItemData(
        name="Satellites",
        type=CivVItemType.tech,
        game_ids=[71],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Robotics": CivVItemData(
        name="Robotics",
        type=CivVItemType.tech,
        game_ids=[72],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Lasers": CivVItemData(
        name="Lasers",
        type=CivVItemType.tech,
        game_ids=[73],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "The Internet": CivVItemData(
        name="The Internet",
        type=CivVItemType.tech,
        game_ids=[74],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Globalization": CivVItemData(
        name="Globalization",
        type=CivVItemType.tech,
        game_ids=[75],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Particle Physics": CivVItemData(
        name="Particle Physics",
        type=CivVItemType.tech,
        game_ids=[76],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Nuclear Fusion": CivVItemData(
        name="Nuclear Fusion",
        type=CivVItemType.tech,
        game_ids=[77],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Nanotechnology": CivVItemData(
        name="Nanotechnology",
        type=CivVItemType.tech,
        game_ids=[78],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
    "Stealth": CivVItemData(
        name="Stealth",
        type=CivVItemType.tech,
        game_ids=[79],
        classification=ItemClassification.progression,
        groups={CivVItemGroup.information_era},
    ),
}
"Dict of all technologies within Civ V"

PROGRESSIVE_TECH_ITEMS = {
    "Progressive Growth": CivVItemData(
        name="Progressive Growth",
        type=CivVItemType.tech,
        game_ids=[1, 19, 22, 46, 47, 60],
        classification=ItemClassification.progression,
    ),
    "Progressive Production": CivVItemData(
        name="Progressive Production",
        type=CivVItemType.tech,
        game_ids=[4, 10, 24, 43, 64],
        classification=ItemClassification.progression,
    ),
    "Progressive Science": CivVItemData(
        name="Progressive Science",
        type=CivVItemType.tech,
        game_ids=[7, 26, 42, 56, 66, 70, 71, 76, 78],
        classification=ItemClassification.progression,
    ),
    "Progressive Culture": CivVItemData(
        name="Progressive Culture",
        type=CivVItemType.tech,
        game_ids=[16, 17, 32, 41, 52, 68, 74],
        classification=ItemClassification.progression,
    ),
    "Progressive Gold": CivVItemData(
        name="Progressive Gold",
        type=CivVItemType.tech,
        game_ids=[2, 18, 23, 33, 38, 48],
        classification=ItemClassification.progression,
    ),
    "Progressive Happiness": CivVItemData(
        name="Progressive Happiness",
        type=CivVItemType.tech,
        game_ids=[6, 8, 15, 34, 51],
        classification=ItemClassification.progression,
    ),
    "Progressive Exploration": CivVItemData(
        name="Progressive Exploration",
        type=CivVItemType.tech,
        game_ids=[5, 12, 25, 31],
        classification=ItemClassification.progression,
    ),
    "Progressive Melee Unit": CivVItemData(
        name="Progressive Melee Unit",
        type=CivVItemType.tech,
        game_ids=[11, 13, 20, 27, 30, 35, 39, 44, 45, 49, 53, 59, 63, 67, 69, 73, 77],
        classification=ItemClassification.progression,
    ),
    "Progressive Ranged Unit": CivVItemData(
        name="Progressive Ranged Unit",
        type=CivVItemType.tech,
        game_ids=[3, 28, 36, 54, 57, 58, 62, 72, 79],
        classification=ItemClassification.progression,
    ),
    "Progressive Siege Unit": CivVItemData(
        name="Progressive Siege Unit",
        type=CivVItemType.tech,
        game_ids=[14, 29, 40, 50],
        classification=ItemClassification.progression,
    ),
    "Progressive Misc": CivVItemData(
        name="Progressive Misc",
        type=CivVItemType.tech,
        game_ids=[9, 21, 37, 55, 61, 65, 75],
        classification=ItemClassification.progression,
    ),
}
"Dict of all progressive technologies within Civ V"


POLICY_ITEMS = {
    "Liberty": CivVItemData(
        name="Liberty",
        type=CivVItemType.policy,
        game_ids=[0],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Collective Rule": CivVItemData(
        name="Collective Rule",
        type=CivVItemType.policy,
        game_ids=[1],
        classification=ItemClassification.useful,
    ),
    "Citizenship": CivVItemData(
        name="Citizenship",
        type=CivVItemType.policy,
        game_ids=[2],
        classification=ItemClassification.useful,
    ),
    "Republic": CivVItemData(
        name="Republic",
        type=CivVItemType.policy,
        game_ids=[3],
        classification=ItemClassification.useful,
    ),
    "Representation": CivVItemData(
        name="Representation",
        type=CivVItemType.policy,
        game_ids=[4],
        classification=ItemClassification.useful,
    ),
    "Meritocracy": CivVItemData(
        name="Meritocracy",
        type=CivVItemType.policy,
        game_ids=[5],
        classification=ItemClassification.useful,
    ),
    "Tradition": CivVItemData(
        name="Tradition",
        type=CivVItemType.policy,
        game_ids=[6],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Aristocracy": CivVItemData(
        name="Aristocracy",
        type=CivVItemType.policy,
        game_ids=[7],
        classification=ItemClassification.useful,
    ),
    "Oligarchy": CivVItemData(
        name="Oligarchy",
        type=CivVItemType.policy,
        game_ids=[8],
        classification=ItemClassification.useful,
    ),
    "Legalism": CivVItemData(
        name="Legalism",
        type=CivVItemType.policy,
        game_ids=[9],
        classification=ItemClassification.useful,
    ),
    "Landed Elite": CivVItemData(
        name="Landed Elite",
        type=CivVItemType.policy,
        game_ids=[10],
        classification=ItemClassification.useful,
    ),
    "Monarchy": CivVItemData(
        name="Monarchy",
        type=CivVItemType.policy,
        game_ids=[11],
        classification=ItemClassification.useful,
    ),
    "Honor": CivVItemData(
        name="Honor",
        type=CivVItemType.policy,
        game_ids=[12],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Warrior Code": CivVItemData(
        name="Warrior Code",
        type=CivVItemType.policy,
        game_ids=[13],
        classification=ItemClassification.useful,
    ),
    "Discipline": CivVItemData(
        name="Discipline",
        type=CivVItemType.policy,
        game_ids=[14],
        classification=ItemClassification.useful,
    ),
    "Military Tradition": CivVItemData(
        name="Military Tradition",
        type=CivVItemType.policy,
        game_ids=[15],
        classification=ItemClassification.useful,
    ),
    "Military Caste": CivVItemData(
        name="Military Caste",
        type=CivVItemType.policy,
        game_ids=[16],
        classification=ItemClassification.useful,
    ),
    "Professional Army": CivVItemData(
        name="Professional Army",
        type=CivVItemType.policy,
        game_ids=[17],
        classification=ItemClassification.useful,
    ),
    "Piety": CivVItemData(
        name="Piety",
        type=CivVItemType.policy,
        game_ids=[18],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Organized Religion": CivVItemData(
        name="Organized Religion",
        type=CivVItemType.policy,
        game_ids=[19],
        classification=ItemClassification.useful,
    ),
    "Mandate of Heaven": CivVItemData(
        name="Mandate of Heaven",
        type=CivVItemType.policy,
        game_ids=[20],
        classification=ItemClassification.useful,
    ),
    "Theocracy": CivVItemData(
        name="Theocracy",
        type=CivVItemType.policy,
        game_ids=[21],
        classification=ItemClassification.useful,
    ),
    "Reformation": CivVItemData(
        name="Reformation",
        type=CivVItemType.policy,
        game_ids=[22],
        classification=ItemClassification.useful,
    ),
    "Religious Tolerance": CivVItemData(
        name="Religious Tolerance",
        type=CivVItemType.policy,
        game_ids=[23],
        classification=ItemClassification.useful,
    ),
    "Patronage": CivVItemData(
        name="Patronage",
        type=CivVItemType.policy,
        game_ids=[24],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Philanthropy": CivVItemData(
        name="Philanthropy",
        type=CivVItemType.policy,
        game_ids=[25],
        classification=ItemClassification.useful,
    ),
    "Consulates": CivVItemData(
        name="Consulates",
        type=CivVItemType.policy,
        game_ids=[26],
        classification=ItemClassification.useful,
    ),
    "Scholasticism": CivVItemData(
        name="Scholasticism",
        type=CivVItemType.policy,
        game_ids=[27],
        classification=ItemClassification.useful,
    ),
    "Cultural Diplomacy": CivVItemData(
        name="Cultural Diplomacy",
        type=CivVItemType.policy,
        game_ids=[28],
        classification=ItemClassification.useful,
    ),
    "Merchant Confederacy": CivVItemData(
        name="Merchant Confederacy",
        type=CivVItemType.policy,
        game_ids=[29],
        classification=ItemClassification.useful,
    ),
    "Commerce": CivVItemData(
        name="Commerce",
        type=CivVItemType.policy,
        game_ids=[30],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Trade Unions": CivVItemData(
        name="Trade Unions",
        type=CivVItemType.policy,
        game_ids=[31],
        classification=ItemClassification.useful,
    ),
    "Entrepreneurship": CivVItemData(
        name="Entrepreneurship",
        type=CivVItemType.policy,
        game_ids=[32],
        classification=ItemClassification.useful,
    ),
    "Mercantilism": CivVItemData(
        name="Mercantilism",
        type=CivVItemType.policy,
        game_ids=[33],
        classification=ItemClassification.useful,
    ),
    "Caravans": CivVItemData(
        name="Caravans",
        type=CivVItemType.policy,
        game_ids=[34],
        classification=ItemClassification.useful,
    ),
    "Protectionism": CivVItemData(
        name="Protectionism",
        type=CivVItemType.policy,
        game_ids=[35],
        classification=ItemClassification.useful,
    ),
    "Rationalism": CivVItemData(
        name="Rationalism",
        type=CivVItemType.policy,
        game_ids=[36],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Secularism": CivVItemData(
        name="Secularism",
        type=CivVItemType.policy,
        game_ids=[37],
        classification=ItemClassification.useful,
    ),
    "Humanism": CivVItemData(
        name="Humanism",
        type=CivVItemType.policy,
        game_ids=[38],
        classification=ItemClassification.useful,
    ),
    "Free Thought": CivVItemData(
        name="Free Thought",
        type=CivVItemType.policy,
        game_ids=[39],
        classification=ItemClassification.useful,
    ),
    "Sovereignty": CivVItemData(
        name="Sovereignty",
        type=CivVItemType.policy,
        game_ids=[40],
        classification=ItemClassification.useful,
    ),
    "Scientific Revolution": CivVItemData(
        name="Scientific Revolution",
        type=CivVItemType.policy,
        game_ids=[41],
        classification=ItemClassification.useful,
    ),
    "Tradition Finisher": CivVItemData(
        name="Tradition Finisher",
        type=CivVItemType.policy,
        game_ids=[42],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Liberty Finisher": CivVItemData(
        name="Liberty Finisher",
        type=CivVItemType.policy,
        game_ids=[43],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Honor Finisher": CivVItemData(
        name="Honor Finisher",
        type=CivVItemType.policy,
        game_ids=[44],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Piety Finisher": CivVItemData(
        name="Piety Finisher",
        type=CivVItemType.policy,
        game_ids=[45],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Patronage Finisher": CivVItemData(
        name="Patronage Finisher",
        type=CivVItemType.policy,
        game_ids=[46],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Commerce Finisher": CivVItemData(
        name="Commerce Finisher",
        type=CivVItemType.policy,
        game_ids=[47],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Rationalism Finisher": CivVItemData(
        name="Rationalism Finisher",
        type=CivVItemType.policy,
        game_ids=[48],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Aesthetics": CivVItemData(
        name="Aesthetics",
        type=CivVItemType.policy,
        game_ids=[49],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Cultural Centers": CivVItemData(
        name="Cultural Centers",
        type=CivVItemType.policy,
        game_ids=[50],
        classification=ItemClassification.useful,
    ),
    "Fine Arts": CivVItemData(
        name="Fine Arts",
        type=CivVItemType.policy,
        game_ids=[51],
        classification=ItemClassification.useful,
    ),
    "Flourishing of the Arts": CivVItemData(
        name="Flourishing of the Arts",
        type=CivVItemType.policy,
        game_ids=[52],
        classification=ItemClassification.useful,
    ),
    "Artistic Genius": CivVItemData(
        name="Artistic Genius",
        type=CivVItemType.policy,
        game_ids=[53],
        classification=ItemClassification.useful,
    ),
    "Cultural Exchange": CivVItemData(
        name="Cultural Exchange",
        type=CivVItemType.policy,
        game_ids=[54],
        classification=ItemClassification.useful,
    ),
    "Aesthetics Finisher": CivVItemData(
        name="Aesthetics Finisher",
        type=CivVItemType.policy,
        game_ids=[55],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
    "Exploration": CivVItemData(
        name="Exploration",
        type=CivVItemType.policy,
        game_ids=[56],
        classification=ItemClassification.progression,
        prefix="Policy Branch",
    ),
    "Maritime Infrastructure": CivVItemData(
        name="Maritime Infrastructure",
        type=CivVItemType.policy,
        game_ids=[57],
        classification=ItemClassification.useful,
    ),
    "Naval Tradition": CivVItemData(
        name="Naval Tradition",
        type=CivVItemType.policy,
        game_ids=[58],
        classification=ItemClassification.useful,
    ),
    "Merchant Navy": CivVItemData(
        name="Merchant Navy",
        type=CivVItemType.policy,
        game_ids=[59],
        classification=ItemClassification.useful,
    ),
    "Navigation School": CivVItemData(
        name="Navigation School",
        type=CivVItemType.policy,
        game_ids=[60],
        classification=ItemClassification.useful,
    ),
    "Treasure Fleets": CivVItemData(
        name="Treasure Fleets",
        type=CivVItemType.policy,
        game_ids=[61],
        classification=ItemClassification.useful,
    ),
    "Exploration Finisher": CivVItemData(
        name="Exploration Finisher",
        type=CivVItemType.policy,
        game_ids=[62],
        classification=ItemClassification.useful,
        prefix="Policy Branch",
    ),
}
"Dict of all policies within Civ V"
