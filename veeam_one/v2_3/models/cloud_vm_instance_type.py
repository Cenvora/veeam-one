from enum import Enum


class CloudVmInstanceType(str, Enum):
    COMPUTEENGINE = "ComputeEngine"
    EC2 = "EC2"
    UNKNOWN = "Unknown"
    VIRTUALMACHINES = "VirtualMachines"

    def __str__(self) -> str:
        return str(self.value)
