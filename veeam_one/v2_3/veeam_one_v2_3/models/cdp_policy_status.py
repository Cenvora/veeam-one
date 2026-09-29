from enum import Enum


class CdpPolicyStatus(str, Enum):
    DISABLED = "Disabled"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
