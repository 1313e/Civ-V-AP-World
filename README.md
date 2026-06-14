# Archipelago for Civilization V

## Required Software

- Civilization V on the Steam store with both Gods & Kings and Brave New World Expansions. Other versions will not work due to adjustments the expansions made to the base game.
- [Civilization V AP World](https://github.com/1313e/Civ-V-AP-World/releases)
- OPTIONAL: [Civilization V AP PopTracker Pack](https://github.com/Sparky5000/Civ5APpoptracker/releases)


## Setup
- Download the latest APWorld from the [releases](https://github.com/1313e/Civ-V-AP-World/releases) page.
- Install the APWorld by double-clicking it or copying it over yourself to the `custom_worlds` folder in `Archipelago`.
- Open the config file at `~/Documents/My Games/Sid Meier's Civilization 5/config.ini` and set the value of `EnableTuner` to `1`.
  This only needs to be done once.
  - NOTE: Enabling the FireTuner disables achievements, so if you wish to play Civ V with achievements in between AP sessions, make sure to disable this and re-enable it later.


## Joining a MultiWorld Game
- Download the patch file for your Civ V slot and open it with the `Archipelago Launcher`. When playing Archipelago locally, the patch file will be inside the generated ZIP that you use to host locally. Extract the ZIP to get access to the patch file.
  - If this is your first time opening a Civ V patch file, the launcher will ask you to provide the location of your Civ V mods folder.
    By default, this should be `~/Documents/My Games/Sid Meier's Civilization 5/MODS`, but it can be a different folder for some installations, including OneDrive folders if you use automated cloud storage.
    NOTE: It will not be in the Steam installation folder.
- Opening the patch file as stated above also automatically opens the `Civ V Client` for you.
  The client will start echoing that it is waiting for Civ V to be ready.
- Open Civ V and make sure to enable and load the `CivVAPMod` via the "Mods" menu first, and then click "Single Player" (which should be the only option you get besides "Back").
  - The small subtitle of the mod should be the same as the name of the patch file you downloaded/extracted.
- Set up your singleplayer game and start it.
- Once you are in-game, you will get two notifications: The first indicating that the `CivVAPMod` itself is loaded and the second indicating that it has successfully connected to the `Civ V Client`.
- Start playing. :)


## Troubleshooting

### WTF is a "Snack from Thes"?
This filler item gives you 200 Gold; 200 Culture; and 100 Faith.
Unlike all other items in the game, this one breaks naming convention and instead is named after my sister, who requested an item to be named after her.
It has a higher chance of appearing compared to other similar filler items.

### There is no patch file
Patch files for Civ V AP were introduced in v0.8.0.
If you get no patch file, then the version of the APWorld used to generate the multiworld is older than that.
Make sure you use the most recent version from the [releases](https://github.com/1313e/Civ-V-AP-World/releases) page.

### Civ V Client keeps echoing "Waiting for Civ V to start..."
Either the `EnableTuner` in the Civ V config file (see `Setup` above) is not set to `1` or the FireTuner program from the Civ V SDK is currently running.
Make sure both of these potential issues are fixed.

### Civ V Client keeps echoing "Waiting for Civ V AP Mod to be ready..."
The Civ V AP Mod is currently not loaded, and therefore not responding to the client.
In Civ V, mods are only loaded during the load screen when starting an actual game.
Make sure that, starting from the game's main menu, you go:

- Mods
- Accept
- *Enable correct version of `CivVAPMod`*
- Next (should show `CivVAPMod` being in use on this screen)
- Single Player
- *When starting a new game*:
  - Set Up Game
  - Start Game
  - Begin Your Journey
- *When loading a game*:
  - Load Game
  - Load Game
  - Continue Your Journey

Only after this final click on `Begin Your Journey` (or `Continue Your Journey` if loading a save file), does the mod actually become active for the client.

### Civ V Client keeps echoing "Loaded Civ V AP Mod does not match the ID of the connected slot"
This happens when the slot your `Civ V Client` is connected to (so, the room port plus slot name) is not the same slot as the one whose patch file you opened to get the `CivVAPMod` version you have loaded currently.
In other words, you are using a version of the `CivVAPMod` meant for a different slot or maybe a different Archipelago entirely.
Make sure you get the proper patch file for the slot you wish to play.
Remember that the subtitle (called a teaser in Civ V) of the correct `CivVAPMod` will be exactly the same as the name of the patch file it belongs to.

### Civ V crashes the moment the game is loaded
There can be several reasons for this, but the vast majority of them are due to either of the following two:

- You are not running Civ V with both Gods & Kings and Brave New World DLCs installed, plus all Civilization packs.
  Make sure they are all installed and that the version of Civ V is `1.0.3.279` (shown on the main menu at the bottom).
- You have other mods currently active that interfere with the `CivVAPMod`.
  Given that the `CivVAPMod` modifies almost all databases in Civ V, most mods will not work together with it.
  The `CivVAPMod` is meant to be an Archipelago version of vanilla Civ V and thus no compatibility with any mod will be taken into account.
  If you do find a mod that is compatible, then this will be a coincidence and this may change very well in the future.

If you checked that neither of the above reasons are the cause for the crashing of the game, please reach out to me (@1313e) on the [AP Discord](https://discord.com/channels/731205301247803413/1342924294757552229) and I will try to help.


## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options. 

### Where do I get a YAML file?
In the `Archipelago Launcher`, use the `Generate Template Options` and select the `Civilization V.yaml` file in the folder that opens.
If it is not there, then the APWorld is not installed correctly.

## Notes on logic
Logic in Civ V is a bit strange, as the soft requirements to perform specific actions in vanilla Civ V depends on the state of the game.
To allow for a fair, but not tedious challenge, the following logic requirements exist within this AP implementation.
Note that these are not enforced, but are purely here to avoid putting you in a situation where getting locations or a victory can be very tedious.
All locations and victory itself can, theoretically, be obtained without ever receiving a single item.


### Victories
- Science (if victory goal logic is set to Science). Focuses on building the Space Station:
  - Tech: Mining (*mining Aluminum*)
  - Tech: Electricity (*reveals Aluminum*)
  - Tech: Ecology (*Recycling Center*)
  - Tech: Rocketry (*Apollo Program*)
  - Tech: Advanced Ballistics (*SS Booster*)
  - Tech: Particle Physics (*SS Engine*)
  - Tech: Satellites (*SS Cockpit*)
  - Tech: Nanotechnology (*SS Stasis Chamber*)

- Culture (if victory goal logic is set to Culture). Focuses on getting Tourism easily:
  - Policy Branch: Aesthetics (*earn Great Writers/Artists/Musicians faster*)
  - Policy Branch Finisher: Aesthetics (*doubles theming bonus*)
  - Policy: Cultural Exchange (*increases Tourism modifier*)
  - Tech: Drama and Poetry (*Amphitheater* and *Writers' Guild*)
  - Tech: Acoustics (*Opera House* and *Musicians' Guild*)
  - Tech: Archaeology (*Museum* and *Archaeologists*)
  - Tech: Guilds (*Artists' Guild*)
  - Tech: Refrigeration (*Hotel*)
  - Tech: Radio (*Broadcast Tower*)
  - Tech: The Internet (*doubles Tourism*)
  - Tech: Telecommunications (*National Visitor's Center* and *CN Tower*)
  - Tech: Writing (*Library required for University*)
  - Tech: Education (*University required for Archaeologists*)

- Diplomatic (if victory goal logic is set to Diplomatic). Focuses on befriending City-States, mostly with gold:
  - Policy Branch: Patronage (*Influence decreases slower*)
  - Policy: Philanthropy (*Gifts generate more Influence*)
  - Policy: Consulates (*Higher Influence resting point*)
  - Tech: Animal Husbandry (*Caravan*)
  - Tech: Currency (*Market*)
  - Tech: Guilds (*Trading Post* and *East India Company*)
  - Tech: Banking (*Bank*)
  - Tech: Economics (*increases Gold yield in tile improvements*)
  - Tech: Electricity (*Stock Exchange*)
  - Tech: Globalization (*Additional delegates for diplomats*)
  - Tech: Printing Press (*unlocks World Congress*)
  - Tech: Optics (*sea embarking*)
  - Tech: Astronomy (*ocean embarking*)
  - Era: Information (*unlocks United Nations*)


### Technology locations
- Classical & Medieval Era:
  - Tech: Writing (*Library*)

- Renaissance & Industrial Era:
  - Tech: Writing (*Library*)
  - Tech: Education (*University*)

- Modern & Atomic Era:
  - Tech: Writing (*Library*)
  - Tech: Education (*University*)
  - Tech: Scientific Theory (*Public School*)

- Information Era:
  - Tech: Writing (*Library*)
  - Tech: Education (*University*)
  - Tech: Scientific Theory (*Public School*)
  - Tech: Plastics (*Research Lab*)


### Policy locations
- Classical & Medieval Era:
  - Tech: Drama and Poetry (*Amphitheater*)

- Renaissance & Industrial Era:
  - Tech: Drama and Poetry (*Amphitheater*)
  - Tech: Acoustics (*Opera House*)

- Modern & Atomic Era:
  - Tech: Drama and Poetry (*Amphitheater*)
  - Tech: Acoustics (*Opera House*)
  - Tech: Archaeology (*Museum*)

- Information Era:
  - Tech: Drama and Poetry (*Amphitheater*)
  - Tech: Acoustics (*Opera House*)
  - Tech: Archaeology (*Museum*)
  - Tech: Radio (*Broadcast Tower*)

## Known issues
- Receiving a policy as an item will very briefly show the "Free Policy" notification.
  This notification stays (and is not true) if you happened to receive one on the same turn as you can adopt an AP policy.
  It is sadly not possible to fix this.

If you find any other ones, please post a message in the [AP Discord](https://discord.com/channels/731205301247803413/1342924294757552229) and ping me (@1313e) in the message.
