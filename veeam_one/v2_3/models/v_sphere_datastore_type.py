from enum import Enum


class VSphereDatastoreType(str, Enum):
    CIFS = "Cifs"
    NAS = "Nas"
    NFS = "Nfs"
    UNKNOWN = "Unknown"
    VMFS = "Vmfs"
    VSAN = "Vsan"
    VVOL = "Vvol"

    def __str__(self) -> str:
        return str(self.value)
