from enum import Enum


class TransactionLogBackupJobType(str, Enum):
    MICROSOFTSQLLOGBACKUP = "MicrosoftSqlLogBackup"
    ORACLESQLLOGBACKUP = "OracleSqlLogBackup"
    POSTGRESQLLOGBACKUP = "PostgreSqlLogBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
