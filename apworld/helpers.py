# %% IMPORTS
from worlds.LauncherComponents import launch_subprocess

from .constants import GAME_NAME

# All declaration
__all__ = [
    "run_client",
    "to_title",
]


# %% HELPER FUNCTION DEFINITIONS
def run_client(*args, **kwargs):
    """
    Runs the Civilization V AP client.

    """

    print(f"Running {GAME_NAME} Client")
    from .client import CivVClient
    launch_subprocess(CivVClient.run_client, name=f"{GAME_NAME} Client")


def to_title(text: str) -> str:
    """
    Converts the given `text` to a title, converting underscores to spaces and capitalizing the first letter in each
    word.

    """

    return " ".join((x.capitalize() for x in text.split("_")))
