from enum import StrEnum


class VSphereHostConnectionState(StrEnum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
