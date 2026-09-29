from enum import StrEnum


class ApplicationPlatform(StrEnum):
    MSSQLPLUGINWINDOWS = "MsSqlPluginWindows"
    ORACLE = "Oracle"
    SAPHANA = "SapHana"
    SAPONORACLE = "SapOnOracle"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
