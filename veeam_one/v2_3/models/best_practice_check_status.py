from enum import StrEnum


class BestPracticeCheckStatus(StrEnum):
    NOTAPPLICABLE = "NotApplicable"
    NOTIMPLEMENTED = "NotImplemented"
    OTHER = "Other"
    PASSED = "Passed"
    UNABLETODETECT = "UnableToDetect"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
