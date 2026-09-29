from enum import StrEnum


class BackupRepositoryType(StrEnum):
    AMAZONS3 = "AmazonS3"
    AMAZONS3GLACIER = "AmazonS3Glacier"
    CLOUD = "Cloud"
    DELLEMCDATADOMAIN = "DellEMCDataDomain"
    EXAGRID = "ExaGrid"
    FOREIGN = "Foreign"
    FUJITSUCS800 = "FujitsuCS800"
    GOOGLECLOUDARCHIVESTORAGE = "GoogleCloudArchiveStorage"
    GOOGLECLOUDSTORAGE = "GoogleCloudStorage"
    HPESTOREONCE = "HPEStoreOnce"
    IBMCLOUDOBJECTSTORAGE = "IBMCloudObjectStorage"
    INFINIDATINFINIGUARD = "InfinidatInfiniGuard"
    LINUX = "Linux"
    LINUXHARDENED = "LinuxHardened"
    MICROSOFTAZUREARCHIVESTORAGE = "MicrosoftAzureArchiveStorage"
    MICROSOFTAZUREBLOBSTORAGE = "MicrosoftAzureBlobStorage"
    MICROSOFTWINDOWS = "MicrosoftWindows"
    NFS = "NFS"
    QUANTUMDXI = "QuantumDXi"
    S3COMPATIBLE = "S3Compatible"
    S3INTEGRATED = "S3Integrated"
    SCALEOUT = "ScaleOut"
    SMB = "SMB"
    SNAPSHOTONLY = "SnapshotOnly"
    UNKNOWN = "Unknown"
    VEEAMDATACLOUDVAULT = "VeeamDataCloudVault"
    WASABICLOUDSTORAGE = "WasabiCloudStorage"

    def __str__(self) -> str:
        return str(self.value)
