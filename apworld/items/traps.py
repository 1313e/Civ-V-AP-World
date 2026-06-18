# %% IMPORTS
from BaseClasses import ItemClassification

from .core import CivVFillerItemData
from ..enums import CivVFillerType, CivVItemType

# All declaration
__all__ = []


# %% TRAP ITEM DECLARATIONS
_ = CivVFillerItemData(
    name="Gold -50",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=25,
    action={
        CivVFillerType.change_gold: -50,
    }
)
_ = CivVFillerItemData(
    name="Gold -100",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=15,
    action={
        CivVFillerType.change_gold: -100,
    }
)
_ = CivVFillerItemData(
    name="Gold -250",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=3,
    action={
        CivVFillerType.change_gold: -250,
    }
)
_ = CivVFillerItemData(
    name="Culture -50",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=25,
    action={
        CivVFillerType.change_culture: -50,
    }
)
_ = CivVFillerItemData(
    name="Culture -100",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=15,
    action={
        CivVFillerType.change_culture: -100,
    }
)
_ = CivVFillerItemData(
    name="Culture -250",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=3,
    action={
        CivVFillerType.change_culture: -250,
    }
)
_ = CivVFillerItemData(
    name="Faith -25",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=25,
    action={
        CivVFillerType.change_faith: -25,
    }
)
_ = CivVFillerItemData(
    name="Faith -50",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=15,
    action={
        CivVFillerType.change_faith: -50,
    }
)
_ = CivVFillerItemData(
    name="Faith -125",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=3,
    action={
        CivVFillerType.change_faith: -125,
    }
)
_ = CivVFillerItemData(
    name="All City-State Influence -15",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=4,
    action={
        CivVFillerType.change_all_city_state_influence: -15,
    }
)
_ = CivVFillerItemData(
    name="All City-State Influence -30",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=2,
    action={
        CivVFillerType.change_all_city_state_influence: -30,
    }
)
_ = CivVFillerItemData(
    name="All City Population -1",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=5,
    action={
        CivVFillerType.change_all_city_population: -1,
    }
)
_ = CivVFillerItemData(
    name="All City Population -2",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=2,
    action={
        CivVFillerType.change_all_city_population: -2,
    }
)
_ = CivVFillerItemData(
    name="Barbarians 1",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=6,
    action={
        CivVFillerType.spawn_barbarians: 3,
    }
)
_ = CivVFillerItemData(
    name="Barbarians 3",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=3,
    action={
        CivVFillerType.spawn_barbarians: 3,
    }
)
_ = CivVFillerItemData(
    name="Barbarians 6",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=1,
    action={
        CivVFillerType.spawn_barbarians: 6,
    }
)
_ = CivVFillerItemData(
    name="Shuffle Units",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=4,
    action={
        CivVFillerType.shuffle_units: 1,
    }
)
_ = CivVFillerItemData(
    name="Denounce",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=2,
    action={
        CivVFillerType.denounce_random: 1,
    }
)
_ = CivVFillerItemData(
    name="War",
    type=CivVItemType.trap,
    classification=ItemClassification.trap,
    weight=1,
    action={
        CivVFillerType.declare_war_random: 1,
    }
)
