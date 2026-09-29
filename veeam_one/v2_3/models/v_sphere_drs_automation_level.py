from enum import StrEnum


class VSphereDrsAutomationLevel(StrEnum):
    AUTOMATIC = "Automatic"
    MANUAL = "Manual"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
