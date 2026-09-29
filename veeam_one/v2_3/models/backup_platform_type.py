from enum import StrEnum


class BackupPlatformType(StrEnum):
    LINUX = "Linux"
    UNKNOWN = "Unknown"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
