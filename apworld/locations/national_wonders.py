# %% IMPORTS
from .core import CivVLocationData
from .. import items, requirements
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
        database_key_prefix="building_heroic_epic",
        requirements=items.ItemRequirements(
            requirements.BARRACKS,
            progression={
                items.TECH_ITEMS["Iron Working"],
            },
        )
    ),
    CivVLocationData(
        name="National College",
        type=CivVLocationType.national_wonder,
        game_id=56,
        database_key_prefix="building_national_college",
        requirements=items.ItemRequirements(
            requirements.LIBRARY,
            progression={
                items.TECH_ITEMS["Philosophy"],
            },
        )
    ),
    CivVLocationData(
        name="National Epic",
        type=CivVLocationType.national_wonder,
        game_id=57,
        database_key_prefix="building_national_epic",
        requirements=items.ItemRequirements(
            requirements.MONUMENT,
            progression={
                items.TECH_ITEMS["Drama and Poetry"],
            },
        )
    ),
    CivVLocationData(
        name="Circus Maximus",
        type=CivVLocationType.national_wonder,
        game_id=58,
        database_key_prefix="building_circus_maximus",
        requirements=items.ItemRequirements(
            requirements.COLOSSEUM,
            progression={
                items.TECH_ITEMS["Horseback Riding"],
            },
        )
    ),
    CivVLocationData(
        name="East India Company",
        type=CivVLocationType.national_wonder,
        game_id=59,
        database_key_prefix="building_national_treasury",
        requirements=items.ItemRequirements(
            requirements.MARKET,
            progression={
                items.TECH_ITEMS["Guilds"],
            },
        )
    ),
    CivVLocationData(
        name="Ironworks",
        type=CivVLocationType.national_wonder,
        game_id=60,
        database_key_prefix="building_ironworks",
        requirements=items.ItemRequirements(
            requirements.WORKSHOP,
            progression={
                items.TECH_ITEMS["Machinery"],
            },
        )
    ),
    CivVLocationData(
        name="Oxford University",
        type=CivVLocationType.national_wonder,
        game_id=61,
        database_key_prefix="building_oxford_university",
        requirements=items.ItemRequirements(
            requirements.UNIVERSITY,
            progression={
                items.TECH_ITEMS["Education"],
            },
        )
    ),
    CivVLocationData(
        name="Hermitage",
        type=CivVLocationType.national_wonder,
        game_id=62,
        database_key_prefix="building_hermitage",
        requirements=items.ItemRequirements(
            requirements.OPERA_HOUSE,
            progression={
                items.TECH_ITEMS["Architecture"],
            },
        )
    ),
    CivVLocationData(
        name="National Intelligence Agency",
        type=CivVLocationType.national_wonder,
        game_id=127,
        database_key_prefix="building_intelligence_agency",
        requirements=items.ItemRequirements(
            requirements.POLICE_STATION,
            progression={
                items.TECH_ITEMS["Radio"],
            },
        )
    ),
    CivVLocationData(
        name="Grand Temple",
        type=CivVLocationType.national_wonder,
        game_id=141,
        database_key_prefix="building_grand_temple",
        requirements=items.ItemRequirements(
            requirements.TEMPLE,
            progression={
                items.TECH_ITEMS["Theology"],
            },
        )
    ),
    CivVLocationData(
        name="National Visitor Center",
        type=CivVLocationType.national_wonder,
        game_id=142,
        database_key_prefix="building_tourist_center",
        requirements=items.ItemRequirements(
            requirements.HOTEL,
            progression={
                items.TECH_ITEMS["Telecommunications"],
            },
        )
    ),
    CivVLocationData(
        name="Writers' Guild",
        type=CivVLocationType.national_wonder,
        game_id=148,
        database_key_prefix="building_writers_guild",
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
        database_key_prefix="building_artists_guild",
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
        database_key_prefix="building_musicians_guild",
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Acoustics"],
            },
        )
    ),
]
"List of all national wonder locations"
