from enum import StrEnum


class Vb365JobType(StrEnum):
    BACKUPCOPYJOB = "BackupCopyJob"
    BACKUPJOB = "BackupJob"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
