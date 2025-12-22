import tempfile
import shutil
from pathlib import Path

import click


# %% COMMAND DEFINITIONS
@click.group(short_help="CivV AP CLI")
def group_cli() -> None:
    """
    Civ V AP mod CLI tool.

    """

    pass


@group_cli.command("create-apworld", short_help="Creates an APWorld and puts it in the 'custom worlds' folder")
@click.option("--aproot", type=click.Path(exists=True, file_okay=False, path_type=Path), help="The APRoot folder",
              default="C:/ProgramData/Archipelago")
def cmd_create_apworld(aproot: Path) -> None:
    tempdir = tempfile.mkdtemp()
    _ = shutil.copytree("./apworld", Path(tempdir)/"civv", dirs_exist_ok=True)
    zipfile = shutil.make_archive("civv", "zip", tempdir, "civv")
    shutil.move(zipfile, aproot/"custom_worlds/civv.apworld")


@group_cli.command("create-release", short_help="Packages the APWorld, ready for a release")
def cmd_create_release() -> None:
    # Make sure release directory exists
    rel_dir = Path.cwd() / "release"
    rel_dir.mkdir(parents=True, exist_ok=True)

    # Create new version of APWorld
    tempdir = tempfile.mkdtemp()
    _ = shutil.copytree("./apworld", Path(tempdir) / "civv", dirs_exist_ok=True)
    zipfile = shutil.make_archive("civv", "zip", tempdir, "civv")
    _ = shutil.move(zipfile, rel_dir / "civv.apworld")
