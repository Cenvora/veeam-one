from enum import Enum


class Vb365ServerConnectionState(str, Enum):
    CONNECTED = "Connected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
