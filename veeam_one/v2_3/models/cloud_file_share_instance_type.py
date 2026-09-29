from enum import StrEnum


class CloudFileShareInstanceType(StrEnum):
    EFS = "EFS"
    FILES = "Files"
    FSX = "FSx"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
