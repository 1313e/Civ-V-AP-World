# %% IMPORTS
from dataclasses import dataclass, field
from typing import Optional

from . import items, requirements

# All declaration
__all__ = [
    "CivVRegionData",
    "REGIONS_DATA",
    "ANCIENT_ERA",
    "ANCIENT_ERA_TECH",
    "ANCIENT_ERA_POLICY",
    "CLASSICAL_ERA",
    "CLASSICAL_ERA_TECH",
    "CLASSICAL_ERA_POLICY",
    "MEDIEVAL_ERA",
    "MEDIEVAL_ERA_TECH",
    "MEDIEVAL_ERA_POLICY",
    "RENAISSANCE_ERA",
    "RENAISSANCE_ERA_TECH",
    "RENAISSANCE_ERA_POLICY",
    "INDUSTRIAL_ERA",
    "INDUSTRIAL_ERA_TECH",
    "INDUSTRIAL_ERA_POLICY",
    "MODERN_ERA",
    "MODERN_ERA_TECH",
    "MODERN_ERA_POLICY",
    "ATOMIC_ERA",
    "ATOMIC_ERA_TECH",
    "ATOMIC_ERA_POLICY",
    "INFORMATION_ERA",
    "INFORMATION_ERA_TECH",
    "INFORMATION_ERA_POLICY",
    "ERA_REGIONS",
    "ERA_TECH_REGIONS",
    "ERA_POLICY_REGIONS",
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
    requirements: items.ItemRequirements = field(default_factory=items.ItemRequirements)
    "Required items to access this region, in addition to the parent's requirements"

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
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 1}),
)
MEDIEVAL_ERA = CivVRegionData(
    name="Medieval Era",
    parent=CLASSICAL_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 2}),
)
RENAISSANCE_ERA = CivVRegionData(
    name="Renaissance Era",
    parent=MEDIEVAL_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 3}),
)
INDUSTRIAL_ERA = CivVRegionData(
    name="Industrial Era",
    parent=RENAISSANCE_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 4}),
)
MODERN_ERA = CivVRegionData(
    name="Modern Era",
    parent=INDUSTRIAL_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 5}),
)
ATOMIC_ERA = CivVRegionData(
    name="Atomic Era",
    parent=MODERN_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 6}),
)
INFORMATION_ERA = CivVRegionData(
    name="Information Era",
    parent=ATOMIC_ERA,
    requirements=items.ItemRequirements(progressive={items.PROGRESSIVE_ERA_ITEM: 7}),
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


ANCIENT_ERA_TECH = CivVRegionData(
    name="Ancient Era Tech",
    parent=ANCIENT_ERA,
)
CLASSICAL_ERA_TECH = CivVRegionData(
    name="Classical Era Tech",
    parent=CLASSICAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Library"]
)
MEDIEVAL_ERA_TECH = CivVRegionData(
    name="Medieval Era Tech",
    parent=MEDIEVAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Library"]
)
RENAISSANCE_ERA_TECH = CivVRegionData(
    name="Renaissance Era Tech",
    parent=RENAISSANCE_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["University"]
)
INDUSTRIAL_ERA_TECH = CivVRegionData(
    name="Industrial Era Tech",
    parent=INDUSTRIAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["University"]
)
MODERN_ERA_TECH = CivVRegionData(
    name="Modern Era Tech",
    parent=MODERN_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Public School"]
)
ATOMIC_ERA_TECH = CivVRegionData(
    name="Atomic Era Tech",
    parent=ATOMIC_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Public School"]
)
INFORMATION_ERA_TECH = CivVRegionData(
    name="Information Era Tech",
    parent=INFORMATION_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Research Lab"]
)
ERA_TECH_REGIONS = [
    ANCIENT_ERA_TECH,
    CLASSICAL_ERA_TECH,
    MEDIEVAL_ERA_TECH,
    RENAISSANCE_ERA_TECH,
    INDUSTRIAL_ERA_TECH,
    MODERN_ERA_TECH,
    ATOMIC_ERA_TECH,
    INFORMATION_ERA_TECH,
]
"List with all era regions for technologies"


ANCIENT_ERA_POLICY = CivVRegionData(
    name="Ancient Era Policy",
    parent=ANCIENT_ERA,
)
CLASSICAL_ERA_POLICY = CivVRegionData(
    name="Classical Era Policy",
    parent=CLASSICAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Amphitheater"]
)
MEDIEVAL_ERA_POLICY = CivVRegionData(
    name="Medieval Era Policy",
    parent=MEDIEVAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Amphitheater"]
)
RENAISSANCE_ERA_POLICY = CivVRegionData(
    name="Renaissance Era Policy",
    parent=RENAISSANCE_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Opera House"]
)
INDUSTRIAL_ERA_POLICY = CivVRegionData(
    name="Industrial Era Policy",
    parent=INDUSTRIAL_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Opera House"]
)
MODERN_ERA_POLICY = CivVRegionData(
    name="Modern Era Policy",
    parent=MODERN_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Museum"]
)
ATOMIC_ERA_POLICY = CivVRegionData(
    name="Atomic Era Policy",
    parent=ATOMIC_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Museum"]
)
INFORMATION_ERA_POLICY = CivVRegionData(
    name="Information Era Policy",
    parent=INFORMATION_ERA,
    requirements=requirements.BUILDING_REQUIREMENTS["Broadcast Tower"]
)
ERA_POLICY_REGIONS = [
    ANCIENT_ERA_POLICY,
    CLASSICAL_ERA_POLICY,
    MEDIEVAL_ERA_POLICY,
    RENAISSANCE_ERA_POLICY,
    INDUSTRIAL_ERA_POLICY,
    MODERN_ERA_POLICY,
    ATOMIC_ERA_POLICY,
    INFORMATION_ERA_POLICY,
]
"List with all era regions for policies"
