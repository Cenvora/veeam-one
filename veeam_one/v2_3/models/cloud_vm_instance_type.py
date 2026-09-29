from enum import StrEnum


class CloudVmInstanceType(StrEnum):
    COMPUTEENGINE = "ComputeEngine"
    EC2 = "EC2"
    UNKNOWN = "Unknown"
    VIRTUALMACHINES = "VirtualMachines"

    def __str__(self) -> str:
        return str(self.value)
