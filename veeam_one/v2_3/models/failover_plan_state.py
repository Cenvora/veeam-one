from enum import Enum


class FailoverPlanState(str, Enum):
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
