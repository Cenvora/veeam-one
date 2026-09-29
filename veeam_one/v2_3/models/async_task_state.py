from enum import Enum


class AsyncTaskState(str, Enum):
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    FAILED = "Failed"
    IDLE = "Idle"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
