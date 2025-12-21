# %% IMPORTS
from .core import CivVProgressionItemData, CivVUsefulItemData
from ..enums import CivVItemType

# All declaration
__all__ = [
    "POLICY_ITEMS",
]


# %% ITEM DECLARATIONS
POLICY_ITEMS = {
    "Liberty": CivVUsefulItemData(
        name="Liberty",
        type=CivVItemType.policy,
        game_id=0,
        prefix="Policy Branch",
    ),
    "Collective Rule": CivVUsefulItemData(
        name="Collective Rule",
        type=CivVItemType.policy,
        game_id=1,
    ),
    "Citizenship": CivVUsefulItemData(
        name="Citizenship",
        type=CivVItemType.policy,
        game_id=2,
    ),
    "Republic": CivVUsefulItemData(
        name="Republic",
        type=CivVItemType.policy,
        game_id=3,
    ),
    "Representation": CivVUsefulItemData(
        name="Representation",
        type=CivVItemType.policy,
        game_id=4,
    ),
    "Meritocracy": CivVUsefulItemData(
        name="Meritocracy",
        type=CivVItemType.policy,
        game_id=5,
    ),
    "Tradition": CivVUsefulItemData(
        name="Tradition",
        type=CivVItemType.policy,
        game_id=6,
        prefix="Policy Branch",
    ),
    "Aristocracy": CivVUsefulItemData(
        name="Aristocracy",
        type=CivVItemType.policy,
        game_id=7,
    ),
    "Oligarchy": CivVUsefulItemData(
        name="Oligarchy",
        type=CivVItemType.policy,
        game_id=8,
    ),
    "Legalism": CivVUsefulItemData(
        name="Legalism",
        type=CivVItemType.policy,
        game_id=9,
    ),
    "Landed Elite": CivVUsefulItemData(
        name="Landed Elite",
        type=CivVItemType.policy,
        game_id=10,
    ),
    "Monarchy": CivVUsefulItemData(
        name="Monarchy",
        type=CivVItemType.policy,
        game_id=11,
    ),
    "Honor": CivVUsefulItemData(
        name="Honor",
        type=CivVItemType.policy,
        game_id=12,
        prefix="Policy Branch",
    ),
    "Warrior Code": CivVUsefulItemData(
        name="Warrior Code",
        type=CivVItemType.policy,
        game_id=13,
    ),
    "Discipline": CivVUsefulItemData(
        name="Discipline",
        type=CivVItemType.policy,
        game_id=14,
    ),
    "Military Tradition": CivVUsefulItemData(
        name="Military Tradition",
        type=CivVItemType.policy,
        game_id=15,
    ),
    "Military Caste": CivVUsefulItemData(
        name="Military Caste",
        type=CivVItemType.policy,
        game_id=16,
    ),
    "Professional Army": CivVUsefulItemData(
        name="Professional Army",
        type=CivVItemType.policy,
        game_id=17,
    ),
    "Piety": CivVUsefulItemData(
        name="Piety",
        type=CivVItemType.policy,
        game_id=18,
        prefix="Policy Branch",
    ),
    "Organized Religion": CivVUsefulItemData(
        name="Organized Religion",
        type=CivVItemType.policy,
        game_id=19,
    ),
    "Mandate of Heaven": CivVUsefulItemData(
        name="Mandate of Heaven",
        type=CivVItemType.policy,
        game_id=20,
    ),
    "Theocracy": CivVUsefulItemData(
        name="Theocracy",
        type=CivVItemType.policy,
        game_id=21,
    ),
    "Reformation": CivVUsefulItemData(
        name="Reformation",
        type=CivVItemType.policy,
        game_id=22,
    ),
    "Religious Tolerance": CivVUsefulItemData(
        name="Religious Tolerance",
        type=CivVItemType.policy,
        game_id=23,
    ),
    "Patronage": CivVProgressionItemData(
        name="Patronage",
        type=CivVItemType.policy,
        game_id=24,
        prefix="Policy Branch",
    ),
    "Philanthropy": CivVProgressionItemData(
        name="Philanthropy",
        type=CivVItemType.policy,
        game_id=25,
    ),
    "Consulates": CivVProgressionItemData(
        name="Consulates",
        type=CivVItemType.policy,
        game_id=26,
    ),
    "Scholasticism": CivVUsefulItemData(
        name="Scholasticism",
        type=CivVItemType.policy,
        game_id=27,
    ),
    "Cultural Diplomacy": CivVUsefulItemData(
        name="Cultural Diplomacy",
        type=CivVItemType.policy,
        game_id=28,
    ),
    "Merchant Confederacy": CivVUsefulItemData(
        name="Merchant Confederacy",
        type=CivVItemType.policy,
        game_id=29,
    ),
    "Commerce": CivVUsefulItemData(
        name="Commerce",
        type=CivVItemType.policy,
        game_id=30,
        prefix="Policy Branch",
    ),
    "Trade Unions": CivVUsefulItemData(
        name="Trade Unions",
        type=CivVItemType.policy,
        game_id=31,
    ),
    "Entrepreneurship": CivVUsefulItemData(
        name="Entrepreneurship",
        type=CivVItemType.policy,
        game_id=32,
    ),
    "Mercantilism": CivVUsefulItemData(
        name="Mercantilism",
        type=CivVItemType.policy,
        game_id=33,
    ),
    "Caravans": CivVUsefulItemData(
        name="Caravans",
        type=CivVItemType.policy,
        game_id=34,
    ),
    "Protectionism": CivVUsefulItemData(
        name="Protectionism",
        type=CivVItemType.policy,
        game_id=35,
    ),
    "Rationalism": CivVUsefulItemData(
        name="Rationalism",
        type=CivVItemType.policy,
        game_id=36,
        prefix="Policy Branch",
    ),
    "Secularism": CivVUsefulItemData(
        name="Secularism",
        type=CivVItemType.policy,
        game_id=37,
    ),
    "Humanism": CivVUsefulItemData(
        name="Humanism",
        type=CivVItemType.policy,
        game_id=38,
    ),
    "Free Thought": CivVUsefulItemData(
        name="Free Thought",
        type=CivVItemType.policy,
        game_id=39,
    ),
    "Sovereignty": CivVUsefulItemData(
        name="Sovereignty",
        type=CivVItemType.policy,
        game_id=40,
    ),
    "Scientific Revolution": CivVUsefulItemData(
        name="Scientific Revolution",
        type=CivVItemType.policy,
        game_id=41,
    ),
    "Tradition Finisher": CivVUsefulItemData(
        name="Tradition Finisher",
        type=CivVItemType.policy,
        game_id=42,
        prefix="Policy Branch",
    ),
    "Liberty Finisher": CivVUsefulItemData(
        name="Liberty Finisher",
        type=CivVItemType.policy,
        game_id=43,
        prefix="Policy Branch",
    ),
    "Honor Finisher": CivVUsefulItemData(
        name="Honor Finisher",
        type=CivVItemType.policy,
        game_id=44,
        prefix="Policy Branch",
    ),
    "Piety Finisher": CivVUsefulItemData(
        name="Piety Finisher",
        type=CivVItemType.policy,
        game_id=45,
        prefix="Policy Branch",
    ),
    "Patronage Finisher": CivVUsefulItemData(
        name="Patronage Finisher",
        type=CivVItemType.policy,
        game_id=46,
        prefix="Policy Branch",
    ),
    "Commerce Finisher": CivVUsefulItemData(
        name="Commerce Finisher",
        type=CivVItemType.policy,
        game_id=47,
        prefix="Policy Branch",
    ),
    "Rationalism Finisher": CivVUsefulItemData(
        name="Rationalism Finisher",
        type=CivVItemType.policy,
        game_id=48,
        prefix="Policy Branch",
    ),
    "Aesthetics": CivVProgressionItemData(
        name="Aesthetics",
        type=CivVItemType.policy,
        game_id=49,
        prefix="Policy Branch",
    ),
    "Cultural Centers": CivVUsefulItemData(
        name="Cultural Centers",
        type=CivVItemType.policy,
        game_id=50,
    ),
    "Fine Arts": CivVUsefulItemData(
        name="Fine Arts",
        type=CivVItemType.policy,
        game_id=51,
    ),
    "Flourishing of the Arts": CivVUsefulItemData(
        name="Flourishing of the Arts",
        type=CivVItemType.policy,
        game_id=52,
    ),
    "Artistic Genius": CivVUsefulItemData(
        name="Artistic Genius",
        type=CivVItemType.policy,
        game_id=53,
    ),
    "Cultural Exchange": CivVProgressionItemData(
        name="Cultural Exchange",
        type=CivVItemType.policy,
        game_id=54,
    ),
    "Aesthetics Finisher": CivVProgressionItemData(
        name="Aesthetics Finisher",
        type=CivVItemType.policy,
        game_id=55,
        prefix="Policy Branch",
    ),
    "Exploration": CivVUsefulItemData(
        name="Exploration",
        type=CivVItemType.policy,
        game_id=56,
        prefix="Policy Branch",
    ),
    "Maritime Infrastructure": CivVUsefulItemData(
        name="Maritime Infrastructure",
        type=CivVItemType.policy,
        game_id=57,
    ),
    "Naval Tradition": CivVUsefulItemData(
        name="Naval Tradition",
        type=CivVItemType.policy,
        game_id=58,
    ),
    "Merchant Navy": CivVUsefulItemData(
        name="Merchant Navy",
        type=CivVItemType.policy,
        game_id=59,
    ),
    "Navigation School": CivVUsefulItemData(
        name="Navigation School",
        type=CivVItemType.policy,
        game_id=60,
    ),
    "Treasure Fleets": CivVUsefulItemData(
        name="Treasure Fleets",
        type=CivVItemType.policy,
        game_id=61,
    ),
    "Exploration Finisher": CivVUsefulItemData(
        name="Exploration Finisher",
        type=CivVItemType.policy,
        game_id=62,
        prefix="Policy Branch",
    ),
}
"Dict of all policies"
