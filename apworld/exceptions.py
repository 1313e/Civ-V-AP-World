# %% IMPORTS
# All declaration
__all__ = [
    "TunerConnectionException",
    "TunerErrorException",
    "TunerException",
    "TunerRuntimeException",
    "TunerTimeoutException",
]


# %% EXCEPTION DEFINITIONS
class TunerException(Exception):
    """
    Generic exception class raised whenever an error occurs in the use of the Civilization V tuner.

    """


class TunerErrorException(TunerException):
    """
    Exception raised when the Civilization V tuner has an internal unresolved error.

    """


class TunerRuntimeException(TunerException):
    """
    Exception raised when the Civilization V tuner has an internal runtime error.

    This mainly occurs when the game's state is not yet ready to respond or is invalid.

    """


class TunerConnectionException(TunerException):
    """
    Exception raised when the Civilization V tuner cannot connect to the game.

    This mainly occurs when the game is not connected to the tuner at all (it is not listening to any socket) or it has
    reset the connection to the tuner.
    The latter can happen due to the game's nature to stop all update cycles in-game whenever you tab out of the game.
    After tabbing back in, the connection gets reset and needs to be set up again.

    """


class TunerTimeoutException(TunerException):
    """
    Exception raised when the Civilization V tuner has a timeout error.

    This mainly occurs when the game is not responding to commands send to it via the tuner, either because the game is
    not connected to the tuner's port or the Civ V AP mod is not loaded currently.

    """
