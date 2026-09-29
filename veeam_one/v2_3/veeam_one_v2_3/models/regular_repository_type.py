from enum import Enum


class RegularRepositoryType(str, Enum):
    CLOUD = "Cloud"
    DELLEMCDATADOMAIN = "DellEMCDataDomain"
    EXAGRID = "ExaGrid"
    HPESTOREONCE = "HPEStoreOnce"
    LINUX = "Linux"
    LINUXHARDENED = "LinuxHardened"
    MICROSOFTWINDOWS = "MicrosoftWindows"
    NFS = "NFS"
    QUANTUMDXI = "QuantumDXi"
    SMB = "SMB"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
