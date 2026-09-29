from enum import Enum


class BackupProxyState(str, Enum):
    DISCONNECTED = "Disconnected"
    INACCESSIBLE = "Inaccessible"
    OK = "Ok"
    OUTOFDATE = "OutOfDate"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
