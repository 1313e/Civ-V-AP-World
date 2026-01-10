# %% IMPORTS
import itertools
import pkgutil
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import TYPE_CHECKING, Any
from xml.etree import ElementTree

from BaseClasses import Item, ItemClassification
from worlds.Files import APPlayerContainer

from .constants import CONTAINER_EXTENSION, GAME_NAME
from .enums import (
    CivVLocationType,
    CivVItemClassificationColors,
    CivVItemClassificationFlags,
    CivVItemClassificationNames,
)
from .locations import LOCATIONS_DATA
if TYPE_CHECKING:
    from .world import CivVWorld

# All declaration
__all__ = ["CivVContainer"]


# %% CIV_V_CONTAINER CLASS DEFINITION
class CivVContainer(APPlayerContainer):
    game = GAME_NAME
    patch_file_ending = CONTAINER_EXTENSION

    # Additional class attributes
    AP_MOD_TEMPLATE_FILES: list[str] = [
        "templates/apmod/APFunctions.lua",
        "templates/apmod/Buildings.xml",
        "templates/apmod/BuildingTextInfos.xml",
        "templates/apmod/CivVAPMod (v 1).modinfo",
        "templates/apmod/NationalWonders.xml",
        "templates/apmod/NationalWonderTextInfos.xml",
        "templates/apmod/Policies.xml",
        "templates/apmod/PolicyBranches.xml",
        "templates/apmod/PolicyBranchTextInfos.xml",
        "templates/apmod/Technologies.xml",
        "templates/apmod/WorldWonders.xml",
        "templates/apmod/WorldWonderTextInfos.xml",
        "templates/apmod/Icons/AP_Icons.xml",
        "templates/apmod/Icons/AP_Policy_64.dds",
        "templates/apmod/Icons/AP_Policy_256.dds",
        "templates/apmod/Icons/AP_Policy_Adopted_64.dds",
        "templates/apmod/Icons/AP_Tech_64.dds",
        "templates/apmod/Icons/AP_Tech_80.dds",
        "templates/apmod/Icons/AP_Tech_128.dds",
        "templates/apmod/Icons/AP_Tech_214.dds",
        "templates/apmod/Icons/AP_Tech_256.dds",
    ]
    "List of paths of all Civ V AP Mod template files"
    AP_MOD_NAME: str = "apmod"
    "Name of the Civ V AP Mod"

    def __init__(self, path: Path, world: "CivVWorld | None", **kwargs):
        # Call super method
        super().__init__(path=path, **kwargs)
        self.path: Path = path

        # Create instance attributes
        self.world: "CivVWorld | None" = world
        "The instance of the Civ V AP world to use for this container"

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Clean the given `text` into a version that is safe for XML.

        """

        return text.replace('"', "'").replace('&', 'and').replace('{', '').replace('}', '')

    def _get_formatted_item(self, item: Item) -> str:
        """
        Formats the given `item` placement into a string usable in the Civ V XML databases.

        """

        # If traps are to be disguised, use progression instead of trap
        classification = item.classification
        if classification == ItemClassification.trap and self.world.options.disguise_traps:
            classification = ItemClassification.progression

        # Format the item into a string depending on the hint mode
        color = CivVItemClassificationColors.get_color(classification)
        match self.world.options.item_hints:
            case "full":
                player_name = (
                    f"{self.clean_text(self.world.multiworld.player_name[item.player])}'s"
                    if item.player != self.world.player else "Your"
                )
                return f"{player_name} [{color}]{self.clean_text(item.name)}[ENDCOLOR]"
            case "classification":
                return f"A [{color}]{CivVItemClassificationNames.get_name(classification)} item[ENDCOLOR]"
            case "none":
                return f"An item"
            case _:
                raise NotImplementedError

    def _get_formatted_item_flag(self, item: Item) -> str:
        """
        Returns the formatted flag icon for the given `item` usable in the Civ V XML databases.

        """

        # If traps are to be disguised, use progression instead of trap
        classification = item.classification
        if classification == ItemClassification.trap and self.world.options.disguise_traps:
            classification = ItemClassification.progression

        # Format the item flag into a string depending on the hint mode
        match self.world.options.item_hints:
            case "full" | "classification":
                return f"[{CivVItemClassificationFlags.get_flag(classification)}] "
            case "none":
                return ""
            case _:
                raise NotImplementedError

    def _get_location_description_building(self, item: Item) -> str:
        """
        Formats the given `item` placement into a location description string usable for buildings in the Civ V XML
        databases.

        """

        return (
            f"[NEWLINE][NEWLINE]Constructing this building for the first time counts as an "
            f"[COLOR_POSITIVE_TEXT]AP Location[ENDCOLOR] ({self._get_formatted_item(item)})."
        )

    def _get_substitution_dict(self) -> dict[str, str]:
        """
        Generates and returns a dictionary that should be used for XML file substitution.

        """

        # Create dict holding all substitutions
        dct = {"policy_cost_modifier": str(self.world.options.policy_cost_modifier-100)}

        # Get all placed locations for this player. Ignore the Victory location
        filled_locations = {
            x.address: x for x in self.world.multiworld.get_filled_locations(self.world.player) if x.name != "Victory"
        }

        # Loop over all defined locations and add their substitution strings
        tech_cost_modifier = self.world.options.tech_cost_modifier / 100
        for location in LOCATIONS_DATA:
            # Get the filled location for this location
            filled_location = filled_locations.get(location.ap_id)

            # Act according to the type of location this is
            match location.type:
                # For buildings, we need a location description at that location if an item was placed there
                case CivVLocationType.building | CivVLocationType.national_wonder | CivVLocationType.world_wonder:
                    if filled_location is not None:
                        location_text = self._get_location_description_building(filled_location.item)
                        flag = self._get_formatted_item_flag(filled_location.item)
                    else:
                        location_text = ""
                        flag = ""
                    dct[f"{location.database_key_prefix}_location"] = location_text
                    dct[f"{location.database_key_prefix}_flag"] = flag

                # For policy branches, we need just the formatted item at that location
                case CivVLocationType.policy_branch:
                    dct[f"{location.database_key_prefix}_item"] = self._get_formatted_item(filled_location.item)

                # For policies, we need the formatted item and the classification flag
                case CivVLocationType.policy:
                    dct[f"{location.database_key_prefix}_item"] = self._get_formatted_item(filled_location.item)
                    dct[f"{location.database_key_prefix}_flag"] = self._get_formatted_item_flag(filled_location.item)

                # For techs, we need formatted item; classification flag; and the cost of that location
                case CivVLocationType.tech:
                    dct[f"{location.database_key_prefix}_item"] = self._get_formatted_item(filled_location.item)
                    dct[f"{location.database_key_prefix}_flag"] = self._get_formatted_item_flag(filled_location.item)
                    dct[f"{location.database_key_prefix}_cost"] = str(int(location.cost * tech_cost_modifier))

                # For all other types, do nothing
                case _:
                    pass

        # Return the substitution dict
        return dct

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        # Obtain the substitution dict
        substitution_dict = self._get_substitution_dict()

        # Copy over the entire contents of the APMod directory
        for filepath in self.AP_MOD_TEMPLATE_FILES:
            # Act according to the extension of this file
            contents = pkgutil.get_data(__name__, filepath)
            zip_path = filepath.replace("templates/", "")
            match filepath.rsplit(".", 1)[1]:
                # For Lua files, we want to insert the output file ID into the file
                case "lua":
                    new_contents = contents.decode().replace("<insert_output_file_id>", self.world.output_file_id)
                    opened_zipfile.writestr(zip_path, new_contents)

                # For XML files, we want to use the file as a template and substitute all appropriate data
                case "xml":
                    new_contents = contents.decode().format(**substitution_dict)
                    opened_zipfile.writestr(zip_path, new_contents)

                # For everything else, simply copy over the full file without modifications
                case _:
                    opened_zipfile.writestr(zip_path, contents)

        # Call super method
        super().write_contents(opened_zipfile)

    def read_contents(self, opened_zipfile: zipfile.ZipFile) -> dict[str, Any]:
        # Get path to mods folder
        from .world import CivVWorld
        mods_folder_path = Path(CivVWorld.settings.mods_folder_path)

        # If the mod does not exist yet, we need to create it from the output file
        zip_name = self.path.name.rsplit('.', 1)[0]
        mod_path = mods_folder_path / f"{self.AP_MOD_NAME} - {zip_name}"
        if not mod_path.exists():
            # Extract all mod files to a temporary directory
            tempdir = Path(tempfile.mkdtemp())
            for file in [x for x in opened_zipfile.namelist() if x.startswith(self.AP_MOD_NAME)]:
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
            _ = shutil.copytree(tempdir / self.AP_MOD_NAME, mod_path)

            # Remove the temporary directory
            shutil.rmtree(tempdir)

        # Call super method and return its result
        return super().read_contents(opened_zipfile)

    def _get_mod_version(self, mods_folder_path) -> int:
        """
        Returns the version to use for an APMod, given the current mods already installed.

        """

        # Get the versions of all installed APMod versions
        modinfo_files = mods_folder_path.glob(f"{self.AP_MOD_NAME}*/*.modinfo")
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

        # Return the server address and player name
        return container.server, container.player_name
