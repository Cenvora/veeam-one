from enum import Enum


class HyperVObjectType(str, Enum):
    CLUSTER = "Cluster"
    CLUSTERRESOURCEFOLDER = "ClusterResourceFolder"
    CSV = "Csv"
    CSV2008 = "Csv2008"
    CSV2008FOLDER = "Csv2008Folder"
    CSVFOLDER = "CsvFolder"
    DATASTOREFOLDER = "DatastoreFolder"
    FILESERVER = "FileServer"
    FILESHARE = "FileShare"
    FILESHAREFOLDER = "FileShareFolder"
    HOST = "Host"
    HOSTGROUP = "HostGroup"
    PHYSICALDISK = "PhysicalDisk"
    SCVMMSERVER = "ScvmmServer"
    VIRTUALINFRASTRUCTURE = "VirtualInfrastructure"
    VM = "Vm"

    def __str__(self) -> str:
        return str(self.value)
