# %% IMPORTS
from settings import Group, UserFolderPath

from .constants import GAME_NAME

# All declaration
__all__ = ["CivVSettings"]


# %% SETTING CLASSES
class ModsFolderPath(UserFolderPath):
    """
    Path to your Civilization V mods folder.

    """

    description = f"{GAME_NAME} mods folder"


# %% CIV V SETTINGS CLASS
class CivVSettings(Group):
    mods_folder_path: ModsFolderPath = ModsFolderPath(None)
