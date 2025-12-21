# %% IMPORTS
from .core import CivVProgressiveItemData
from ..enums import CivVItemType

# All declaration
__all__ = [
    "PROGRESSIVE_ERA_ITEM",
]


# %% ITEM DECLARATIONS
PROGRESSIVE_ERA_ITEM = CivVProgressiveItemData(
    name="Progressive",
    type=CivVItemType.era,
    game_ids=[169, 170, 171, 172, 173, 174, 175],
)
"Progressive era item"
