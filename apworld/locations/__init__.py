# %% IMPORTS
# Import core module first
from . import core
from .core import *

# Import all other modules after
from . import buildings, national_wonders, policies, settlers, techs, units, world_wonders
from .buildings import *
from .national_wonders import *
from .policies import *
from .settlers import *
from .techs import *
from .units import *
from .world_wonders import *

# All declaration
__all__ = []
__all__.extend(core.__all__)
__all__.extend(buildings.__all__)
__all__.extend(national_wonders.__all__)
__all__.extend(policies.__all__)
__all__.extend(settlers.__all__)
__all__.extend(techs.__all__)
__all__.extend(units.__all__)
__all__.extend(world_wonders.__all__)
