from enum import StrEnum


class CollectingObjectType(StrEnum):
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
