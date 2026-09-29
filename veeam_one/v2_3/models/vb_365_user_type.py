from enum import Enum


class Vb365UserType(str, Enum):
    O365USER = "O365User"
    PUBLIC = "Public"
    SHARED = "Shared"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
