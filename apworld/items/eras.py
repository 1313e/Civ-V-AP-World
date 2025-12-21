# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVUsefulItemData
from ..enums import CivVItemType

# All declaration
__all__ = [
    "PROGRESSIVE_ERA_ITEM",
]


# %% ITEM DECLARATIONS
PROGRESSIVE_ERA_ITEM = CivVUsefulItemData(
    name="Progressive",
    type=CivVItemType.era,
    game_ids=[169, 170, 171, 172, 173, 174, 175],
    classification=ItemClassification.progression,
)
"Progressive era item"
