from enum import StrEnum


class RemediationMode(StrEnum):
    AUTOMATIC = "Automatic"
    DISABLE = "Disable"
    MANUAL = "Manual"

    def __str__(self) -> str:
        return str(self.value)
