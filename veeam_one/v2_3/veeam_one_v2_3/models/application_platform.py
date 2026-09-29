from enum import Enum


class ApplicationPlatform(str, Enum):
    MSSQLPLUGINWINDOWS = "MsSqlPluginWindows"
    ORACLE = "Oracle"
    SAPHANA = "SapHana"
    SAPONORACLE = "SapOnOracle"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
