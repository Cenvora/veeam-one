from enum import StrEnum


class HyperVConnectionState(StrEnum):
    CONNECTED = "Connected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
