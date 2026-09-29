from enum import StrEnum


class PolicyState(StrEnum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
