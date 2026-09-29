from enum import Enum


class VSphereHostPowerState(str, Enum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    STANDBY = "Standby"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
