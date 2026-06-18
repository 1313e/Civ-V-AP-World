# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVFillerItemData
from ..enums import CivVFillerType, CivVItemType

# All declaration
__all__ = []


# %% ITEM DECLARATIONS
FILLER_ITEMS: list[CivVFillerItemData] = [
    CivVFillerItemData(
        name="Gold: +100",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_gold: 100,
        }
    ),
    CivVFillerItemData(
        name="Gold: +250",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_gold: 250,
        }
    ),
    CivVFillerItemData(
        name="Gold: +1000",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_gold: 1000,
        }
    ),
    CivVFillerItemData(
        name="Culture: +100",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=11,
        action={
            CivVFillerType.change_culture: 100,
        }
    ),
    CivVFillerItemData(
        name="Culture: +250",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=6,
        action={
            CivVFillerType.change_culture: 250,
        }
    ),
    CivVFillerItemData(
        name="Culture: +1000",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=3,
        action={
            CivVFillerType.change_culture: 1000,
        }
    ),
    CivVFillerItemData(
        name="Faith: +50",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=7,
        action={
            CivVFillerType.change_faith: 50,
        }
    ),
    CivVFillerItemData(
        name="Faith: +125",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=4,
        action={
            CivVFillerType.change_faith: 125,
        }
    ),
    CivVFillerItemData(
        name="Faith: +500",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_faith: 500,
        }
    ),
    CivVFillerItemData(
        name="Snack from Thes",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=9,
        action={
            CivVFillerType.change_gold: 200,
            CivVFillerType.change_culture: 200,
            CivVFillerType.change_faith: 100,
        }
    ),
    CivVFillerItemData(
        name="Free Great Person",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_great_people: 1,
        }
    ),
    CivVFillerItemData(
        name="Free Policy",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_free_policies: 1,
        }
    ),
    CivVFillerItemData(
        name="Free Tech",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_techs: 1,
        }
    ),
    CivVFillerItemData(
        name="Free Unit",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=3,
        action={
            CivVFillerType.grant_free_unit: 1,
        }
    ),
    CivVFillerItemData(
        name="Free Worker",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.grant_free_worker: 1,
        }
    ),
    CivVFillerItemData(
        name="All City-State Influence: +15",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=3,
        action={
            CivVFillerType.change_all_city_state_influence: 15,
        }
    ),
    CivVFillerItemData(
        name="All City-State Influence: +30",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_all_city_state_influence: 30,
        }
    ),
    CivVFillerItemData(
        name="All City Population: +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=4,
        action={
            CivVFillerType.change_all_city_population: 1,
        }
    ),
    CivVFillerItemData(
        name="All City Population: +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_all_city_population: 2,
        }
    ),
    CivVFillerItemData(
        name="New City Extra Population: +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=3,
        action={
            CivVFillerType.change_new_city_extra_population: 1,
        }
    ),
    CivVFillerItemData(
        name="New City Extra Population: +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_new_city_extra_population: 2,
        }
    ),
    CivVFillerItemData(
        name="Extra Happiness Per City: +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_extra_happiness_per_city: 1,
        }
    ),
    CivVFillerItemData(
        name="Extra Happiness Per City: +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_extra_happiness_per_city: 2,
        }
    ),
    CivVFillerItemData(
        name="Culture Per Turn For Free: +50",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=3,
        action={
            CivVFillerType.change_culture_per_turn_for_free: 50,
        }
    ),
    CivVFillerItemData(
        name="All Unit Experience: +15",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=8,
        action={
            CivVFillerType.change_all_unit_experience: 15,
        }
    ),
    CivVFillerItemData(
        name="All Unit Experience: +35",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=4,
        action={
            CivVFillerType.change_all_unit_experience: 35,
        }
    ),
    CivVFillerItemData(
        name="All Unit Experience: +80",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_all_unit_experience: 80,
        }
    ),
    CivVFillerItemData(
        name="All Unit Free Promotion",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.all_units_free_promotion: 1,
        }
    ),
    CivVFillerItemData(
        name="Golden Age",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.start_golden_age: 1,
        }
    ),
]
"List of all filler items"
