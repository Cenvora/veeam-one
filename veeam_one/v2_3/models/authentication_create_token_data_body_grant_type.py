from enum import StrEnum


class AuthenticationCreateTokenDataBodyGrantType(StrEnum):
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
