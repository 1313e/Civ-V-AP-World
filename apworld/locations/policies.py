# %% IMPORTS
from .core import CivVLocationData
from .. import regions
from ..enums import CivVLocationType

# All declaration
__all__ = [
    "POLICY_BRANCH_LOCATIONS",
    "POLICY_LOCATIONS",
]


# %% LOCATION DECLARATIONS
POLICY_BRANCH_LOCATIONS = [
    # All vanilla policy branches
    CivVLocationData(name="Tradition", type=CivVLocationType.policy_branch, game_id=0, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Liberty", type=CivVLocationType.policy_branch, game_id=1, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Honor", type=CivVLocationType.policy_branch, game_id=2, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Piety", type=CivVLocationType.policy_branch, game_id=3, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Patronage", type=CivVLocationType.policy_branch, game_id=4, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Aesthetics", type=CivVLocationType.policy_branch, game_id=5, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Commerce", type=CivVLocationType.policy_branch, game_id=6, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Exploration", type=CivVLocationType.policy_branch, game_id=7, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism", type=CivVLocationType.policy_branch, game_id=8, region=regions.INFORMATION_ERA_POLICY),

    # Policy branch finishers masked as policy branches
    CivVLocationData(name="Tradition Finished", type=CivVLocationType.policy_branch, game_id=12, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Liberty Finished", type=CivVLocationType.policy_branch, game_id=13, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Honor Finished", type=CivVLocationType.policy_branch, game_id=14, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Piety Finished", type=CivVLocationType.policy_branch, game_id=15, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Patronage Finished", type=CivVLocationType.policy_branch, game_id=16, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Aesthetics Finished", type=CivVLocationType.policy_branch, game_id=17, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Commerce Finished", type=CivVLocationType.policy_branch, game_id=18, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Exploration Finished", type=CivVLocationType.policy_branch, game_id=19, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism Finished", type=CivVLocationType.policy_branch, game_id=20, region=regions.INFORMATION_ERA_POLICY),
]
"List of all policy branch locations"


POLICY_LOCATIONS = [
    # All vanilla policies converted to AP policies
    CivVLocationData(name="Tradition AP 1", type=CivVLocationType.policy, game_id=111, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Tradition AP 2", type=CivVLocationType.policy, game_id=112, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Tradition AP 3", type=CivVLocationType.policy, game_id=113, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Tradition AP 4", type=CivVLocationType.policy, game_id=114, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Tradition AP 5", type=CivVLocationType.policy, game_id=115, region=regions.ANCIENT_ERA_POLICY),
    CivVLocationData(name="Liberty AP 1", type=CivVLocationType.policy, game_id=116, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Liberty AP 2", type=CivVLocationType.policy, game_id=117, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Liberty AP 3", type=CivVLocationType.policy, game_id=118, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Liberty AP 4", type=CivVLocationType.policy, game_id=119, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Liberty AP 5", type=CivVLocationType.policy, game_id=120, region=regions.CLASSICAL_ERA_POLICY),
    CivVLocationData(name="Honor AP 1", type=CivVLocationType.policy, game_id=121, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Honor AP 2", type=CivVLocationType.policy, game_id=122, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Honor AP 3", type=CivVLocationType.policy, game_id=123, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Honor AP 4", type=CivVLocationType.policy, game_id=124, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Honor AP 5", type=CivVLocationType.policy, game_id=125, region=regions.MEDIEVAL_ERA_POLICY),
    CivVLocationData(name="Piety AP 1", type=CivVLocationType.policy, game_id=126, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Piety AP 2", type=CivVLocationType.policy, game_id=127, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Piety AP 3", type=CivVLocationType.policy, game_id=128, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Piety AP 4", type=CivVLocationType.policy, game_id=129, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Piety AP 5", type=CivVLocationType.policy, game_id=130, region=regions.RENAISSANCE_ERA_POLICY),
    CivVLocationData(name="Patronage AP 1", type=CivVLocationType.policy, game_id=131, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Patronage AP 2", type=CivVLocationType.policy, game_id=132, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Patronage AP 3", type=CivVLocationType.policy, game_id=133, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Patronage AP 4", type=CivVLocationType.policy, game_id=134, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Patronage AP 5", type=CivVLocationType.policy, game_id=135, region=regions.INDUSTRIAL_ERA_POLICY),
    CivVLocationData(name="Aesthetics AP 1", type=CivVLocationType.policy, game_id=136, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Aesthetics AP 2", type=CivVLocationType.policy, game_id=137, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Aesthetics AP 3", type=CivVLocationType.policy, game_id=138, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Aesthetics AP 4", type=CivVLocationType.policy, game_id=139, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Aesthetics AP 5", type=CivVLocationType.policy, game_id=140, region=regions.MODERN_ERA_POLICY),
    CivVLocationData(name="Commerce AP 1", type=CivVLocationType.policy, game_id=141, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Commerce AP 2", type=CivVLocationType.policy, game_id=142, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Commerce AP 3", type=CivVLocationType.policy, game_id=143, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Commerce AP 4", type=CivVLocationType.policy, game_id=144, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Commerce AP 5", type=CivVLocationType.policy, game_id=145, region=regions.ATOMIC_ERA_POLICY),
    CivVLocationData(name="Exploration AP 1", type=CivVLocationType.policy, game_id=146, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Exploration AP 2", type=CivVLocationType.policy, game_id=147, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Exploration AP 3", type=CivVLocationType.policy, game_id=148, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Exploration AP 4", type=CivVLocationType.policy, game_id=149, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Exploration AP 5", type=CivVLocationType.policy, game_id=150, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism AP 1", type=CivVLocationType.policy, game_id=151, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism AP 2", type=CivVLocationType.policy, game_id=152, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism AP 3", type=CivVLocationType.policy, game_id=153, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism AP 4", type=CivVLocationType.policy, game_id=154, region=regions.INFORMATION_ERA_POLICY),
    CivVLocationData(name="Rationalism AP 5", type=CivVLocationType.policy, game_id=155, region=regions.INFORMATION_ERA_POLICY),
]
"List of all policy locations"
