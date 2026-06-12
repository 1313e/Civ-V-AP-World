# %% IMPORTS
from .core import CivVProgressiveItemData
from ..enums import CivVItemType

# All declaration
__all__ = [
    "PROGRESSIVE_SETTLER_ITEM",
]


# %% ITEM DECLARATIONS
PROGRESSIVE_SETTLER_ITEM: CivVProgressiveItemData = CivVProgressiveItemData(
    name="Progressive",
    type=CivVItemType.settler,
    game_ids=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    option_toggle_name="settler_sanity",
    option_count_name="settler_sanity_amount"
)
"Progressive settler item"
