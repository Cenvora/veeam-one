from enum import StrEnum


class FileShareType(StrEnum):
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
