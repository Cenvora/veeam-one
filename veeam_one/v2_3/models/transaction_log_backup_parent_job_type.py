from enum import StrEnum


class TransactionLogBackupParentJobType(StrEnum):
    AGENTBACKUP = "AgentBackup"
    AGENTPOLICY = "AgentPolicy"
    UNKNOWN = "Unknown"
    VMBACKUP = "VmBackup"

    def __str__(self) -> str:
        return str(self.value)
