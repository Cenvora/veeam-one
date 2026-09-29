from enum import StrEnum


class ProtectedObjectStorageType(StrEnum):
    AMAZONS3 = "AmazonS3"
    AZUREBLOBCONTAINER = "AzureBlobContainer"
    AZUREDATALAKE = "AzureDataLake"
    GOOGLESTORAGE = "GoogleStorage"
    S3COMPATIBLE = "S3Compatible"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
