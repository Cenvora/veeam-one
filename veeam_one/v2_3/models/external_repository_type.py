from enum import Enum


class ExternalRepositoryType(str, Enum):
    AMAZONGLACIER = "AmazonGlacier"
    AMAZONS3 = "AmazonS3"
    GOOGLECLOUDARCHIVESTORAGE = "GoogleCloudArchiveStorage"
    GOOGLECLOUDSTORAGE = "GoogleCloudStorage"
    MICROSOFTAZUREARCHIVESTORAGE = "MicrosoftAzureArchiveStorage"
    MICROSOFTAZUREBLOBSTORAGE = "MicrosoftAzureBlobStorage"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
