from enum import Enum


class TransactionLogBackupParentJobType(str, Enum):
    AGENTBACKUP = "AgentBackup"
    AGENTPOLICY = "AgentPolicy"
    UNKNOWN = "Unknown"
    VMBACKUP = "VmBackup"

    def __str__(self) -> str:
        return str(self.value)
