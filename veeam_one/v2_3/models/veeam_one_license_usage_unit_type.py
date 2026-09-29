from enum import StrEnum


class VeeamOneLicenseUsageUnitType(StrEnum):
    INSTANCES = "Instances"
    POINTS = "Points"
    SOCKETS = "Sockets"

    def __str__(self) -> str:
        return str(self.value)
