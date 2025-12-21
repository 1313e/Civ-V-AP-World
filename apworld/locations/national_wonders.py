# %% IMPORTS
from .core import CivVLocationData
from .. import items
from ..enums import CivVLocationType

# All declaration
__all__ = [
    "NATIONAL_WONDER_LOCATIONS",
]


# %% LOCATION DECLARATIONS
NATIONAL_WONDER_LOCATIONS = [
    # All vanilla national wonders
    CivVLocationData(
        name="Heroic Epic",
        type=CivVLocationType.national_wonder,
        game_id=55,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Iron Working"].name: 1,
                    items.TECH_ITEMS["Bronze Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Melee Unit"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National College",
        type=CivVLocationType.national_wonder,
        game_id=56,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Philosophy"].name: 1,
                    items.TECH_ITEMS["Writing"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Misc"].name: 2,
                    items.PROGRESSIVE_TECH_ITEMS["Science"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Epic",
        type=CivVLocationType.national_wonder,
        game_id=57,
        requirements=(
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
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Circus Maximus",
        type=CivVLocationType.national_wonder,
        game_id=58,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Horseback Riding"].name: 1,
                    items.TECH_ITEMS["Construction"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Melee Unit"].name: 2,
                    items.PROGRESSIVE_TECH_ITEMS["Happiness"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="East India Company",
        type=CivVLocationType.national_wonder,
        game_id=59,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Guilds"].name: 1,
                    items.TECH_ITEMS["Currency"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Ironworks",
        type=CivVLocationType.national_wonder,
        game_id=60,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Machinery"].name: 1,
                    items.TECH_ITEMS["Metal Casting"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Ranged Unit"].name: 2,
                    items.PROGRESSIVE_TECH_ITEMS["Production"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Oxford University",
        type=CivVLocationType.national_wonder,
        game_id=61,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Education"].name: 1,
                    items.TECH_ITEMS["Writing"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Science"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hermitage",
        type=CivVLocationType.national_wonder,
        game_id=62,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                    items.TECH_ITEMS["Acoustics"].name: 1,
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Misc"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Intelligence Agency",
        type=CivVLocationType.national_wonder,
        game_id=127,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Radio"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Banking"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Gold"].name: 6,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Grand Temple",
        type=CivVLocationType.national_wonder,
        game_id=141,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                    items.TECH_ITEMS["Philosophy"].name: 1,
                    items.TECH_ITEMS["Pottery"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Misc"].name: 3,
                    items.PROGRESSIVE_TECH_ITEMS["Growth"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="National Visitor Center",
        type=CivVLocationType.national_wonder,
        game_id=142,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                    items.TECH_ITEMS["Refrigeration"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Navy"].name: 8,
                    items.PROGRESSIVE_TECH_ITEMS["Happiness"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Writers' Guild",
        type=CivVLocationType.national_wonder,
        game_id=148,
        requirements=(
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
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Artists' Guild",
        type=CivVLocationType.national_wonder,
        game_id=149,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Guilds"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Musicians' Guild",
        type=CivVLocationType.national_wonder,
        game_id=150,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Acoustics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
]
"List of all national wonder locations"
