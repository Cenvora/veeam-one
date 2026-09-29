from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_user_type import Vb365UserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365UserInfo")


@_attrs_define
class Vb365UserInfo:
    """
    Attributes:
        user_uid (Union[Unset, UUID]): UID assigned to a user.
        user_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a user in Veeam Backup for Microsoft 365.
        name (Union[None, Unset, str]): User name.
        email (Union[None, Unset, str]): User email address.
        type_ (Union[Unset, Vb365UserType]):
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 organization to which a user belongs.
        organization_name (Union[None, Unset, str]): Name of a Microsoft 365 organization to which a user belongs.
    """

    user_uid: Union[Unset, UUID] = UNSET
    user_uid_in_vb_365: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    type_: Union[Unset, Vb365UserType] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_uid: Union[Unset, str] = UNSET
        if not isinstance(self.user_uid, Unset):
            user_uid = str(self.user_uid)

        user_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.user_uid_in_vb_365, Unset):
            user_uid_in_vb_365 = UNSET
        else:
            user_uid_in_vb_365 = self.user_uid_in_vb_365

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        vb_365_server_id = self.vb_365_server_id

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if user_uid_in_vb_365 is not UNSET:
            field_dict["userUidInVb365"] = user_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

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

        vb_365_user_info = cls(
            user_uid=user_uid,
            user_uid_in_vb_365=user_uid_in_vb_365,
            name=name,
            email=email,
            type_=type_,
            vb_365_server_id=vb_365_server_id,
            organization_uid=organization_uid,
            organization_name=organization_name,
        )

        return vb_365_user_info
