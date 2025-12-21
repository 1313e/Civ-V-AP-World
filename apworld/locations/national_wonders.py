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
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Iron Working"],
                items.TECH_ITEMS["Bronze Working"],
            },
        )
    ),
    CivVLocationData(
        name="National College",
        type=CivVLocationType.national_wonder,
        game_id=56,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Philosophy"],
                items.TECH_ITEMS["Writing"],
            },
        )
    ),
    CivVLocationData(
        name="National Epic",
        type=CivVLocationType.national_wonder,
        game_id=57,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Drama and Poetry"],
            },
        )
    ),
    CivVLocationData(
        name="Circus Maximus",
        type=CivVLocationType.national_wonder,
        game_id=58,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Horseback Riding"],
                items.TECH_ITEMS["Construction"],
            },
        )
    ),
    CivVLocationData(
        name="East India Company",
        type=CivVLocationType.national_wonder,
        game_id=59,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Guilds"],
                items.TECH_ITEMS["Currency"],
            },
        )
    ),
    CivVLocationData(
        name="Ironworks",
        type=CivVLocationType.national_wonder,
        game_id=60,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Machinery"],
                items.TECH_ITEMS["Metal Casting"],
            },
        )
    ),
    CivVLocationData(
        name="Oxford University",
        type=CivVLocationType.national_wonder,
        game_id=61,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Education"],
                items.TECH_ITEMS["Writing"],
            },
        )
    ),
    CivVLocationData(
        name="Hermitage",
        type=CivVLocationType.national_wonder,
        game_id=62,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Architecture"],
                items.TECH_ITEMS["Acoustics"],
                items.TECH_ITEMS["Drama and Poetry"],
            },
        )
    ),
    CivVLocationData(
        name="National Intelligence Agency",
        type=CivVLocationType.national_wonder,
        game_id=127,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Radio"],
                items.TECH_ITEMS["Electricity"],
                items.TECH_ITEMS["Banking"],
            },
        )
    ),
    CivVLocationData(
        name="Grand Temple",
        type=CivVLocationType.national_wonder,
        game_id=141,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Theology"],
                items.TECH_ITEMS["Philosophy"],
                items.TECH_ITEMS["Pottery"],
            },
        )
    ),
    CivVLocationData(
        name="National Visitor Center",
        type=CivVLocationType.national_wonder,
        game_id=142,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Telecommunications"],
                items.TECH_ITEMS["Refrigeration"],
            },
        )
    ),
    CivVLocationData(
        name="Writers' Guild",
        type=CivVLocationType.national_wonder,
        game_id=148,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Drama and Poetry"],
            },
        )
    ),
    CivVLocationData(
        name="Artists' Guild",
        type=CivVLocationType.national_wonder,
        game_id=149,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Guilds"],
            },
        )
    ),
    CivVLocationData(
        name="Musicians' Guild",
        type=CivVLocationType.national_wonder,
        game_id=150,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Acoustics"],
            },
        )
    ),
]
"List of all national wonder locations"
