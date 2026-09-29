from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialSaveRequest")


@_attrs_define
class CredentialSaveRequest:
    """
    Attributes:
        type_ (str): Type of credentials. Default: 'Password'.
        user_name (None | str | Unset): User name.
        password (None | str | Unset): Password.
        description (None | str | Unset): Description.
        ssh_key (None | str | Unset): SSH key.
        ssh_key_password (None | str | Unset): SSH key password.
    """

    type_: str = "Password"
    user_name: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    ssh_key: None | str | Unset = UNSET
    ssh_key_password: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        ssh_key: None | str | Unset
        if isinstance(self.ssh_key, Unset):
            ssh_key = UNSET
        else:
            ssh_key = self.ssh_key

        ssh_key_password: None | str | Unset
        if isinstance(self.ssh_key_password, Unset):
            ssh_key_password = UNSET
        else:
            ssh_key_password = self.ssh_key_password

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if password is not UNSET:
            field_dict["password"] = password
        if description is not UNSET:
            field_dict["description"] = description
        if ssh_key is not UNSET:
            field_dict["sshKey"] = ssh_key
        if ssh_key_password is not UNSET:
            field_dict["sshKeyPassword"] = ssh_key_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_ssh_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_key = _parse_ssh_key(d.pop("sshKey", UNSET))

        def _parse_ssh_key_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ssh_key_password = _parse_ssh_key_password(d.pop("sshKeyPassword", UNSET))

        credential_save_request = cls(
            type_=type_,
            user_name=user_name,
            password=password,
            description=description,
            ssh_key=ssh_key,
            ssh_key_password=ssh_key_password,
        )

        return credential_save_request
