from enum import Enum


class VSphereDrsAutomationLevel(str, Enum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
