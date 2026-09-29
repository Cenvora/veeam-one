from enum import Enum


class CredentialsType(str, Enum):
    INVALID = "Invalid"
    PASSWORD = "Password"
    SSHKEY = "SshKey"

    def __str__(self) -> str:
        return str(self.value)
