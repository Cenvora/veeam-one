from enum import StrEnum


class LicenseUsageReportStatus(StrEnum):
    APPROVED = "Approved"
    DRAFT = "Draft"

    def __str__(self) -> str:
        return str(self.value)
