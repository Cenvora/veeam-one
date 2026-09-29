from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_organization_region import Vb365OrganizationRegion
from ..models.vb_365_organization_type import Vb365OrganizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365OrganizationInfo")


@_attrs_define
class Vb365OrganizationInfo:
    """
    Attributes:
        organization_uid (UUID | Unset): UID assigned to a Microsoft 365 organization.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        name (None | str | Unset): Name of a Microsoft 365 organization.
        office_name (None | str | Unset): Microsoft 365 Online name.
        type_ (Vb365OrganizationType | Unset):
        region (Vb365OrganizationRegion | Unset):
        is_backedup (bool | None | Unset): Indicates whether the Microsoft 365 organization files are protected by a
            backup job.
        first_backup_time (datetime.datetime | None | Unset): Date and time of the first backup job run protecting
            Microsoft 365 organization files.
        last_backup_time (datetime.datetime | None | Unset): Date and time of the latest backup job run protecting
            Microsoft 365 organization files.
        is_exchange_online (bool | None | Unset): Indicates whether a Microsoft 365 organization contains Microsoft
            Exchange components.
        is_share_point_online (bool | None | Unset): Indicates whether a Microsoft 365 organization contains Microsoft
            SharePoint components.
        is_teams_online (bool | None | Unset): Indicates whether a Microsoft 365 organization contains Microsoft Teams
            components.
    """

    organization_uid: UUID | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    office_name: None | str | Unset = UNSET
    type_: Vb365OrganizationType | Unset = UNSET
    region: Vb365OrganizationRegion | Unset = UNSET
    is_backedup: bool | None | Unset = UNSET
    first_backup_time: datetime.datetime | None | Unset = UNSET
    last_backup_time: datetime.datetime | None | Unset = UNSET
    is_exchange_online: bool | None | Unset = UNSET
    is_share_point_online: bool | None | Unset = UNSET
    is_teams_online: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        vb_365_server_id = self.vb_365_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        office_name: None | str | Unset
        if isinstance(self.office_name, Unset):
            office_name = UNSET
        else:
            office_name = self.office_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        region: str | Unset = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        is_backedup: bool | None | Unset
        if isinstance(self.is_backedup, Unset):
            is_backedup = UNSET
        else:
            is_backedup = self.is_backedup

        first_backup_time: None | str | Unset
        if isinstance(self.first_backup_time, Unset):
            first_backup_time = UNSET
        elif isinstance(self.first_backup_time, datetime.datetime):
            first_backup_time = self.first_backup_time.isoformat()
        else:
            first_backup_time = self.first_backup_time

        last_backup_time: None | str | Unset
        if isinstance(self.last_backup_time, Unset):
            last_backup_time = UNSET
        elif isinstance(self.last_backup_time, datetime.datetime):
            last_backup_time = self.last_backup_time.isoformat()
        else:
            last_backup_time = self.last_backup_time

        is_exchange_online: bool | None | Unset
        if isinstance(self.is_exchange_online, Unset):
            is_exchange_online = UNSET
        else:
            is_exchange_online = self.is_exchange_online

        is_share_point_online: bool | None | Unset
        if isinstance(self.is_share_point_online, Unset):
            is_share_point_online = UNSET
        else:
            is_share_point_online = self.is_share_point_online

        is_teams_online: bool | None | Unset
        if isinstance(self.is_teams_online, Unset):
            is_teams_online = UNSET
        else:
            is_teams_online = self.is_teams_online

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if office_name is not UNSET:
            field_dict["officeName"] = office_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if region is not UNSET:
            field_dict["region"] = region
        if is_backedup is not UNSET:
            field_dict["isBackedup"] = is_backedup
        if first_backup_time is not UNSET:
            field_dict["firstBackupTime"] = first_backup_time
        if last_backup_time is not UNSET:
            field_dict["lastBackupTime"] = last_backup_time
        if is_exchange_online is not UNSET:
            field_dict["isExchangeOnline"] = is_exchange_online
        if is_share_point_online is not UNSET:
            field_dict["isSharePointOnline"] = is_share_point_online
        if is_teams_online is not UNSET:
            field_dict["isTeamsOnline"] = is_teams_online

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_office_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        office_name = _parse_office_name(d.pop("officeName", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Vb365OrganizationType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365OrganizationType(_type_)

        _region = d.pop("region", UNSET)
        region: Vb365OrganizationRegion | Unset
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationRegion(_region)

        def _parse_is_backedup(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_backedup = _parse_is_backedup(d.pop("isBackedup", UNSET))

        def _parse_first_backup_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_backup_time_type_0 = datetime.datetime.fromisoformat(data)

                return first_backup_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_backup_time = _parse_first_backup_time(d.pop("firstBackupTime", UNSET))

        def _parse_last_backup_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_time_type_0 = datetime.datetime.fromisoformat(data)

                return last_backup_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_time = _parse_last_backup_time(d.pop("lastBackupTime", UNSET))

        def _parse_is_exchange_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_exchange_online = _parse_is_exchange_online(d.pop("isExchangeOnline", UNSET))

        def _parse_is_share_point_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_share_point_online = _parse_is_share_point_online(d.pop("isSharePointOnline", UNSET))

        def _parse_is_teams_online(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_teams_online = _parse_is_teams_online(d.pop("isTeamsOnline", UNSET))

        vb_365_organization_info = cls(
            organization_uid=organization_uid,
            vb_365_server_id=vb_365_server_id,
            name=name,
            office_name=office_name,
            type_=type_,
            region=region,
            is_backedup=is_backedup,
            first_backup_time=first_backup_time,
            last_backup_time=last_backup_time,
            is_exchange_online=is_exchange_online,
            is_share_point_online=is_share_point_online,
            is_teams_online=is_teams_online,
        )

        return vb_365_organization_info
