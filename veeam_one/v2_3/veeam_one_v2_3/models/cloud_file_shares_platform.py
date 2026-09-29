from enum import Enum


class CloudFileSharesPlatform(str, Enum):
    AWS = "AWS"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
