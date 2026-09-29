from enum import Enum


class CloudGatewayState(str, Enum):
    DISCONNECTED = "Disconnected"
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    OUTOFDATE = "OutOfDate"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
