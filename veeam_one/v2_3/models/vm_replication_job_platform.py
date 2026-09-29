from enum import StrEnum


class VmReplicationJobPlatform(StrEnum):
    HYPERV = "HyperV"
    UNKNOWN = "Unknown"
    VSPHERE = "VSphere"

    def __str__(self) -> str:
        return str(self.value)
