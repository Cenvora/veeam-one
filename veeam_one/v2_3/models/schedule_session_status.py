from enum import Enum


class ScheduleSessionStatus(str, Enum):
    FAILED = "Failed"
    FAILEDWITHOUTSTART = "FailedWithoutStart"
    INQUEUE = "InQueue"
    PROCESSING = "Processing"
    ROLLBACK = "Rollback"
    STOPPED = "Stopped"
    STOPPING = "Stopping"
    SUCCESS = "Success"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
