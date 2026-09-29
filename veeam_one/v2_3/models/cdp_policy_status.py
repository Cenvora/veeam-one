from enum import StrEnum


class CdpPolicyStatus(StrEnum):
    DISABLED = "Disabled"
    RUNNING = "Running"

    def __str__(self) -> str:
        return str(self.value)
