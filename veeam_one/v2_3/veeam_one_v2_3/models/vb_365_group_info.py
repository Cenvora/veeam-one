from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_group_location_type import Vb365GroupLocationType
from ..models.vb_365_group_type import Vb365GroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365GroupInfo")


@_attrs_define
class Vb365GroupInfo:
    """
    Attributes:
        group_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 group.
        group_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a Microsoft 365 group in Veeam Backup for
            Microsoft 365.
        name (Union[None, Unset, str]): Name of a Microsoft 365 group.
        email (Union[None, Unset, str]): Email address of the Microsoft 365 group inbox.
        type_ (Union[Unset, Vb365GroupType]):
        location_type (Union[Unset, Vb365GroupLocationType]):
        managed_by (Union[None, Unset, str]): Name of a user that manages a Microsoft 365 group.
        site (Union[None, Unset, str]): URL of a Microsoft 365 organization SharePoint site.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft 365 organization.
    """

    group_uid: Union[Unset, UUID] = UNSET
    group_uid_in_vb_365: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    type_: Union[Unset, Vb365GroupType] = UNSET
    location_type: Union[Unset, Vb365GroupLocationType] = UNSET
    managed_by: Union[None, Unset, str] = UNSET
    site: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_uid: Union[Unset, str] = UNSET
        if not isinstance(self.group_uid, Unset):
            group_uid = str(self.group_uid)

        group_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.group_uid_in_vb_365, Unset):
            group_uid_in_vb_365 = UNSET
        else:
            group_uid_in_vb_365 = self.group_uid_in_vb_365

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

        location_type: Union[Unset, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        managed_by: Union[None, Unset, str]
        if isinstance(self.managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = self.managed_by

        site: Union[None, Unset, str]
        if isinstance(self.site, Unset):
            site = UNSET
        else:
            site = self.site

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
        if group_uid is not UNSET:
            field_dict["groupUid"] = group_uid
        if group_uid_in_vb_365 is not UNSET:
            field_dict["groupUidInVb365"] = group_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if site is not UNSET:
            field_dict["site"] = site
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
        _group_uid = d.pop("groupUid", UNSET)
        group_uid: Union[Unset, UUID]
        if isinstance(_group_uid, Unset):
            group_uid = UNSET
        else:
            group_uid = UUID(_group_uid)

        def _parse_group_uid_in_vb_365(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_uid_in_vb_365 = _parse_group_uid_in_vb_365(d.pop("groupUidInVb365", UNSET))

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
        type_: Union[Unset, Vb365GroupType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365GroupType(_type_)

        _location_type = d.pop("locationType", UNSET)
        location_type: Union[Unset, Vb365GroupLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = Vb365GroupLocationType(_location_type)

        def _parse_managed_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        managed_by = _parse_managed_by(d.pop("managedBy", UNSET))

        def _parse_site(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        site = _parse_site(d.pop("site", UNSET))

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

        vb_365_group_info = cls(
            group_uid=group_uid,
            group_uid_in_vb_365=group_uid_in_vb_365,
            name=name,
            email=email,
            type_=type_,
            location_type=location_type,
            managed_by=managed_by,
            site=site,
            vb_365_server_id=vb_365_server_id,
            organization_uid=organization_uid,
            organization_name=organization_name,
        )

        return vb_365_group_info
