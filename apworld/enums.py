# %% IMPORTS
from enum import StrEnum

# All declaration
__all__ = ["CivVItemGroup", "CivVItemType", "CivVLocationType"]


# %% ENUM DEFINITIONS
class CivVItemGroup(StrEnum):
    """
    Enum defining the various item groups for Civ V.

    These are in addition to the item types defined in :class:`CivVItemType`.

    """

    # Eras
    ancient_era = "ancient_era"
    classical_era = "classical_era"
    medieval_era = "medieval_era"
    renaissance_era = "renaissance_era"
    industrial_era = "industrial_era"
    modern_era = "modern_era"
    atomic_era = "atomic_era"
    information_era = "information_era"


class CivVItemType(StrEnum):
    """
    Enum defining the various item types for Civ V.

    """

    era = "era"
    policy = "policy"
    tech = "tech"


class CivVLocationType(StrEnum):
    """
    Enum defining the various location types for Civ V.

    """

    policy = "policy"
    policy_branch = "policy_branch"
    tech = "tech"
    national_wonder = "national_wonder"
    world_wonder = "world_wonder"
