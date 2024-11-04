import socket
from typing import List, Optional
from .Coordinates import Coordinates

class CobotService:
    def __init__(self, host: str, port: int, acceleration: float, speed: float) -> None:
        self.cobotSocket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cobotSocket.connect((host, port))
        self.acceleration: float = acceleration
        self.speed: float = speed

    def moveL(self,
            coordinates: Coordinates,
            time: Optional[float] = None, 
            acceleration: Optional[float] = None,
            speed: Optional[float] = None
        ) -> None:

        self._validate_coordinates_object(coordinates)
        command: str = (
            f"movel(p[{', '.join(map(str, coordinates._to_tuple()))}], "
            f"a={self.acceleration if acceleration is None else acceleration}, "
            f"v={self.speed if speed is None else speed}"
            f"{f', t={time:.2f}' if time is not None else ''})\n"
        )

        self._send(command)

    def _send(self, command: str) -> None:
        self.cobotSocket.send(command.encode('utf-8'))
        print(f"Command sent: {command}")

    def _validate_coordinates_object(self, coordinates):
        if not isinstance(coordinates, Coordinates):
            raise TypeError(f"Expected coordinates to be an instance of Coordinates, got {type(coordinates).__name__}")
