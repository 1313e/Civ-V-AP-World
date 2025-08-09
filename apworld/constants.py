# %% GLOBALS DEFINITIONS
# GENERAL
APWORLD_VERSION: str = "0.6.0"
"Version of this APWorld"
GAME_NAME: str = "Civilization V"
"Name of the game this APWorld is for"
ID_OFFSET: int = 140319
"ID offset for this APWorld"

# MESSAGES
GAME_READY: str = "Civ V is running"
"Message logged when game is running"
GAME_NOT_READY: str = "Waiting for Civ V to start..."
"Message logged when game is currently not running"
MOD_READY: str = "Civ V AP Mod is connected and ready"
"Message logged when game is ready to be interacted with"
MOD_NOT_READY: str = "Waiting for Civ V AP Mod to be ready..."
"Message logged when game is currently not ready to be interacted with"

# WEBSOCKET
ADDRESS: str = "127.0.0.1"
"Localhost address"
PORT: int = 4318
"Port to use for the Firetuner"
