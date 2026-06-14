# %% IMPORTS
from .core import CivVUsefulItemData
from ..enums import CivVItemType

# All declaration
__all__ = [
    "PROMOTION_ITEMS",
]


# %% ITEM DECLARATIONS
PROMOTION_ITEMS: dict[str, CivVUsefulItemData] = {
    "Shock I": CivVUsefulItemData(
        name="Shock I",
        type=CivVItemType.promotion,
        game_id=1,
    ),
    "Shock II": CivVUsefulItemData(
        name="Shock II",
        type=CivVItemType.promotion,
        game_id=2,
    ),
    "Shock III": CivVUsefulItemData(
        name="Shock III",
        type=CivVItemType.promotion,
        game_id=3,
    ),
    "Drill I": CivVUsefulItemData(
        name="Drill I",
        type=CivVItemType.promotion,
        game_id=4,
    ),
    "Drill II": CivVUsefulItemData(
        name="Drill II",
        type=CivVItemType.promotion,
        game_id=5,
    ),
    "Drill III": CivVUsefulItemData(
        name="Drill III",
        type=CivVItemType.promotion,
        game_id=6,
    ),
    "Accuracy I": CivVUsefulItemData(
        name="Accuracy I",
        type=CivVItemType.promotion,
        game_id=7,
    ),
    "Accuracy II": CivVUsefulItemData(
        name="Accuracy II",
        type=CivVItemType.promotion,
        game_id=8,
    ),
    "Accuracy III": CivVUsefulItemData(
        name="Accuracy III",
        type=CivVItemType.promotion,
        game_id=9,
    ),
    "Barrage I": CivVUsefulItemData(
        name="Barrage I",
        type=CivVItemType.promotion,
        game_id=10,
    ),
    "Barrage II": CivVUsefulItemData(
        name="Barrage II",
        type=CivVItemType.promotion,
        game_id=11,
    ),
    "Barrage III": CivVUsefulItemData(
        name="Barrage III",
        type=CivVItemType.promotion,
        game_id=12,
    ),
    "Targeting I": CivVUsefulItemData(
        name="Targeting I",
        type=CivVItemType.promotion,
        game_id=13,
    ),
    "Targeting II": CivVUsefulItemData(
        name="Targeting II",
        type=CivVItemType.promotion,
        game_id=14,
    ),
    "Targeting III": CivVUsefulItemData(
        name="Targeting III",
        type=CivVItemType.promotion,
        game_id=15,
    ),
    "Sentry": CivVUsefulItemData(
        name="Sentry",
        type=CivVItemType.promotion,
        game_id=16,
    ),
    "Siege": CivVUsefulItemData(
        name="Siege",
        type=CivVItemType.promotion,
        game_id=17,
    ),
    "Volley": CivVUsefulItemData(
        name="Volley",
        type=CivVItemType.promotion,
        game_id=18,
    ),
    "Medic I": CivVUsefulItemData(
        name="Medic I",
        type=CivVItemType.promotion,
        game_id=19,
    ),
    "Medic II": CivVUsefulItemData(
        name="Medic II",
        type=CivVItemType.promotion,
        game_id=20,
    ),
    "Amphibious": CivVUsefulItemData(
        name="Amphibious",
        type=CivVItemType.promotion,
        game_id=21,
    ),
    "Cover I": CivVUsefulItemData(
        name="Cover I",
        type=CivVItemType.promotion,
        game_id=22,
    ),
    "Cover II": CivVUsefulItemData(
        name="Cover II",
        type=CivVItemType.promotion,
        game_id=23,
    ),
    "Charge": CivVUsefulItemData(
        name="Charge",
        type=CivVItemType.promotion,
        game_id=25,
    ),
    "Formation I": CivVUsefulItemData(
        name="Formation I",
        type=CivVItemType.promotion,
        game_id=26,
    ),
    "Formation II": CivVUsefulItemData(
        name="Formation II",
        type=CivVItemType.promotion,
        game_id=27,
    ),
    "Ambush I": CivVUsefulItemData(
        name="Ambush I",
        type=CivVItemType.promotion,
        game_id=28,
    ),
    "Ambush II": CivVUsefulItemData(
        name="Ambush II",
        type=CivVItemType.promotion,
        game_id=29,
    ),
    "Supply": CivVUsefulItemData(
        name="Supply",
        type=CivVItemType.promotion,
        game_id=30,
    ),
    "March": CivVUsefulItemData(
        name="March",
        type=CivVItemType.promotion,
        game_id=31,
    ),
    "Blitz": CivVUsefulItemData(
        name="Blitz",
        type=CivVItemType.promotion,
        game_id=32,
    ),
    "Woodsman": CivVUsefulItemData(
        name="Woodsman",
        type=CivVItemType.promotion,
        game_id=33,
    ),
    "Logistics": CivVUsefulItemData(
        name="Logistics",
        type=CivVItemType.promotion,
        game_id=34,
    ),
    "Range": CivVUsefulItemData(
        name="Range",
        type=CivVItemType.promotion,
        game_id=35,
    ),
    "Mobility": CivVUsefulItemData(
        name="Mobility",
        type=CivVItemType.promotion,
        game_id=36,
    ),
    "Interception I": CivVUsefulItemData(
        name="Interception I",
        type=CivVItemType.promotion,
        game_id=37,
    ),
    "Interception II": CivVUsefulItemData(
        name="Interception II",
        type=CivVItemType.promotion,
        game_id=38,
    ),
    "Interception III": CivVUsefulItemData(
        name="Interception III",
        type=CivVItemType.promotion,
        game_id=39,
    ),
    "Dogfighting I": CivVUsefulItemData(
        name="Dogfighting I",
        type=CivVItemType.promotion,
        game_id=40,
    ),
    "Dogfighting II": CivVUsefulItemData(
        name="Dogfighting II",
        type=CivVItemType.promotion,
        game_id=41,
    ),
    "Dogfighting III": CivVUsefulItemData(
        name="Dogfighting III",
        type=CivVItemType.promotion,
        game_id=42,
    ),
    "Air Siege I": CivVUsefulItemData(
        name="Air Siege I",
        type=CivVItemType.promotion,
        game_id=43,
    ),
    "Air Siege II": CivVUsefulItemData(
        name="Air Siege II",
        type=CivVItemType.promotion,
        game_id=44,
    ),
    "Air Siege III": CivVUsefulItemData(
        name="Air Siege III",
        type=CivVItemType.promotion,
        game_id=45,
    ),
    "Bombardment I": CivVUsefulItemData(
        name="Bombardment I",
        type=CivVItemType.promotion,
        game_id=46,
    ),
    "Bombardment II": CivVUsefulItemData(
        name="Bombardment II",
        type=CivVItemType.promotion,
        game_id=47,
    ),
    "Bombardment III": CivVUsefulItemData(
        name="Bombardment III",
        type=CivVItemType.promotion,
        game_id=48,
    ),
    "Air Targeting I": CivVUsefulItemData(
        name="Air Targeting I",
        type=CivVItemType.promotion,
        game_id=49,
    ),
    "Air Targeting II": CivVUsefulItemData(
        name="Air Targeting II",
        type=CivVItemType.promotion,
        game_id=50,
    ),
    "Air Ambush I": CivVUsefulItemData(
        name="Air Ambush I",
        type=CivVItemType.promotion,
        game_id=51,
    ),
    "Air Ambush II": CivVUsefulItemData(
        name="Air Ambush II",
        type=CivVItemType.promotion,
        game_id=52,
    ),
    "Air Range": CivVUsefulItemData(
        name="Air Range",
        type=CivVItemType.promotion,
        game_id=53,
    ),
    "Sortie": CivVUsefulItemData(
        name="Sortie",
        type=CivVItemType.promotion,
        game_id=54,
    ),
    "Repair": CivVUsefulItemData(
        name="Repair",
        type=CivVItemType.promotion,
        game_id=55,
    ),
    "Air Repair": CivVUsefulItemData(
        name="Air Repair",
        type=CivVItemType.promotion,
        game_id=56,
    ),
    "Air Logistics": CivVUsefulItemData(
        name="Air Logistics",
        type=CivVItemType.promotion,
        game_id=57,
    ),
    "Evasion": CivVUsefulItemData(
        name="Evasion",
        type=CivVItemType.promotion,
        game_id=58,
    ),
    "Scouting I": CivVUsefulItemData(
        name="Scouting I",
        type=CivVItemType.promotion,
        game_id=59,
    ),
    "Scouting II": CivVUsefulItemData(
        name="Scouting II",
        type=CivVItemType.promotion,
        game_id=60,
    ),
    "Scouting III": CivVUsefulItemData(
        name="Scouting III",
        type=CivVItemType.promotion,
        game_id=61,
    ),
    "Survivalism I": CivVUsefulItemData(
        name="Survivalism I",
        type=CivVItemType.promotion,
        game_id=62,
    ),
    "Survivalism II": CivVUsefulItemData(
        name="Survivalism II",
        type=CivVItemType.promotion,
        game_id=63,
    ),
    "Survivalism III": CivVUsefulItemData(
        name="Survivalism III",
        type=CivVItemType.promotion,
        game_id=64,
    ),
    "Heli Ambush I": CivVUsefulItemData(
        name="Heli Ambush I",
        type=CivVItemType.promotion,
        game_id=65,
    ),
    "Heli Ambush II": CivVUsefulItemData(
        name="Heli Ambush II",
        type=CivVItemType.promotion,
        game_id=66,
    ),
    "Heli Mobility I": CivVUsefulItemData(
        name="Heli Mobility I",
        type=CivVItemType.promotion,
        game_id=67,
    ),
    "Heli Mobility II": CivVUsefulItemData(
        name="Heli Mobility II",
        type=CivVItemType.promotion,
        game_id=68,
    ),
    "Heli Repair": CivVUsefulItemData(
        name="Heli Repair",
        type=CivVItemType.promotion,
        game_id=69,
    ),
    "Coastal Raider I": CivVUsefulItemData(
        name="Coastal Raider I",
        type=CivVItemType.promotion,
        game_id=70,
    ),
    "Coastal Raider II": CivVUsefulItemData(
        name="Coastal Raider II",
        type=CivVItemType.promotion,
        game_id=71,
    ),
    "Coastal Raider III": CivVUsefulItemData(
        name="Coastal Raider III",
        type=CivVItemType.promotion,
        game_id=72,
    ),
    "Boarding Party I": CivVUsefulItemData(
        name="Boarding Party I",
        type=CivVItemType.promotion,
        game_id=73,
    ),
    "Boarding Party II": CivVUsefulItemData(
        name="Boarding Party II",
        type=CivVItemType.promotion,
        game_id=74,
    ),
    "Boarding Party III": CivVUsefulItemData(
        name="Boarding Party III",
        type=CivVItemType.promotion,
        game_id=75,
    ),
    "Wolfpack I": CivVUsefulItemData(
        name="Wolfpack I",
        type=CivVItemType.promotion,
        game_id=76,
    ),
    "Wolfpack II": CivVUsefulItemData(
        name="Wolfpack II",
        type=CivVItemType.promotion,
        game_id=77,
    ),
    "Wolfpack III": CivVUsefulItemData(
        name="Wolfpack III",
        type=CivVItemType.promotion,
        game_id=78,
    ),
    "Flight Deck I": CivVUsefulItemData(
        name="Flight Deck I",
        type=CivVItemType.promotion,
        game_id=79,
    ),
    "Flight Deck II": CivVUsefulItemData(
        name="Flight Deck II",
        type=CivVItemType.promotion,
        game_id=80,
    ),
    "Flight Deck III": CivVUsefulItemData(
        name="Flight Deck III",
        type=CivVItemType.promotion,
        game_id=81,
    ),
    "Armor Plating I": CivVUsefulItemData(
        name="Armor Plating I",
        type=CivVItemType.promotion,
        game_id=82,
    ),
    "Armor Plating II": CivVUsefulItemData(
        name="Armor Plating II",
        type=CivVItemType.promotion,
        game_id=83,
    ),
    "Armor Plating III": CivVUsefulItemData(
        name="Armor Plating III",
        type=CivVItemType.promotion,
        game_id=84,
    ),
}
"Dict of all earnable promotion items"
