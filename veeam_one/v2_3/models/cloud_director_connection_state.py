from enum import StrEnum


class CloudDirectorConnectionState(StrEnum):
    CONNECTED = "Connected"
    INACCESSIBLE = "Inaccessible"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
