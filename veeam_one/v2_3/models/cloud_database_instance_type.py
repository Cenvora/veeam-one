from enum import StrEnum


class CloudDatabaseInstanceType(StrEnum):
    CLOUDSPANNER = "CloudSpanner"
    CLOUDSQL = "CloudSQL"
    COSMOSDB = "CosmosDB"
    DYNAMODB = "DynamoDB"
    RDS = "RDS"
    REDSHIFT = "Redshift"
    REDSHIFTSERVERLESS = "RedshiftServerless"
    SQLDATABASE = "SQLDatabase"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
