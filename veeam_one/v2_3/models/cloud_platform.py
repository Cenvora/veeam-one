from enum import Enum


class CloudPlatform(str, Enum):
    AWS = "AWS"
    GCP = "GCP"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
