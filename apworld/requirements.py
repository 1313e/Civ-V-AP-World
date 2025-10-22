# %% IMPORTS
from . import items

# All declaration
__all__ = ["EMBARKING_REQUIREMENTS", "BUILDING_REQUIREMENTS"]


# %% REQUIREMENT DEFINITIONS
EMBARKING_REQUIREMENTS = (
    items.ItemRequirements.create(
        items={
            items.TECH_ITEMS["Optics"].name: 1,
            items.TECH_ITEMS["Astronomy"].name: 1,
        },
        when={
            "progressive_techs": False,
        }
    ) |
    items.ItemRequirements.create(
        items={
            items.PROGRESSIVE_TECH_ITEMS["Progressive Navy"].name: 4,
        },
        when={
            "progressive_techs": True,
        }
    )
)
"Requirements for being able to embark"

BUILDING_REQUIREMENTS = {
    "Library": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Writing"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 1,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "University": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Writing"].name: 1,
                items.TECH_ITEMS["Education"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 2,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Public School": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Writing"].name: 1,
                items.TECH_ITEMS["Education"].name: 1,
                items.TECH_ITEMS["Scientific Theory"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 3,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Research Lab": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Writing"].name: 1,
                items.TECH_ITEMS["Education"].name: 1,
                items.TECH_ITEMS["Scientific Theory"].name: 1,
                items.TECH_ITEMS["Plastics"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 4,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Amphitheater": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Drama and Poetry"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 1,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Opera House": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Drama and Poetry"].name: 1,
                items.TECH_ITEMS["Acoustics"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 2,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Museum": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Drama and Poetry"].name: 1,
                items.TECH_ITEMS["Acoustics"].name: 1,
                items.TECH_ITEMS["Archaeology"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 3,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
    "Broadcast Tower": (
        items.ItemRequirements.create(
            items={
                items.TECH_ITEMS["Drama and Poetry"].name: 1,
                items.TECH_ITEMS["Acoustics"].name: 1,
                items.TECH_ITEMS["Archaeology"].name: 1,
                items.TECH_ITEMS["Radio"].name: 1,
            },
            when={
                "progressive_techs": False,
            }
        ) |
        items.ItemRequirements.create(
            items={
                items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 4,
            },
            when={
                "progressive_techs": True,
            }
        )
    ),
}
"Dict of building requirements"
