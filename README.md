# Setup Guide for Civilization V

**Civilization V ap world is in the very early stages of testing an may be unstable.**

## Required Software

- Civilization V on the Steam store with both Gods & Kings and Brave New World Expansions.
- Other versions of Civilization V have not been tested.
- [Civilization V AP World and Mod](https://github.com/battary/Civ-V-AP-World/releases)

## Setup
- Download latest .zip file and extract all files
- Install the ap world in the custom worlds folder
- Take the Civ V mod and paste the mod folder into the Civ V mods folder in the Documents\My Games\Sid Meier's Civilization 5\MODS folder
- Open the config file at Documents\My Games\Sid Meier's Civilization 5\config and enable the fire tuner
    - The first option should be labeled "EnableTuner" change the 0 value to 1. Note: This will disable achievments.


## Configuring your YAML file

### What is a YAML file and why do I need one?

Your YAML file contains a set of configuration options which provide the generator with information about how it should
generate your game. Each player of a multiworld will provide their own YAML file. This setup allows each player to enjoy
an experience customized for their taste, and different players in the same multiworld can all have different options. 

### Where do I get a YAML file?
In the archipelago launcher use the generate template options and select the Civilization V yaml. 

## Joining a MultiWorld Game

**IMPORTANT: DO NOT OPEN THE CIVV CLIENT UNTIL YOU'VE LOADED INTO A GAME AND HAVE ESTABLISHED YOUR FIRST CITY!!!** 
  - If you're not sending or recieving checks, follow these steps. *Looking into possible fix*
    1. Close the CivV Client.
    2. Open and close your social policy menu.
    3. Reopen the CivV client and reconnect to the archipelago server using the address and port numbers.

To connect the client to the multiserver simply put `<address>:<port>` on the textfield on top and press enter (if the
server uses password, type in the bottom textfield `/connect <address>:<port> [password]`)




