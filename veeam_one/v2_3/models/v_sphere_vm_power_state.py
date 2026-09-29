from enum import StrEnum


class VSphereVmPowerState(StrEnum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
