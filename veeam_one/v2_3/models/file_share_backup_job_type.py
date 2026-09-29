from enum import StrEnum


class FileShareBackupJobType(StrEnum):
    BACKUPCOPY = "BackupCopy"
    FILEBACKUP = "FileBackup"
    FILECOPY = "FileCopy"
    FILETOTAPE = "FileToTape"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
