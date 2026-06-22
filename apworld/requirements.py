# %% IMPORTS
from . import items

# All declaration
__all__ = [
    "AIRPORT",
    "ALUMINUM",
    "AMPHITHEATER",
    "ANTI_AIRCRAFT_GUN",
    "ANTI_TANK_GUN",
    "AQUEDUCT",
    "ARCHAEOLOGIST",
    "ARCHER",
    "ARCHER_CLASS",
    "ARMOR_CLASS",
    "ARMORY",
    "ARSENAL",
    "ARTILLERY",
    "ARTISTS_GUILD",
    "ATOMIC_BOMB",
    "BANK",
    "BARRACKS",
    "BATTLESHIP",
    "BAZOOKA",
    "BOMB_SHELTER",
    "BOMBER",
    "BOMBER_CLASS",
    "BROADCAST_TOWER",
    "CANNON",
    "CARAVAN",
    "CARAVANSARY",
    "CARAVEL",
    "CARGO_SHIP",
    "CARRIER",
    "CARRIER_CLASS",
    "CASTLE",
    "CATAPULT",
    "CAVALRY",
    "CHARIOT_ARCHER",
    "CIRCUS",
    "COAL",
    "COLOSSEUM",
    "COMPOSITE_BOWMAN",
    "CONSTABULARY",
    "CROSSBOWMAN",
    "DESTROYER",
    "EMBARKING",
    "FACTORY",
    "FIGHTER",
    "FIGHTER_CLASS",
    "FORGE",
    "FRIGATE",
    "GALLEASS",
    "GATLING_GUN",
    "GIANT_DEATH_ROBOT",
    "GOLD_SILVER",
    "GRANARY",
    "GREAT_WAR_BOMBER",
    "GREAT_WAR_INFANTRY",
    "GUIDED_MISSILE",
    "GUN_CLASS",
    "HARBOR",
    "HELICOPTER_CLASS",
    "HELICOPTER_GUNSHIP",
    "HORSEMAN",
    "HORSES_SHEEP_CATTLE",
    "HOSPITAL",
    "HOTEL",
    "HYDRO_PLANT",
    "INFANTRY",
    "IRON",
    "IRONCLAD",
    "JET_FIGHTER",
    "KNIGHT",
    "LANCER",
    "LANDSHIP",
    "LANDSKNECHT",
    "LIBRARY",
    "LIGHTHOUSE",
    "LONGSWORDSMAN",
    "MACHINE_GUN",
    "MARINE",
    "MARKET",
    "MECHANIZED_INFANTRY",
    "MEDICAL_LAB",
    "MELEE_CLASS",
    "MILITARY_ACADEMY",
    "MILITARY_BASE",
    "MINT",
    "MISSILE_CRUISER",
    "MOBILE_SAM",
    "MODERN_ARMOR",
    "MONUMENT",
    "MOUNTED_CLASS",
    "MUSEUM",
    "MUSICIANS_GUILD",
    "MUSKETMAN",
    "NAVAL_MELEE_CLASS",
    "NAVAL_RANGED_CLASS",
    "NUCLEAR_PLANT",
    "NUCLEAR_MISSILE",
    "NUCLEAR_SUBMARINE",
    "OIL",
    "OPERA_HOUSE",
    "PARATROOPER",
    "PIKEMAN",
    "POLICE_STATION",
    "PRIVATEER",
    "PUBLIC_SCHOOL",
    "RECON_CLASS",
    "RECYCLING_CENTER",
    "RESEARCH_LAB",
    "RIFLEMAN",
    "ROCKET_ARTILLERY",
    "SCOUT",
    "SEAPORT",
    "SETTLER",
    "SHRINE",
    "SIEGE_CLASS",
    "SOLAR_PLANT",
    "SPACESHIP_FACTORY",
    "SPEARMAN",
    "STABLE",
    "STADIUM",
    "STEALTH_BOMBER",
    "STOCK_EXCHANGE",
    "STONE_MARBLE",
    "STONE_WORKS",
    "SUBMARINE",
    "SUBMARINE_CLASS",
    "SWORDSMAN",
    "TANK",
    "TEMPLE",
    "TREBUCHET",
    "TRIPLANE",
    "TRIREME",
    "UNIVERSITY",
    "VICTORIES",
    "WALLS",
    "WARRIOR",
    "WATER_MILL",
    "WINDMILL",
    "WORK_BOAT",
    "WORKER",
    "WORKSHOP",
    "WRITERS_GUILD",
    "URANIUM",
    "XCOM_SQUAD",
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
OIL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Biology"],
    }
)
"Requirements for obtaining Oil"
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


# %% GUILDS
ARTISTS_GUILD = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Guilds"],
    }
)
"Requirements for building a Artists' Guild"
MUSICIANS_GUILD = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Acoustics"],
    }
)
"Requirements for building a Musicians' Guild"
WRITERS_GUILD = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Drama and Poetry"],
    }
)
"Requirements for building a Writers' Guild"


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
EMBARKING = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Optics"],
        items.TECH_ITEMS["Astronomy"],
    },
)
"Requirements for being able to embark"
MANHATTAN_PROJECT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Atomic Theory"],
    },
)
"Requirements for research the Manhattan Project special project"


# %% UNIT REQUIREMENT DEFINITIONS
SETTLER = items.ItemRequirements()
"Requirements for training a Settler"
WORKER = items.ItemRequirements()
"Requirements for training a Worker"
WORK_BOAT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Sailing"],
    }
)
"Requirements for training a Work Boat"
MISSILE_CRUISER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Robotics"],
    }
)
"Requirements for training a Missile Cruiser"
NUCLEAR_SUBMARINE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Telecommunications"],
    }
)
"Requirements for training a Nuclear Submarine"
CARRIER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Electronics"]
    }
)
"Requirements for training a Carrier"
BATTLESHIP = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Electronics"],
    }
)
"Requirements for training a Battleship"
SUBMARINE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Refrigeration"],
    }
)
"Requirements for training a Submarine"
DESTROYER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Combustion"],
    }
)
"Requirements for training a Destroyer"
IRONCLAD = items.ItemRequirements(
    COAL,
    progression={
        items.TECH_ITEMS["Steam Power"],
    }
)
"Requirements for training an Ironclad"
FRIGATE = items.ItemRequirements(
    IRON,
    progression={
        items.TECH_ITEMS["Navigation"],
    }
)
"Requirements for training a Frigate"
CARAVEL = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Astronomy"],
    }
)
"Requirements for training a Caravel"
TRIREME = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Sailing"],
    }
)
"Requirements for training a Trireme"
GIANT_DEATH_ROBOT = items.ItemRequirements(
    URANIUM,
    progression={
        items.TECH_ITEMS["Nuclear Fusion"],
    }
)
"Requirements for training a Giant Death Robot"
NUCLEAR_MISSILE = items.ItemRequirements(
    MANHATTAN_PROJECT,
    URANIUM,
    progression={
        items.TECH_ITEMS["Advanced Ballistics"],
    }
)
"Requirements for training a Nuclear Missile"
STEALTH_BOMBER = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Stealth"],
    }
)
"Requirements for training a Stealth Bomber"
JET_FIGHTER = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Lasers"],
    }
)
"Requirements for training a Jet Fighter"
GUIDED_MISSILE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Advanced Ballistics"],
    }
)
"Requirements for training a Guided Missile"
MODERN_ARMOR = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Lasers"],
    }
)
"Requirements for training a Modern Armor"
HELICOPTER_GUNSHIP = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Computers"],
    }
)
"Requirements for training a Helicopter Gunship"
MOBILE_SAM = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Rocketry"],
    }
)
"Requirements for training a Mobile SAM"
ROCKET_ARTILLERY = items.ItemRequirements(
    ALUMINUM,
    progression={
        items.TECH_ITEMS["Rocketry"],
    }
)
"Requirements for training a Rocket Artillery"
MECHANIZED_INFANTRY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mobile Tactics"],
    }
)
"Requirements for training a Mechanized Infantry"
ATOMIC_BOMB = items.ItemRequirements(
    MANHATTAN_PROJECT,
    URANIUM,
    progression={
        items.TECH_ITEMS["Nuclear Fission"],
    }
)
"Requirements for training an Atomic Bomb"
BOMBER = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Radar"],
    }
)
"Requirements for training a Bomber"
FIGHTER = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Radar"],
    }
)
"Requirements for training a Fighter"
PARATROOPER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Radar"],
    }
)
"Requirements for training a Paratrooper"
TANK = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Combined Arms"],
    }
)
"Requirements for training a Tank"
ARTILLERY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Dynamite"],
    }
)
"Requirements for training an Artillery"
ANTI_AIRCRAFT_GUN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Ballistics"],
    }
)
"Requirements for training an Anti-Aircraft Gun"
ANTI_TANK_GUN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Combined Arms"],
    }
)
"Requirements for training an Anti-Tank Gun"
INFANTRY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Plastics"],
    }
)
"Requirements for training an Infantry"
CAVALRY = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["Military Science"],
    }
)
"Requirements for training a Cavalry"
RIFLEMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Rifling"],
    }
)
"Requirements for training a Rifleman"
LANCER = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["Metallurgy"],
    }
)
"Requirements for training a Lancer"
CANNON = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Chemistry"],
    }
)
"Requirements for training a Cannon"
MUSKETMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Gunpowder"],
    }
)
"Requirements for training a Musketman"
LONGSWORDSMAN = items.ItemRequirements(
    IRON,
    progression={
        items.TECH_ITEMS["Steel"],
    }
)
"Requirements for training a Longswordsman"
TREBUCHET = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Physics"],
    }
)
"Requirements for training a Trebuchet"
KNIGHT = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["Chivalry"],
    }
)
"Requirements for training a Knight"
CROSSBOWMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Machinery"],
    }
)
"Requirements for training a Crossbowman"
PIKEMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Civil Service"]
    }
)
"Requirements for training a Pikeman"
LANDSKNECHT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Civil Service"],
        items.POLICY_ITEMS["Mercenary Army"],
    }
)
"Requirements for training a Landsknecht"
CATAPULT = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Mathematics"],
    }
)
"Requirements for training a Catapult"
HORSEMAN = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["Horseback Riding"],
    }
)
"Requirements for training a Horseman"
SWORDSMAN = items.ItemRequirements(
    IRON,
    progression={
        items.TECH_ITEMS["Iron Working"],
    }
)
"Requirements for training a Swordsman"
CHARIOT_ARCHER = items.ItemRequirements(
    HORSES_SHEEP_CATTLE,
    progression={
        items.TECH_ITEMS["The Wheel"],
    }
)
"Requirements for training a Chariot Archer"
SPEARMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Bronze Working"],
    }
)
"Requirements for training a Spearman"
ARCHER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Archery"],
    }
)
"Requirements for training an Archer"
SCOUT = items.ItemRequirements()
"Requirements for training a Scout"
WARRIOR = items.ItemRequirements()
"Requirements for training a Warrior"
COMPOSITE_BOWMAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Construction"],
    }
)
"Requirements for training a Composite Bowman"
GALLEASS = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Compass"],
    }
)
"Requirements for training a Galleass"
GREAT_WAR_INFANTRY = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Replaceable Parts"],
    }
)
"Requirements for training a Great War Infantry"
MARINE = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Penicillin"],
    }
)
"Requirements for training a Marine"
TRIPLANE = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Flight"],
    }
)
"Requirements for training a Triplane"
GREAT_WAR_BOMBER = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Flight"],
    }
)
"Requirements for training a Great War Bomber"
LANDSHIP = items.ItemRequirements(
    OIL,
    progression={
        items.TECH_ITEMS["Combustion"],
    }
)
"Requirements for training a Landship"
MACHINE_GUN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Ballistics"]
    }
)
"Requirements for training a Machine Gun"
PRIVATEER = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Navigation"],
    }
)
"Requirements for training a Privateer"
GATLING_GUN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Industrialization"],
    }
)
"Requirements for training a Gatling Gun"
CARGO_SHIP = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Sailing"],
    }
)
"Requirements for training a Cargo Ship"
CARAVAN = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Animal Husbandry"],
    }
)
"Requirements for training a Caravan"
ARCHAEOLOGIST = items.ItemRequirements(
    UNIVERSITY,
    progression={
        items.TECH_ITEMS["Archaeology"],
    }
)
"Requirements for training an Archaeologist"
BAZOOKA = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Nuclear Fission"],
    }
)
"Requirements for training a Bazooka"
XCOM_SQUAD = items.ItemRequirements(
    progression={
        items.TECH_ITEMS["Nanotechnology"],
    }
)
"Requirements for training an XCOM Squad"


# %% COMBAT CLASS DEFINITIONS
ARCHER_CLASS = ARCHER | BAZOOKA | CHARIOT_ARCHER | COMPOSITE_BOWMAN | CROSSBOWMAN | GATLING_GUN | MACHINE_GUN
"Requirements for training an Archer combat class unit"
ARMOR_CLASS = GIANT_DEATH_ROBOT | LANDSHIP | MODERN_ARMOR | TANK
"Requirements for training an Armor combat class unit"
BOMBER_CLASS = BOMBER | GREAT_WAR_BOMBER | STEALTH_BOMBER
"Requirements for training a Bomber combat class unit"
CARRIER_CLASS = CARRIER
"Requirements for training a Carrier class unit"
FIGHTER_CLASS = FIGHTER | JET_FIGHTER | TRIPLANE
"Requirements for training a Fighter combat class unit"
GUN_CLASS = (
    ANTI_AIRCRAFT_GUN | ANTI_TANK_GUN | GREAT_WAR_INFANTRY | INFANTRY | MARINE | MECHANIZED_INFANTRY | MOBILE_SAM
    | MUSKETMAN | PARATROOPER | RIFLEMAN | XCOM_SQUAD
)
"Requirements for training a Gun combat class unit"
HELICOPTER_CLASS = HELICOPTER_GUNSHIP
"Requirements for training a Helicopter combat class unit"
MELEE_CLASS = LANDSKNECHT | LONGSWORDSMAN | PIKEMAN | SPEARMAN | SWORDSMAN | WARRIOR
"Requirements for training a Melee combat class unit"
MOUNTED_CLASS = CAVALRY | HORSEMAN | KNIGHT | LANCER
"Requirements for training a Mounted combat class unit"
NAVAL_MELEE_CLASS = CARAVEL | DESTROYER | IRONCLAD | PRIVATEER | TRIREME
"Requirements for training a Naval Melee combat class unit"
NAVAL_RANGED_CLASS = BATTLESHIP | FRIGATE | GALLEASS | MISSILE_CRUISER
"Requirements for training a Naval Ranged combat class unit"
RECON_CLASS = SCOUT
"Requirements for training a Recon combat class unit"
SIEGE_CLASS = ARTILLERY | CANNON | CATAPULT | ROCKET_ARTILLERY | TREBUCHET
"Requirements for training a Siege combat class unit"
SUBMARINE_CLASS = NUCLEAR_SUBMARINE | SUBMARINE
"Requirements for training a Submarine combat class unit"


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
        ARCHAEOLOGIST,
        ARTISTS_GUILD,
        BROADCAST_TOWER,
        HOTEL,
        MUSICIANS_GUILD,
        WRITERS_GUILD,
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
