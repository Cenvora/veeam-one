from enum import Enum


class ComputerPlatform(str, Enum):
    CUSTOM = "Custom"
    IBMAIX = "IbmAix"
    LINUX = "Linux"
    MACOS = "MacOs"
    MICROSOFTWINDOWS = "MicrosoftWindows"
    ORACLESOLARIS = "OracleSolaris"
    UNIX = "Unix"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
