from enum import Enum


class VAppPowerState(str, Enum):
    INCONSISTENTSTATE = "InconsistentState"
    PARTIALLYRUNNING = "PartiallyRunning"
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
