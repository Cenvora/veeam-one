from enum import Enum


class ApplicationJobPlatform(str, Enum):
    KASTEN = "Kasten"
    MSSQLPLUGINBASE = "MsSqlPluginBase"
    MSSQLPLUGINWINDOWS = "MsSqlPluginWindows"
    ORACLE = "Oracle"
    SAPHANA = "SapHana"
    SAPONORACLE = "SapOnOracle"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
