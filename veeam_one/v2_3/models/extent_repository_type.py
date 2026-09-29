from enum import StrEnum


class ExtentRepositoryType(StrEnum):
    OBJECTSTORAGE = "ObjectStorage"
    REGULAR = "Regular"

    def __str__(self) -> str:
        return str(self.value)
