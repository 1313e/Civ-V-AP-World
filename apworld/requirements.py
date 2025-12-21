# %% IMPORTS
from . import items

# All declaration
__all__ = [
    "BUILDING_REQUIREMENTS",
    "EMBARKING_REQUIREMENTS",
]


# %% REQUIREMENT DEFINITIONS
EMBARKING_REQUIREMENTS = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Optics"],
        items.TECH_ITEMS["Astronomy"],
    },
)
"Requirements for being able to embark"

BUILDING_REQUIREMENTS = {
    "Library": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Writing"],
        },
    ),
    "University": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Writing"],
            items.TECH_ITEMS["Education"],
        },
    ),
    "Public School": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Writing"],
            items.TECH_ITEMS["Education"],
            items.TECH_ITEMS["Scientific Theory"],
        },
    ),
    "Research Lab": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Writing"],
            items.TECH_ITEMS["Education"],
            items.TECH_ITEMS["Scientific Theory"],
            items.TECH_ITEMS["Plastics"],
        },
    ),
    "Amphitheater": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Drama and Poetry"],
        },
    ),
    "Opera House": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Drama and Poetry"],
            items.TECH_ITEMS["Acoustics"],
        },
    ),
    "Museum": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Drama and Poetry"],
            items.TECH_ITEMS["Acoustics"],
            items.TECH_ITEMS["Archaeology"],
        },
    ),
    "Broadcast Tower": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Drama and Poetry"],
            items.TECH_ITEMS["Acoustics"],
            items.TECH_ITEMS["Archaeology"],
            items.TECH_ITEMS["Radio"],
        },
    ),
}
"Dict of building requirements"
