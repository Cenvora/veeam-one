from enum import StrEnum


class Vb365ProxyStatus(StrEnum):
    OFFLINE = "Offline"
    ONLINE = "Online"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
