from enum import StrEnum


class CertificateExportType(StrEnum):
    CSV = "Csv"
    JSON = "Json"

    def __str__(self) -> str:
        return str(self.value)
