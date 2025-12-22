# %% IMPORTS
import itertools
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Any
from xml.etree import ElementTree

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

    # Additional class attributes
    AP_MOD_TEMPLATE_DIRECTORY: Path = Path(__file__).parent / "templates/apmod"
    "Path towards the directory holding the templates of the Civ V AP Mod"

    def __init__(self, path: Path, world: "CivVWorld | None", **kwargs):
        # Call super method
        super().__init__(path=path, **kwargs)
        self.path: Path = path

        # Create instance attributes
        self.world: "CivVWorld | None" = world
        "The instance of the Civ V AP world to use for this container"

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        # Copy over the entire contents of the APMod directory
        for root, dirs, files in self.AP_MOD_TEMPLATE_DIRECTORY.walk():
            for file in files:
                # Act according to the extension of this file
                filepath = root / file
                zip_path = str(filepath.relative_to(self.AP_MOD_TEMPLATE_DIRECTORY.parent))
                match file.rsplit(".", 1)[1]:
                    # For XML files, we want to use the file as a template and substitute all appropriate data
                    case "xml":
                        # TODO: Actually implement the substitution
                        contents = filepath.read_text()
                        opened_zipfile.writestr(zip_path, contents)

                    # For everything else, simply copy over the full file without modifications
                    case _:
                        opened_zipfile.write(filepath, zip_path)

        # Call super method
        super().write_contents(opened_zipfile)

    def read_contents(self, opened_zipfile: zipfile.ZipFile) -> dict[str, Any]:
        # Get path to mods folder
        from .world import CivVWorld
        mods_folder_path = Path(CivVWorld.settings.mods_folder_path)

        # If the mod does not exist yet, we need to create it from the output file
        zip_name = self.path.name.rsplit('.', 1)[0]
        mod_path = mods_folder_path / f"{self.AP_MOD_TEMPLATE_DIRECTORY.name} - {zip_name}"
        if not mod_path.exists():
            # Extract all mod files to a temporary directory
            tempdir = Path(tempfile.mkdtemp())
            for file in [x for x in opened_zipfile.namelist() if x.startswith(self.AP_MOD_TEMPLATE_DIRECTORY.name)]:
                # Act according to the extension of this file
                match file.rsplit(".", 1)[1]:
                    # For modinfo files, we want to update its teaser to match the name of the zipfile
                    # And the version to a value that is currently not in use
                    case "modinfo":
                        # Parse the file as XML
                        xml_tree = ElementTree.parse(opened_zipfile.open(file))
                        xml_root = xml_tree.getroot()

                        # Update the version and teaser fields
                        xml_root.set("version", str(self._get_mod_version(mods_folder_path)))
                        xml_root.find("Properties/Teaser").text = zip_name

                        # Store the modinfo file
                        xml_tree.write(tempdir / file)

                    # For every other file, extract file as is
                    case _:
                        opened_zipfile.extract(file, tempdir)

            # Copy the apmod folder inside this temporary directory to the mods folder
            _ = shutil.copytree(tempdir / self.AP_MOD_TEMPLATE_DIRECTORY.name, mod_path)

            # Remove the temporary directory
            shutil.rmtree(tempdir)

        # Call super method and return its result
        return super().read_contents(opened_zipfile)

    def _get_mod_version(self, mods_folder_path) -> int:
        """
        Returns the version to use for an APMod, given the current mods already installed.

        """

        # Get the versions of all installed APMod versions
        modinfo_files = mods_folder_path.glob(f"{self.AP_MOD_TEMPLATE_DIRECTORY.name}*/*.modinfo")
        versions = {int(ElementTree.parse(x).getroot().get("version")) for x in modinfo_files}

        # Return the lowest value not currently in use
        return next(itertools.filterfalse(versions.__contains__, itertools.count(1)))

    @classmethod
    def create_output_file(cls, output_directory: str, world: "CivVWorld") -> None:
        """
        Creates a new output file for the given `world` in the provided `output_directory`.

        This process involves taking the state of the given `world` like the items placed and the user's YAML options,
        and creating a new APMod version that is specific to this slot.
        This APMod is then loaded during the startup of the client when the slot is played.

        """

        # Get path to player output file
        filename = f"{world.output_file_id}{cls.patch_file_ending}"
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

        # Return the server address and player name
        return container.server, container.player_name
