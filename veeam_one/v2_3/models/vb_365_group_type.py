from enum import StrEnum


class Vb365GroupType(StrEnum):
    DISTRIBUTION = "Distribution"
    DYNAMICDISTRIBUTION = "DynamicDistribution"
    OFFICE365 = "Office365"
    SECURITY = "Security"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
