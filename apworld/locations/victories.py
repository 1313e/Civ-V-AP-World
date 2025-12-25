# %% IMPORTS
from .core import CivVLocationData
from .. import items, regions
from ..enums import CivVLocationType

# All declaration
__all__ = [
    "VICTORY_LOCATIONS",
]


# %% LOCATION DECLARATIONS
VICTORY_LOCATIONS = {
    "Science": CivVLocationData(
        name="Science",
        type=CivVLocationType.victory,
        game_id=1,
        requirements=items.ItemRequirements(
            progression={
                items.TECH_ITEMS["Mining"],
                items.TECH_ITEMS["Electricity"],
                items.TECH_ITEMS["Ecology"],
                items.TECH_ITEMS["Rocketry"],
                items.TECH_ITEMS["Advanced Ballistics"],
                items.TECH_ITEMS["Particle Physics"],
                items.TECH_ITEMS["Satellites"],
                items.TECH_ITEMS["Nanotechnology"],
            },
        )
    ),
    "Culture": CivVLocationData(
        name="Culture",
        type=CivVLocationType.victory,
        game_id=3,
        requirements=items.ItemRequirements(
            progression={
                items.POLICY_ITEMS["Aesthetics"],
                items.POLICY_ITEMS["Cultural Exchange"],
                items.POLICY_ITEMS["Aesthetics Finisher"],
                items.TECH_ITEMS["Drama and Poetry"],
                items.TECH_ITEMS["Acoustics"],
                items.TECH_ITEMS["Archaeology"],
                items.TECH_ITEMS["Refrigeration"],
                items.TECH_ITEMS["Radio"],
                items.TECH_ITEMS["The Internet"],
                items.TECH_ITEMS["Telecommunications"],
                items.TECH_ITEMS["Writing"],
                items.TECH_ITEMS["Education"],
            },
        )
    ),
    "Diplomatic": CivVLocationData(
        name="Diplomatic",
        type=CivVLocationType.victory,
        game_id=4,
        region=regions.INFORMATION_ERA,
        requirements=items.ItemRequirements(
            progression={
                items.POLICY_ITEMS["Patronage"],
                items.POLICY_ITEMS["Philanthropy"],
                items.POLICY_ITEMS["Consulates"],
                items.TECH_ITEMS["Animal Husbandry"],
                items.TECH_ITEMS["Currency"],
                items.TECH_ITEMS["Guilds"],
                items.TECH_ITEMS["Banking"],
                items.TECH_ITEMS["Economics"],
                items.TECH_ITEMS["Electricity"],
                items.TECH_ITEMS["Globalization"],
                items.TECH_ITEMS["Printing Press"],
                items.TECH_ITEMS["Optics"],
                items.TECH_ITEMS["Astronomy"],
            },
        )
    ),
}
"Dict of all victory locations"
