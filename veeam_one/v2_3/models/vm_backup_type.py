from enum import Enum


class VmBackupType(str, Enum):
    BACKUPCOPYIMMEDIATE = "BackupCopyImmediate"
    BACKUPCOPYIMMEDIATEPARENTWORKER = "BackupCopyImmediateParentWorker"
    BACKUPCOPYIMMEDIATEWORKER = "BackupCopyImmediateWorker"
    BACKUPCOPYPERIODIC = "BackupCopyPeriodic"
    BACKUPTOTAPE = "BackupToTape"
    CDPPOLICY = "CDPPolicy"
    HPEVME = "HpeVme"
    KVMBACKUP = "KvmBackup"
    NUTANIXAHVBACKUP = "NutanixAhvBackup"
    PROXMOXVEBACKUP = "ProxmoxVeBackup"
    REPLICATION = "Replication"
    SANGFOR = "Sangfor"
    SCALECOMPUTING = "ScaleComputing"
    UNKNOWN = "Unknown"
    VMBACKUP = "VMBackup"
    XCPING = "XCPing"

    def __str__(self) -> str:
        return str(self.value)
