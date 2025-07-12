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
    RESPONSE_PATTERN: re.Pattern = re.compile(r"APSTART:(.*):APEND")
    "Regex pattern to use for extracting responses given by the Civ V AP mod to this Tuner"
    READY_CHECK_COMMAND_STRINGS: tuple[bytes, bytes] = (
        b"\x05\x00\x00\x00\x04\x00\x00\x00APP:\x00",
        b"\x05\x00\x00\x00\x00\x00\x00\x00LSQ:\x00",
    )
    "Tuple of specific command strings that must be sent to the game to check whether it is ready to be interacted with"

    @staticmethod
    async def _retrieve_response(sock: socket.socket, size: int) -> bytes:
        """
        Retrieves a response from the Civ V socket `sock` of up to `size` bytes and returns it.

        """

        return await asyncio.wait_for(asyncio.get_event_loop().sock_recv(sock, size), 2.0)

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

    async def _send_commands(
            self, *command_strings: bytes, sock: socket.socket, loop: asyncio.AbstractEventLoop, size: int
    ) -> dict[str, Any]:
        """
        Sends the given `command_strings` to the game; parses the response and returns it.

        Args:
            command_strings: The commands to send.
            sock: The socket to send the command to.
            loop: The asyncio event loop.
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
                await loop.sock_sendall(sock, command_string)
            await asyncio.sleep(0.2)

            # Retrieve and parse the response
            response = self._parse_response(await self._retrieve_response(sock, size))
            logger.debug(f"Received data: {response}")
            return response

        # Deal with any specific errors that may have occurred during the retrieval and parsing of the response
        except TimeoutError:
            logger.debug('Timeout while receiving data')
            raise TunerTimeoutException
        except ConnectionError:
            logger.debug('Connection error while receiving data')
            raise TunerConnectionException
        except TunerException:
            logger.debug(f'Error occurred while receiving data')
            raise

        # If no tuner-specific exception occurred, then the exception was unhandled.
        # This should never be hit, but is here to avoid the tuner (and thus the client) to crash entirely in case it
        # does happen
        except Exception as e:
            logger.debug(f'Unhandled error occurred while receiving data: {str(e)}')
            raise TunerException(e)

    async def send_ready_check(self, sock: socket.socket, loop: asyncio.AbstractEventLoop) -> None:
        """
        Sends a ready check to the game to verify that the game is currently connected and listening to the given
        `sock`.

        This function acts as a connection enforcer: It sends the game the command to specifically start listening to
        the given `sock` and drop all other connections, if any. This function only fails if the game is currently
        unable to fulfill this request.

        Args:
            sock: The socket to send the command to.
            loop: The asyncio event loop.

        Raises:
            TunerErrorException: If an unexpected error occurred during the processing of the command.
            TunerRuntimeException: If a runtime error occurred during the processing of the command.

        """

        _ = await self._send_commands(*self.READY_CHECK_COMMAND_STRINGS, sock=sock, loop=loop, size=20*1024)

    async def send_command(
            self, command: str, sock: socket.socket, loop: asyncio.AbstractEventLoop, size: int = 4 * 1024
    ) -> dict[str, Any]:
        """
        Sends the given `command` to the game via the provided `sock` and returns the response.

        Args:
            command: The command to send.
            sock: The socket to send the command to.
            loop: The asyncio event loop.
            size: The size of the response to retrieve.

        Returns:
            dict[str, Any]: The parsed response from the Civ V socket.

        Raises:
            TunerErrorException: If an unexpected error occurred during the processing of the command.
            TunerRuntimeException: If a runtime error occurred during the processing of the command.

        """

        # Build up the command message to send
        message = b"CMD:0:" + f"GameCore.Game.{command}".encode("utf-8") + b"\x00"
        message_length = len(message).to_bytes(1, byteorder='little')
        command_string = message_length + b"\x00\x00\x00\x03\x00\x00\x00" + message

        # Send the command
        logger.debug(f"Sending command: {command}")
        return await self._send_commands(command_string, sock=sock, loop=loop, size=size)
