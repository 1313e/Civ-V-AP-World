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
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Optics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Navy"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Stonehenge",
        type=CivVLocationType.world_wonder,
        game_id=64,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Calendar"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Library",
        type=CivVLocationType.world_wonder,
        game_id=65,
        requirements=(
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
        )
    ),
    CivVLocationData(
        name="Pyramids",
        type=CivVLocationType.world_wonder,
        game_id=66,
        region=regions.CLASSICAL_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Masonry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Colossus",
        type=CivVLocationType.world_wonder,
        game_id=67,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Iron Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Oracle",
        type=CivVLocationType.world_wonder,
        game_id=68,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Philosophy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hanging Gardens",
        type=CivVLocationType.world_wonder,
        game_id=69,
        region=regions.ANCIENT_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Mathematics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Siege Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Wall",
        type=CivVLocationType.world_wonder,
        game_id=70,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Engineering"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Growth"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Angkor Wat",
        type=CivVLocationType.world_wonder,
        game_id=71,
        requirements=(
            items.ItemRequirements.create(
                items={
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
        )
    ),
    CivVLocationData(
        name="Hagia Sophia",
        type=CivVLocationType.world_wonder,
        game_id=72,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Chichen Itza",
        type=CivVLocationType.world_wonder,
        game_id=73,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Civil Service"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Growth"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Machu Pichu",
        type=CivVLocationType.world_wonder,
        game_id=74,
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
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Notre Dame",
        type=CivVLocationType.world_wonder,
        game_id=75,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Physics"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Siege Unit"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Porcelain Tower",
        type=CivVLocationType.world_wonder,
        game_id=76,
        region=regions.INFORMATION_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Himeji Castle",
        type=CivVLocationType.world_wonder,
        game_id=77,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Gunpowder"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 6,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Sistine Chapel",
        type=CivVLocationType.world_wonder,
        game_id=78,
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
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Kremlin",
        type=CivVLocationType.world_wonder,
        game_id=79,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Railroad"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Forbidden Palace",
        type=CivVLocationType.world_wonder,
        game_id=80,
        region=regions.INDUSTRIAL_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Banking"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Taj Mahal",
        type=CivVLocationType.world_wonder,
        game_id=81,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Big Ben",
        type=CivVLocationType.world_wonder,
        game_id=82,
        region=regions.ATOMIC_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Industrialization"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Louvre",
        type=CivVLocationType.world_wonder,
        game_id=83,
        region=regions.INFORMATION_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
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
        )
    ),
    CivVLocationData(
        name="Brandenburg Gate",
        type=CivVLocationType.world_wonder,
        game_id=84,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Military Science"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 9,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Statue of Liberty",
        type=CivVLocationType.world_wonder,
        game_id=85,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Replaceable Parts"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 10,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Cristo Redentor",
        type=CivVLocationType.world_wonder,
        game_id=86,
        requirements=(
            items.ItemRequirements.create(
                items={
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
        )
    ),
    CivVLocationData(
        name="Eiffel Tower",
        type=CivVLocationType.world_wonder,
        game_id=87,
        requirements=(
            items.ItemRequirements.create(
                items={
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
        )
    ),
    CivVLocationData(
        name="Pentagon",
        type=CivVLocationType.world_wonder,
        game_id=88,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Combined Arms"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 11,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Sydney Opera House",
        type=CivVLocationType.world_wonder,
        game_id=90,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Ecology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Statue of Zeus",
        type=CivVLocationType.world_wonder,
        game_id=93,
        region=regions.MEDIEVAL_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Bronze Working"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Temple of Artemis",
        type=CivVLocationType.world_wonder,
        game_id=94,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Archery"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Ranged Unit"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Mausoleum of Halicarnassus",
        type=CivVLocationType.world_wonder,
        game_id=95,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Masonry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Production"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Alhambra",
        type=CivVLocationType.world_wonder,
        game_id=128,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Chivalry"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="CN Tower",
        type=CivVLocationType.world_wonder,
        game_id=129,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Navy"].name: 8,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Hubble Space Telescope",
        type=CivVLocationType.world_wonder,
        game_id=130,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Satellites"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Leaning Tower of Pisa",
        type=CivVLocationType.world_wonder,
        game_id=131,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Printing Press"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Mosque of Djenne",
        type=CivVLocationType.world_wonder,
        game_id=132,
        region=regions.RENAISSANCE_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Neuschwanstein",
        type=CivVLocationType.world_wonder,
        game_id=133,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Railroad"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 5,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Petra",
        type=CivVLocationType.world_wonder,
        game_id=134,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Currency"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Gold"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Terracotta Army",
        type=CivVLocationType.world_wonder,
        game_id=135,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Construction"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Great Firewall",
        type=CivVLocationType.world_wonder,
        game_id=136,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Computers"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 12,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Uffizi",
        type=CivVLocationType.world_wonder,
        game_id=154,
        region=regions.MODERN_ERA_POLICY,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Architecture"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Globe Theatre",
        type=CivVLocationType.world_wonder,
        game_id=155,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Printing Press"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Happiness"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Broadway",
        type=CivVLocationType.world_wonder,
        game_id=156,
        requirements=(
            items.ItemRequirements.create(
                items={
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
        )
    ),
    CivVLocationData(
        name="Red Fort",
        type=CivVLocationType.world_wonder,
        game_id=157,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Metallurgy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Melee Unit"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Prora",
        type=CivVLocationType.world_wonder,
        game_id=158,
        region=regions.MODERN_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Flight"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Ranged Unit"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Borobudur",
        type=CivVLocationType.world_wonder,
        game_id=159,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Theology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Misc"].name: 3,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="Parthenon",
        type=CivVLocationType.world_wonder,
        game_id=160,
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
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Culture"].name: 1,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    CivVLocationData(
        name="International Space Station",
        type=CivVLocationType.world_wonder,
        game_id=161,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Satellites"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Progressive Science"].name: 7,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
]
"List of all world wonder locations"
