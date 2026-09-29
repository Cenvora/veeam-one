from enum import Enum


class BusinessViewCategoryType(str, Enum):
    COMPUTERS = "Computers"
    ENTERPRISEAPPLICATIONS = "EnterpriseApplications"
    HYPERVDATASTORE = "HyperVDatastore"
    HYPERVHOST = "HyperVHost"
    HYPERVHOSTCLUSTER = "HyperVHostCluster"
    HYPERVVM = "HyperVVm"
    VSPHEREDATASTORE = "VSphereDatastore"
    VSPHEREHOST = "VSphereHost"
    VSPHEREHOSTCLUSTER = "VSphereHostCluster"
    VSPHEREVM = "VSphereVm"

    def __str__(self) -> str:
        return str(self.value)
