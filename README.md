# Archipelago for Civilization V

## Required Software

- Civilization V on the Steam store with both Gods & Kings and Brave New World Expansions. Other versions will not work due to adjustments the expansions made to the base game.
- [Civilization V AP World and Mod](https://github.com/1313e/Civ-V-AP-World/releases)

## Setup
- Download the latest APWorld and APMod from the [releases](https://github.com/1313e/Civ-V-AP-World/releases) page.
- Install the APWorld by double-clicking it or copying it over yourself to the `custom_worlds` folder in AP.
- Unzip the APMod and paste the mod folder (the one that ends with `(v XXX)`) into the Civ V mods folder in the `~/Documents/My Games/Sid Meier's Civilization 5/MODS` folder.
- Open the config file at `~/Documents/My Games/Sid Meier's Civilization 5/config.ini` and set the value of `EnableTuner` to `1`.
  This only needs to be done once.
  - NOTE: Enabling the FireTuner disables achievements, so if you wish to play Civ V with achievements in between AP sessions, make sure to disable this and re-enable it later.

## Joining a MultiWorld Game
- Open the `Civ V Client` from Archipelago Launcher and connect to your slot.
  The client will start echoing that it is waiting for Civ V to be ready.
- Open Civ V and make sure to enable and load the `CivVAPMod` via the "Mods" menu first, and then click "Singleplayer" (which should be the only option you get besides "Back").
- Set up your singleplayer game and start it.
- Once you are in-game, the client will stop echoing that it is waiting for the game to be ready, indicating that the two are connected.
- Start playing. :)

## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options. 

### Where do I get a YAML file?
In the Archipelago Launcher, use the `Generate Template Options` and select the `Civilization V.yaml` file in the folder that opens.
If it is not there, then the APWorld is not installed correctly.


## Known issues
- Receiving a policy as an item will very briefly show the "Free Policy" notification.
  This notification stays (and is not true) if you happened to receive one on the same turn as you can adopt an AP policy.
  It is sadly not possible to fix this.

If you find any other ones, please post a message in the [AP Discord](https://discord.com/channels/731205301247803413/1342924294757552229) and ping me (@1313e) in the message.


## Future implementation/improvement ideas
Some ideas I currently have that I want to look into (in order of priority):
- Adding ability to add a specific required victory to the AP. Adding logic for all victory conditions.
- Creating a Poptracker pack for the AP.
- Allowing certain technologies to be forced early. For example, Mining; Trapping; and Calendar are kinda critical and I would assume you want them somewhat early.
- Adding a bunch of additional stuff to the checks list: Culture; eras; city-states; trade routes; barbarian camps; etc.
