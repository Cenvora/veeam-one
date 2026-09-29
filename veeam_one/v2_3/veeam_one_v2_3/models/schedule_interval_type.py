from enum import Enum


class ScheduleIntervalType(str, Enum):
    HOURS = "Hours"
    MINUTES = "Minutes"

    def __str__(self) -> str:
        return str(self.value)
