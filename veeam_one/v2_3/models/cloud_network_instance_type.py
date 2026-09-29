from enum import Enum


class CloudNetworkInstanceType(str, Enum):
    UNKNOWN = "Unknown"
    VNET = "VNET"
    VPC = "VPC"

    def __str__(self) -> str:
        return str(self.value)
