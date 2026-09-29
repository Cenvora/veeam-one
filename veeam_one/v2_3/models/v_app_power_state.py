from enum import StrEnum


class VAppPowerState(StrEnum):
    INCONSISTENTSTATE = "InconsistentState"
    PARTIALLYRUNNING = "PartiallyRunning"
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
