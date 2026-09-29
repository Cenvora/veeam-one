from enum import Enum


class GuestAssignType(str, Enum):
    GUESTLINUX = "GuestLinux"
    GUESTWINDOWS = "GuestWindows"

    def __str__(self) -> str:
        return str(self.value)
