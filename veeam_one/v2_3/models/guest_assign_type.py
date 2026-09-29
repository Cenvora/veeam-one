from enum import StrEnum


class GuestAssignType(StrEnum):
    GUESTLINUX = "GuestLinux"
    GUESTWINDOWS = "GuestWindows"

    def __str__(self) -> str:
        return str(self.value)
