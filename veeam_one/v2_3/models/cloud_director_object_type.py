from enum import Enum


class CloudDirectorObjectType(str, Enum):
    CLOUDDIRECTORINFRASTRUCTURE = "CloudDirectorInfrastructure"
    CLOUDDIRECTORSERVER = "CloudDirectorServer"
    ORGANIZATION = "Organization"
    ORGANIZATIONFOLDER = "OrganizationFolder"
    ORGANIZATIONVDC = "OrganizationVdc"
    PROVIDERVDC = "ProviderVdc"
    PROVIDERVDCFOLDER = "ProviderVdcFolder"
    VAPP = "Vapp"

    def __str__(self) -> str:
        return str(self.value)
