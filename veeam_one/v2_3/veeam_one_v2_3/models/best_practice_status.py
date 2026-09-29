from enum import Enum


class BestPracticeStatus(str, Enum):
    NOTCHECKED = "NotChecked"
    NOTIMPLEMENTED = "NotImplemented"
    PASSED = "Passed"
    SUPPRESSED = "Suppressed"
    UNABLETODETECT = "UnableToDetect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
