# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVFillerItemData
from ..enums import CivVFillerType, CivVItemType

# All declaration
__all__ = []


# %% ITEM DECLARATIONS
TRAP_ITEMS: list[CivVFillerItemData] = [
    CivVFillerItemData(
        name="Gold: -50",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_gold: -50,
        }
    ),
    CivVFillerItemData(
        name="Gold: -100",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_gold: -100,
        }
    ),
    CivVFillerItemData(
        name="Gold: -250",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_gold: -250,
        }
    ),
    CivVFillerItemData(
        name="Culture: -50",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_culture: -50,
        }
    ),
    CivVFillerItemData(
        name="Culture: -100",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_culture: -100,
        }
    ),
    CivVFillerItemData(
        name="Culture: -250",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_culture: -250,
        }
    ),
    CivVFillerItemData(
        name="Faith: -25",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_faith: -25,
        }
    ),
    CivVFillerItemData(
        name="Faith: -50",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_faith: -50,
        }
    ),
    CivVFillerItemData(
        name="Faith: -125",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_faith: -125,
        }
    ),
    CivVFillerItemData(
        name="All City-State Influence: -15",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=4,
        action={
            CivVFillerType.change_all_city_state_influence: -15,
        }
    ),
    CivVFillerItemData(
        name="All City-State Influence: -30",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=2,
        action={
            CivVFillerType.change_all_city_state_influence: -30,
        }
    ),
    CivVFillerItemData(
        name="All City Population: -1",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=5,
        action={
            CivVFillerType.change_all_city_population: -1,
        }
    ),
    CivVFillerItemData(
        name="All City Population: -2",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=2,
        action={
            CivVFillerType.change_all_city_population: -2,
        }
    ),
    CivVFillerItemData(
        name="Barbarians: 1",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=6,
        action={
            CivVFillerType.spawn_barbarians: 3,
        }
    ),
        CivVFillerItemData(
        name="Barbarians: 3",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.spawn_barbarians: 3,
        }
    ),
    CivVFillerItemData(
        name="Barbarians: 6",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=1,
        action={
            CivVFillerType.spawn_barbarians: 6,
        }
    ),
    CivVFillerItemData(
        name="Shuffle Units",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=4,
        action={
            CivVFillerType.shuffle_units: 1,
        }
    ),
    CivVFillerItemData(
        name="Denounce",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=2,
        action={
            CivVFillerType.denounce_random: 1,
        }
    ),
    CivVFillerItemData(
        name="War",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=1,
        action={
            CivVFillerType.declare_war_random: 1,
        }
    ),
]
"List of all trap items"
