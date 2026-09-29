from enum import StrEnum


class VSphereVmConnectionState(StrEnum):
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    INACCESSIBLE = "Inaccessible"
    INVALID = "Invalid"
    ORPHANED = "Orphaned"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
