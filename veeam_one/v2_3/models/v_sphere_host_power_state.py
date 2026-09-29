from enum import StrEnum


class VSphereHostPowerState(StrEnum):
    POWEREDOFF = "PoweredOff"
    POWEREDON = "PoweredOn"
    STANDBY = "Standby"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
