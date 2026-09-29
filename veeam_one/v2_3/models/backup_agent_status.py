from enum import StrEnum


class BackupAgentStatus(StrEnum):
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
