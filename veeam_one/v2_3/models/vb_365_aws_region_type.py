from enum import Enum


class Vb365AwsRegionType(str, Enum):
    CHINA = "China"
    GLOBAL = "Global"
    UNKNOWN = "Unknown"
    USGOVERNMENT = "UsGovernment"

    def __str__(self) -> str:
        return str(self.value)
