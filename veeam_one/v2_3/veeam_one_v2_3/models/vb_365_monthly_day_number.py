from enum import Enum


class Vb365MonthlyDayNumber(str, Enum):
    FIRST = "First"
    FOURTH = "Fourth"
    LAST = "Last"
    SECOND = "Second"
    THIRD = "Third"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
