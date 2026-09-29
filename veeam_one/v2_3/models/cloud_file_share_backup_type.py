from enum import Enum


class CloudFileShareBackupType(str, Enum):
    CLOUDBACKUP = "CloudBackup"
    CLOUDBACKUPCOPY = "CloudBackupCopy"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
