from enum import Enum


class RemediationMode(str, Enum):
    AUTOMATIC = "Automatic"
    DISABLE = "Disable"
    MANUAL = "Manual"

    def __str__(self) -> str:
        return str(self.value)
