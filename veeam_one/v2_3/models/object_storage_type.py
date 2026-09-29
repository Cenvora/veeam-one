from enum import Enum


class ObjectStorageType(str, Enum):
    AMAZONS3 = "AmazonS3"
    AMAZONS3GLACIER = "AmazonS3Glacier"
    CLOUDOBJECTSTORAGE_11_11 = "CloudObjectStorage_11_11"
    GOOGLECLOUDSTORAGE = "GoogleCloudStorage"
    IBMCLOUDOBJECTSTORAGE = "IBMCloudObjectStorage"
    MICROSOFTAZUREARCHIVESTORAGE = "MicrosoftAzureArchiveStorage"
    MICROSOFTAZUREBLOBSTORAGE = "MicrosoftAzureBlobStorage"
    S3COMPATIBLE = "S3Compatible"
    S3INTEGRATED = "S3Integrated"
    UNKNOWN = "Unknown"
    VEEAMDATACLOUDVAULT = "VeeamDataCloudVault"
    WASABICLOUDSTORAGE = "WasabiCloudStorage"

    def __str__(self) -> str:
        return str(self.value)
