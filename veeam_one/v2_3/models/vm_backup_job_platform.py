from enum import StrEnum


class VmBackupJobPlatform(StrEnum):
    HPEVME = "HpeVme"
    HYPERV = "HyperV"
    NUTANIX = "Nutanix"
    OVIRTKVM = "OVirtKVM"
    PROXMOX = "Proxmox"
    SANGFOR = "Sangfor"
    UNKNOWN = "Unknown"
    VSPHERE = "VSphere"
    XCPNG = "XCPng"

    def __str__(self) -> str:
        return str(self.value)
