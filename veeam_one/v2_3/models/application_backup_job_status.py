from enum import StrEnum


class ApplicationBackupJobStatus(StrEnum):
    DISABLED = "Disabled"
    FAILED = "Failed"
    NONE = "None"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
