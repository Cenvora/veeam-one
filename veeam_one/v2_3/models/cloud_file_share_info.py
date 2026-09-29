from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.cloud_file_share_instance_type import CloudFileShareInstanceType
from ..models.cloud_file_shares_platform import CloudFileSharesPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudFileShareInfo")


@_attrs_define
class CloudFileShareInfo:
    """
    Attributes:
        resource_id (Union[None, Unset, str]): ID assigned to a file share on cloud platform.
        name (Union[None, Unset, str]): Name of a cloud file share.
        platform (Union[Unset, CloudFileSharesPlatform]):
        instance_type (Union[Unset, CloudFileShareInstanceType]):
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
        region (Union[None, Unset, str]): Region where a cloud file share is located.
        size_bytes (Union[None, Unset, int]): Cloud file share storage capacity, in bytes.
    """

    resource_id: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    platform: Union[Unset, CloudFileSharesPlatform] = UNSET
    instance_type: Union[Unset, CloudFileShareInstanceType] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    region: Union[None, Unset, str] = UNSET
    size_bytes: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id: Union[None, Unset, str]
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        instance_type: Union[Unset, str] = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.value

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        size_bytes: Union[None, Unset, int]
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if region is not UNSET:
            field_dict["region"] = region
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resource_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, CloudFileSharesPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudFileSharesPlatform(_platform)

        _instance_type = d.pop("instanceType", UNSET)
        instance_type: Union[Unset, CloudFileShareInstanceType]
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = CloudFileShareInstanceType(_instance_type)

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        cloud_file_share_info = cls(
            resource_id=resource_id,
            name=name,
            platform=platform,
            instance_type=instance_type,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            region=region,
            size_bytes=size_bytes,
        )

        return cloud_file_share_info
