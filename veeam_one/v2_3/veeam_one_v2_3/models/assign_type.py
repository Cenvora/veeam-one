from enum import Enum


class AssignType(str, Enum):
    GUESTLINUX = "GuestLinux"
    GUESTWINDOWS = "GuestWindows"
    ORDINARY = "Ordinary"

    def __str__(self) -> str:
        return str(self.value)
