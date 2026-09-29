from enum import Enum


class LicenseUsageReportStatus(str, Enum):
    APPROVED = "Approved"
    DRAFT = "Draft"

    def __str__(self) -> str:
        return str(self.value)
