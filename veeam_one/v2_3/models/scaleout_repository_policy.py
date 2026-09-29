from enum import Enum


class ScaleoutRepositoryPolicy(str, Enum):
    DATALOCALITY = "DataLocality"
    PERFORMANCE = "Performance"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
