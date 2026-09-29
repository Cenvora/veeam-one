from enum import Enum


class VSphereVmConnectionState(str, Enum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    INACCESSIBLE = "Inaccessible"
    INVALID = "Invalid"
    ORPHANED = "Orphaned"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
