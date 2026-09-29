from enum import Enum


class BestPracticeGroup(str, Enum):
    BACKUPINFRASTRUCTURESECURITY = "BackupInfrastructureSecurity"
    PRODUCTCONFIGURATION = "ProductConfiguration"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
