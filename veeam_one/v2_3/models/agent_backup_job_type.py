from enum import Enum


class AgentBackupJobType(str, Enum):
    AGENTPOLICY = "AgentPolicy"
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
