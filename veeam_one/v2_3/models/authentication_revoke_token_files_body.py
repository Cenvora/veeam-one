from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticationRevokeTokenFilesBody")


@_attrs_define
class AuthenticationRevokeTokenFilesBody:
    """
    Attributes:
        token (str | Unset):
        user_sid (str | Unset):
    """

    token: str | Unset = UNSET
    user_sid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        user_sid = self.user_sid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if user_sid is not UNSET:
            field_dict["UserSid"] = user_sid

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.token, Unset):
            files.append(("token", (None, str(self.token).encode(), "text/plain")))

        if not isinstance(self.user_sid, Unset):
            files.append(("UserSid", (None, str(self.user_sid).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        user_sid = d.pop("UserSid", UNSET)

        authentication_revoke_token_files_body = cls(
            token=token,
            user_sid=user_sid,
        )

        authentication_revoke_token_files_body.additional_properties = d
        return authentication_revoke_token_files_body

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
