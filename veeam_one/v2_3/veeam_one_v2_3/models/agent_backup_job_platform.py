from enum import Enum


class AgentBackupJobPlatform(str, Enum):
    CUSTOM = "Custom"
    IBMAIX = "IbmAix"
    IBMAIXORACLESOLARIS = "IbmAixOracleSolaris"
    LINUX = "Linux"
    MAC = "Mac"
    MICROSOFTWINDOWS = "MicrosoftWindows"
    ORACLESOLARIS = "OracleSolaris"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
