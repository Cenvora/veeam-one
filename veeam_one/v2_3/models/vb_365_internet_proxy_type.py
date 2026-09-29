from enum import Enum


class Vb365InternetProxyType(str, Enum):
    CUSTOM = "Custom"
    FROMMANAGEMENTSERVER = "FromManagementServer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
