import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vb_365_group_location_type import Vb365GroupLocationType
from ..models.vb_365_group_type import Vb365GroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedGroupInfo")


@_attrs_define
class Vb365ProtectedGroupInfo:
    """
    Attributes:
        group_uid (Union[Unset, UUID]): UID assigned to a group.
        group_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a group in Veeam Backup for Microsoft 365.
        group_name (Union[None, Unset, str]): Name of a group.
        managed_by (Union[None, Unset, str]): Name of a user that manages a group.
        site (Union[None, Unset, str]): URL of a group site.
        email (Union[None, Unset, str]): Group email address.
        type_ (Union[Unset, Vb365GroupType]):
        location_type (Union[Unset, Vb365GroupLocationType]):
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft organization.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[None, Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        last_protected_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
    """

    group_uid: Union[Unset, UUID] = UNSET
    group_uid_in_vb_365: Union[None, Unset, str] = UNSET
    group_name: Union[None, Unset, str] = UNSET
    managed_by: Union[None, Unset, str] = UNSET
    site: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    type_: Union[Unset, Vb365GroupType] = UNSET
    location_type: Union[Unset, Vb365GroupLocationType] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    vb_365_server_name: Union[None, Unset, str] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_uid: Union[Unset, str] = UNSET
        if not isinstance(self.group_uid, Unset):
            group_uid = str(self.group_uid)

        group_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.group_uid_in_vb_365, Unset):
            group_uid_in_vb_365 = UNSET
        else:
            group_uid_in_vb_365 = self.group_uid_in_vb_365

        group_name: Union[None, Unset, str]
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

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
        if group_uid is not UNSET:
            field_dict["groupUid"] = group_uid
        if group_uid_in_vb_365 is not UNSET:
            field_dict["groupUidInVb365"] = group_uid_in_vb_365
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if site is not UNSET:
            field_dict["site"] = site
        if email is not UNSET:
            field_dict["email"] = email
        if type_ is not UNSET:
            field_dict["type"] = type_
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
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

        def _parse_group_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))

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

        vb_365_protected_group_info = cls(
            group_uid=group_uid,
            group_uid_in_vb_365=group_uid_in_vb_365,
            group_name=group_name,
            managed_by=managed_by,
            site=site,
            email=email,
            type_=type_,
            location_type=location_type,
            organization_uid=organization_uid,
            organization_name=organization_name,
            vb_365_server_id=vb_365_server_id,
            vb_365_server_name=vb_365_server_name,
            last_protected_date=last_protected_date,
        )

        return vb_365_protected_group_info
