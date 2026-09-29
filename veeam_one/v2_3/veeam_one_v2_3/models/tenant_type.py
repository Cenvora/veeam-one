from enum import Enum


class TenantType(str, Enum):
    ACTIVEDIRECTORY = "ActiveDirectory"
    CLOUDDIRECTOR = "CloudDirector"
    STANDALONE = "Standalone"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
