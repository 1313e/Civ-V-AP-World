# %% IMPORTS
from dataclasses import dataclass, field
from typing import Optional

from . import items

# All declaration
__all__ = [
    "CivVRegionData",
    "REGIONS_DATA",
    "ANCIENT_ERA",
    "CLASSICAL_ERA",
    "MEDIEVAL_ERA",
    "RENAISSANCE_ERA",
    "INDUSTRIAL_ERA",
    "MODERN_ERA",
    "ATOMIC_ERA",
    "INFORMATION_ERA",
    "ERA_REGIONS",
]


# %% GLOBALS
REGIONS_DATA: list["CivVRegionData"] = []
"List of all defined regions"


# %% REGION_DATA CLASS DEFINITION
@dataclass
class CivVRegionData:
    """
    Dataclass used for specifying a region within Civ V.

    """

    name: str
    "Name of this region"
    parent: Optional["CivVRegionData"] = None
    "The parent of this region. If None, this region is reachable from the origin region"
    requirements: dict[str, int] = field(default_factory=dict)
    "Dict of required items to access this region, in addition to the parent's requirements"

    def __post_init__(self):
        # Add self to the REGIONS_DATA list
        REGIONS_DATA.append(self)


# %% REGION DECLARATIONS
ANCIENT_ERA = CivVRegionData(
    name="Ancient Era",
)
CLASSICAL_ERA = CivVRegionData(
    name="Classical Era",
    parent=ANCIENT_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 1},
)
MEDIEVAL_ERA = CivVRegionData(
    name="Medieval Era",
    parent=CLASSICAL_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 2},
)
RENAISSANCE_ERA = CivVRegionData(
    name="Renaissance Era",
    parent=MEDIEVAL_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 3},
)
INDUSTRIAL_ERA = CivVRegionData(
    name="Industrial Era",
    parent=RENAISSANCE_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 4},
)
MODERN_ERA = CivVRegionData(
    name="Modern Era",
    parent=INDUSTRIAL_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 5},
)
ATOMIC_ERA = CivVRegionData(
    name="Atomic Era",
    parent=MODERN_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 6},
)
INFORMATION_ERA = CivVRegionData(
    name="Information Era",
    parent=ATOMIC_ERA,
    requirements={items.PROGRESSIVE_ERA_ITEM.name: 7},
)
ERA_REGIONS = [
    ANCIENT_ERA,
    CLASSICAL_ERA,
    MEDIEVAL_ERA,
    RENAISSANCE_ERA,
    INDUSTRIAL_ERA,
    MODERN_ERA,
    ATOMIC_ERA,
    INFORMATION_ERA,
]
"List with all era regions"
