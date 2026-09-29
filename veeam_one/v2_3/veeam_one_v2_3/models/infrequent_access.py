from enum import Enum


class InfrequentAccess(str, Enum):
    COLDTIER = "ColdTier"
    DISABLED = "Disabled"
    S3ONEZONEIA = "S3OneZoneIA"
    S3STANDARDIA = "S3StandardIA"

    def __str__(self) -> str:
        return str(self.value)
