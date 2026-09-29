from enum import StrEnum


class VSphereHostSensorState(StrEnum):
    EMPTY = "Empty"
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
