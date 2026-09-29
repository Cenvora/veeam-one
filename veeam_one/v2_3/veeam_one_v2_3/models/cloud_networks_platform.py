from enum import Enum


class CloudNetworksPlatform(str, Enum):
    AWS = "AWS"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
