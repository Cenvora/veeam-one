from enum import Enum


class Vb365OrganizationRegion(str, Enum):
    CHINA = "China"
    GERMANY = "Germany"
    UNKNOWN = "Unknown"
    USDEFENCE = "UsDefence"
    USGOVERNMENT = "UsGovernment"
    WORLDWIDE = "Worldwide"

    def __str__(self) -> str:
        return str(self.value)
