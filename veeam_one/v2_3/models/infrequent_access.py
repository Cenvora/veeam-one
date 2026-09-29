from enum import StrEnum


class InfrequentAccess(StrEnum):
    COLDTIER = "ColdTier"
    DISABLED = "Disabled"
    S3ONEZONEIA = "S3OneZoneIA"
    S3STANDARDIA = "S3StandardIA"

    def __str__(self) -> str:
        return str(self.value)
