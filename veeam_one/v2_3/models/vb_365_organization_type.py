from enum import Enum


class Vb365OrganizationType(str, Enum):
    HYBRID = "Hybrid"
    OFFICE365 = "Office365"
    ONPREMISES = "OnPremises"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
