from enum import StrEnum


class CloudPlatform(StrEnum):
    AWS = "AWS"
    GCP = "GCP"
    MICROSOFTAZURE = "MicrosoftAzure"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
