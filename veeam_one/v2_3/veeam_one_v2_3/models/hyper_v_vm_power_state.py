from enum import Enum


class HyperVVmPowerState(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    PAUSED = "Paused"
    PAUSING = "Pausing"
    RESUMING = "Resuming"
    SAVING = "Saving"
    SNAPSHOTTING = "Snapshotting"
    STARTING = "Starting"
    STOPPING = "Stopping"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
