from enum import StrEnum


class CredentialsType(StrEnum):
    INVALID = "Invalid"
    PASSWORD = "Password"
    SSHKEY = "SshKey"

    def __str__(self) -> str:
        return str(self.value)
