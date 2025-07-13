# %% IMPORTS
from collections.abc import Callable
from dataclasses import dataclass
from typing import Optional

from BaseClasses import CollectionState

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
    rule: Callable[[CollectionState], bool] | None = None
    "Rule to determine whether this region is currently accessible, in addition to the parent accessibility rule"

    def __post_init__(self):
        # Add self to the REGIONS_DATA list
        REGIONS_DATA.append(self)


# %% REGION DECLARATIONS
ANCIENT_ERA = CivVRegionData(name="Ancient Era")
CLASSICAL_ERA = CivVRegionData(name="Classical Era")
MEDIEVAL_ERA = CivVRegionData(name="Medieval Era")
RENAISSANCE_ERA = CivVRegionData(name="Renaissance Era")
INDUSTRIAL_ERA = CivVRegionData(name="Industrial Era")
MODERN_ERA = CivVRegionData(name="Modern Era")
ATOMIC_ERA = CivVRegionData(name="Atomic Era")
INFORMATION_ERA = CivVRegionData(name="Information Era")
