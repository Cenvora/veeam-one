from enum import Enum


class Vb365ObjectType(str, Enum):
    BACKUPPROXY = "BackupProxy"
    BACKUPPROXYFOLDER = "BackupProxyFolder"
    BACKUPREPOSITORY = "BackupRepository"
    BACKUPREPOSITORYFOLDER = "BackupRepositoryFolder"
    OBJECTSTORAGEREPOSITORY = "ObjectStorageRepository"
    OBJECTSTORAGEREPOSITORYFOLDER = "ObjectStorageRepositoryFolder"
    SERVER = "Server"
    VIRTUALINFRASTRUCTURE = "VirtualInfrastructure"

    def __str__(self) -> str:
        return str(self.value)
