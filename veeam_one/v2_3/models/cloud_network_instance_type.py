from enum import StrEnum


class CloudNetworkInstanceType(StrEnum):
    UNKNOWN = "Unknown"
    VNET = "VNET"
    VPC = "VPC"

    def __str__(self) -> str:
        return str(self.value)
