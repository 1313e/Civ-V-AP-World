# %% IMPORTS
from dataclasses import dataclass, field

from BaseClasses import Location

from . import items, regions
from .constants import GAME_NAME, ID_OFFSET
from .enums import CivVLocationType
from .helpers import to_title

# All declaration
__all__ = ["CivVLocation", "CivVLocationData", "LOCATIONS_DATA", "LOCATIONS_DATA_BY_ID", "LOCATIONS_DATA_BY_TYPE_ID"]


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
    requirements: dict[str, int] = field(default_factory=dict)
    "Dict of required items to access this location, in addition to the region's requirements"
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


# %% LOCATION DECLARATIONS
TECH_LOCATIONS = [
    # All vanilla techs converted to AP techs
    CivVLocationData(name="AP 1", type=CivVLocationType.tech, game_id=83, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 2", type=CivVLocationType.tech, game_id=84, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 3", type=CivVLocationType.tech, game_id=85, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 4", type=CivVLocationType.tech, game_id=86, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 5", type=CivVLocationType.tech, game_id=87, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 6", type=CivVLocationType.tech, game_id=88, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 7", type=CivVLocationType.tech, game_id=89, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 8", type=CivVLocationType.tech, game_id=90, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 9", type=CivVLocationType.tech, game_id=91, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 10", type=CivVLocationType.tech, game_id=92, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 11", type=CivVLocationType.tech, game_id=93, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP 12", type=CivVLocationType.tech, game_id=94, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 13", type=CivVLocationType.tech, game_id=95, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 14", type=CivVLocationType.tech, game_id=96, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 15", type=CivVLocationType.tech, game_id=97, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 16", type=CivVLocationType.tech, game_id=98, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 17", type=CivVLocationType.tech, game_id=99, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 18", type=CivVLocationType.tech, game_id=100, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 19", type=CivVLocationType.tech, game_id=101, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 20", type=CivVLocationType.tech, game_id=102, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP 21", type=CivVLocationType.tech, game_id=103, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 22", type=CivVLocationType.tech, game_id=104, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 23", type=CivVLocationType.tech, game_id=105, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 24", type=CivVLocationType.tech, game_id=106, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 25", type=CivVLocationType.tech, game_id=107, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 26", type=CivVLocationType.tech, game_id=108, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 27", type=CivVLocationType.tech, game_id=109, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 28", type=CivVLocationType.tech, game_id=110, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 29", type=CivVLocationType.tech, game_id=111, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 30", type=CivVLocationType.tech, game_id=112, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP 31", type=CivVLocationType.tech, game_id=113, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 32", type=CivVLocationType.tech, game_id=114, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 33", type=CivVLocationType.tech, game_id=115, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 34", type=CivVLocationType.tech, game_id=116, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 35", type=CivVLocationType.tech, game_id=117, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 36", type=CivVLocationType.tech, game_id=118, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 37", type=CivVLocationType.tech, game_id=119, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 38", type=CivVLocationType.tech, game_id=120, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 39", type=CivVLocationType.tech, game_id=121, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 40", type=CivVLocationType.tech, game_id=122, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP 41", type=CivVLocationType.tech, game_id=123, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 42", type=CivVLocationType.tech, game_id=124, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 43", type=CivVLocationType.tech, game_id=125, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 44", type=CivVLocationType.tech, game_id=126, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 45", type=CivVLocationType.tech, game_id=127, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 46", type=CivVLocationType.tech, game_id=128, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 47", type=CivVLocationType.tech, game_id=129, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 48", type=CivVLocationType.tech, game_id=130, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 49", type=CivVLocationType.tech, game_id=131, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 50", type=CivVLocationType.tech, game_id=132, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP 51", type=CivVLocationType.tech, game_id=133, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 52", type=CivVLocationType.tech, game_id=134, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 53", type=CivVLocationType.tech, game_id=135, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 54", type=CivVLocationType.tech, game_id=136, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 55", type=CivVLocationType.tech, game_id=137, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 56", type=CivVLocationType.tech, game_id=138, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 57", type=CivVLocationType.tech, game_id=139, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 58", type=CivVLocationType.tech, game_id=140, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 59", type=CivVLocationType.tech, game_id=141, region=regions.MODERN_ERA),
    CivVLocationData(name="AP 60", type=CivVLocationType.tech, game_id=142, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 61", type=CivVLocationType.tech, game_id=143, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 62", type=CivVLocationType.tech, game_id=144, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 63", type=CivVLocationType.tech, game_id=145, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 64", type=CivVLocationType.tech, game_id=146, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 65", type=CivVLocationType.tech, game_id=147, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 66", type=CivVLocationType.tech, game_id=148, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 67", type=CivVLocationType.tech, game_id=149, region=regions.ATOMIC_ERA),
    CivVLocationData(name="AP 68", type=CivVLocationType.tech, game_id=150, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 69", type=CivVLocationType.tech, game_id=151, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 70", type=CivVLocationType.tech, game_id=152, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 71", type=CivVLocationType.tech, game_id=153, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 72", type=CivVLocationType.tech, game_id=154, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 73", type=CivVLocationType.tech, game_id=155, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 74", type=CivVLocationType.tech, game_id=156, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 75", type=CivVLocationType.tech, game_id=157, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 76", type=CivVLocationType.tech, game_id=158, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 77", type=CivVLocationType.tech, game_id=159, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 78", type=CivVLocationType.tech, game_id=160, region=regions.INFORMATION_ERA),
    CivVLocationData(name="AP 79", type=CivVLocationType.tech, game_id=161, region=regions.INFORMATION_ERA),

    # Additional techs
    CivVLocationData(name="AP Bonus 1", type=CivVLocationType.tech, game_id=162, region=regions.ANCIENT_ERA),
    CivVLocationData(name="AP Bonus 2", type=CivVLocationType.tech, game_id=163, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="AP Bonus 3", type=CivVLocationType.tech, game_id=164, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="AP Bonus 4", type=CivVLocationType.tech, game_id=165, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="AP Bonus 5", type=CivVLocationType.tech, game_id=166, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="AP Bonus 6", type=CivVLocationType.tech, game_id=167, region=regions.MODERN_ERA),
    CivVLocationData(name="AP Bonus 7", type=CivVLocationType.tech, game_id=168, region=regions.ATOMIC_ERA),
]
"List of all technology locations within Civ V"


POLICY_LOCATIONS = [
    # All vanilla policies converted to AP policies
    CivVLocationData(name="Tradition AP 1", type=CivVLocationType.policy, game_id=111, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Tradition AP 2", type=CivVLocationType.policy, game_id=112, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Tradition AP 3", type=CivVLocationType.policy, game_id=113, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Tradition AP 4", type=CivVLocationType.policy, game_id=114, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Tradition AP 5", type=CivVLocationType.policy, game_id=115, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Liberty AP 1", type=CivVLocationType.policy, game_id=116, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Liberty AP 2", type=CivVLocationType.policy, game_id=117, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Liberty AP 3", type=CivVLocationType.policy, game_id=118, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Liberty AP 4", type=CivVLocationType.policy, game_id=119, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Liberty AP 5", type=CivVLocationType.policy, game_id=120, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Honor AP 1", type=CivVLocationType.policy, game_id=121, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Honor AP 2", type=CivVLocationType.policy, game_id=122, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Honor AP 3", type=CivVLocationType.policy, game_id=123, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Honor AP 4", type=CivVLocationType.policy, game_id=124, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Honor AP 5", type=CivVLocationType.policy, game_id=125, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Piety AP 1", type=CivVLocationType.policy, game_id=126, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Piety AP 2", type=CivVLocationType.policy, game_id=127, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Piety AP 3", type=CivVLocationType.policy, game_id=128, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Piety AP 4", type=CivVLocationType.policy, game_id=129, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Piety AP 5", type=CivVLocationType.policy, game_id=130, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Patronage AP 1", type=CivVLocationType.policy, game_id=131, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Patronage AP 2", type=CivVLocationType.policy, game_id=132, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Patronage AP 3", type=CivVLocationType.policy, game_id=133, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Patronage AP 4", type=CivVLocationType.policy, game_id=134, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Patronage AP 5", type=CivVLocationType.policy, game_id=135, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Aesthetics AP 1", type=CivVLocationType.policy, game_id=136, region=regions.MODERN_ERA),
    CivVLocationData(name="Aesthetics AP 2", type=CivVLocationType.policy, game_id=137, region=regions.MODERN_ERA),
    CivVLocationData(name="Aesthetics AP 3", type=CivVLocationType.policy, game_id=138, region=regions.MODERN_ERA),
    CivVLocationData(name="Aesthetics AP 4", type=CivVLocationType.policy, game_id=139, region=regions.MODERN_ERA),
    CivVLocationData(name="Aesthetics AP 5", type=CivVLocationType.policy, game_id=140, region=regions.MODERN_ERA),
    CivVLocationData(name="Commerce AP 1", type=CivVLocationType.policy, game_id=141, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Commerce AP 2", type=CivVLocationType.policy, game_id=142, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Commerce AP 3", type=CivVLocationType.policy, game_id=143, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Commerce AP 4", type=CivVLocationType.policy, game_id=144, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Commerce AP 5", type=CivVLocationType.policy, game_id=145, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Exploration AP 1", type=CivVLocationType.policy, game_id=146, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Exploration AP 2", type=CivVLocationType.policy, game_id=147, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Exploration AP 3", type=CivVLocationType.policy, game_id=148, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Exploration AP 4", type=CivVLocationType.policy, game_id=149, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Exploration AP 5", type=CivVLocationType.policy, game_id=150, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism AP 1", type=CivVLocationType.policy, game_id=151, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism AP 2", type=CivVLocationType.policy, game_id=152, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism AP 3", type=CivVLocationType.policy, game_id=153, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism AP 4", type=CivVLocationType.policy, game_id=154, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism AP 5", type=CivVLocationType.policy, game_id=155, region=regions.INFORMATION_ERA),
]
"List of all policy locations within Civ V"


POLICY_BRANCH_LOCATIONS = [
    # All vanilla policy branches
    CivVLocationData(name="Tradition", type=CivVLocationType.policy_branch, game_id=0, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Liberty", type=CivVLocationType.policy_branch, game_id=1, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Honor", type=CivVLocationType.policy_branch, game_id=2, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Piety", type=CivVLocationType.policy_branch, game_id=3, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Patronage", type=CivVLocationType.policy_branch, game_id=4, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Aesthetics", type=CivVLocationType.policy_branch, game_id=5, region=regions.MODERN_ERA),
    CivVLocationData(name="Commerce", type=CivVLocationType.policy_branch, game_id=6, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Exploration", type=CivVLocationType.policy_branch, game_id=7, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism", type=CivVLocationType.policy_branch, game_id=8, region=regions.INFORMATION_ERA),

    # Policy branch finishers masked as policy branches
    CivVLocationData(name="Tradition Finished", type=CivVLocationType.policy_branch, game_id=12, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Liberty Finished", type=CivVLocationType.policy_branch, game_id=13, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Honor Finished", type=CivVLocationType.policy_branch, game_id=14, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Piety Finished", type=CivVLocationType.policy_branch, game_id=15, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Patronage Finished", type=CivVLocationType.policy_branch, game_id=16, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Aesthetics Finished", type=CivVLocationType.policy_branch, game_id=17, region=regions.MODERN_ERA),
    CivVLocationData(name="Commerce Finished", type=CivVLocationType.policy_branch, game_id=18, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Exploration Finished", type=CivVLocationType.policy_branch, game_id=19, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Rationalism Finished", type=CivVLocationType.policy_branch, game_id=20, region=regions.INFORMATION_ERA),
]
"List of all policy branch locations within Civ V"
