from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.authentication_create_token_data_body_grant_type import AuthenticationCreateTokenDataBodyGrantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationCreateTokenDataBody")


@_attrs_define
class AuthenticationCreateTokenDataBody:
    """
    Attributes:
        grant_type (AuthenticationCreateTokenDataBodyGrantType):  Default:
            AuthenticationCreateTokenDataBodyGrantType.PASSWORD.
        username (str | Unset):
        password (str | Unset):
        refresh_token (str | Unset):
    """

    grant_type: AuthenticationCreateTokenDataBodyGrantType = AuthenticationCreateTokenDataBodyGrantType.PASSWORD
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

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grant_type = AuthenticationCreateTokenDataBodyGrantType(d.pop("grant_type"))

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        refresh_token = d.pop("refresh_token", UNSET)

        authentication_create_token_data_body = cls(
            grant_type=grant_type,
            username=username,
            password=password,
            refresh_token=refresh_token,
        )

        authentication_create_token_data_body.additional_properties = d
        return authentication_create_token_data_body

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
