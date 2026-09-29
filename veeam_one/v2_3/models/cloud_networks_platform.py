from enum import StrEnum


class CloudNetworksPlatform(StrEnum):
    AWS = "AWS"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
