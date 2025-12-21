# %% IMPORTS
from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Literal

from BaseClasses import CollectionState, ItemClassification, Item
from Options import PerGameCommonOptions

from ..constants import GAME_NAME, ID_OFFSET
from ..enums import CivVFillerType, CivVItemGroup, CivVItemType
from ..helpers import to_title


# All declaration
__all__ = [
    "FILLER_ITEMS",
    "ITEMS_DATA",
    "ITEMS_DATA_BY_ID",
    "ITEM_GROUPS",
    "PROGRESSION_ITEMS",
    "PROGRESSIVE_ITEMS",
    "TRAP_ITEMS",
    "USEFUL_ITEMS",
    "CivVFillerItemData",
    "CivVItem",
    "CivVItemData",
    "CivVProgressiveItemData",
    "CivVProgressionItemData",
    "CivVUsefulItemData",
    "ItemRequirements",
]


# %% GLOBALS
ITEMS_DATA: list["CivVItemData"] = []
"List of all defined items"
ITEMS_DATA_BY_ID: dict[int, "CivVItemData"] = {}
"Dict of all defined items, separated by AP ID"
ITEMS_DATA_BY_NAME: dict[str, "CivVItemData"] = {}
"Dict of all defined items, separated by name"
ITEM_GROUPS: defaultdict[str, list[str]] = defaultdict(list)
"Dict of all defined item names per item group. Used by the CivVWorld"
PROGRESSIVE_ITEMS: list["CivVProgressiveItemData"] = []
"List of all defined progressive items"
PROGRESSION_ITEMS: list["CivVProgressionItemData"] = []
"List of all defined progression items"
USEFUL_ITEMS: list["CivVUsefulItemData"] = []
"List of all defined useful items"
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
            always_requirements=self._merge_dicts(self.always_requirements, other.always_requirements),
            option_requirements=[*self.option_requirements, *other.option_requirements],
        )

    @staticmethod
    def _merge_dicts(dct1: dict, dct2: dict) -> dict:
        return {k: max(dct1.get(k, 0), dct2.get(k, 0)) for k in {*dct1.keys(), *dct2.keys()}}

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
                requirements = self._merge_dicts(requirements, requirements_dct)

        # Create rule function that uses the CollectionState to determine if region/location is reachable
        def rule(state: CollectionState) -> bool:
            return all((state.has(name, player, count) for name, count in requirements.items()))

        # Return created rule
        return rule


# %% ITEM_DATA CLASS DEFINITIONS
@dataclass
class CivVItemData:
    """
    Dataclass used for specifying an item.

    """

    name: str
    "Name of this item"
    type: CivVItemType
    "Type of this item"
    game_id: int | None
    "ID of this item with this item type. If None, this item has no singular ID"
    game_ids: list[int] | None
    "IDs of this item with this item type. If None, this item has no defined IDs"
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

        # If game_id is set, set it as the single entry for game_ids
        if self.game_id is not None:
            self.game_ids = [self.game_id]

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
class CivVProgressiveItemData(CivVItemData):
    """
    Dataclass used for specifying a progressive item.

    """

    game_id: None = field(default=None, init=False)
    game_ids: list[int] = field(default_factory=list)
    classification: Literal[ItemClassification.progression] = field(default=ItemClassification.progression, init=False)
    count: int = field(init=False)
    option_toggle_name: str | None = None
    "If provided, the name of the option that toggles the use of this progressive item. Default is to always use"

    def __post_init__(self):
        # Call super method
        super().__post_init__()

        # Add self to dict
        PROGRESSIVE_ITEMS.append(self)

    def add_game_id(self, game_id) -> None:
        """
        Adds the given `game_id` to this item.

        """

        self.game_ids.append(game_id)
        self.count += 1


@dataclass
class CivVProgressionItemData(CivVItemData):
    """
    Dataclass used for specifying a progression item.

    """

    game_id: int
    game_ids: list[int] = field(default_factory=list, init=False)
    classification: Literal[ItemClassification.progression] = field(default=ItemClassification.progression, init=False)
    count: int = field(init=False)
    progressive_parent: CivVProgressiveItemData | None = None
    "If provided, the progressive parent item this item belongs to"

    def __post_init__(self):
        # Call super method
        super().__post_init__()

        # Add game_id to its progressive parent, if it has one
        if self.progressive_parent is not None:
            self.progressive_parent.add_game_id(self.game_id)

        # Add self to dict
        PROGRESSION_ITEMS.append(self)


@dataclass
class CivVUsefulItemData(CivVItemData):
    """
    Dataclass used for specifying a useful item.

    """

    game_id: int
    game_ids: list[int] = field(default_factory=list, init=False)
    classification: Literal[ItemClassification.useful] = field(default=ItemClassification.useful, init=False)
    count: int = field(init=False)

    def __post_init__(self):
        # Call super method
        super().__post_init__()

        # Add self to dict
        USEFUL_ITEMS.append(self)


@dataclass
class CivVFillerItemData(CivVItemData):
    """
    Dataclass used for specifying a filler item.

    """

    game_id: None = field(default=None, init=False)
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
