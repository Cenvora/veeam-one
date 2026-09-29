from enum import StrEnum


class BackupServerConnectionState(StrEnum):
    CONNECTED = "Connected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
