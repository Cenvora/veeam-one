from enum import Enum


class VmReplicationJobPlatform(str, Enum):
    HYPERV = "HyperV"
    UNKNOWN = "Unknown"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
