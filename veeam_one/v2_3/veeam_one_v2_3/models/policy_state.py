from enum import Enum


class PolicyState(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
