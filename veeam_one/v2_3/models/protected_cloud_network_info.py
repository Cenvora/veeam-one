import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.cloud_platform import CloudPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudNetworkInfo")


@_attrs_define
class ProtectedCloudNetworkInfo:
    """
    Attributes:
        cloud_network_uid_in_vbr (Union[Unset, UUID]): UID assigned to a cloud network.
        name (Union[None, Unset, str]): Name of a cloud network.
        platform (Union[Unset, CloudPlatform]):
        region (Union[None, Unset, str]): Date and time when the latest restore point was created.
        last_protection_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
    """

    cloud_network_uid_in_vbr: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    platform: Union[Unset, CloudPlatform] = UNSET
    region: Union[None, Unset, str] = UNSET
    last_protection_date: Union[None, Unset, datetime.datetime] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_network_uid_in_vbr: Union[Unset, str] = UNSET
        if not isinstance(self.cloud_network_uid_in_vbr, Unset):
            cloud_network_uid_in_vbr = str(self.cloud_network_uid_in_vbr)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        last_protection_date: Union[None, Unset, str]
        if isinstance(self.last_protection_date, Unset):
            last_protection_date = UNSET
        elif isinstance(self.last_protection_date, datetime.datetime):
            last_protection_date = self.last_protection_date.isoformat()
        else:
            last_protection_date = self.last_protection_date

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_network_uid_in_vbr is not UNSET:
            field_dict["cloudNetworkUidInVbr"] = cloud_network_uid_in_vbr
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if region is not UNSET:
            field_dict["region"] = region
        if last_protection_date is not UNSET:
            field_dict["lastProtectionDate"] = last_protection_date
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _cloud_network_uid_in_vbr = d.pop("cloudNetworkUidInVbr", UNSET)
        cloud_network_uid_in_vbr: Union[Unset, UUID]
        if isinstance(_cloud_network_uid_in_vbr, Unset):
            cloud_network_uid_in_vbr = UNSET
        else:
            cloud_network_uid_in_vbr = UUID(_cloud_network_uid_in_vbr)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, CloudPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudPlatform(_platform)

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_last_protection_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protection_date_type_0 = isoparse(data)

                return last_protection_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_protection_date = _parse_last_protection_date(d.pop("lastProtectionDate", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        protected_cloud_network_info = cls(
            cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
            name=name,
            platform=platform,
            region=region,
            last_protection_date=last_protection_date,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_cloud_network_info
