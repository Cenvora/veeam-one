import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vb_365_organization_region import Vb365OrganizationRegion
from ..models.vb_365_organization_type import Vb365OrganizationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365OrganizationInfo")


@_attrs_define
class Vb365OrganizationInfo:
    """
    Attributes:
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 organization.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        name (Union[None, Unset, str]): Name of a Microsoft 365 organization.
        office_name (Union[None, Unset, str]): Microsoft 365 Online name.
        type_ (Union[Unset, Vb365OrganizationType]):
        region (Union[Unset, Vb365OrganizationRegion]):
        is_backedup (Union[None, Unset, bool]): Indicates whether the Microsoft 365 organization files are protected by
            a backup job.
        first_backup_time (Union[None, Unset, datetime.datetime]): Date and time of the first backup job run protecting
            Microsoft 365 organization files.
        last_backup_time (Union[None, Unset, datetime.datetime]): Date and time of the latest backup job run protecting
            Microsoft 365 organization files.
        is_exchange_online (Union[None, Unset, bool]): Indicates whether a Microsoft 365 organization contains Microsoft
            Exchange components.
        is_share_point_online (Union[None, Unset, bool]): Indicates whether a Microsoft 365 organization contains
            Microsoft SharePoint components.
        is_teams_online (Union[None, Unset, bool]): Indicates whether a Microsoft 365 organization contains Microsoft
            Teams components.
    """

    organization_uid: Union[Unset, UUID] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    office_name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, Vb365OrganizationType] = UNSET
    region: Union[Unset, Vb365OrganizationRegion] = UNSET
    is_backedup: Union[None, Unset, bool] = UNSET
    first_backup_time: Union[None, Unset, datetime.datetime] = UNSET
    last_backup_time: Union[None, Unset, datetime.datetime] = UNSET
    is_exchange_online: Union[None, Unset, bool] = UNSET
    is_share_point_online: Union[None, Unset, bool] = UNSET
    is_teams_online: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        vb_365_server_id = self.vb_365_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        office_name: Union[None, Unset, str]
        if isinstance(self.office_name, Unset):
            office_name = UNSET
        else:
            office_name = self.office_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        region: Union[Unset, str] = UNSET
        if not isinstance(self.region, Unset):
            region = self.region.value

        is_backedup: Union[None, Unset, bool]
        if isinstance(self.is_backedup, Unset):
            is_backedup = UNSET
        else:
            is_backedup = self.is_backedup

        first_backup_time: Union[None, Unset, str]
        if isinstance(self.first_backup_time, Unset):
            first_backup_time = UNSET
        elif isinstance(self.first_backup_time, datetime.datetime):
            first_backup_time = self.first_backup_time.isoformat()
        else:
            first_backup_time = self.first_backup_time

        last_backup_time: Union[None, Unset, str]
        if isinstance(self.last_backup_time, Unset):
            last_backup_time = UNSET
        elif isinstance(self.last_backup_time, datetime.datetime):
            last_backup_time = self.last_backup_time.isoformat()
        else:
            last_backup_time = self.last_backup_time

        is_exchange_online: Union[None, Unset, bool]
        if isinstance(self.is_exchange_online, Unset):
            is_exchange_online = UNSET
        else:
            is_exchange_online = self.is_exchange_online

        is_share_point_online: Union[None, Unset, bool]
        if isinstance(self.is_share_point_online, Unset):
            is_share_point_online = UNSET
        else:
            is_share_point_online = self.is_share_point_online

        is_teams_online: Union[None, Unset, bool]
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
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_office_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        office_name = _parse_office_name(d.pop("officeName", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Vb365OrganizationType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365OrganizationType(_type_)

        _region = d.pop("region", UNSET)
        region: Union[Unset, Vb365OrganizationRegion]
        if isinstance(_region, Unset):
            region = UNSET
        else:
            region = Vb365OrganizationRegion(_region)

        def _parse_is_backedup(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_backedup = _parse_is_backedup(d.pop("isBackedup", UNSET))

        def _parse_first_backup_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_backup_time_type_0 = isoparse(data)

                return first_backup_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        first_backup_time = _parse_first_backup_time(d.pop("firstBackupTime", UNSET))

        def _parse_last_backup_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_time_type_0 = isoparse(data)

                return last_backup_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_backup_time = _parse_last_backup_time(d.pop("lastBackupTime", UNSET))

        def _parse_is_exchange_online(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_exchange_online = _parse_is_exchange_online(d.pop("isExchangeOnline", UNSET))

        def _parse_is_share_point_online(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_share_point_online = _parse_is_share_point_online(d.pop("isSharePointOnline", UNSET))

        def _parse_is_teams_online(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

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
