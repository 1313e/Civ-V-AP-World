# %% IMPORTS
import socket
import asyncio
from logging import Logger


# %% GLOBALS
CLIENT_PREFIX = "APSTART:"
CLIENT_POSTFIX = ":APEND"


# %% FUNCTION DEFINITIONS
def decode_mixed_string(data):
    return ''.join(chr(b) if 32 <= b < 127 else '' for b in data)


class TunerException(Exception):
    pass


class TunerRuntimeException(TunerException):
    pass

class TunerTimeoutException(TunerException):
    pass


class TunerErrorException(TunerException):
    pass


class TunerConnectionException(TunerException):
    pass

class Tuner:
    logger: Logger

    def __init__(self, logger):
        self.logger = logger

    def __parse_response(self, response: str) -> str:
        """Parses the response from the tuner socket"""
        split = response.split(CLIENT_PREFIX)
        if len(split) > 1:
            start = split[1]
            end = start.split(CLIENT_POSTFIX)[0]
            return end
        elif "ERR:Runtime Error" in response:
            raise TunerRuntimeException(response.replace("?", ""))
        elif "ERR:" in response:
            raise TunerErrorException(response.replace("?", ""))
        else:
            return ""

    async def send_init_command(self, sock: socket.socket, loop: asyncio.AbstractEventLoop):
        command_string1 = b"\x05\x00\x00\x00\x04\x00\x00\x00APP:\x00"
        command_string2 = b"\x05\x00\x00\x00\x00\x00\x00\x00LSQ:\x00"
        print(f"Sending commands: {command_string1}, {command_string2}")
        try:
            await loop.sock_sendall(sock, command_string1)
            await loop.sock_sendall(sock, command_string2)
            await asyncio.sleep(0.2)

            received_data = await self.async_recv(sock, 20*1024)
            response = self.__parse_response(decode_mixed_string(received_data))
            print(f"Received data: {response}")
            return response
        except TimeoutError:
            self.logger.debug('Timeout while receiving data')
            raise TunerTimeoutException
        except ConnectionError:
            self.logger.debug('Connection error while receiving data')
            raise TunerConnectionException
        except Exception as e:
            self.logger.debug(f'Unhandled error occurred while receiving data: {str(e)}')
            raise TunerException(e)


    async def send_command(self, command_string: str, sock: socket.socket, loop: asyncio.AbstractEventLoop, size=4*1024):
        prefix_string = "GameCore.Game."
        b_command_string = f"{prefix_string}{command_string}".encode("utf-8")

        command_prefix = b"CMD:0:"
        delimiter = b"\x00"
        full_command = b_command_string
        message = command_prefix + full_command + delimiter
        message_length = len(message).to_bytes(1,byteorder='little')

        message_header = message_length + b"\x00\x00\x00\x03\x00\x00\x00"
        data = message_header + message
        print(f"Sending command: {command_string}")

        try:
            await loop.sock_sendall(sock, data)
            await asyncio.sleep(0.2)

            received_data = await self.async_recv(sock, size)
            response = self.__parse_response(decode_mixed_string(received_data))
            print(f"Received data: {response}")
            return response
        except TimeoutError:
            self.logger.debug('Timeout while receiving data')
            raise TunerTimeoutException
        except ConnectionError:
            self.logger.debug('Connection error while receiving data')
            raise TunerConnectionException
        except TunerException:
            self.logger.debug(f'Error occurred while receiving data')
            raise
        except Exception as e:
            self.logger.debug(f'Unhandled error occurred while receiving data: {str(e)}')
            raise TunerException(e)

    async def async_recv(self, sock, size):
        return await asyncio.wait_for(asyncio.get_event_loop().sock_recv(sock, size), 2.0)
