from enum import Enum


class CloudDirectorConnectionState(str, Enum):
    CONNECTED = "Connected"
    INACCESSIBLE = "Inaccessible"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
