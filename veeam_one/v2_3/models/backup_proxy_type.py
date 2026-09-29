from enum import StrEnum


class BackupProxyType(StrEnum):
    CDP = "Cdp"
    GENERALPURPOSE = "GeneralPurpose"
    HYPERV = "HyperV"
    HYPERVOFFHOST = "HyperVOffhost"
    TAPE = "Tape"
    UNKNOWN = "Unknown"
    VMWARE = "Vmware"

    def __str__(self) -> str:
        return str(self.value)
