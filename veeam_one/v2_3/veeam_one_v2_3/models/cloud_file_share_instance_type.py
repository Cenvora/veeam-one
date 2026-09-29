from enum import Enum


class CloudFileShareInstanceType(str, Enum):
    EFS = "EFS"
    FILES = "Files"
    FSX = "FSx"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
