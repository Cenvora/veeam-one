from enum import StrEnum


class AsyncTaskState(StrEnum):
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    FAILED = "Failed"
    IDLE = "Idle"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
