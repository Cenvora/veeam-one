from enum import Enum


class BestPracticeCheckStatus(str, Enum):
    NOTAPPLICABLE = "NotApplicable"
    NOTIMPLEMENTED = "NotImplemented"
    OTHER = "Other"
    PASSED = "Passed"
    UNABLETODETECT = "UnableToDetect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
