from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_group_location_type import Vb365GroupLocationType
from ..models.vb_365_group_type import Vb365GroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedGroupInfo")


@_attrs_define
class Vb365ProtectedGroupInfo:
    """
    Attributes:
        group_uid (UUID | Unset): UID assigned to a group.
        group_uid_in_vb_365 (None | str | Unset): UID assigned to a group in Veeam Backup for Microsoft 365.
        group_name (None | str | Unset): Name of a group.
        managed_by (None | str | Unset): Name of a user that manages a group.
        site (None | str | Unset): URL of a group site.
        email (None | str | Unset): Group email address.
        type_ (Vb365GroupType | Unset):
        location_type (Vb365GroupLocationType | Unset):
        organization_uid (UUID | Unset): UID assigned to a Microsoft organization.
        organization_name (None | str | Unset): Name of a Microsoft organization.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (None | str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        last_protected_date (datetime.datetime | None | Unset): Date and time when the latest restore point was created.
    """

    group_uid: UUID | Unset = UNSET
    group_uid_in_vb_365: None | str | Unset = UNSET
    group_name: None | str | Unset = UNSET
    managed_by: None | str | Unset = UNSET
    site: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    type_: Vb365GroupType | Unset = UNSET
    location_type: Vb365GroupLocationType | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    organization_name: None | str | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    vb_365_server_name: None | str | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_uid: str | Unset = UNSET
        if not isinstance(self.group_uid, Unset):
            group_uid = str(self.group_uid)

        group_uid_in_vb_365: None | str | Unset
        if isinstance(self.group_uid_in_vb_365, Unset):
            group_uid_in_vb_365 = UNSET
        else:
            group_uid_in_vb_365 = self.group_uid_in_vb_365

        group_name: None | str | Unset
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        managed_by: None | str | Unset
        if isinstance(self.managed_by, Unset):
            managed_by = UNSET
        else:
            managed_by = self.managed_by

        site: None | str | Unset
        if isinstance(self.site, Unset):
            site = UNSET
        else:
            site = self.site

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        location_type: str | Unset = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

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
        group_uid: UUID | Unset
        if isinstance(_group_uid, Unset):
            group_uid = UNSET
        else:
            group_uid = UUID(_group_uid)

        def _parse_group_uid_in_vb_365(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_uid_in_vb_365 = _parse_group_uid_in_vb_365(d.pop("groupUidInVb365", UNSET))

        def _parse_group_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))

        def _parse_managed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        managed_by = _parse_managed_by(d.pop("managedBy", UNSET))

        def _parse_site(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site = _parse_site(d.pop("site", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Vb365GroupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365GroupType(_type_)

        _location_type = d.pop("locationType", UNSET)
        location_type: Vb365GroupLocationType | Unset
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = Vb365GroupLocationType(_location_type)

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
