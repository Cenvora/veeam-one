from enum import StrEnum


class Vb365OrganizationType(StrEnum):
    HYBRID = "Hybrid"
    OFFICE365 = "Office365"
    ONPREMISES = "OnPremises"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
