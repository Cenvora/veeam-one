from enum import StrEnum


class VmPlatform(StrEnum):
    CLOUDDIRECTOR = "CloudDirector"
    HPEVME = "HpeVme"
    HYPERV = "HyperV"
    NUTANIXAHV = "NutanixAhv"
    OVIRTKVM = "OVirtKVM"
    PROXMOX = "Proxmox"
    SANGFOR = "Sangfor"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VSPHERE = "VSphere"
    XCPNG = "XCPng"

    def __str__(self) -> str:
        return str(self.value)
