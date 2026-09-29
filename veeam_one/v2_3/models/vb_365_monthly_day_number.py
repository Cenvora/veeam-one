from enum import StrEnum


class Vb365MonthlyDayNumber(StrEnum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
