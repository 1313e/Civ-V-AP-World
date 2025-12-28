# %% IMPORTS
import functools
import itertools
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
class ItemRequirements:
    """
    Class used for specifying the item requirements of a region or location.

    """

    def __init__(
            self,
            *requirements: "ItemRequirements",
            progressive: dict["CivVProgressiveItemData", int] | None = None,
            progression: set["CivVProgressionItemData"] | None = None,
    ):
        """
        Initializes this item requirements, combining the given base `requirements` with the provided `progressive` and
        `progression` requirements.

        Args:
             requirements: Base requirements to use for this requirement.
             progressive: Dict of progressive items and their corresponding required count.
             progression: Set of required progression items.

        """

        # Set progressive and progression to empty containers if their defaults are used
        progressive = progressive or {}
        progression = progression or set()

        # Check that each item in progressive and progression are marked as progression items
        for item in [*progressive.keys(), *progression]:
            if item.classification != ItemClassification.progression:
                raise ValueError(f"Required item with name {item.name!r} is not a progression item")

        # Combine the base item requirements together with the additional requirements and store them
        self._progressive = functools.reduce(self._merge_dicts, (x.progressive for x in requirements), progressive)
        self._progression = {*itertools.chain.from_iterable(x.progression for x in requirements), *progression}

    @property
    def progressive(self) -> dict["CivVProgressiveItemData", int]:
        """
        Dict of progressive items and their corresponding required count.

        """

        return self._progressive

    @property
    def progression(self) -> set["CivVProgressionItemData"]:
        """
        Set of required progression items.

        """

        return self._progression

    @staticmethod
    def _merge_dicts(dct1: dict, dct2: dict) -> dict:
        return {k: max(dct1.get(k, 0), dct2.get(k, 0)) for k in {*dct1.keys(), *dct2.keys()}}

    def create_access_rule(self, player: int, options: PerGameCommonOptions) -> Callable[[CollectionState], bool]:
        """
        Creates the access rule function for this instance and returns it.

        This function can be used as the access rule when creating :class:`Region` and :class:`Location` instances.

        """

        # Determine all the requirements that must be satisfied
        requirements: dict[str, int] = {}

        # Add all the progressive requirements
        for item, count in self._progressive.items():
            # If this progressive item is always required or is toggled on in the options, add it
            if item.option_toggle_name is None or getattr(options, item.option_toggle_name):
                requirements[item.name] = count

        # Add all the progression requirements
        for item in self._progression:
            # If this progression item is always required or its progressive parent is NOT in use, add it
            if item.progressive_parent is None or not (
                    item.progressive_parent.option_toggle_name is None
                    or getattr(options, item.progressive_parent.option_toggle_name)
            ):
                requirements[item.name] = 1

            # Else, we have to add its progressive parent count equivalent to the requirements
            else:
                requirements = self._merge_dicts(
                    requirements,
                    {item.progressive_parent.name: item.progressive_parent.game_ids.index(item.game_id)+1},
                )

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

    def __eq__(self, other: "CivVItemData") -> bool:
        return self.ap_id == other.ap_id

    def __hash__(self) -> int:
        return self.ap_id

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


@dataclass(eq=False)
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


@dataclass(eq=False)
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


@dataclass(eq=False)
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


@dataclass(eq=False)
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
