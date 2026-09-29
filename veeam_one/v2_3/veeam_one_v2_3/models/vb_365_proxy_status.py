from enum import Enum


class Vb365ProxyStatus(str, Enum):
    OFFLINE = "Offline"
    ONLINE = "Online"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
