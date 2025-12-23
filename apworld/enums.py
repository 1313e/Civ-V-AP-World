# %% IMPORTS
from enum import IntEnum, StrEnum

# All declaration
__all__ = ["CivVFillerType", "CivVItemGroup", "CivVItemType", "CivVLocationType", "NotificationTypes"]


# %% ENUM DEFINITIONS
class CivVFillerType(StrEnum):
    """
    Enum defining the various filler item types for Civ V.

    """

    change_all_city_population = "change_all_city_population"
    change_culture = "change_culture"
    change_culture_per_turn_for_free = "change_culture_per_turn_for_free"
    change_extra_happiness_per_city = "change_extra_happiness_per_city"
    change_faith = "change_faith"
    change_free_great_people = "change_free_great_people"
    change_free_policies = "change_free_policies"
    change_free_techs = "change_free_techs"
    change_gold = "change_gold"
    change_new_city_extra_population = "change_new_city_extra_population"
    declare_war_random = "declare_war_random"
    denounce_random = "denounce_random"
    start_golden_age = "start_golden_age"


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

    bonus = "bonus"
    era = "era"
    policy = "policy"
    tech = "tech"
    trap = "trap"


class CivVLocationType(StrEnum):
    """
    Enum defining the various location types for Civ V.

    """

    policy = "policy"
    policy_branch = "policy_branch"
    tech = "tech"
    national_wonder = "national_wonder"
    victory = "victory"
    world_wonder = "world_wonder"


class NotificationTypes(IntEnum):
    """
    Enum defining the different notification types for Civ V.

    """

    generic = 0
    positive = 1
    negative = 2
