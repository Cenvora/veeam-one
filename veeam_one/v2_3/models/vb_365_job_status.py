from enum import StrEnum


class Vb365JobStatus(StrEnum):
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
