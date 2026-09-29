from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDatabaseInfo")


@_attrs_define
class CloudDatabaseInfo:
    """
    Attributes:
        resource_id (None | str | Unset): ID assigned to a database on cloud platform.
        name (None | str | Unset): Name of a database.
        platform (Any | Unset): Cloud platform on which a database resides.
        instance_type (Any | Unset): Type of an instance.
        engine_type (None | str | Unset): Database engine version.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        region (None | str | Unset): Region where a database is located.
        size_bytes (int | None | Unset): Database storage capacity, in bytes.
    """

    resource_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    platform: Any | Unset = UNSET
    instance_type: Any | Unset = UNSET
    engine_type: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    size_bytes: int | None | Unset = UNSET

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

        platform = self.platform

        instance_type = self.instance_type

        engine_type: None | str | Unset
        if isinstance(self.engine_type, Unset):
            engine_type = UNSET
        else:
            engine_type = self.engine_type

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

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
        if engine_type is not UNSET:
            field_dict["engineType"] = engine_type
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

        platform = d.pop("platform", UNSET)

        instance_type = d.pop("instanceType", UNSET)

        def _parse_engine_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        engine_type = _parse_engine_type(d.pop("engineType", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

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

        cloud_database_info = cls(
            resource_id=resource_id,
            name=name,
            platform=platform,
            instance_type=instance_type,
            engine_type=engine_type,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            region=region,
            size_bytes=size_bytes,
        )

        return cloud_database_info
