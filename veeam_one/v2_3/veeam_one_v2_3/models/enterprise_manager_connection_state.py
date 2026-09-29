from enum import Enum


class EnterpriseManagerConnectionState(str, Enum):
    CONNECTED = "Connected"
    NOTRESPONDING = "NotResponding"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
