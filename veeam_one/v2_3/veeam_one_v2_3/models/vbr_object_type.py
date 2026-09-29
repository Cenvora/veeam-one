from enum import Enum


class VbrObjectType(str, Enum):
    ARCHIVEREPOSITORY = "ArchiveRepository"
    BACKUP = "Backup"
    BACKUPPROXY = "BackupProxy"
    BACKUPPROXYFOLDER = "BackupProxyFolder"
    BACKUPREPOSITORY = "BackupRepository"
    BACKUPREPOSITORYFOLDER = "BackupRepositoryFolder"
    BACKUPSERVER = "BackupServer"
    CDPPROXYFOLDER = "CdpProxyFolder"
    CLOUDGATEWAY = "CloudGateway"
    CLOUDGATEWAYFOLDER = "CloudGatewayFolder"
    CLOUDGATEWAYPOOL = "CloudGatewayPool"
    CLOUDREPOSITORY = "CloudRepository"
    ENTERPRISEMANAGER = "EnterpriseManager"
    EXTERNALREPOSITORY = "ExternalRepository"
    FILEPROXYFOLDER = "FileProxyFolder"
    JOB = "Job"
    TAPESERVER = "TapeServer"
    TAPESERVERFOLDER = "TapeServerFolder"
    TENANTBACKUPREPOSITORYFOLDER = "TenantBackupRepositoryFolder"
    VBRINFRASTRUCTURE = "VbrInfrastructure"
    VMPROXYFOLDER = "VmProxyFolder"
    WANACCELERATOR = "WanAccelerator"
    WANACCELERATORFOLDER = "WanAcceleratorFolder"

    def __str__(self) -> str:
        return str(self.value)
