from enum import Enum


class Vb365JobType(str, Enum):
    BACKUPCOPYJOB = "BackupCopyJob"
    BACKUPJOB = "BackupJob"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
