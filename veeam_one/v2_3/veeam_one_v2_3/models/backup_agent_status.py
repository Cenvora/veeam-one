from enum import Enum


class BackupAgentStatus(str, Enum):
    EXCLUDE = "Exclude"
    FAILED = "Failed"
    INSTALLED = "Installed"
    NOTINITIALIZED = "NotInitialized"
    NOTINSTALLED = "NotInstalled"
    NOTSET = "NotSet"
    REBOOTREQUIRED = "RebootRequired"
    UNSUPPORTEDOS = "UnsupportedOs"

    def __str__(self) -> str:
        return str(self.value)
