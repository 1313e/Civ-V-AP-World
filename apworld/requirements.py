# %% IMPORTS
from . import items

# All declaration
__all__ = [
    "BUILDING_REQUIREMENTS",
    "EMBARKING_REQUIREMENTS",
    "VICTORY_REQUIREMENTS",
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


# %% VICTORY REQUIREMENT DEFINITIONS
VICTORY_REQUIREMENTS = {
    "Science": items.ItemRequirements(
        progression={
            items.TECH_ITEMS["Mining"],
            items.TECH_ITEMS["Electricity"],
            items.TECH_ITEMS["Ecology"],
            items.TECH_ITEMS["Rocketry"],
            items.TECH_ITEMS["Advanced Ballistics"],
            items.TECH_ITEMS["Particle Physics"],
            items.TECH_ITEMS["Satellites"],
            items.TECH_ITEMS["Nanotechnology"],
        },
    ),
    "Culture": items.ItemRequirements(
        progression={
            items.POLICY_ITEMS["Aesthetics"],
            items.POLICY_ITEMS["Cultural Exchange"],
            items.POLICY_ITEMS["Aesthetics Finisher"],
            items.TECH_ITEMS["Drama and Poetry"],
            items.TECH_ITEMS["Acoustics"],
            items.TECH_ITEMS["Archaeology"],
            items.TECH_ITEMS["Refrigeration"],
            items.TECH_ITEMS["Radio"],
            items.TECH_ITEMS["The Internet"],
            items.TECH_ITEMS["Telecommunications"],
            items.TECH_ITEMS["Writing"],
            items.TECH_ITEMS["Education"],
        },
    ),
    "Diplomatic": items.ItemRequirements(
        progressive={items.PROGRESSIVE_ERA_ITEM: 7},
        progression={
            items.POLICY_ITEMS["Patronage"],
            items.POLICY_ITEMS["Philanthropy"],
            items.POLICY_ITEMS["Consulates"],
            items.TECH_ITEMS["Animal Husbandry"],
            items.TECH_ITEMS["Currency"],
            items.TECH_ITEMS["Guilds"],
            items.TECH_ITEMS["Banking"],
            items.TECH_ITEMS["Economics"],
            items.TECH_ITEMS["Electricity"],
            items.TECH_ITEMS["Globalization"],
            items.TECH_ITEMS["Printing Press"],
            items.TECH_ITEMS["Optics"],
            items.TECH_ITEMS["Astronomy"],
        },
    )
}
"Dict of all victory requirements"
