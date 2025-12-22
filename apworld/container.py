# %% IMPORTS
from pathlib import Path
from typing import TYPE_CHECKING

from worlds.Files import APPlayerContainer

from .constants import CONTAINER_EXTENSION, GAME_NAME
if TYPE_CHECKING:
    from .world import CivVWorld

# All declaration
__all__ = ["CivVContainer"]


# %% CIV_V_CONTAINER CLASS DEFINITION
class CivVContainer(APPlayerContainer):
    game = GAME_NAME
    patch_file_ending = CONTAINER_EXTENSION

    def __init__(self, path: Path, world: "CivVWorld | None", **kwargs):
        # Call super method
        super().__init__(path=path, **kwargs)

        # Create instance attributes
        self.world: "CivVWorld | None" = world
        "The instance of the Civ V AP world to use for this container"

    @classmethod
    def create_output_file(cls, output_directory: str, world: "CivVWorld") -> None:
        """
        Creates a new output file for the given `world` in the provided `output_directory`.

        This process involves taking the state of the given `world` like the items placed and the user's YAML options,
        and creating a new APMod version that is specific to this slot.
        This APMod is then loaded during the startup of the client when the slot is played.

        """

        # Get path to player output file
        filename = f"{world.multiworld.get_out_file_name_base(world.player)}{cls.patch_file_ending}"
        filepath = Path(output_directory) / filename

        # Create container instance
        container = cls(
            path=filepath,
            world=world,
            player=world.player,
            player_name=world.multiworld.get_file_safe_player_name(world.player),
        )

        # Create output file with this container
        container.write()

    @classmethod
    def read_output_file(cls, path: str) -> tuple[str, str]:
        """
        Reads the output file at the given `path` and copies over the contained APMod to the correct folder.
        Also returns the `server_address` and `player_name` in the output file.

        """

        # Create container instance
        container = cls(path=Path(path), world=None)
        container.read()

        # Get path to mods folder
        from .world import CivVWorld
        mods_folder_path = CivVWorld.settings.mods_folder_path

        # Return the server address and player name
        return container.server, container.player_name
