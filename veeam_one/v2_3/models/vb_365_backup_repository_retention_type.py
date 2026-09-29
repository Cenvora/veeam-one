from enum import StrEnum


class Vb365BackupRepositoryRetentionType(StrEnum):
    ITEMLEVEL = "ItemLevel"
    SNAPSHOTBASED = "SnapshotBased"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
