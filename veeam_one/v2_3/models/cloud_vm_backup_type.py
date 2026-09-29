from enum import StrEnum


class CloudVmBackupType(StrEnum):
    BACKUPCOPY = "BackupCopy"
    BACKUPTOTAPE = "BackupToTape"
    CLOUDARCHIVE = "CloudArchive"
    CLOUDBACKUP = "CloudBackup"
    CLOUDREPLICA = "CloudReplica"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
