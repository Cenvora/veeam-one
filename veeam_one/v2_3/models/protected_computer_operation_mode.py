from enum import StrEnum


class ProtectedComputerOperationMode(StrEnum):
    SERVER = "Server"
    UNKNOWN = "Unknown"
    WORKSTATION = "Workstation"

    def __str__(self) -> str:
        return str(self.value)
