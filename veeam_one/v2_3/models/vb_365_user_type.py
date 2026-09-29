from enum import StrEnum


class Vb365UserType(StrEnum):
    O365USER = "O365User"
    PUBLIC = "Public"
    SHARED = "Shared"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
