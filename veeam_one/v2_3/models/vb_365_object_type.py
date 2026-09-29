from enum import StrEnum


class Vb365ObjectType(StrEnum):
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
