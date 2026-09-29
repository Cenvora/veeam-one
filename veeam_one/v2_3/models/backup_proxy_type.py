from enum import Enum


class BackupProxyType(str, Enum):
    CDP = "Cdp"
    GENERALPURPOSE = "GeneralPurpose"
    HYPERV = "HyperV"
    HYPERVOFFHOST = "HyperVOffhost"
    TAPE = "Tape"
    UNKNOWN = "Unknown"
    VMWARE = "Vmware"

    def __str__(self) -> str:
        return str(self.value)
