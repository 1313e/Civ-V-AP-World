# %% IMPORTS
from dataclasses import dataclass, field

from BaseClasses import Location

from . import items, regions
from .constants import GAME_NAME, ID_OFFSET
from .enums import CivVLocationType
from .helpers import to_title

# All declaration
__all__ = [
    "CivVLocation",
    "CivVLocationData",
    "LOCATIONS_DATA",
    "LOCATIONS_DATA_BY_ID",
    "LOCATIONS_DATA_BY_TYPE_ID",
    "NATIONAL_WONDER_LOCATIONS",
    "POLICY_BRANCH_LOCATIONS",
    "POLICY_LOCATIONS",
    "TECH_LOCATIONS",
    "VICTORY_LOCATIONS",
    "WORLD_WONDER_LOCATIONS",
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


# %% LOCATION DECLARATIONS
TECH_LOCATIONS = [
    # All vanilla techs converted to AP techs
    CivVLocationData(name="Ancient AP 1", type=CivVLocationType.tech, game_id=83, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 2", type=CivVLocationType.tech, game_id=84, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 3", type=CivVLocationType.tech, game_id=85, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 4", type=CivVLocationType.tech, game_id=86, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 5", type=CivVLocationType.tech, game_id=87, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 6", type=CivVLocationType.tech, game_id=88, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 7", type=CivVLocationType.tech, game_id=89, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 8", type=CivVLocationType.tech, game_id=90, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 9", type=CivVLocationType.tech, game_id=91, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 10", type=CivVLocationType.tech, game_id=92, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Ancient AP 11", type=CivVLocationType.tech, game_id=93, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Classical AP 1", type=CivVLocationType.tech, game_id=94, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 2", type=CivVLocationType.tech, game_id=95, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 3", type=CivVLocationType.tech, game_id=96, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 4", type=CivVLocationType.tech, game_id=97, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 5", type=CivVLocationType.tech, game_id=98, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 6", type=CivVLocationType.tech, game_id=99, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 7", type=CivVLocationType.tech, game_id=100, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 8", type=CivVLocationType.tech, game_id=101, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Classical AP 9", type=CivVLocationType.tech, game_id=102, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Medieval AP 1", type=CivVLocationType.tech, game_id=103, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 2", type=CivVLocationType.tech, game_id=104, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 3", type=CivVLocationType.tech, game_id=105, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 4", type=CivVLocationType.tech, game_id=106, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 5", type=CivVLocationType.tech, game_id=107, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 6", type=CivVLocationType.tech, game_id=108, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 7", type=CivVLocationType.tech, game_id=109, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 8", type=CivVLocationType.tech, game_id=110, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 9", type=CivVLocationType.tech, game_id=111, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Medieval AP 10", type=CivVLocationType.tech, game_id=112, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Renaissance AP 1", type=CivVLocationType.tech, game_id=113, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 2", type=CivVLocationType.tech, game_id=114, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 3", type=CivVLocationType.tech, game_id=115, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 4", type=CivVLocationType.tech, game_id=116, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 5", type=CivVLocationType.tech, game_id=117, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 6", type=CivVLocationType.tech, game_id=118, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 7", type=CivVLocationType.tech, game_id=119, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 8", type=CivVLocationType.tech, game_id=120, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 9", type=CivVLocationType.tech, game_id=121, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Renaissance AP 10", type=CivVLocationType.tech, game_id=122, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Industrial AP 1", type=CivVLocationType.tech, game_id=123, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 2", type=CivVLocationType.tech, game_id=124, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 3", type=CivVLocationType.tech, game_id=125, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 4", type=CivVLocationType.tech, game_id=126, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 5", type=CivVLocationType.tech, game_id=127, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 6", type=CivVLocationType.tech, game_id=128, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 7", type=CivVLocationType.tech, game_id=129, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 8", type=CivVLocationType.tech, game_id=130, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 9", type=CivVLocationType.tech, game_id=131, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Industrial AP 10", type=CivVLocationType.tech, game_id=132, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Modern AP 1", type=CivVLocationType.tech, game_id=133, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 2", type=CivVLocationType.tech, game_id=134, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 3", type=CivVLocationType.tech, game_id=135, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 4", type=CivVLocationType.tech, game_id=136, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 5", type=CivVLocationType.tech, game_id=137, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 6", type=CivVLocationType.tech, game_id=138, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 7", type=CivVLocationType.tech, game_id=139, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 8", type=CivVLocationType.tech, game_id=140, region=regions.MODERN_ERA),
    CivVLocationData(name="Modern AP 9", type=CivVLocationType.tech, game_id=141, region=regions.MODERN_ERA),
    CivVLocationData(name="Atomic AP 1", type=CivVLocationType.tech, game_id=142, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 2", type=CivVLocationType.tech, game_id=143, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 3", type=CivVLocationType.tech, game_id=144, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 4", type=CivVLocationType.tech, game_id=145, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 5", type=CivVLocationType.tech, game_id=146, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 6", type=CivVLocationType.tech, game_id=147, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 7", type=CivVLocationType.tech, game_id=148, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Atomic AP 8", type=CivVLocationType.tech, game_id=149, region=regions.ATOMIC_ERA),
    CivVLocationData(name="Information AP 1", type=CivVLocationType.tech, game_id=150, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 2", type=CivVLocationType.tech, game_id=151, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 3", type=CivVLocationType.tech, game_id=152, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 4", type=CivVLocationType.tech, game_id=153, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 5", type=CivVLocationType.tech, game_id=154, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 6", type=CivVLocationType.tech, game_id=155, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 7", type=CivVLocationType.tech, game_id=156, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 8", type=CivVLocationType.tech, game_id=157, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 9", type=CivVLocationType.tech, game_id=158, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 10", type=CivVLocationType.tech, game_id=159, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 11", type=CivVLocationType.tech, game_id=160, region=regions.INFORMATION_ERA),
    CivVLocationData(name="Information AP 12", type=CivVLocationType.tech, game_id=161, region=regions.INFORMATION_ERA),

    # Additional techs
    CivVLocationData(name="Ancient AP Bonus", type=CivVLocationType.tech, game_id=162, region=regions.ANCIENT_ERA),
    CivVLocationData(name="Classical AP Bonus", type=CivVLocationType.tech, game_id=163, region=regions.CLASSICAL_ERA),
    CivVLocationData(name="Medieval AP Bonus", type=CivVLocationType.tech, game_id=164, region=regions.MEDIEVAL_ERA),
    CivVLocationData(name="Renaissance AP Bonus", type=CivVLocationType.tech, game_id=165, region=regions.RENAISSANCE_ERA),
    CivVLocationData(name="Industrial AP Bonus", type=CivVLocationType.tech, game_id=166, region=regions.INDUSTRIAL_ERA),
    CivVLocationData(name="Modern AP Bonus", type=CivVLocationType.tech, game_id=167, region=regions.MODERN_ERA),
    CivVLocationData(name="Atomic AP Bonus", type=CivVLocationType.tech, game_id=168, region=regions.ATOMIC_ERA),
]
"List of all technology locations"


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
"List of all policy locations"


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
"List of all policy branch locations"


NATIONAL_WONDER_LOCATIONS = [
    # All vanilla national wonders
    CivVLocationData(
        name="Heroic Epic",
        type=CivVLocationType.national_wonder,
        game_id=55,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Iron Working"].name: 1,
                    items.TECH_ITEMS["Bronze Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National College",
        type=CivVLocationType.national_wonder,
        game_id=56,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Philosophy"].name: 1,
                    items.TECH_ITEMS["Writing"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 1,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Epic",
        type=CivVLocationType.national_wonder,
        game_id=57,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Circus Maximus",
        type=CivVLocationType.national_wonder,
        game_id=58,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Horseback Riding"].name: 1,
                    items.TECH_ITEMS["Construction"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 2,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="East India Company",
        type=CivVLocationType.national_wonder,
        game_id=59,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Guilds"].name: 1,
                    items.TECH_ITEMS["Currency"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Ironworks",
        type=CivVLocationType.national_wonder,
        game_id=60,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Machinery"].name: 1,
                    items.TECH_ITEMS["Metal Casting"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Ranged Unit"].name: 2,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Oxford University",
        type=CivVLocationType.national_wonder,
        game_id=61,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Education"].name: 1,
                    items.TECH_ITEMS["Writing"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hermitage",
        type=CivVLocationType.national_wonder,
        game_id=62,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                    items.TECH_ITEMS["Acoustics"].name: 1,
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Intelligence Agency",
        type=CivVLocationType.national_wonder,
        game_id=127,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Radio"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Banking"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 6,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Grand Temple",
        type=CivVLocationType.national_wonder,
        game_id=141,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                    items.TECH_ITEMS["Philosophy"].name: 1,
                    items.TECH_ITEMS["Pottery"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Growth"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Visitor Center",
        type=CivVLocationType.national_wonder,
        game_id=142,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                    items.TECH_ITEMS["Refrigeration"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 5,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Writers' Guild",
        type=CivVLocationType.national_wonder,
        game_id=148,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Artists' Guild",
        type=CivVLocationType.national_wonder,
        game_id=149,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Guilds"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Musicians' Guild",
        type=CivVLocationType.national_wonder,
        game_id=150,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Acoustics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
]
"List of all national wonder locations"


WORLD_WONDER_LOCATIONS = [
    # All vanilla world wonders
    CivVLocationData(
        name="Great Lighthouse",
        type=CivVLocationType.world_wonder,
        game_id=63,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Optics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Exploration"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Stonehenge",
        type=CivVLocationType.world_wonder,
        game_id=64,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Calendar"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Library",
        type=CivVLocationType.world_wonder,
        game_id=65,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Writing"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Pyramids",
        type=CivVLocationType.world_wonder,
        game_id=66,
        region=regions.CLASSICAL_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Masonry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Colossus",
        type=CivVLocationType.world_wonder,
        game_id=67,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Iron Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Oracle",
        type=CivVLocationType.world_wonder,
        game_id=68,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Philosophy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hanging Gardens",
        type=CivVLocationType.world_wonder,
        game_id=69,
        region=regions.ANCIENT_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Mathematics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Siege Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Wall",
        type=CivVLocationType.world_wonder,
        game_id=70,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Engineering"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Growth"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Angkor Wat",
        type=CivVLocationType.world_wonder,
        game_id=71,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Education"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hagia Sophia",
        type=CivVLocationType.world_wonder,
        game_id=72,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Chichen Itza",
        type=CivVLocationType.world_wonder,
        game_id=73,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Civil Service"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Growth"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Machu Pichu",
        type=CivVLocationType.world_wonder,
        game_id=74,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Guilds"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Notre Dame",
        type=CivVLocationType.world_wonder,
        game_id=75,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Physics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Siege Unit"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Porcelain Tower",
        type=CivVLocationType.world_wonder,
        game_id=76,
        region=regions.INFORMATION_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Himeji Castle",
        type=CivVLocationType.world_wonder,
        game_id=77,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Gunpowder"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 6,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Sistine Chapel",
        type=CivVLocationType.world_wonder,
        game_id=78,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Acoustics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Kremlin",
        type=CivVLocationType.world_wonder,
        game_id=79,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Railroad"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Forbidden Palace",
        type=CivVLocationType.world_wonder,
        game_id=80,
        region=regions.INDUSTRIAL_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Banking"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Taj Mahal",
        type=CivVLocationType.world_wonder,
        game_id=81,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Big Ben",
        type=CivVLocationType.world_wonder,
        game_id=82,
        region=regions.ATOMIC_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Industrialization"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Louvre",
        type=CivVLocationType.world_wonder,
        game_id=83,
        region=regions.INFORMATION_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Archaeology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Brandenburg Gate",
        type=CivVLocationType.world_wonder,
        game_id=84,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Military Science"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 9,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Statue of Liberty",
        type=CivVLocationType.world_wonder,
        game_id=85,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Replaceable Parts"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 11,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Cristo Redentor",
        type=CivVLocationType.world_wonder,
        game_id=86,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Plastics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Eiffel Tower",
        type=CivVLocationType.world_wonder,
        game_id=87,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Radio"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Pentagon",
        type=CivVLocationType.world_wonder,
        game_id=88,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Combined Arms"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 13,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Sydney Opera House",
        type=CivVLocationType.world_wonder,
        game_id=90,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Ecology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Statue of Zeus",
        type=CivVLocationType.world_wonder,
        game_id=93,
        region=regions.MEDIEVAL_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Bronze Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Temple of Artemis",
        type=CivVLocationType.world_wonder,
        game_id=94,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Archery"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Ranged Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Mausoleum of Halicarnassus",
        type=CivVLocationType.world_wonder,
        game_id=95,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Masonry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Alhambra",
        type=CivVLocationType.world_wonder,
        game_id=128,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Chivalry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="CN Tower",
        type=CivVLocationType.world_wonder,
        game_id=129,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hubble Space Telescope",
        type=CivVLocationType.world_wonder,
        game_id=130,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Satellites"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Leaning Tower of Pisa",
        type=CivVLocationType.world_wonder,
        game_id=131,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Printing Press"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Mosque of Djenne",
        type=CivVLocationType.world_wonder,
        game_id=132,
        region=regions.RENAISSANCE_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Neuschwanstein",
        type=CivVLocationType.world_wonder,
        game_id=133,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Railroad"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Petra",
        type=CivVLocationType.world_wonder,
        game_id=134,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Currency"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Terracotta Army",
        type=CivVLocationType.world_wonder,
        game_id=135,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Construction"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Firewall",
        type=CivVLocationType.world_wonder,
        game_id=136,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Computers"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 14,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Uffizi",
        type=CivVLocationType.world_wonder,
        game_id=154,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Globe Theatre",
        type=CivVLocationType.world_wonder,
        game_id=155,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Printing Press"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Broadway",
        type=CivVLocationType.world_wonder,
        game_id=156,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Radio"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Red Fort",
        type=CivVLocationType.world_wonder,
        game_id=157,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Metallurgy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Prora",
        type=CivVLocationType.world_wonder,
        game_id=158,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Flight"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Ranged Unit"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Borobudur",
        type=CivVLocationType.world_wonder,
        game_id=159,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Parthenon",
        type=CivVLocationType.world_wonder,
        game_id=160,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="International Space Station",
        type=CivVLocationType.world_wonder,
        game_id=161,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Satellites"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
]
"List of all world wonder locations"


VICTORY_LOCATIONS = {
    "Science": CivVLocationData(
        name="Science",
        type=CivVLocationType.victory,
        game_id=1,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Mining"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Rocketry"].name: 1,
                    items.TECH_ITEMS["Advanced Ballistics"].name: 1,
                    items.TECH_ITEMS["Particle Physics"].name: 1,
                    items.TECH_ITEMS["Satellites"].name: 1,
                    items.TECH_ITEMS["Nanotechnology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 1,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 6,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 9,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    "Culture": CivVLocationData(
        name="Culture",
        type=CivVLocationType.victory,
        game_id=3,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.POLICY_ITEMS["Aesthetics"].name: 1,
                    items.POLICY_ITEMS["Cultural Exchange"].name: 1,
                    items.POLICY_ITEMS["Aesthetics Finisher"].name: 1,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                    items.TECH_ITEMS["Acoustics"].name: 1,
                    items.TECH_ITEMS["Archaeology"].name: 1,
                    items.TECH_ITEMS["Radio"].name: 1,
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                    items.TECH_ITEMS["The Internet"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 6,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    "Diplomatic": CivVLocationData(
        name="Diplomatic",
        type=CivVLocationType.victory,
        game_id=4,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.POLICY_ITEMS["Patronage"].name: 1,
                    items.POLICY_ITEMS["Philanthropy"].name: 1,
                    items.POLICY_ITEMS["Consulates"].name: 1,
                    items.PROGRESSIVE_ERA_ITEM.name: 7,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Animal Husbandry"].name: 1,
                    items.TECH_ITEMS["Currency"].name: 1,
                    items.TECH_ITEMS["Guilds"].name: 1,
                    items.TECH_ITEMS["Banking"].name: 1,
                    items.TECH_ITEMS["Economics"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Globalization"].name: 1,
                    items.TECH_ITEMS["Printing Press"].name: 1,
                    items.TECH_ITEMS["Optics"].name: 1,
                    items.TECH_ITEMS["Astronomy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 7,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Exploration"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
}
"Dict of all victory locations"
