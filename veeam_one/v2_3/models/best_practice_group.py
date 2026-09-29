from enum import StrEnum


class BestPracticeGroup(StrEnum):
    BACKUPINFRASTRUCTURESECURITY = "BackupInfrastructureSecurity"
    PRODUCTCONFIGURATION = "ProductConfiguration"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
