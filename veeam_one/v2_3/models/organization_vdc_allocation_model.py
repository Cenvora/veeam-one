from enum import StrEnum


class OrganizationVdcAllocationModel(StrEnum):
    ALLOCATIONPOOL = "AllocationPool"
    FLEX = "Flex"
    PAYASYOUGO = "PayAsYouGo"
    RESERVATIONPOOL = "ReservationPool"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
