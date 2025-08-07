# %% IMPORTS
from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions, OptionSet, Range, Toggle

from . import items

# All declaration
__all__ = ["CivVOptions"]


# %% OPTION CLASSES
class EraGoal(Choice):
    """
    Which era must be unlocked before the game is considered beatable?

    """

    display_name = "Era Goal"
    option_ancient = 0
    option_classical = 1
    option_medieval = 2
    option_renaissance = 3
    option_industrial = 4
    option_modern = 5
    option_atomic = 6
    option_information = 7
    default = option_information


class ProgressiveTechs(DefaultOnToggle):
    """
    Use progressive technologies.

    Progressive technologies divides all 79 technologies (excl. Agriculture) into 11 categories.
    This makes the unlocking of technologies feel less chaotic and more streamlined compared to true random
    technologies. It also makes it far less likely to not have important early-era buildings in the mid to late game.

    """

    display_name = "Progressive Techs"


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
    """
    Blacklist the given traps from being included in the filler item pool.

    Has no effect if traps are not enabled.

    """

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
    era_goal: EraGoal
    progressive_techs: ProgressiveTechs
    national_wonder_sanity: NationalWonderSanity
    world_wonder_sanity: WorldWonderSanity
    enable_traps: EnableTraps
    trap_blacklist: TrapBlacklist
    trap_filler_chance: TrapFillerChance
