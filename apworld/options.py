# %% IMPORTS
from dataclasses import dataclass

from Options import Choice, DeathLink, DefaultOnToggle, PerGameCommonOptions, OptionCounter, Range, Toggle

from . import death_link, items

# All declaration
__all__ = ["CivVOptions"]


# %% OPTION CLASSES
class VictoryGoalLogic(Choice):
    """
    Which victory should be achievable before the game is considered beatable?

    Note that this solely affects progression logic. You can still beat the game earlier than expected or pursue a
    different victory if you so choose.

    Domination and Time victories are not included here as Domination can be achieved at any moment and Time has no
    requirements.

    """

    display_name = "Victory Goal Logic"
    option_none = 0
    option_science = 1
    option_culture = 3
    option_diplomatic = 4
    default = option_none


class EraGoalLogic(Choice):
    """
    Which era must be unlocked before the game is considered beatable?

    This is in addition to the value given for "Victory Goal Logic".
    Similarly, this solely affects progression logic.

    """

    display_name = "Era Goal Logic"
    option_ancient = 0
    option_classical = 1
    option_medieval = 2
    option_renaissance = 3
    option_industrial = 4
    option_modern = 5
    option_atomic = 6
    option_information = 7
    default = option_information


class EmbarkingGoalLogic(DefaultOnToggle):
    """
    Add Optics and Astronomy as requirements before the game is considered beatable.

    Similarly to other goal logic options, this solely affects progression logic.

    """

    display_name = "Embarking Goal Logic"


class PolicyCostModifier(Range):
    """
    Multiplies the base cost of adopting social policies with the given percentage.

    """

    display_name = "Policy Cost Modifier"
    range_start = 0
    range_end = 1000
    default = 90


class TechCostModifier(Range):
    """
    Multiplies the base cost of researching technologies with the given percentage.

    """

    display_name = "Tech Cost Modifier"
    range_start = 0
    range_end = 1000
    default = 100


class ProgressiveTechs(DefaultOnToggle):
    """
    Use progressive technologies.

    Progressive technologies divides all 79 technologies (excl. Agriculture) into 11 categories.
    This makes the unlocking of technologies feel less chaotic and more streamlined compared to true random
    technologies. It also makes it far less likely to not have important early-era buildings in the mid to late game.

    """

    display_name = "Progressive Techs"


class ItemHints(Choice):
    """
    Enable item hints for all locations.

    Options are:
    - full: Locations state their exact item.
    - classification: Locations state the classification of their item (progression; useful; filler; trap).
    - none: Locations do not state their item.

    """

    display_name = "Item Hints"
    option_full = 0
    option_classification = 1
    option_none = 2
    default = option_classification


class DisguiseTraps(Toggle):
    """
    Item classification hints will classify traps as progression items.

    Keep in mind that if item hints are set to 'full', the name of the trap is still visible and could potentially spoil
    you of the true nature of the item.

    Has no effect if item hints are set to 'none'.

    """

    display_name = "Disguise Traps"


class SatellitesMeetsAll(Toggle):
    """
    Receiving the Satellites technology will also meet all civilizations and city-states.

    """

    display_name = "Satellites Meets All"


class BuildingSanity(Toggle):
    """
    Add most standard buildings to the location pool.

    This adds 53 buildings to the location pool in total.

    Buildings that will not be added:
    - Palace
    - Courthouse
    - Any religious building (Cathedral; Monastery; Mosque; and Pagoda)
    - Any civilization-unique building (they count as the building they replace instead)
    - Any National Wonder (see National Wonder Sanity instead)
    - Any World Wonder (see World Wonder Sanity instead)

    """

    display_name = "Building Sanity"


class NationalWonderSanity(Toggle):
    """
    Add all national wonders to the location pool.

    This adds the 11 national wonders and the 3 guilds to the location pool.

    """

    display_name = "National Wonder Sanity"


class WorldWonderSanity(Toggle):
    """
    Add all world wonders to the location pool.

    This adds the 47 world wonders to the location pool, including the 3 ideology world wonders.

    WARNING: This option is NOT suitable for syncs.

    """

    display_name = "World Wonder Sanity"


class UnitSanity(Toggle):
    """
    Add most standard units to the location pool.

    This adds 66 units to the location pool in total.

    Units that will not be added:
    - Foreign Legion
    - Dromon (exclusive to Byzantium; does not replace a standard unit)
    - Any religious unit (Inquisitor and Missionary)
    - Any civilization-unique unit (they count as the unit they replace instead)
    - Any Great Person
    - Any Spaceship unit (SS Booster; SS Cockpit; SS Engine; and SS Stasis Chamber)

    """

    display_name = "Unit Sanity"


class SettlerSanity(Toggle):
    """
    Adds Settlers to the item and location pools, with the amount being determined by the Settler Sanity Amount option.

    When enabled, Settlers can only be obtained as a progressive item. Training them counts as a location, up to the
    amount, after which they can no longer be trained. When receiving a Settler as an item, they spawn near the capital
    (or a different city if you happen to not have one).

    Enabling this option will remove the Settler from the Unit Sanity location pool, if it is enabled.

    """

    display_name = "Settler Sanity"


class SettlerSanityAmount(Range):
    """
    Number of Settlers to put in the item and location pools.

    Progression logic will expect you to be able to get the following number of Settlers per era:
    - Ancient: 1
    - Classical; Medieval; and Renaissance: 2
    - Industrial; Modern; and Atomic: 3
    - Information: 4

    Has no effect if Settler Sanity is not enabled.

    NOTE: The lower limit being 0 is not a mistake. If you want to be Venice as a different civilization, be my guest.

    """

    display_name = "Settler Sanity Amount"
    range_start = 0
    range_end = 20
    default = 10


class PromotionSanity(Toggle):
    """
    Add all earnable unit promotions (excl. Heal Instantly) to the item and location pools.

    This adds 83 promotions to the item and location pools in total.

    WARNING: This option can cause situations where you need to level up many units types to find logical progression.

    """

    display_name = "Promotion Sanity"


class FillerItemWeights(OptionCounter):
    """
    The weights of each filler item to be chosen when a filler item is required.

    """

    display_name = "Filler Item Weights"
    min = 0
    cull_zeroes = True
    valid_keys = [x.name for x in items.FILLER_ITEMS]
    default = {x.name: x.weight for x in items.FILLER_ITEMS}


class EnableTraps(Toggle):
    """
    Add traps to the filler item pool.

    """

    display_name = "Enable Traps"


class TrapFillerChance(Range):
    """
    The percent chance for a filler item to be a trap instead.

    Has no effect if traps are not enabled.

    """

    display_name = "Trap Filler Chance"
    range_start = 0
    range_end = 100
    default = 5


class TrapItemWeights(OptionCounter):
    """
    The weights of each trap to be chosen when a trap item is required.

    Has no effect if traps are not enabled.

    """

    display_name = "Trap Item Weights"
    min = 0
    cull_zeroes = True
    valid_keys = [x.name for x in items.TRAP_ITEMS]
    default = {x.name: x.weight for x in items.TRAP_ITEMS}


class DeathLinkTrigger(Choice):
    """
    What triggers a death link to be sent?

    Has no effect if death link is disabled.

    Possible triggers:
    - Unit killed: When any of your units gets killed.
    - City captured: When any of your cities gets captured.
    - Capital captured: When your capital gets captured.
    - Game lost: When you lose a game.

    """

    display_name = "Death Link Trigger"
    option_unit_killed = 0
    option_city_captured = 1
    option_capital_captured = 2
    option_game_lost = 3
    default = option_game_lost


class DeathLinkEffect(Choice):
    """
    What effect occurs when a death link is received?

    Has no effect if death link is disabled.

    Possible effects:
    - Random unit HP: A random unit loses X HP.
    - All units HP: All units lose X HP.
    - Random city population: A random city loses X population.
    - All city population: All cities lose X population.
    - Random city: Lose a random non-capital city.
    - All cities not capital: Lose all cities that are not your capital.
    - Barbarians: Spawn X random Barbarians.
    - Denounce: X random civilizations denounce you.
    - Declare war: X random civilizations declare war on you.
    - Lose game: Lose the game immediately.

    """

    display_name = "Death Link Effect"
    option_random_unit_hp = 0
    option_all_units_hp = 1
    option_random_city_population = 2
    option_all_cities_population = 3
    option_random_city = 4
    option_all_cities_not_capital = 5
    option_barbarians = 6
    option_denounce = 7
    option_declare_war = 8
    option_lose_game = 9
    default = option_random_unit_hp


class DeathLinkEffectWeights(OptionCounter):
    """
    The weights of each death link to be chosen when a death link is received.

    Has no effect if death link is not enabled.

    """

    display_name = "Death Link Effect Weights"
    min = 0
    cull_zeroes = True
    valid_keys = [x.name for x in death_link.DEATH_LINK_EFFECTS]
    default = {x.name: 1 if not i else 0 for i, x in enumerate(death_link.DEATH_LINK_EFFECTS)}


# %% CIV V OPTIONS CLASS
@dataclass
class CivVOptions(PerGameCommonOptions):
    victory_goal_logic: VictoryGoalLogic
    era_goal_logic: EraGoalLogic
    embarking_goal_logic: EmbarkingGoalLogic
    policy_cost_modifier: PolicyCostModifier
    tech_cost_modifier: TechCostModifier
    progressive_techs: ProgressiveTechs
    item_hints: ItemHints
    disguise_traps: DisguiseTraps
    satellites_meets_all: SatellitesMeetsAll
    building_sanity: BuildingSanity
    national_wonder_sanity: NationalWonderSanity
    world_wonder_sanity: WorldWonderSanity
    unit_sanity: UnitSanity
    settler_sanity: SettlerSanity
    settler_sanity_amount: SettlerSanityAmount
    promotion_sanity: PromotionSanity
    filler_item_weights: FillerItemWeights
    enable_traps: EnableTraps
    trap_filler_chance: TrapFillerChance
    trap_item_weights: TrapItemWeights
    death_link: DeathLink
    death_link_trigger: DeathLinkTrigger
    death_link_effect_weights: DeathLinkEffectWeights
