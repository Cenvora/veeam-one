from enum import Enum


class FileShareBackupJobType(str, Enum):
    BACKUPCOPY = "BackupCopy"
    FILEBACKUP = "FileBackup"
    FILECOPY = "FileCopy"
    FILETOTAPE = "FileToTape"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
