from enum import StrEnum


class Vb365BackupType(StrEnum):
    ENTIREORGANIZATION = "EntireOrganization"
    SELECTEDITEMS = "SelectedItems"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
