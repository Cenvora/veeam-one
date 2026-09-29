from enum import Enum


class VeeamOneLicenseUsageUnitType(str, Enum):
    INSTANCES = "Instances"
    POINTS = "Points"
    SOCKETS = "Sockets"

    def __str__(self) -> str:
        return str(self.value)
