from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedSiteInfo")


@_attrs_define
class Vb365ProtectedSiteInfo:
    """
    Attributes:
        site_uid (UUID | Unset): UID assigned to a site.
        site_uid_in_vb_365 (None | str | Unset): UID assigned to a site in Veeam Backup for Microsoft 365.
        site_name (None | str | Unset): Name of a site.
        title (None | str | Unset): Title of a site.
        url (None | str | Unset): URL of a site.
        is_cloud (bool | Unset): Indicates whether a site is located in cloud.
        is_personal (bool | Unset): Indicates whether a site is personal.
        is_available (bool | Unset): Indicates whether a site is available for backup and restore.
        organization_uid (UUID | Unset): UID assigned to a Microsoft organization.
        organization_name (None | str | Unset): Name of a Microsoft organization.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (None | str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        last_protected_date (datetime.datetime | None | Unset): Date and time when the latest restore point was created.
    """

    site_uid: UUID | Unset = UNSET
    site_uid_in_vb_365: None | str | Unset = UNSET
    site_name: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    is_cloud: bool | Unset = UNSET
    is_personal: bool | Unset = UNSET
    is_available: bool | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    organization_name: None | str | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    vb_365_server_name: None | str | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        site_uid: str | Unset = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        site_uid_in_vb_365: None | str | Unset
        if isinstance(self.site_uid_in_vb_365, Unset):
            site_uid_in_vb_365 = UNSET
        else:
            site_uid_in_vb_365 = self.site_uid_in_vb_365

        site_name: None | str | Unset
        if isinstance(self.site_name, Unset):
            site_name = UNSET
        else:
            site_name = self.site_name

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        is_cloud = self.is_cloud

        is_personal = self.is_personal

        is_available = self.is_available

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
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if site_uid_in_vb_365 is not UNSET:
            field_dict["siteUidInVb365"] = site_uid_in_vb_365
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud
        if is_personal is not UNSET:
            field_dict["isPersonal"] = is_personal
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
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
        _site_uid = d.pop("siteUid", UNSET)
        site_uid: UUID | Unset
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        def _parse_site_uid_in_vb_365(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_uid_in_vb_365 = _parse_site_uid_in_vb_365(d.pop("siteUidInVb365", UNSET))

        def _parse_site_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        site_name = _parse_site_name(d.pop("siteName", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        is_cloud = d.pop("isCloud", UNSET)

        is_personal = d.pop("isPersonal", UNSET)

        is_available = d.pop("isAvailable", UNSET)

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

        vb_365_protected_site_info = cls(
            site_uid=site_uid,
            site_uid_in_vb_365=site_uid_in_vb_365,
            site_name=site_name,
            title=title,
            url=url,
            is_cloud=is_cloud,
            is_personal=is_personal,
            is_available=is_available,
            organization_uid=organization_uid,
            organization_name=organization_name,
            vb_365_server_id=vb_365_server_id,
            vb_365_server_name=vb_365_server_name,
            last_protected_date=last_protected_date,
        )

        return vb_365_protected_site_info
