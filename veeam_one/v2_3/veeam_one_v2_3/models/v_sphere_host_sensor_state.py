from enum import Enum


class VSphereHostSensorState(str, Enum):
    EMPTY = "Empty"
    ERROR = "Error"
    HEALTHY = "Healthy"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
