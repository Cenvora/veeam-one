from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_user_type import Vb365UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedUserInfo")


@_attrs_define
class Vb365ProtectedUserInfo:
    """
    Attributes:
        user_uid (UUID | Unset): UID assigned to a protected user.
        user_uid_in_vb_365 (None | str | Unset): UID assigned to a user in Veeam Backup for Microsoft 365.
        user_name (None | str | Unset): User name.
        email (None | str | Unset): User email address.
        type_ (Vb365UserType | Unset):
        organization_uid (UUID | Unset): UID assigned to a Microsoft organization.
        organization_name (None | str | Unset): Name of a Microsoft organization.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (None | str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        last_protected_date (datetime.datetime | None | Unset): Date and time when the latest restore point was created.
    """

    user_uid: UUID | Unset = UNSET
    user_uid_in_vb_365: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    type_: Vb365UserType | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    organization_name: None | str | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    vb_365_server_name: None | str | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_uid: str | Unset = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        user_uid_in_vb_365: None | str | Unset
        if isinstance(self.user_uid_in_vb_365, Unset):
            user_uid_in_vb_365 = UNSET
        else:
            user_uid_in_vb_365 = self.user_uid_in_vb_365

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: None | str | Unset
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        vb_365_server_id = self.vb_365_server_id

        vb_365_server_name: None | str | Unset
        if isinstance(self.vb_365_server_name, Unset):
            vb_365_server_name = UNSET
        else:
            vb_365_server_name = self.vb_365_server_name

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if user_uid_in_vb_365 is not UNSET:
            field_dict["userUidInVb365"] = user_uid_in_vb_365
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_uid = d.pop("userUid", UNSET)
        user_uid: UUID | Unset
        if isinstance(_user_uid, Unset):
            user_uid = UNSET
        else:
            user_uid = UUID(_user_uid)

        def _parse_user_uid_in_vb_365(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_uid_in_vb_365 = _parse_user_uid_in_vb_365(d.pop("userUidInVb365", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Vb365UserType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365UserType(_type_)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_vb_365_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vb_365_server_name = _parse_vb_365_server_name(d.pop("vb365ServerName", UNSET))

        def _parse_last_protected_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protected_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

        vb_365_protected_user_info = cls(
            user_uid=user_uid,
            user_uid_in_vb_365=user_uid_in_vb_365,
            user_name=user_name,
            email=email,
            type_=type_,
            organization_uid=organization_uid,
            organization_name=organization_name,
            vb_365_server_id=vb_365_server_id,
            vb_365_server_name=vb_365_server_name,
            last_protected_date=last_protected_date,
        )

        return vb_365_protected_user_info
