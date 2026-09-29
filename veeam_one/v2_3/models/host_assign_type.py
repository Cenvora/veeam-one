from enum import Enum


class HostAssignType(str, Enum):
    BPBACKUPSERVER = "BpBackupServer"
    BPENTERPRISEMANAGER = "BpEnterpriseManager"
    BPPROXY = "BpProxy"
    BPREPOSITORY = "BpRepository"
    BPTAPEPROXY = "BpTapeProxy"
    BPWANACCELERATOR = "BpWanAccelerator"
    HVCLUSTER = "HvCluster"
    HVCLUSTERRESOURCEFOLDER = "HvClusterResourceFolder"
    HVHOST = "HvHost"
    HVSCVMMSERVER = "HvScvmmServer"
    HVVM = "HvVm"
    SERVICENOW = "ServiceNow"
    UNKNOWN = "Unknown"
    VBMPROXY = "VbmProxy"
    VBMSERVER = "VbmServer"
    VCDVCLOUDDIRECTOR = "VcdVcloudDirector"
    VIROOTNODE = "ViRootNode"
    VWCLUSTER = "VwCluster"
    VWDATACENTER = "VwDatacenter"
    VWESX = "VwEsx"
    VWFOLDER = "VwFolder"
    VWRESOURCEPOOL = "VwResourcePool"
    VWVCENTER = "VwVCenter"
    VWVIRTUALAPP = "VwVirtualApp"
    VWVM = "VwVm"

    def __str__(self) -> str:
        return str(self.value)
