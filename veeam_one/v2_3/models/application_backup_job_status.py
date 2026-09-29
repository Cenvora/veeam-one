from enum import Enum


class ApplicationBackupJobStatus(str, Enum):
    DISABLED = "Disabled"
    FAILED = "Failed"
    NONE = "None"
    RUNNING = "Running"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
