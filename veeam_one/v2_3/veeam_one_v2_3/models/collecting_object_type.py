from enum import Enum


class CollectingObjectType(str, Enum):
    ENTERPRISEMANAGER = "EnterpriseManager"
    HYPERVFAILOVERCLUSTER = "HyperVFailoverCluster"
    HYPERVHOST = "HyperVHost"
    HYPERVSCVMM = "HyperVSCVMM"
    UNKNOWN = "Unknown"
    VB365 = "VB365"
    VBR = "VBR"
    VMWARECLOUDDIRECTOR = "VMwareCloudDirector"
    VMWAREHOST = "VMwareHost"
    VMWAREVCENTER = "VMwarevCenter"

    def __str__(self) -> str:
        return str(self.value)
