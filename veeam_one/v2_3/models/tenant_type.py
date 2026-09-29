from enum import StrEnum


class TenantType(StrEnum):
    ACTIVEDIRECTORY = "ActiveDirectory"
    CLOUDDIRECTOR = "CloudDirector"
    STANDALONE = "Standalone"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
