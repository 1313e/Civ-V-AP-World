# %% IMPORTS
from dataclasses import dataclass

from .enums import CivVDeathLinkEffectType

# All declaration
__all__ = [
    "DEATH_LINK_EFFECTS",
    "DEATH_LINK_EFFECTS_BY_NAME",
    "CivVDeathLinkEffect",
]


# %% GLOBALS
DEATH_LINK_EFFECTS: list["CivVDeathLinkEffect"] = []
"List of all defined death link effects"
DEATH_LINK_EFFECTS_BY_NAME: dict[str, "CivVDeathLinkEffect"] = {}
"Dict of all defined death link effects, separated by name"


# %% DEATH_LINK_EFFECT CLASS DEFINITION
@dataclass
class CivVDeathLinkEffect:
    """
    Dataclass used for specifying a death link effect.

    """

    name: str
    "Name of this death link effect"
    type: CivVDeathLinkEffectType
    "Type of this death link effect"
    amount: int | None
    "Amount for this death link effect"

    def __post_init__(self):
        # Add self to the dicts
        DEATH_LINK_EFFECTS.append(self)
        DEATH_LINK_EFFECTS_BY_NAME[self.name] = self


# %% DEATH_LINK_EFFECTS DEFINITIONS
_ = CivVDeathLinkEffect(
    name="Random Unit 25% HP",
    type=CivVDeathLinkEffectType.random_unit_hp,
    amount=25,
)
_ = CivVDeathLinkEffect(
    name="Random Unit 50% HP",
    type=CivVDeathLinkEffectType.random_unit_hp,
    amount=50,
)
_ = CivVDeathLinkEffect(
    name="Random Unit 100% HP",
    type=CivVDeathLinkEffectType.random_unit_hp,
    amount=100,
)
_ = CivVDeathLinkEffect(
    name="All Units 25% HP",
    type=CivVDeathLinkEffectType.all_units_hp,
    amount=25,
)
_ = CivVDeathLinkEffect(
    name="All Units 50% HP",
    type=CivVDeathLinkEffectType.all_units_hp,
    amount=50,
)
_ = CivVDeathLinkEffect(
    name="All Units 100% HP",
    type=CivVDeathLinkEffectType.all_units_hp,
    amount=100,
)
_ = CivVDeathLinkEffect(
    name="Random City 1 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=1,
)
_ = CivVDeathLinkEffect(
    name="Random City 3 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=3,
)
_ = CivVDeathLinkEffect(
    name="Random City 5 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=5,
)
_ = CivVDeathLinkEffect(
    name="Random City 10 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=10,
)
_ = CivVDeathLinkEffect(
    name="Random City 20 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=20,
)
_ = CivVDeathLinkEffect(
    name="Random City 40 Population",
    type=CivVDeathLinkEffectType.random_city_population,
    amount=40,
)
_ = CivVDeathLinkEffect(
    name="All Cities 1 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=1,
)
_ = CivVDeathLinkEffect(
    name="All Cities 3 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=3,
)
_ = CivVDeathLinkEffect(
    name="All Cities 5 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=5,
)
_ = CivVDeathLinkEffect(
    name="All Cities 10 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=10,
)
_ = CivVDeathLinkEffect(
    name="All Cities 20 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=20,
)
_ = CivVDeathLinkEffect(
    name="All Cities 40 Population",
    type=CivVDeathLinkEffectType.all_cities_population,
    amount=40,
)
_ = CivVDeathLinkEffect(
    name="Lose Random City",
    type=CivVDeathLinkEffectType.lose_random_city,
    amount=None,
)
_ = CivVDeathLinkEffect(
    name="Lose All Cities Not Capital",
    type=CivVDeathLinkEffectType.lose_all_cities_not_capital,
    amount=None,
)
_ = CivVDeathLinkEffect(
    name="Barbarians 3",
    type=CivVDeathLinkEffectType.barbarians,
    amount=3,
)
_ = CivVDeathLinkEffect(
    name="Barbarians 6",
    type=CivVDeathLinkEffectType.barbarians,
    amount=6,
)
_ = CivVDeathLinkEffect(
    name="Barbarians 9",
    type=CivVDeathLinkEffectType.barbarians,
    amount=9,
)
_ = CivVDeathLinkEffect(
    name="Barbarians 12",
    type=CivVDeathLinkEffectType.barbarians,
    amount=12,
)
_ = CivVDeathLinkEffect(
    name="Denounce 1",
    type=CivVDeathLinkEffectType.denounce,
    amount=1,
)
_ = CivVDeathLinkEffect(
    name="Denounce 3",
    type=CivVDeathLinkEffectType.denounce,
    amount=3,
)
_ = CivVDeathLinkEffect(
    name="Denounce 5",
    type=CivVDeathLinkEffectType.denounce,
    amount=5,
)
_ = CivVDeathLinkEffect(
    name="Declare War 1",
    type=CivVDeathLinkEffectType.denounce,
    amount=1,
)
_ = CivVDeathLinkEffect(
    name="Declare War 3",
    type=CivVDeathLinkEffectType.denounce,
    amount=3,
)
_ = CivVDeathLinkEffect(
    name="Declare War 5",
    type=CivVDeathLinkEffectType.declare_war,
    amount=5,
)
_ = CivVDeathLinkEffect(
    name="Lose Game",
    type=CivVDeathLinkEffectType.lose_game,
    amount=None,
)
