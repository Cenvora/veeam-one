from enum import StrEnum


class Vb365ProxyType(StrEnum):
    DOMAIN = "Domain"
    LOCAL = "Local"
    UNKNOWN = "Unknown"
    WORKGROUP = "Workgroup"

    def __str__(self) -> str:
        return str(self.value)
