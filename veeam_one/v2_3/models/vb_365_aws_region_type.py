from enum import StrEnum


class Vb365AwsRegionType(StrEnum):
    CHINA = "China"
    GLOBAL = "Global"
    UNKNOWN = "Unknown"
    USGOVERNMENT = "UsGovernment"

    def __str__(self) -> str:
        return str(self.value)
