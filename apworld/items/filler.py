# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVFillerItemData
from ..enums import CivVFillerType, CivVItemType

# All declaration
__all__ = []


# %% ITEM DECLARATIONS
GOLD_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Gold": CivVFillerItemData(
        name="Minor Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_gold: 100,
        }
    ),
    "Gold": CivVFillerItemData(
        name="Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_gold: 250,
        }
    ),
    "Major Gold": CivVFillerItemData(
        name="Major Gold",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_gold: 1000,
        }
    ),
}
"Dict of all gold filler items"


CULTURE_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Culture": CivVFillerItemData(
        name="Minor Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_culture: 100,
        }
    ),
    "Culture": CivVFillerItemData(
        name="Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_culture: 250,
        }
    ),
    "Major Culture": CivVFillerItemData(
        name="Major Culture",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_culture: 1000,
        }
    ),
}
"Dict of all culture filler items"


FAITH_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Faith": CivVFillerItemData(
        name="Minor Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=10,
        action={
            CivVFillerType.change_faith: 50,
        }
    ),
    "Faith": CivVFillerItemData(
        name="Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_faith: 125,
        }
    ),
    "Major Faith": CivVFillerItemData(
        name="Major Faith",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_faith: 500,
        }
    ),
}
"Dict of all faith filler items"


COMBO_FILLER_ITEM: CivVFillerItemData = CivVFillerItemData(
    name="Snack from Thes",
    type=CivVItemType.bonus,
    classification=ItemClassification.filler,
    weight=8,
    action={
        CivVFillerType.change_gold: 200,
        CivVFillerType.change_culture: 200,
        CivVFillerType.change_faith: 100,
    }
)
"Filler item that gives a bit of everything"


FREE_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "Free Great Person": CivVFillerItemData(
        name="Free Great Person",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_great_people: 1,
        }
    ),
    "Free Policy": CivVFillerItemData(
        name="Free Policy",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_policies: 1,
        }
    ),
    "Free Tech": CivVFillerItemData(
        name="Free Tech",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=1,
        action={
            CivVFillerType.change_free_techs: 1,
        }
    ),
}
"Dict of free reward filler items"


ALL_CITY_POPULATION_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "All City Population +1": CivVFillerItemData(
        name="All City Population +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_all_city_population: 1,
        }
    ),
    "All City Population +2": CivVFillerItemData(
        name="All City Population +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_all_city_population: 2,
        }
    ),
}
"Dict of city population filler items"


NEW_CITY_EXTRA_POPULATION_FILLER_ITEMS: dict[str, CivVFillerItemData] = {
    "New City Extra Population +1": CivVFillerItemData(
        name="New City Extra Population +1",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=5,
        action={
            CivVFillerType.change_new_city_extra_population: 1,
        }
    ),
    "New City Extra Population +2": CivVFillerItemData(
        name="New City Extra Population +2",
        type=CivVItemType.bonus,
        classification=ItemClassification.filler,
        weight=2,
        action={
            CivVFillerType.change_new_city_extra_population: 2,
        }
    ),
}
"Dict of extra population in newly founded cities filler items"


EXTRA_HAPPINESS_PER_CITY_FILLER_ITEM: CivVFillerItemData = CivVFillerItemData(
    name="Extra Happiness Per City",
    type=CivVItemType.bonus,
    classification=ItemClassification.filler,
    weight=2,
    action={
        CivVFillerType.change_extra_happiness_per_city: 1,
    }
)
"Extra happiness per city filler item"


GOLDEN_AGE_FILLER_ITEM: CivVFillerItemData = CivVFillerItemData(
    name="Golden Age",
    type=CivVItemType.bonus,
    classification=ItemClassification.filler,
    weight=1,
    action={
        CivVFillerType.start_golden_age: 1,
    }
)
"Golden age filler item"
