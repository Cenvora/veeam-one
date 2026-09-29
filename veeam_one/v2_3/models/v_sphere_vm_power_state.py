from enum import Enum


class VSphereVmPowerState(str, Enum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
