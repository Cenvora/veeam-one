from enum import StrEnum


class CloudDirectorObjectType(StrEnum):
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
