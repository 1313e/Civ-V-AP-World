# %% IMPORTS
from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions

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


# %% CIV V OPTIONS CLASS
@dataclass
class CivVOptions(PerGameCommonOptions):
    era_goal: EraGoal
