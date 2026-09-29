from enum import StrEnum


class ScheduleIntervalType(StrEnum):
    HOURS = "Hours"
    MINUTES = "Minutes"

    def __str__(self) -> str:
        return str(self.value)
