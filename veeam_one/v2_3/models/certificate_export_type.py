from enum import Enum


class CertificateExportType(str, Enum):
    CSV = "Csv"
    JSON = "Json"

    def __str__(self) -> str:
        return str(self.value)
