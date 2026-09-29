from enum import Enum


class FileShareType(str, Enum):
    CIFS = "Cifs"
    CIFSSERVER = "CifsServer"
    CIFSSHARE = "CifsShare"
    HARDWAREFILESERVER = "HardwareFileServer"
    NFS = "Nfs"
    NFSSERVER = "NfsServer"
    NFSSHARE = "NfsShare"
    SANCIFSSERVER = "SanCifsServer"
    SANNFSSERVER = "SanNfsServer"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
