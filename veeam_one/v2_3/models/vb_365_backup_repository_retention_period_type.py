from enum import StrEnum


class Vb365BackupRepositoryRetentionPeriodType(StrEnum):
    DAILY = "Daily"
    MONTHLY = "Monthly"
    UNKNOWN = "Unknown"
    YEARLY = "Yearly"

    def __str__(self) -> str:
        return str(self.value)
