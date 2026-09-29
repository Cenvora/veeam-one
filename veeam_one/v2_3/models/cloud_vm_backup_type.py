from enum import Enum


class CloudVmBackupType(str, Enum):
    BACKUPCOPY = "BackupCopy"
    BACKUPTOTAPE = "BackupToTape"
    CLOUDARCHIVE = "CloudArchive"
    CLOUDBACKUP = "CloudBackup"
    CLOUDREPLICA = "CloudReplica"
    CLOUDSNAPSHOT = "CloudSnapshot"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
