from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cloud_file_share_instance_type import CloudFileShareInstanceType
from ..models.cloud_file_shares_platform import CloudFileSharesPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudFileShareInfo")


@_attrs_define
class ProtectedCloudFileShareInfo:
    """
    Attributes:
        cloud_file_share_uid_in_vbr (UUID | Unset): UID assigned to a cloud file share in Veeam Backup & Replication.
        instance_id (None | str | Unset): Resource ID of a cloud file share.
        name (None | str | Unset): Name of a cloud file share.
        platform (CloudFileSharesPlatform | Unset):
        instance_type (CloudFileShareInstanceType | Unset):
        region (None | str | Unset): Region where a cloud file share is located.
        size_bytes (int | None | Unset): Cloud file share storage capacity, in bytes.
        last_protection_date (datetime.datetime | None | Unset): Date and time when the latest restore point was created
            for a cloud file share.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
    """

    cloud_file_share_uid_in_vbr: UUID | Unset = UNSET
    instance_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    platform: CloudFileSharesPlatform | Unset = UNSET
    instance_type: CloudFileShareInstanceType | Unset = UNSET
    region: None | str | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    last_protection_date: datetime.datetime | None | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_file_share_uid_in_vbr: str | Unset = UNSET
        if not isinstance(self.cloud_file_share_uid_in_vbr, Unset):
            cloud_file_share_uid_in_vbr = str(self.cloud_file_share_uid_in_vbr)

        instance_id: None | str | Unset
        if isinstance(self.instance_id, Unset):
            instance_id = UNSET
        else:
            instance_id = self.instance_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        instance_type: str | Unset = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.value

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        last_protection_date: None | str | Unset
        if isinstance(self.last_protection_date, Unset):
            last_protection_date = UNSET
        elif isinstance(self.last_protection_date, datetime.datetime):
            last_protection_date = self.last_protection_date.isoformat()
        else:
            last_protection_date = self.last_protection_date

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_file_share_uid_in_vbr is not UNSET:
            field_dict["cloudFileShareUidInVbr"] = cloud_file_share_uid_in_vbr
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if region is not UNSET:
            field_dict["region"] = region
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
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
        _cloud_file_share_uid_in_vbr = d.pop("cloudFileShareUidInVbr", UNSET)
        cloud_file_share_uid_in_vbr: UUID | Unset
        if isinstance(_cloud_file_share_uid_in_vbr, Unset):
            cloud_file_share_uid_in_vbr = UNSET
        else:
            cloud_file_share_uid_in_vbr = UUID(_cloud_file_share_uid_in_vbr)

        def _parse_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_id = _parse_instance_id(d.pop("instanceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: CloudFileSharesPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudFileSharesPlatform(_platform)

        _instance_type = d.pop("instanceType", UNSET)
        instance_type: CloudFileShareInstanceType | Unset
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = CloudFileShareInstanceType(_instance_type)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        def _parse_last_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protection_date = _parse_last_protection_date(d.pop("lastProtectionDate", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        protected_cloud_file_share_info = cls(
            cloud_file_share_uid_in_vbr=cloud_file_share_uid_in_vbr,
            instance_id=instance_id,
            name=name,
            platform=platform,
            instance_type=instance_type,
            region=region,
            size_bytes=size_bytes,
            last_protection_date=last_protection_date,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_cloud_file_share_info
