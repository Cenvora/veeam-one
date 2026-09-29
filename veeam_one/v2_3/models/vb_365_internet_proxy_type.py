from enum import StrEnum


class Vb365InternetProxyType(StrEnum):
    CUSTOM = "Custom"
    FROMMANAGEMENTSERVER = "FromManagementServer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
