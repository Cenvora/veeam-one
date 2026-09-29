from enum import Enum


class Vb365JobStatus(str, Enum):
    DISCONNECTED = "Disconnected"
    FAILED = "Failed"
    NOTCONFIGURED = "NotConfigured"
    QUEUED = "Queued"
    RUNNING = "Running"
    STOPPED = "Stopped"
    SUCCESS = "Success"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
