from enum import StrEnum


class CloudFileShareBackupType(StrEnum):
    CLOUDBACKUP = "CloudBackup"
    CLOUDBACKUPCOPY = "CloudBackupCopy"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
