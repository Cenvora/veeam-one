from enum import Enum


class MemorySharesLevel(str, Enum):
    CUSTOM = "Custom"
    HIGH = "High"
    LOW = "Low"
    NORMAL = "Normal"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
