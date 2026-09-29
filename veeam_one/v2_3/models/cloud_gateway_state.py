from enum import StrEnum


class CloudGatewayState(StrEnum):
    DISCONNECTED = "Disconnected"
    HEALTHY = "Healthy"
    INACCESSIBLE = "Inaccessible"
    OUTOFDATE = "OutOfDate"
    UNKNOWN = "Unknown"
    WARNING = "Warning"

    def __str__(self) -> str:
        return str(self.value)
