from enum import StrEnum


class Vb365BackupRepositoryRetentionFrequencyType(StrEnum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
