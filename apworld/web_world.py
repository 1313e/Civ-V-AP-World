# %% IMPORTS
from collections import defaultdict
from dataclasses import fields

from .options import CivVOption, CivVOptions

from Options import OptionGroup
from worlds.AutoWorld import WebWorld

# All declaration
__all__ = ["CivVWebWorld"]


# %% GLOBALS
OPTION_GROUPS = defaultdict(list)
for option_cls in [x.type for x in fields(CivVOptions)
                   if not isinstance(x.type, str) and issubclass(x.type, CivVOption)]:
    OPTION_GROUPS[option_cls.civv_option_group].append(option_cls)


# %% WEB_WORLD CLASS DEFINITION
class CivVWebWorld(WebWorld):
    """
    Web world for Civ V.

    """

    option_groups = [OptionGroup(name=name, options=options) for name, options in OPTION_GROUPS.items()]
