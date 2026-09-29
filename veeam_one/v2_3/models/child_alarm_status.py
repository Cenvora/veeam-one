from enum import StrEnum


class ChildAlarmStatus(StrEnum):
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
