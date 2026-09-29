from enum import Enum


class ExtentRepositoryType(str, Enum):
    OBJECTSTORAGE = "ObjectStorage"
    REGULAR = "Regular"

    def __str__(self) -> str:
        return str(self.value)
