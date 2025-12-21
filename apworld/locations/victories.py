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
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Mining"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Rocketry"].name: 1,
                    items.TECH_ITEMS["Advanced Ballistics"].name: 1,
                    items.TECH_ITEMS["Particle Physics"].name: 1,
                    items.TECH_ITEMS["Satellites"].name: 1,
                    items.TECH_ITEMS["Nanotechnology"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Production"].name: 1,
                    items.PROGRESSIVE_TECH_ITEMS["Gold"].name: 6,
                    items.PROGRESSIVE_TECH_ITEMS["Science"].name: 9,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    "Culture": CivVLocationData(
        name="Culture",
        type=CivVLocationType.victory,
        game_id=3,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.POLICY_ITEMS["Aesthetics"].name: 1,
                    items.POLICY_ITEMS["Cultural Exchange"].name: 1,
                    items.POLICY_ITEMS["Aesthetics Finisher"].name: 1,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Drama and Poetry"].name: 1,
                    items.TECH_ITEMS["Acoustics"].name: 1,
                    items.TECH_ITEMS["Archaeology"].name: 1,
                    items.TECH_ITEMS["Radio"].name: 1,
                    items.TECH_ITEMS["The Internet"].name: 1,
                    items.TECH_ITEMS["Telecommunications"].name: 1,
                    items.TECH_ITEMS["Writing"].name: 1,
                    items.TECH_ITEMS["Education"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Culture"].name: 5,
                    items.PROGRESSIVE_TECH_ITEMS["Navy"].name: 8,
                    items.PROGRESSIVE_TECH_ITEMS["Science"].name: 2,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
    "Diplomatic": CivVLocationData(
        name="Diplomatic",
        type=CivVLocationType.victory,
        game_id=4,
        region=regions.INFORMATION_ERA,
        requirements=(
            items.ItemRequirements.create(
                items={
                    items.POLICY_ITEMS["Patronage"].name: 1,
                    items.POLICY_ITEMS["Philanthropy"].name: 1,
                    items.POLICY_ITEMS["Consulates"].name: 1,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.TECH_ITEMS["Animal Husbandry"].name: 1,
                    items.TECH_ITEMS["Currency"].name: 1,
                    items.TECH_ITEMS["Guilds"].name: 1,
                    items.TECH_ITEMS["Banking"].name: 1,
                    items.TECH_ITEMS["Economics"].name: 1,
                    items.TECH_ITEMS["Electricity"].name: 1,
                    items.TECH_ITEMS["Globalization"].name: 1,
                    items.TECH_ITEMS["Printing Press"].name: 1,
                    items.TECH_ITEMS["Optics"].name: 1,
                    items.TECH_ITEMS["Astronomy"].name: 1,
                },
                when={
                    "progressive_techs": False,
                }
            ) |
            items.ItemRequirements.create(
                items={
                    items.PROGRESSIVE_TECH_ITEMS["Gold"].name: 7,
                    items.PROGRESSIVE_TECH_ITEMS["Happiness"].name: 4,
                    items.PROGRESSIVE_TECH_ITEMS["Navy"].name: 4,
                },
                when={
                    "progressive_techs": True,
                }
            )
        )
    ),
}
"Dict of all victory locations"
