# %% IMPORTS
from dataclasses import dataclass
from textwrap import dedent

from Options import Choice, DefaultOnToggle, PerGameCommonOptions, OptionSet, Range, Toggle

from . import items

# All declaration
__all__ = ["CivVOptions"]


# %% OPTION CLASSES
class VictoryGoalLogic(Choice):
    """
    Which victory should be achievable before the game is considered beatable?

    Note that this solely affects progression logic. You can still beat the game earlier than expected or pursue a
    different victory if you so choose.

    Domination and Time victories are not included here as Domination can be achieved at any moment and Time has no
    requirements.

    """

    display_name = "Victory Goal Logic"
    option_none = 0
    option_science = 1
    option_culture = 3
    option_diplomatic = 4
    default = option_none


class EraGoalLogic(Choice):
    """
    Which era must be unlocked before the game is considered beatable?

    This is in addition to the value given for "Victory Goal Logic".
    Similarly, this solely affects progression logic.

    """

    display_name = "Era Goal Logic"
    option_ancient = 0
    option_classical = 1
    option_medieval = 2
    option_renaissance = 3
    option_industrial = 4
    option_modern = 5
    option_atomic = 6
    option_information = 7
    default = option_information


class EmbarkingGoalLogic(DefaultOnToggle):
    """
    Add Optics and Astronomy as requirements before the game is considered beatable.

    Similarly to other goal logic options, this solely affects progression logic.

    """

    display_name = "Embarking Goal Logic"


class PolicyCostModifier(Range):
    """
    Multiplies the base cost of adopting social policies with the given percentage.

    """

    display_name = "Policy Cost Modifier"
    range_start = 0
    range_end = 1000
    default = 90


class TechCostModifier(Range):
    """
    Multiplies the base cost of researching technologies with the given percentage.

    """

    display_name = "Tech Cost Modifier"
    range_start = 0
    range_end = 1000
    default = 100


class ProgressiveTechs(DefaultOnToggle):
    """
    Use progressive technologies.

    Progressive technologies divides all 79 technologies (excl. Agriculture) into 11 categories.
    This makes the unlocking of technologies feel less chaotic and more streamlined compared to true random
    technologies. It also makes it far less likely to not have important early-era buildings in the mid to late game.

    """

    display_name = "Progressive Techs"


class ItemHints(Choice):
    """
    Enable item hints for all policy branch; policy; and technology locations.

    Options are:
    - full: Locations state their exact item.
    - classification: Locations state the classification of their item (progression; useful; filler; trap).
    - none: Locations do not state their item.

    """

    display_name = "Item Hints"
    option_full = 0
    option_classification = 1
    option_none = 2
    default = option_classification


class DisguiseTraps(Toggle):
    """
    Item classification hints will classify traps as progression items.

    Has no effect if item hints are set to 'none'.

    """

    display_name = "Disguise Traps"


class BuildingSanity(Toggle):
    """
    Add most standard buildings to the location pool.

    Buildings that will not be added:
    - Palace
    - Courthouse
    - Any religious building (Cathedral; Monastery; Mosque; and Pagoda)
    - Any civilization-unique building (they count as the building they replace instead)
    - Any National Wonder (see National Wonder Sanity instead)
    - Any World Wonder (see World Wonder Sanity instead)
    This adds 53 buildings to the location pool in total.

    """

    display_name = "Building Sanity"


class NationalWonderSanity(Toggle):
    """
    Add all national wonders to the location pool.

    This adds the 11 national wonders and the 3 guilds to the location pool.

    """

    display_name = "National Wonder Sanity"


class WorldWonderSanity(Toggle):
    """
    Add all world wonders to the location pool.

    This adds the 47 world wonders to the location pool, including the 3 ideology world wonders.

    WARNING: This option is NOT suitable for syncs.

    """

    display_name = "World Wonder Sanity"


class EnableTraps(Toggle):
    """
    Add traps to the filler item pool.

    """

    display_name = "Enable Traps"


class TrapBlacklist(OptionSet):
    __doc__ = dedent(
        """
        Blacklist the given traps from being included in the filler item pool.
    
        Has no effect if traps are not enabled.
        
        Valid keys are:
        {keys}
    
        """)[1:].format(keys="\n".join(sorted(set((item_data.name for item_data in items.TRAP_ITEMS)))))

    display_name = "Trap Blacklist"
    valid_keys = set((item_data.name for item_data in items.TRAP_ITEMS))


class TrapFillerChance(Range):
    """
    The percent chance for a filler item to be a trap instead.

    Has no effect if traps are not enabled.

    """

    display_name = "Trap Filler Chance"
    range_start = 0
    range_end = 100
    default = 5


# %% CIV V OPTIONS CLASS
@dataclass
class CivVOptions(PerGameCommonOptions):
    victory_goal_logic: VictoryGoalLogic
    era_goal_logic: EraGoalLogic
    embarking_goal_logic: EmbarkingGoalLogic
    policy_cost_modifier: PolicyCostModifier
    tech_cost_modifier: TechCostModifier
    progressive_techs: ProgressiveTechs
    item_hints: ItemHints
    disguise_traps: DisguiseTraps
    building_sanity: BuildingSanity
    national_wonder_sanity: NationalWonderSanity
    world_wonder_sanity: WorldWonderSanity
    enable_traps: EnableTraps
    trap_blacklist: TrapBlacklist
    trap_filler_chance: TrapFillerChance
