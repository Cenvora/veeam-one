from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.cloud_platform import CloudPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudVmInfo")


@_attrs_define
class CloudVmInfo:
    """
    Attributes:
        resource_id (None | str | Unset): ID assigned to a VM on a cloud platform.
        name (None | str | Unset): Name of a VM.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server that manages VM protection.
        platform (CloudPlatform | Unset):
        region (None | str | Unset): Region where a VM is located.
        ip_addresses (list[str] | None | Unset): Array of VM IP addresses.
    """

    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    platform: CloudPlatform | Unset = UNSET
    region: None | str | Unset = UNSET
    ip_addresses: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_id: None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup_server_id = self.backup_server_id

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        ip_addresses: list[str] | None | Unset
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_id is not UNSET:
            field_dict["resourceId"] = resource_id
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if region is not UNSET:
            field_dict["region"] = region
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_resource_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resourceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: CloudPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudPlatform(_platform)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_ip_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        cloud_vm_info = cls(
            resource_id=resource_id,
            name=name,
            backup_server_id=backup_server_id,
            platform=platform,
            region=region,
            ip_addresses=ip_addresses,
        )

        return cloud_vm_info
