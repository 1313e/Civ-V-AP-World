# %% IMPORTS
from enum import IntEnum, StrEnum

from BaseClasses import ItemClassification

# All declaration
__all__ = [
    "CivVFillerType",
    "CivVItemClassificationColors",
    "CivVItemClassificationFlags",
    "CivVItemClassificationNames",
    "CivVItemGroup",
    "CivVItemType",
    "CivVLocationType",
    "CivVNotificationTypes",
]


# %% ENUM DEFINITIONS
class CivVFillerType(StrEnum):
    """
    Enum defining the various filler item types for Civ V.

    """

    all_units_free_promotion = "all_units_free_promotion"
    change_all_city_population = "change_all_city_population"
    change_all_city_state_influence = "change_all_city_state_influence"
    change_all_unit_experience = "change_all_unit_experience"
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
    grant_free_unit = "grant_free_unit"
    grant_free_worker = "grant_free_worker"
    shuffle_units = "shuffle_units"
    spawn_barbarians = "spawn_barbarians"
    start_golden_age = "start_golden_age"


class CivVItemClassificationColors(StrEnum):
    """
    Enum defining the colors to use for each item classification in Civ V.

    """

    progression = "COLOR:117:255:43:255"
    useful = "COLOR:64:251:252:255"
    filler = "COLOR:39:113:255:255"
    trap = "COLOR:248:38:38:255"
    default = "COLOR:155:155:155:255"

    @classmethod
    def get_color(cls, classification: ItemClassification) -> "CivVItemClassificationColors":
        # Check in order of priority which base classification is given and returns its enum value
        if ItemClassification.progression in classification:
            return cls.progression
        elif ItemClassification.useful in classification:
            return cls.useful
        elif ItemClassification.trap in classification:
            return cls.trap
        else:
            return cls.filler


class CivVItemClassificationFlags(StrEnum):
    """
    Enum defining the flags to use for each item classification in Civ V.

    """

    progression = "ICON_TEAM_4"
    useful = "ICON_TEAM_5"
    filler = "ICON_TEAM_8"
    trap = "ICON_TEAM_2"
    default = "ICON_TEAM_10"

    @classmethod
    def get_flag(cls, classification: ItemClassification) -> "CivVItemClassificationFlags":
        # Check in order of priority which base classification is given and returns its enum value
        if ItemClassification.progression in classification:
            return cls.progression
        elif ItemClassification.useful in classification:
            return cls.useful
        elif ItemClassification.trap in classification:
            return cls.trap
        else:
            return cls.filler

class CivVItemClassificationNames(StrEnum):
    """
    Enum defining the names to use for each item classification in Civ V.

    """

    progression = "progression"
    useful = "useful"
    filler = "filler"
    trap = "trap"

    @classmethod
    def get_name(cls, classification: ItemClassification) -> "CivVItemClassificationNames":
        # Check in order of priority which base classification is given and returns its enum value
        if ItemClassification.progression in classification:
            return cls.progression
        elif ItemClassification.useful in classification:
            return cls.useful
        elif ItemClassification.trap in classification:
            return cls.trap
        else:
            return cls.filler

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
    promotion = "promotion"
    settler = "settler"
    tech = "tech"
    trap = "trap"


class CivVLocationType(StrEnum):
    """
    Enum defining the various location types for Civ V.

    """

    building = "building"
    policy = "policy"
    policy_branch = "policy_branch"
    promotion = "promotion"
    tech = "tech"
    national_wonder = "national_wonder"
    settler = "settler"
    unit = "unit"
    world_wonder = "world_wonder"


class CivVNotificationTypes(IntEnum):
    """
    Enum defining the different notification types for Civ V.

    """

    generic = 0
    positive = 1
    negative = 2
