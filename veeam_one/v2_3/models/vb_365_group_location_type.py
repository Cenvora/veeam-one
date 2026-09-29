from enum import StrEnum


class Vb365GroupLocationType(StrEnum):
    CLOUD = "Cloud"
    HYBRID = "Hybrid"
    ONPREMISES = "OnPremises"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
