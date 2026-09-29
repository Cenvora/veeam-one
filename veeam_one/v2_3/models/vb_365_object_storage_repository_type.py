from enum import Enum


class Vb365ObjectStorageRepositoryType(str, Enum):
    AMAZONS3 = "AmazonS3"
    AMAZONS3COMPATIBLE = "AmazonS3Compatible"
    AMAZONS3GLACIER = "AmazonS3Glacier"
    AZUREBLOB = "AzureBlob"
    AZUREBLOBARCHIVE = "AzureBlobArchive"
    IBMCLOUD = "IbmCloud"
    UNKNOWN = "Unknown"
    WASABICLOUD = "WasabiCloud"

    def __str__(self) -> str:
        return str(self.value)
