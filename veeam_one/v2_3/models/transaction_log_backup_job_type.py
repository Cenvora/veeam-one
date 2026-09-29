from enum import StrEnum


class TransactionLogBackupJobType(StrEnum):
    MICROSOFTSQLLOGBACKUP = "MicrosoftSqlLogBackup"
    ORACLESQLLOGBACKUP = "OracleSqlLogBackup"
    POSTGRESQLLOGBACKUP = "PostgreSqlLogBackup"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
