import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vb_365_user_type import Vb365UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedUserInfo")


@_attrs_define
class Vb365ProtectedUserInfo:
    """
    Attributes:
        user_uid (Union[Unset, UUID]): UID assigned to a protected user.
        user_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a user in Veeam Backup for Microsoft 365.
        user_name (Union[None, Unset, str]): User name.
        email (Union[None, Unset, str]): User email address.
        type_ (Union[Unset, Vb365UserType]):
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft organization.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[None, Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        last_protected_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
    """

    user_uid: Union[Unset, UUID] = UNSET
    user_uid_in_vb_365: Union[None, Unset, str] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    type_: Union[Unset, Vb365UserType] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    vb_365_server_name: Union[None, Unset, str] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_uid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        user_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.user_uid_in_vb_365, Unset):
            user_uid_in_vb_365 = UNSET
        else:
            user_uid_in_vb_365 = self.user_uid_in_vb_365

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        vb_365_server_id = self.vb_365_server_id

        vb_365_server_name: Union[None, Unset, str]
        if isinstance(self.vb_365_server_name, Unset):
            vb_365_server_name = UNSET
        else:
            vb_365_server_name = self.vb_365_server_name

        last_protected_date: Union[None, Unset, str]
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
        user_uid: Union[Unset, UUID]
        if isinstance(_user_uid, Unset):
            user_uid = UNSET
        else:
            user_uid = UUID(_user_uid)

        def _parse_user_uid_in_vb_365(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_uid_in_vb_365 = _parse_user_uid_in_vb_365(d.pop("userUidInVb365", UNSET))

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Vb365UserType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365UserType(_type_)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_vb_365_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vb_365_server_name = _parse_vb_365_server_name(d.pop("vb365ServerName", UNSET))

        def _parse_last_protected_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = isoparse(data)

                return last_protected_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

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
