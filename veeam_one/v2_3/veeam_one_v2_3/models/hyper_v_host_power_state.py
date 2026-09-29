from enum import Enum


class HyperVHostPowerState(str, Enum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    STANDBY = "Standby"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
