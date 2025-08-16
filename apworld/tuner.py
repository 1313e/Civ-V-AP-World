# %% IMPORTS
import asyncio
import json
import re
import socket
from typing import Any

from CommonClient import logger

from .exceptions import (
    TunerConnectionException,
    TunerErrorException,
    TunerException,
    TunerRuntimeException,
    TunerTimeoutException,
)

# All declaration
__all__ = ["Tuner"]


# %% FUNCTION DEFINITIONS
class Tuner:
    """
    Interface class that mimics the behavior of the Civ V Firetuner and allows the Civ V AP Client to interact with the
    game.

    """

    # Class attributes
    RESPONSE_PATTERN: re.Pattern = re.compile(r"APSTART:(.*?):APEND")
    "Regex pattern to use for extracting responses given by the Civ V AP mod to this Tuner"
    READY_CHECK_COMMAND_STRINGS: tuple[bytes, bytes] = (
        b"\x05\x00\x00\x00\x04\x00\x00\x00APP:\x00",
        b"\x05\x00\x00\x00\x00\x00\x00\x00LSQ:\x00",
    )
    "Tuple of specific command strings that must be sent to the game to check whether it is ready to be interacted with"

    def __init__(self):
        # Define instance attributes
        self._sock: socket.socket | None = None
        "The socket to use for the connection to Civ V"

    @property
    def sock(self) -> socket.socket:
        """
        The socket to use for the connection to Civ V.

        """

        return self._sock

    @sock.setter
    def sock(self, sock: socket.socket) -> None:
        self._sock = sock

    async def _retrieve_response(self, size: int) -> bytes:
        """
        Retrieves a response from the Civ V socket `sock` of up to `size` bytes and returns it.

        """

        return await asyncio.wait_for(asyncio.get_event_loop().sock_recv(self._sock, size), 2.0)

    @classmethod
    def _parse_response(cls, response: bytes) -> dict[str, Any]:
        """
        Parses the given `response` coming from the Civ V socket and returns the result.

        If any error occurred in the response, the appropriate exception will be raised.

        Args:
            response: The response from the Civ V socket.

        Returns:
            str: The parsed response from the Civ V socket.

        Raises:
            TunerErrorException: If an unexpected error occurred during the processing of the command.
            TunerRuntimeException: If a runtime error occurred during the processing of the command.

        """

        # Decode the given response to a normal string
        decoded_response = ''.join(chr(b) if 32 <= b < 127 else '' for b in response)

        # Check whether there is an AP-specific section in this response
        match = re.search(cls.RESPONSE_PATTERN, decoded_response)
        if match is not None:
            return json.loads(match.group(1))

        # If there is no match, check if an error occurred instead. If not, return nothing
        if "ERR:Runtime Error" in decoded_response:
            raise TunerRuntimeException(decoded_response.replace("?", ""))
        elif "ERR:" in decoded_response:
            raise TunerErrorException(decoded_response.replace("?", ""))
        else:
            return {}

    async def _send_commands(self, *command_strings: bytes, size: int) -> dict[str, Any]:
        """
        Sends the given `command_strings` to the game; parses the response and returns it.

        Args:
            command_strings: The commands to send.
            size: The size of the response to retrieve.

        Returns:
            dict[str, Any]: The parsed response from the Civ V socket.

        Raises:
            TunerErrorException: If an unexpected error occurred during the processing of the command.
            TunerRuntimeException: If a runtime error occurred during the processing of the command.

        """

        # Try to send the commands to the tuner
        logger.debug(f"Sending command strings: {b','.join(command_strings)}")
        try:
            # Send the commands
            for command_string in command_strings:
                await asyncio.get_event_loop().sock_sendall(self._sock, command_string)
            await asyncio.sleep(0.2)

            # Retrieve and parse the response
            response = self._parse_response(await self._retrieve_response(size))
            logger.debug(f"Received data: {response}")
            return response

        # Deal with any specific errors that may have occurred during the retrieval and parsing of the response
        except TimeoutError:
            logger.debug('Timeout while receiving data')
            raise TunerTimeoutException
        except ConnectionError:
            logger.debug('Connection error while receiving data')
            raise TunerConnectionException
        except TunerException as e:
            logger.debug(f'Error occurred while receiving data: {str(e)}')
            raise

        # If no tuner-specific exception occurred, then the exception was unhandled.
        # This should never be hit, but is here to avoid the tuner (and thus the client) to crash entirely in case it
        # does happen
        except Exception as e:
            logger.debug(f'Unhandled error occurred while receiving data: {str(e)}')
            raise TunerException(e)

    async def _send_mod_command(self, command: str, size: int = 4 * 1024) -> dict[str, Any]:
        """
        Sends the given `command` provided by the Civ V AP mod to the game and returns the response.

        Args:
            command: The command to send.
            size: The size of the response to retrieve.

        Returns:
            dict[str, Any]: The parsed response from the Civ V socket.

        Raises:
            TunerErrorException: If an unexpected error occurred during the processing of the command.
            TunerRuntimeException: If a runtime error occurred during the processing of the command.

        """

        # Build up the command message to send
        message = b"CMD:0:" + f"GameCore.Game.AP.{command}".encode("utf-8") + b"\x00"
        message_length = len(message).to_bytes(1, byteorder='little')
        command_string = message_length + b"\x00\x00\x00\x03\x00\x00\x00" + message

        # Send the command
        logger.debug(f"Sending command: {command}")
        return await self._send_commands(command_string, size=size)

    async def send_ready_check(self) -> bool:
        """
        Sends a ready check to the game to verify that the game is currently connected and listening, and returns the
        result.

        This function acts as a connection enforcer: It sends the game the command to specifically start listening to
        the registered socket and drop all other connections, if any. This function only fails if the game is currently
        unable to fulfill this request.

        """

        # Send ready check to the game
        try:
            _ = await self._send_commands(*self.READY_CHECK_COMMAND_STRINGS, size=20 * 1024)

        # If this request times out, then the ready check failed
        except TunerTimeoutException:
            return False

        # Else, the ready check succeeded
        else:
            return True

    async def is_mod_ready(self) -> bool:
        """
        Returns whether the AP mod is currently loaded and ready.

        """

        # Request execution of the "IsModReady" function that is defined by the AP mod
        # Use a very large response size to flush anything unrelated to AP that is still waiting on the socket
        try:
            return (await self._send_mod_command("IsModReady()", size=100 * 1024)).get("ready", False)

        # If the function cannot be found (runtime error) or the request times out, the mod is not ready
        except (TunerRuntimeException, TunerTimeoutException):
            return False

    async def grant_policies(self, *policy_ids: int) -> None:
        """
        Grants the policies with the given `policy_ids` to the player.

        """

        # Grant all policies in batches of 10
        for i in range(0, len(policy_ids), 10):
            await self._send_mod_command(f"GrantPolicies({{{','.join(map(str, policy_ids[i:i+10]))}}})")

    async def unlock_policy_branches(self, *policy_branch_ids: int) -> None:
        """
        Unlocks the policy branches with the given `policy_branch_ids` for the player.

        """

        await self._send_mod_command(f"UnlockPolicyBranches({{{','.join(map(str, policy_branch_ids))}}})")

    async def grant_techs(self, *tech_ids: int) -> None:
        """
        Grants the technologies with the given `tech_ids` to the player.

        """

        # Grant all techs in batches of 10
        for i in range(0, len(tech_ids), 10):
            await self._send_mod_command(f"GrantTechs({{{','.join(map(str, tech_ids[i:i+10]))}}})")

    async def change_gold(self, value: int) -> None:
        """
        Changes the gold value by the given `value`.

        """

        await self._send_mod_command(f"ChangeGold({value})")

    async def change_culture(self, value: int) -> None:
        """
        Changes the culture value by the given `value`.

        """

        await self._send_mod_command(f"ChangeCulture({value})")

    async def change_faith(self, value: int) -> None:
        """
        Changes the faith value by the given `value`.

        """

        await self._send_mod_command(f"ChangeFaith({value})")

    async def change_free_great_people(self, value: int) -> None:
        """
        Changes the number of free great people by the given `value`.

        """

        await self._send_mod_command(f"ChangeNumFreeGreatPeople({value})")

    async def change_free_policies(self, value: int) -> None:
        """
        Changes the number of free policies by the given `value`.

        """

        await self._send_mod_command(f"ChangeNumFreePolicies({value})")

    async def change_free_techs(self, value: int) -> None:
        """
        Changes the number of free technologies by the given `value`.

        """

        await self._send_mod_command(f"ChangeNumFreeTechs({value})")

    async def change_all_city_population(self, value: int) -> None:
        """
        Changes the number of population in all cities by the given `value`.

        """

        await self._send_mod_command(f"ChangeAllCityPopulation({value})")

    async def change_new_city_extra_population(self, value: int) -> None:
        """
        Changes the number of extra population for new cities by the given `value`.

        """

        await self._send_mod_command(f"ChangeNewCityExtraPopulation({value})")

    async def change_culture_per_turn_for_free(self, value: int) -> None:
        """
        Changes the amount of free culture per turn by the given `value`.

        """

        await self._send_mod_command(f"ChangeCulturePerTurnForFree({value})")

    async def change_extra_happiness_per_city(self, value: int) -> None:
        """
        Changes the amount of extra happiness per city by the given `value`.

        """

        await self._send_mod_command(f"ChangeExtraHappinessPerCity({value})")

    async def start_golden_age(self, value: int) -> None:
        """
        Starts a golden age for the player `value` times.

        """

        await self._send_mod_command(f"StartGoldenAge({value})")

    async def denounce_random(self, value: int) -> None:
        """
        Denounces `value` times the player by an AI player at random.

        """

        await self._send_mod_command(f"DenounceRandom({value})")

    async def declare_war_random(self, value: int) -> None:
        """
        Declares `value` times a war on the player's team at random.

        """

        await self._send_mod_command(f"DeclareWarRandom({value})")

    async def get_push_table(self) -> dict[str, Any]:
        """
        Returns the push table managed by the APMod containing requests made by the game to the client.

        """

        return await self._send_mod_command("GetPushTable()")
