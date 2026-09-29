from enum import Enum


class AuthenticationCreateTokenFilesBodyGrantType(str, Enum):
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
