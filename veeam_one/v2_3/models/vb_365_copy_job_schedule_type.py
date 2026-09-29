from enum import StrEnum


class Vb365CopyJobScheduleType(StrEnum):
    DAILYATTIME = "DailyAtTime"
    IMMEDIATE = "Immediate"
    PERIODICALLY = "Periodically"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
