from enum import Enum


class VSphereHostConnectionState(str, Enum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
