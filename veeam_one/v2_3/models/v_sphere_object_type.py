from enum import Enum


class VSphereObjectType(str, Enum):
    DATACENTER = "Datacenter"
    DATASTORE = "Datastore"
    DATASTORECLUSTER = "DatastoreCluster"
    DATASTOREFOLDER = "DatastoreFolder"
    HOST = "Host"
    HOSTANDCLUSTERFOLDER = "HostAndClusterFolder"
    HOSTCLUSTER = "HostCluster"
    NETWORK = "Network"
    RESOURCEPOOL = "ResourcePool"
    UNKNOWN = "Unknown"
    VAPP = "VApp"
    VCENTER = "VCenter"
    VIRTUALINFRASTRUCTURE = "VirtualInfrastructure"
    VM = "Vm"

    def __str__(self) -> str:
        return str(self.value)
