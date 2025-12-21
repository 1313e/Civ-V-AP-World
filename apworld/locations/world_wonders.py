# %% IMPORTS
from .core import CivVLocationData
from .. import items, regions
from ..enums import CivVLocationType

# All declaration
__all__ = [
    "WORLD_WONDER_LOCATIONS",
]


# %% LOCATION DECLARATIONS
WORLD_WONDER_LOCATIONS = [
    # All vanilla world wonders
    CivVLocationData(
        name="Great Lighthouse",
        type=CivVLocationType.world_wonder,
        game_id=63,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Optics"],
            },
        )
    ),
    CivVLocationData(
        name="Stonehenge",
        type=CivVLocationType.world_wonder,
        game_id=64,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Calendar"],
            },
        )
    ),
    CivVLocationData(
        name="Great Library",
        type=CivVLocationType.world_wonder,
        game_id=65,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Writing"],
            },
        )
    ),
    CivVLocationData(
        name="Pyramids",
        type=CivVLocationType.world_wonder,
        game_id=66,
        region=regions.CLASSICAL_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Masonry"],
            },
        )
    ),
    CivVLocationData(
        name="Colossus",
        type=CivVLocationType.world_wonder,
        game_id=67,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Iron Working"],
            },
        )
    ),
    CivVLocationData(
        name="Oracle",
        type=CivVLocationType.world_wonder,
        game_id=68,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Philosophy"],
            },
        )
    ),
    CivVLocationData(
        name="Hanging Gardens",
        type=CivVLocationType.world_wonder,
        game_id=69,
        region=regions.ANCIENT_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Mathematics"],
            },
        )
    ),
    CivVLocationData(
        name="Great Wall",
        type=CivVLocationType.world_wonder,
        game_id=70,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Engineering"],
            },
        )
    ),
    CivVLocationData(
        name="Angkor Wat",
        type=CivVLocationType.world_wonder,
        game_id=71,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Education"],
            },
        )
    ),
    CivVLocationData(
        name="Hagia Sophia",
        type=CivVLocationType.world_wonder,
        game_id=72,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Theology"],
            },
        )
    ),
    CivVLocationData(
        name="Chichen Itza",
        type=CivVLocationType.world_wonder,
        game_id=73,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Civil Service"],
            },
        )
    ),
    CivVLocationData(
        name="Machu Pichu",
        type=CivVLocationType.world_wonder,
        game_id=74,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Guilds"],
            },
        )
    ),
    CivVLocationData(
        name="Notre Dame",
        type=CivVLocationType.world_wonder,
        game_id=75,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Physics"],
            },
        )
    ),
    CivVLocationData(
        name="Porcelain Tower",
        type=CivVLocationType.world_wonder,
        game_id=76,
        region=regions.INFORMATION_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Architecture"],
            },
        )
    ),
    CivVLocationData(
        name="Himeji Castle",
        type=CivVLocationType.world_wonder,
        game_id=77,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Gunpowder"],
            },
        )
    ),
    CivVLocationData(
        name="Sistine Chapel",
        type=CivVLocationType.world_wonder,
        game_id=78,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Acoustics"],
            },
        )
    ),
    CivVLocationData(
        name="Kremlin",
        type=CivVLocationType.world_wonder,
        game_id=79,
        region=regions.MODERN_ERA,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Railroad"],
            },
        )
    ),
    CivVLocationData(
        name="Forbidden Palace",
        type=CivVLocationType.world_wonder,
        game_id=80,
        region=regions.INDUSTRIAL_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Banking"],
            },
        )
    ),
    CivVLocationData(
        name="Taj Mahal",
        type=CivVLocationType.world_wonder,
        game_id=81,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Architecture"],
            },
        )
    ),
    CivVLocationData(
        name="Big Ben",
        type=CivVLocationType.world_wonder,
        game_id=82,
        region=regions.ATOMIC_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Industrialization"],
            },
        )
    ),
    CivVLocationData(
        name="Louvre",
        type=CivVLocationType.world_wonder,
        game_id=83,
        region=regions.INFORMATION_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Archaeology"],
            },
        )
    ),
    CivVLocationData(
        name="Brandenburg Gate",
        type=CivVLocationType.world_wonder,
        game_id=84,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Military Science"],
            },
        )
    ),
    CivVLocationData(
        name="Statue of Liberty",
        type=CivVLocationType.world_wonder,
        game_id=85,
        region=regions.MODERN_ERA,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Replaceable Parts"],
            },
        )
    ),
    CivVLocationData(
        name="Cristo Redentor",
        type=CivVLocationType.world_wonder,
        game_id=86,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Plastics"],
            },
        )
    ),
    CivVLocationData(
        name="Eiffel Tower",
        type=CivVLocationType.world_wonder,
        game_id=87,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Radio"],
            },
        )
    ),
    CivVLocationData(
        name="Pentagon",
        type=CivVLocationType.world_wonder,
        game_id=88,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Combined Arms"],
            },
        )
    ),
    CivVLocationData(
        name="Sydney Opera House",
        type=CivVLocationType.world_wonder,
        game_id=90,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Ecology"],
            },
        )
    ),
    CivVLocationData(
        name="Statue of Zeus",
        type=CivVLocationType.world_wonder,
        game_id=93,
        region=regions.MEDIEVAL_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Bronze Working"],
            },
        )
    ),
    CivVLocationData(
        name="Temple of Artemis",
        type=CivVLocationType.world_wonder,
        game_id=94,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Archery"],
            },
        )
    ),
    CivVLocationData(
        name="Mausoleum of Halicarnassus",
        type=CivVLocationType.world_wonder,
        game_id=95,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Masonry"],
            },
        )
    ),
    CivVLocationData(
        name="Alhambra",
        type=CivVLocationType.world_wonder,
        game_id=128,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Chivalry"],
            },
        )
    ),
    CivVLocationData(
        name="CN Tower",
        type=CivVLocationType.world_wonder,
        game_id=129,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Telecommunications"],
            },
        )
    ),
    CivVLocationData(
        name="Hubble Space Telescope",
        type=CivVLocationType.world_wonder,
        game_id=130,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Satellites"],
            },
        )
    ),
    CivVLocationData(
        name="Leaning Tower of Pisa",
        type=CivVLocationType.world_wonder,
        game_id=131,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Printing Press"],
            },
        )
    ),
    CivVLocationData(
        name="Great Mosque of Djenne",
        type=CivVLocationType.world_wonder,
        game_id=132,
        region=regions.RENAISSANCE_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Theology"],
            },
        )
    ),
    CivVLocationData(
        name="Neuschwanstein",
        type=CivVLocationType.world_wonder,
        game_id=133,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Railroad"],
            },
        )
    ),
    CivVLocationData(
        name="Petra",
        type=CivVLocationType.world_wonder,
        game_id=134,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Currency"],
            },
        )
    ),
    CivVLocationData(
        name="Terracotta Army",
        type=CivVLocationType.world_wonder,
        game_id=135,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Construction"],
            },
        )
    ),
    CivVLocationData(
        name="Great Firewall",
        type=CivVLocationType.world_wonder,
        game_id=136,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Computers"],
            },
        )
    ),
    CivVLocationData(
        name="Uffizi",
        type=CivVLocationType.world_wonder,
        game_id=154,
        region=regions.MODERN_ERA_POLICY,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Architecture"],
            },
        )
    ),
    CivVLocationData(
        name="Globe Theatre",
        type=CivVLocationType.world_wonder,
        game_id=155,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Printing Press"],
            },
        )
    ),
    CivVLocationData(
        name="Broadway",
        type=CivVLocationType.world_wonder,
        game_id=156,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Radio"],
            },
        )
    ),
    CivVLocationData(
        name="Red Fort",
        type=CivVLocationType.world_wonder,
        game_id=157,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Metallurgy"],
            },
        )
    ),
    CivVLocationData(
        name="Prora",
        type=CivVLocationType.world_wonder,
        game_id=158,
        region=regions.MODERN_ERA,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Flight"],
            },
        )
    ),
    CivVLocationData(
        name="Borobudur",
        type=CivVLocationType.world_wonder,
        game_id=159,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Theology"],
            },
        )
    ),
    CivVLocationData(
        name="Parthenon",
        type=CivVLocationType.world_wonder,
        game_id=160,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Drama and Poetry"],
            },
        )
    ),
    CivVLocationData(
        name="International Space Station",
        type=CivVLocationType.world_wonder,
        game_id=161,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Satellites"],
            },
        )
    ),
]
"List of all world wonder locations"
