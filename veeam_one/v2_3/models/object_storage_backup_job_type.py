from enum import Enum


class ObjectStorageBackupJobType(str, Enum):
    BACKUPCOPY = "BackupCopy"
    OBJECTSTORAGEBACKUP = "ObjectStorageBackup"
    OBJECTSTORAGETOTAPE = "ObjectStorageToTape"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
