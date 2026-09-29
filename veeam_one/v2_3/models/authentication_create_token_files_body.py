from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.authentication_create_token_files_body_grant_type import AuthenticationCreateTokenFilesBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationCreateTokenFilesBody")


@_attrs_define
class AuthenticationCreateTokenFilesBody:
    """
    Attributes:
        grant_type (AuthenticationCreateTokenFilesBodyGrantType):  Default:
            AuthenticationCreateTokenFilesBodyGrantType.PASSWORD.
        username (str | Unset):
        password (str | Unset):
        refresh_token (str | Unset):
    """

    grant_type: AuthenticationCreateTokenFilesBodyGrantType = AuthenticationCreateTokenFilesBodyGrantType.PASSWORD
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    refresh_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grant_type = self.grant_type.value

        username = self.username

        password = self.password

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("grant_type", (None, str(self.grant_type.value).encode(), "text/plain")))

        if not isinstance(self.username, Unset):
            files.append(("username", (None, str(self.username).encode(), "text/plain")))

        if not isinstance(self.password, Unset):
            files.append(("password", (None, str(self.password).encode(), "text/plain")))

        if not isinstance(self.refresh_token, Unset):
            files.append(("refresh_token", (None, str(self.refresh_token).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = AuthenticationCreateTokenFilesBodyGrantType(d.pop("grant_type"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        authentication_create_token_files_body = cls(
            grant_type=grant_type,
            username=username,
            password=password,
            refresh_token=refresh_token,
        )

        authentication_create_token_files_body.additional_properties = d
        return authentication_create_token_files_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
