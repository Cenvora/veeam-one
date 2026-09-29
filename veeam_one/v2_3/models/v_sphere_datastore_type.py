from enum import StrEnum


class VSphereDatastoreType(StrEnum):
    CIFS = "Cifs"
    NAS = "Nas"
    NFS = "Nfs"
    UNKNOWN = "Unknown"
    VMFS = "Vmfs"
    VSAN = "Vsan"
    VVOL = "Vvol"

    def __str__(self) -> str:
        return str(self.value)
