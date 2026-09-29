from enum import Enum


class CloudDatabaseBackupType(str, Enum):
    CLOUDARCHIVE = "CloudArchive"
    CLOUDBACKUP = "CloudBackup"
    CLOUDREPLICA = "CloudReplica"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
