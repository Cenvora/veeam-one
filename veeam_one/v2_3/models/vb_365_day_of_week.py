from enum import StrEnum


class Vb365DayOfWeek(StrEnum):
    FRIDAY = "Friday"
    MONDAY = "Monday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    THURSDAY = "Thursday"
    TUESDAY = "Tuesday"
    UNKNOWN = "Unknown"
    WEDNESDAY = "Wednesday"

    def __str__(self) -> str:
        return str(self.value)
