from enum import StrEnum


class ScheduleType(StrEnum):
    DAILY = "Daily"
    MANUALLY = "Manually"
    MONTHLYDAYS = "MonthlyDays"
    MONTHLYWEEKDAYS = "MonthlyWeekDays"
    PERIODIC = "Periodic"

    def __str__(self) -> str:
        return str(self.value)
