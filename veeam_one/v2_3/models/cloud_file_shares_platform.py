from enum import StrEnum


class CloudFileSharesPlatform(StrEnum):
    AWS = "AWS"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
