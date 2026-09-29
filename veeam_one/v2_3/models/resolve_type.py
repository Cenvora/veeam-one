from enum import StrEnum


class ResolveType(StrEnum):
    ACKNOWLEDGE = "Acknowledge"
    ACTION = "Action"
    RESOLVE = "Resolve"

    def __str__(self) -> str:
        return str(self.value)
