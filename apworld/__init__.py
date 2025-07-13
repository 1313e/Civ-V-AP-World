# %% IMPORTS
from .helpers import run_client
from .world import CivVWorld


# %% COMPONENT DEFINITIONS
# Register the run_client function as a client component
from worlds.LauncherComponents import Component, Type, components
from .constants import GAME_NAME
components.append(
    Component(
        display_name="Civ V Client",
        func=run_client,
        component_type=Type.CLIENT,
        description=f"A client for connecting to {GAME_NAME}",
    )
)
