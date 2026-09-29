from enum import Enum


class OrganizationVdcAllocationModel(str, Enum):
    ALLOCATIONPOOL = "AllocationPool"
    FLEX = "Flex"
    PAYASYOUGO = "PayAsYouGo"
    RESERVATIONPOOL = "ReservationPool"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
