# %% IMPORTS
from dataclasses import dataclass, field

from BaseClasses import Location

from .. import items, regions
from ..constants import GAME_NAME, ID_OFFSET
from ..enums import CivVLocationType
from ..helpers import to_title

# All declaration
__all__ = [
    "LOCATIONS_DATA",
    "LOCATIONS_DATA_BY_ID",
    "LOCATIONS_DATA_BY_TYPE_ID",
    "CivVLocation",
    "CivVLocationData",
]


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
    Dataclass used for specifying a location.

    """

    name: str
    "Name of this location"
    type: CivVLocationType
    "Type of this location"
    game_id: int
    "ID of this location with this location type"
    region: regions.CivVRegionData | None = None
    "The region of this location. If None, this location is in the origin region"
    requirements: items.ItemRequirements = field(default_factory=items.ItemRequirements)
    "Required items to access this location, in addition to the region's requirements"
    ap_id: int = field(init=False)
    "ID of this location within AP"


    def __post_init__(self):
        # Add the location type as a prefix to the location name
        self.name = f"{to_title(self.type)} - {self.name}"

        # Set AP ID for this location
        self.ap_id = len(LOCATIONS_DATA) + ID_OFFSET

        # Add self to the dicts
        LOCATIONS_DATA.append(self)
        LOCATIONS_DATA_BY_ID[self.ap_id] = self
        LOCATIONS_DATA_BY_TYPE_ID[(self.type, self.game_id)] = self
