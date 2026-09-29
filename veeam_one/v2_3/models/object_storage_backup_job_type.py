from enum import StrEnum


class ObjectStorageBackupJobType(StrEnum):
    BACKUPCOPY = "BackupCopy"
    OBJECTSTORAGEBACKUP = "ObjectStorageBackup"
    OBJECTSTORAGETOTAPE = "ObjectStorageToTape"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
