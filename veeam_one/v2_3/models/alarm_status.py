from enum import Enum


class AlarmStatus(str, Enum):
    ACKNOWLEDGED = "Acknowledged"
    ERROR = "Error"
    INFORMATION = "Information"
    REMEDIATED = "Remediated"
    RESOLVED = "Resolved"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
