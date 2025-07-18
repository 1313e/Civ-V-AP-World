# %% IMPORTS
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import ClassVar

from BaseClasses import Location, CollectionState

from . import regions
from .constants import GAME_NAME, ID_OFFSET, TECH_ID_OFFSET
from .enums import CivVLocationType

# All declaration
__all__ = ["CivVLocation", "LOCATIONS_DATA", "LOCATIONS_DATA_BY_ID", "LOCATIONS_DATA_BY_TYPE_ID"]


# %% GLOBALS
LOCATIONS_DATA: list["CivVLocationData"] = []
"List of all defined locations"
LOCATIONS_DATA_BY_ID: dict[int, "CivVLocationData"] = {}
"Dict of all defined locations, separated by AP ID"
LOCATIONS_DATA_BY_TYPE_ID: dict[tuple[CivVLocationType, int], "CivVLocationData"] = {}
"Dict of all defined locations, separated by type + game ID"


# %% LOCATION CLASS DEFINITION
class CivVLocation(Location):
    game: str = GAME_NAME


# %% LOCATION_DATA CLASS DEFINITION
@dataclass
class CivVLocationData:
    """
    Dataclass used for specifying a location within Civ V.

    """

    name: str
    "Name of this location"
    type: CivVLocationType
    "Type of this location"
    game_id: int
    "ID of this location with this location type within Civ V"
    region: regions.CivVRegionData | None = None
    "The region of this location. If None, this location is in the origin region"
    rule: Callable[[CollectionState], bool] | None = None
    "Rule to determine whether this location is currently accessible, in addition to the region accessibility rule"
    ap_id: int = field(init=False)
    "ID of this location within AP"

    # Class attributes
    ID_OFFSET_DCT: ClassVar[dict[CivVLocationType, int]] = {
        CivVLocationType.tech: TECH_ID_OFFSET,
    }
    "Dict that indicates what offset specific location types must have"


    def __post_init__(self):
        # Add the location type as a prefix to the location name
        self.name = f"{self.type.capitalize()} - {self.name}"

        # Set game ID properly
        self.game_id += self.ID_OFFSET_DCT[self.type]

        # Set AP ID for this location
        self.ap_id = len(LOCATIONS_DATA) + ID_OFFSET

        # Add self to the dicts
        LOCATIONS_DATA.append(self)
        LOCATIONS_DATA_BY_ID[self.ap_id] = self
        LOCATIONS_DATA_BY_TYPE_ID[(self.type, self.game_id)] = self


# %% LOCATION DECLARATIONS
TECH_LOCATIONS = [
    CivVLocationData(name="AP1", type=CivVLocationType.tech, game_id=1, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP2", type=CivVLocationType.tech, game_id=2, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP3", type=CivVLocationType.tech, game_id=3, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP4", type=CivVLocationType.tech, game_id=4, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP5", type=CivVLocationType.tech, game_id=5, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP6", type=CivVLocationType.tech, game_id=6, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP7", type=CivVLocationType.tech, game_id=7, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP8", type=CivVLocationType.tech, game_id=8, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP9", type=CivVLocationType.tech, game_id=9, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP10", type=CivVLocationType.tech, game_id=10, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP11", type=CivVLocationType.tech, game_id=11, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP12", type=CivVLocationType.tech, game_id=12, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP13", type=CivVLocationType.tech, game_id=13, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP14", type=CivVLocationType.tech, game_id=14, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP15", type=CivVLocationType.tech, game_id=15, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP16", type=CivVLocationType.tech, game_id=16, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP17", type=CivVLocationType.tech, game_id=17, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP18", type=CivVLocationType.tech, game_id=18, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP19", type=CivVLocationType.tech, game_id=19, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP20", type=CivVLocationType.tech, game_id=20, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP21", type=CivVLocationType.tech, game_id=21, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP22", type=CivVLocationType.tech, game_id=22, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP23", type=CivVLocationType.tech, game_id=23, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP24", type=CivVLocationType.tech, game_id=24, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP25", type=CivVLocationType.tech, game_id=25, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP26", type=CivVLocationType.tech, game_id=26, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP27", type=CivVLocationType.tech, game_id=27, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP28", type=CivVLocationType.tech, game_id=28, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP29", type=CivVLocationType.tech, game_id=29, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP30", type=CivVLocationType.tech, game_id=30, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP31", type=CivVLocationType.tech, game_id=31, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP32", type=CivVLocationType.tech, game_id=32, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP33", type=CivVLocationType.tech, game_id=33, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP34", type=CivVLocationType.tech, game_id=34, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP35", type=CivVLocationType.tech, game_id=35, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP36", type=CivVLocationType.tech, game_id=36, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP37", type=CivVLocationType.tech, game_id=37, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP38", type=CivVLocationType.tech, game_id=38, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP39", type=CivVLocationType.tech, game_id=39, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP40", type=CivVLocationType.tech, game_id=40, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP41", type=CivVLocationType.tech, game_id=41, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP42", type=CivVLocationType.tech, game_id=42, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP43", type=CivVLocationType.tech, game_id=43, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP44", type=CivVLocationType.tech, game_id=44, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP45", type=CivVLocationType.tech, game_id=45, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP46", type=CivVLocationType.tech, game_id=46, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP47", type=CivVLocationType.tech, game_id=47, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP48", type=CivVLocationType.tech, game_id=48, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP49", type=CivVLocationType.tech, game_id=49, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP50", type=CivVLocationType.tech, game_id=50, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP51", type=CivVLocationType.tech, game_id=51, region=regions.MODERN_ERA),
    CivVLocationData(name="AP52", type=CivVLocationType.tech, game_id=52, region=regions.MODERN_ERA),
    CivVLocationData(name="AP53", type=CivVLocationType.tech, game_id=53, region=regions.MODERN_ERA),
    CivVLocationData(name="AP54", type=CivVLocationType.tech, game_id=54, region=regions.MODERN_ERA),
    CivVLocationData(name="AP55", type=CivVLocationType.tech, game_id=55, region=regions.MODERN_ERA),
    CivVLocationData(name="AP56", type=CivVLocationType.tech, game_id=56, region=regions.MODERN_ERA),
    CivVLocationData(name="AP57", type=CivVLocationType.tech, game_id=57, region=regions.MODERN_ERA),
    CivVLocationData(name="AP58", type=CivVLocationType.tech, game_id=58, region=regions.MODERN_ERA),
    CivVLocationData(name="AP59", type=CivVLocationType.tech, game_id=59, region=regions.MODERN_ERA),
    CivVLocationData(name="AP60", type=CivVLocationType.tech, game_id=60, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP61", type=CivVLocationType.tech, game_id=61, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP62", type=CivVLocationType.tech, game_id=62, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP63", type=CivVLocationType.tech, game_id=63, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP64", type=CivVLocationType.tech, game_id=64, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP65", type=CivVLocationType.tech, game_id=65, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP66", type=CivVLocationType.tech, game_id=66, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP67", type=CivVLocationType.tech, game_id=67, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP68", type=CivVLocationType.tech, game_id=68, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP69", type=CivVLocationType.tech, game_id=69, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP70", type=CivVLocationType.tech, game_id=70, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP71", type=CivVLocationType.tech, game_id=71, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP72", type=CivVLocationType.tech, game_id=72, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP73", type=CivVLocationType.tech, game_id=73, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP74", type=CivVLocationType.tech, game_id=74, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP75", type=CivVLocationType.tech, game_id=75, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP76", type=CivVLocationType.tech, game_id=76, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP77", type=CivVLocationType.tech, game_id=77, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP78", type=CivVLocationType.tech, game_id=78, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP79", type=CivVLocationType.tech, game_id=79, region=regions.INFORMATION_ERA),
]
"List of all technology locations within Civ V"
