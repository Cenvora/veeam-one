from enum import StrEnum


class AssignType(StrEnum):
    GUESTLINUX = "GuestLinux"
    GUESTWINDOWS = "GuestWindows"
    ORDINARY = "Ordinary"

    def __str__(self) -> str:
        return str(self.value)
