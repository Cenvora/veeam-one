from enum import StrEnum


class Vb365OrganizationRegion(StrEnum):
    CHINA = "China"
    GERMANY = "Germany"
    UNKNOWN = "Unknown"
    USDEFENCE = "UsDefence"
    USGOVERNMENT = "UsGovernment"
    WORLDWIDE = "Worldwide"

    def __str__(self) -> str:
        return str(self.value)
