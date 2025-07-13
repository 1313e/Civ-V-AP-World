# %% IMPORTS
from worlds.LauncherComponents import launch_subprocess

from .constants import GAME_NAME

# All declaration
__all__ = ["run_client"]


# %% HELPER FUNCTION DEFINITIONS
def run_client(*args, **kwargs):
    """
    Runs the Civilization V AP client.

    """

    print(f"Running {GAME_NAME} Client")
    from .client import CivVClient
    launch_subprocess(CivVClient.run_client, name=f"{GAME_NAME} Client")
