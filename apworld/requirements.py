# %% IMPORTS
from . import items

# All declaration
__all__ = [
    "AIRPORT",
    "ALUMINUM",
    "AMPHITHEATER",
    "AQUEDUCT",
    "ARCHAEOLOGISTS",
    "ARMORY",
    "ARSENAL",
    "BANK",
    "BARRACKS",
    "BOMB_SHELTER",
    "BROADCAST_TOWER",
    "CARAVANSARY",
    "CASTLE",
    "CIRCUS",
    "COAL",
    "COLOSSEUM",
    "CONSTABULARY",
    "EMBARKING",
    "FACTORY",
    "FORGE",
    "GOLD_SILVER",
    "GRANARY",
    "HARBOR",
    "HORSES_SHEEP_CATTLE",
    "HOSPITAL",
    "HOTEL",
    "HYDRO_PLANT",
    "IRON",
    "LIBRARY",
    "LIGHTHOUSE",
    "MARKET",
    "MEDICAL_LAB",
    "MILITARY_ACADEMY",
    "MILITARY_BASE",
    "MINT",
    "MONUMENT",
    "MUSEUM",
    "NUCLEAR_PLANT",
    "OPERA_HOUSE",
    "POLICE_STATION",
    "PUBLIC_SCHOOL",
    "RECYCLING_CENTER",
    "RESEARCH_LAB",
    "SEAPORT",
    "SHRINE",
    "SOLAR_PLANT",
    "SPACESHIP_FACTORY",
    "STABLE",
    "STADIUM",
    "STOCK_EXCHANGE",
    "STONE_MARBLE",
    "STONE_WORKS",
    "TEMPLE",
    "UNIVERSITY",
    "VICTORIES",
    "WALLS",
    "WATER_MILL",
    "WINDMILL",
    "WORKSHOP",
    "URANIUM",
    "ZOO",
]


# %% RESOURCE REQUIREMENTS DEFINITIONS
ALUMINUM = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mining"],
        items.TECH_ITEMS["Electricity"],
    }
)
"Requirements for obtaining Aluminum"
COAL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mining"],
        items.TECH_ITEMS["Industrialization"],
    }
)
"Requirements for obtaining Coal"
GOLD_SILVER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mining"],
    }
)
"Requirements for obtaining Gold or Silver"
HORSES_SHEEP_CATTLE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Animal Husbandry"],
    }
)
"Requirements for obtaining Horses; Sheep; or Cattle"
IRON = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mining"],
        items.TECH_ITEMS["Iron Working"],
    }
)
"Requirements for obtaining Iron"
STONE_MARBLE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Masonry"],
    }
)
"Requirements for obtaining Stone or Marble"
URANIUM = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mining"],
        items.TECH_ITEMS["Atomic Theory"],
    }
)
"Requirements for obtaining Uranium"


# %% GROWTH BUILDING REQUIREMENTS DEFINITIONS
GRANARY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Pottery"],
    }
)
"Requirements for building a Granary"
WATER_MILL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["The Wheel"],
    }
)
"Requirements for building a Water Mill"
AQUEDUCT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Engineering"],
    }
)
"Requirements for building an Aqueduct"
HOSPITAL = items.ItemRequirements(
    AQUEDUCT,
    progression={
        items.TECH_ITEMS["Biology"],
    }
)
"Requirements for building a Hospital"
MEDICAL_LAB = items.ItemRequirements(
    HOSPITAL,
    progression={
        items.TECH_ITEMS["Penicillin"],
    }
)
"Requirements for building a Medical Lab"


# %% SCIENCE BUILDING REQUIREMENTS DEFINITIONS
LIBRARY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Writing"],
    },
)
"Requirements for building a Library"
UNIVERSITY = items.ItemRequirements(
    LIBRARY,
    progression={
        items.TECH_ITEMS["Education"],
    },
)
"Requirements for building a University"
PUBLIC_SCHOOL = items.ItemRequirements(
    UNIVERSITY,
    progression={
        items.TECH_ITEMS["Scientific Theory"],
    },
)
"Requirements for building a Public School"
RESEARCH_LAB = items.ItemRequirements(
    PUBLIC_SCHOOL,
    progression={
        items.TECH_ITEMS["Plastics"],
    },
)
"Requirements for building a Research Lab"


# %% CULTURE/TOURISM BUILDING REQUIREMENTS DEFINITIONS
MONUMENT = items.ItemRequirements()
"Requirements for building a Monument"
AMPHITHEATER = items.ItemRequirements(
    MONUMENT,
    progression={
        items.TECH_ITEMS["Drama and Poetry"],
    },
)
"Requirements for building an Amphitheater"
OPERA_HOUSE = items.ItemRequirements(
    AMPHITHEATER,
    progression={
        items.TECH_ITEMS["Acoustics"],
    },
)
"Requirements for building an Opera House"
MUSEUM = items.ItemRequirements(
    OPERA_HOUSE,
    progression={
        items.TECH_ITEMS["Archaeology"],
    },
)
"Requirements for building a Museum"
BROADCAST_TOWER = items.ItemRequirements(
    MUSEUM,
    progression={
        items.TECH_ITEMS["Radio"],
    },
)
"Requirements for building a Broadcast Tower"
HOTEL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Refrigeration"],
    }
)
"Requirements for building a Hotel"
AIRPORT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Radar"],
    }
)
"Requirements for building an Airport"


# %% GOLD BUILDING REQUIREMENTS DEFINITIONS
MARKET = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Currency"],
    }
)
"Requirements for building a Market"
BANK = items.ItemRequirements(
    MARKET,
    progression={
        items.TECH_ITEMS["Banking"],
    }
)
"Requirements for building a Bank"
STOCK_EXCHANGE = items.ItemRequirements(
    BANK,
    progression={
        items.TECH_ITEMS["Electricity"],
    }
)
"Requirements for building a Stock Exchange"


# %% FAITH BUILDING REQUIREMENTS DEFINITIONS
SHRINE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Pottery"],
    }
)
"Requirements for building a Shrine"
TEMPLE = items.ItemRequirements(
    SHRINE,
    progression={
        items.TECH_ITEMS["Philosophy"],
    }
)
"Requirements for building a Temple"


# %% HAPPINESS BUILDING REQUIREMENTS DEFINITIONS
CIRCUS = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Trapping"],
    }
)
"Requirements for building a Circus"
COLOSSEUM = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Construction"],
    }
)
"Requirements for building a Colosseum"
ZOO = items.ItemRequirements(
    COLOSSEUM,
    progression={
        items.TECH_ITEMS["Printing Press"],
    }
)
"Requirements for building a Zoo"
STADIUM = items.ItemRequirements(
    ZOO,
    progression={
        items.TECH_ITEMS["Refrigeration"],
    }
)
"Requirements for building a Stadium"


# %% PRODUCTION BUILDING REQUIREMENTS DEFINITIONS
WORKSHOP = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Metal Casting"],
    }
)
"Requirements for building a Workshop"
FACTORY = items.ItemRequirements(
    WORKSHOP,
    COAL,
    progression={
        items.TECH_ITEMS["Industrialization"],
    }
)
"Requirements for building a Factory"
NUCLEAR_PLANT = items.ItemRequirements(
    FACTORY,
    URANIUM,
    progression={
        items.TECH_ITEMS["Nuclear Fission"],
    }
)
"Requirements for building a Nuclear Plant"
SOLAR_PLANT = items.ItemRequirements(
    FACTORY,
    progression={
        items.TECH_ITEMS["Ecology"],
    }
)
"Requirements for building a Solar Plant"
SPACESHIP_FACTORY = items.ItemRequirements(
    FACTORY,
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Robotics"],
    }
)
"Requirements for building a Spaceship Factory"


# %% COAST BUILDING REQUIREMENTS DEFINITIONS
LIGHTHOUSE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Optics"],
    }
)
"Requirements for building a Lighthouse"
HARBOR = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Compass"],
    }
)
"Requirements for building a Harbor"
SEAPORT = items.ItemRequirements(
    HARBOR,
    progression={
        items.TECH_ITEMS["Navigation"],
    }
)
"Requirements for building a Seaport"


# %% MILITARY BUILDING REQUIREMENTS DEFINITIONS
BARRACKS = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Bronze Working"],
    }
)
"Requirements for building a Barracks"
ARMORY = items.ItemRequirements(
    BARRACKS,
    progression={
        items.TECH_ITEMS["Steel"],
    }
)
"Requirements for building a Armory"
MILITARY_ACADEMY = items.ItemRequirements(
    ARMORY,
    progression={
        items.TECH_ITEMS["Military Science"],
    }
)
"Requirements for building a Military Academy"

# %% DEFENSIVE BUILDING REQUIREMENTS DEFINITIONS
WALLS = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Masonry"],
    }
)
"Requirements for building Walls"
CASTLE = items.ItemRequirements(
    WALLS,
    progression={
        items.TECH_ITEMS["Chivalry"],
    }
)
"Requirements for building a Castle"
ARSENAL = items.ItemRequirements(
    CASTLE,
    progression={
        items.TECH_ITEMS["Metallurgy"],
    }
)
"Requirements for building an Arsenal"
MILITARY_BASE = items.ItemRequirements(
    ARSENAL,
    progression={
        items.TECH_ITEMS["Replaceable Parts"],
    }
)
"Requirements for building a Military Base"


# %% ANTI-SPY BUILDING REQUIREMENTS DEFINITIONS
CONSTABULARY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Banking"],
    }
)
"Requirements for building a Constabulary"
POLICE_STATION = items.ItemRequirements(
    CONSTABULARY,
    progression={
        items.TECH_ITEMS["Electricity"],
    }
)
"Requirements for building a Police Station"


# %% BONUS/MISC BUILDING REQUIREMENTS DEFINITIONS
BOMB_SHELTER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Telecommunications"],
    }
)
"Requirements for building a Bomb Shelter"
CARAVANSARY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Horseback Riding"],
    }
)
"Requirements for building a Caravansary"
FORGE = items.ItemRequirements(
    IRON,
    progression={
        items.TECH_ITEMS["Metal Casting"],
    }
)
"Requirements for building a Forge"
GARDEN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Theology"],
    }
)
"Requirements for building a Garden"
HYDRO_PLANT = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Electricity"],
    }
)
"Requirements for building a Hydro Plant"
MINT = items.ItemRequirements(
    GOLD_SILVER,
    progression={
        items.TECH_ITEMS["Currency"],
    }
)
"Requirements for building a Mint"
OBSERVATORY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Astronomy"],
    }
)
"Requirements for building an Observatory"
RECYCLING_CENTER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Ecology"],
    }
)
"Requirements for building a Recycling Center"
STABLE = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["Horseback Riding"],
    }
)
"Requirements for building a Stable"
STONE_WORKS = items.ItemRequirements(
    STONE_MARBLE,
    progression={
        items.TECH_ITEMS["Calendar"],
    }
)
"Requirements for building a Stone Works"
WINDMILL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Economics"],
    }
)
"Requirements for building a Windmill"


# %% MISC REQUIREMENTS DEFINITIONS
ARCHAEOLOGISTS = items.ItemRequirements(
    UNIVERSITY,
    progression={
        items.TECH_ITEMS["Archaeology"],
    }
)
"Requirements for training Archaeologists"
EMBARKING = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Optics"],
        items.TECH_ITEMS["Astronomy"],
    },
)
"Requirements for being able to embark"


# %% VICTORY REQUIREMENTS DEFINITIONS
VICTORIES = {
    "Science": items.ItemRequirements(
        ALUMINUM,
        RECYCLING_CENTER,
        progression={
            items.TECH_ITEMS["Rocketry"],
            items.TECH_ITEMS["Advanced Ballistics"],
            items.TECH_ITEMS["Particle Physics"],
            items.TECH_ITEMS["Satellites"],
            items.TECH_ITEMS["Nanotechnology"],
        },
    ),
    "Culture": items.ItemRequirements(
        ARCHAEOLOGISTS,
        BROADCAST_TOWER,
        HOTEL,
        progression={
            items.POLICY_ITEMS["Aesthetics"],
            items.POLICY_ITEMS["Cultural Exchange"],
            items.POLICY_ITEMS["Aesthetics Finisher"],
            items.TECH_ITEMS["The Internet"],
            items.TECH_ITEMS["Telecommunications"],
        },
    ),
    "Diplomatic": items.ItemRequirements(
        EMBARKING,
        STOCK_EXCHANGE,
        progressive={items.PROGRESSIVE_ERA_ITEM: 7},
        progression={
            items.POLICY_ITEMS["Patronage"],
            items.POLICY_ITEMS["Philanthropy"],
            items.POLICY_ITEMS["Consulates"],
            items.TECH_ITEMS["Animal Husbandry"],
            items.TECH_ITEMS["Guilds"],
            items.TECH_ITEMS["Economics"],
            items.TECH_ITEMS["Globalization"],
            items.TECH_ITEMS["Printing Press"],
        },
    )
}
"Dict of all victory requirements"
