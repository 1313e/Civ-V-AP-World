# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVFillerItemData
from ..enums import CivVFillerType, CivVItemType

# All declaration
__all__ = []


# %% ITEM DECLARATIONS
GOLD_TRAP_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Gold": CivVFillerItemData(
        name="Minor Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_gold: -50,
        }
    ),
    "Gold": CivVFillerItemData(
        name="Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_gold: -100,
        }
    ),
    "Major Gold": CivVFillerItemData(
        name="Major Gold",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_gold: -250,
        }
    ),
}
"Dict of all gold trap items"


CULTURE_TRAP_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Culture": CivVFillerItemData(
        name="Minor Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_culture: -50,
        }
    ),
    "Culture": CivVFillerItemData(
        name="Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_culture: -100,
        }
    ),
    "Major Culture": CivVFillerItemData(
        name="Major Culture",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_culture: -250,
        }
    ),
}
"Dict of all culture trap items"


FAITH_TRAP_ITEMS: dict[str, CivVFillerItemData] = {
    "Minor Faith": CivVFillerItemData(
        name="Minor Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=25,
        action={
            CivVFillerType.change_faith: -25,
        }
    ),
    "Faith": CivVFillerItemData(
        name="Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=15,
        action={
            CivVFillerType.change_faith: -50,
        }
    ),
    "Major Faith": CivVFillerItemData(
        name="Major Faith",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=3,
        action={
            CivVFillerType.change_faith: -125,
        }
    ),
}
"Dict of all faith trap items"


ALL_CITY_POPULATION_TRAP_ITEMS: dict[str, CivVFillerItemData] = {
    "All City Population -1": CivVFillerItemData(
        name="All City Population -1",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=5,
        action={
            CivVFillerType.change_all_city_population: -1,
        }
    ),
    "All City Population -2": CivVFillerItemData(
        name="All City Population -2",
        type=CivVItemType.trap,
        classification=ItemClassification.trap,
        weight=2,
        action={
            CivVFillerType.change_all_city_population: -2,
        }
    ),
}
"Dict of city population trap items"


DENOUNCE_TRAP_ITEM: CivVFillerItemData = CivVFillerItemData(
    name="Denounce",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=2,
    action={
        CivVFillerType.denounce_random: 1,
    }
)
"Denounce trap item"


WAR_TRAP_ITEM: CivVFillerItemData = CivVFillerItemData(
    name="War",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=1,
    action={
        CivVFillerType.declare_war_random: 1,
    }
)
"War trap item"
