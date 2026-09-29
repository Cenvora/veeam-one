from enum import StrEnum


class AgentBackupJobType(StrEnum):
    AGENTPOLICY = "AgentPolicy"
    BACKUP = "Backup"
    BACKUPCOPY = "BackupCopy"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
