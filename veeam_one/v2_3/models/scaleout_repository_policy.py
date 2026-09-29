from enum import StrEnum


class ScaleoutRepositoryPolicy(StrEnum):
    DATALOCALITY = "DataLocality"
    PERFORMANCE = "Performance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
