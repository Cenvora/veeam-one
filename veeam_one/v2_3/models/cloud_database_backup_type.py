from enum import StrEnum


class CloudDatabaseBackupType(StrEnum):
    CLOUDARCHIVE = "CloudArchive"
    CLOUDBACKUP = "CloudBackup"
    CLOUDREPLICA = "CloudReplica"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
