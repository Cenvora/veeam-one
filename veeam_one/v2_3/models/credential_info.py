from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.credentials_type import CredentialsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialInfo")


@_attrs_define
class CredentialInfo:
    """
    Attributes:
        credentials_id (int | Unset): ID assigned to a set of credentials.
        type_ (CredentialsType | Unset):
        user_name (None | str | Unset): User name.
        description (None | str | Unset): Description.
        last_modified (datetime.datetime | Unset): Date and time of the latest credentials modification.
        currently_assigned (bool | Unset): Indicates whether credentials are assigned to a user.
        is_propagated (bool | Unset): Indicates whether credentials of a parent object account are used.
    """

    credentials_id: int | Unset = UNSET
    type_: CredentialsType | Unset = UNSET
    user_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    last_modified: datetime.datetime | Unset = UNSET
    currently_assigned: bool | Unset = UNSET
    is_propagated: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credentials_id = self.credentials_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_modified: str | Unset = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        currently_assigned = self.currently_assigned

        is_propagated = self.is_propagated

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if currently_assigned is not UNSET:
            field_dict["currentlyAssigned"] = currently_assigned
        if is_propagated is not UNSET:
            field_dict["isPropagated"] = is_propagated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credentials_id = d.pop("credentialsId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CredentialsType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CredentialsType(_type_)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: datetime.datetime | Unset
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = datetime.datetime.fromisoformat(_last_modified)

        currently_assigned = d.pop("currentlyAssigned", UNSET)

        is_propagated = d.pop("isPropagated", UNSET)

        credential_info = cls(
            credentials_id=credentials_id,
            type_=type_,
            user_name=user_name,
            description=description,
            last_modified=last_modified,
            currently_assigned=currently_assigned,
            is_propagated=is_propagated,
        )

        return credential_info
