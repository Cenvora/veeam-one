from enum import Enum


class ResolveType(str, Enum):
    ACKNOWLEDGE = "Acknowledge"
    ACTION = "Action"
    RESOLVE = "Resolve"

    def __str__(self) -> str:
        return str(self.value)
