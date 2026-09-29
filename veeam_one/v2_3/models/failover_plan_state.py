from enum import StrEnum


class FailoverPlanState(StrEnum):
    FAILED = "Failed"
    INPROGRESS = "InProgress"
    INUNDOPROGRESS = "InUndoProgress"
    READY = "Ready"
    SUCCESS = "Success"
    UNDOFAILED = "UndoFailed"
    UNDOSUCCESS = "UndoSuccess"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
