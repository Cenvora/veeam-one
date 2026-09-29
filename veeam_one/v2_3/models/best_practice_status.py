from enum import StrEnum


class BestPracticeStatus(StrEnum):
    NOTCHECKED = "NotChecked"
    NOTIMPLEMENTED = "NotImplemented"
    PASSED = "Passed"
    SUPPRESSED = "Suppressed"
    UNABLETODETECT = "UnableToDetect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
