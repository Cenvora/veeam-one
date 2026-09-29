from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupClusterInfo")


@_attrs_define
class BackupClusterInfo:
    """
    Attributes:
        backup_cluster_id (int | Unset): ID assigned to a High Availability cluster.
        backup_cluster_name (None | str | Unset): Name of a High Availability cluster.
        backup_cluster_status (None | str | Unset): Status of a High Availability cluster.
        backup_cluster_active_server_name (None | str | Unset): Name of a High Availability cluster primary node.
        backup_cluster_passive_server_name (None | str | Unset): Name of a High Availability cluster secondary node.
    """

    backup_cluster_id: int | Unset = UNSET
    backup_cluster_name: None | str | Unset = UNSET
    backup_cluster_status: None | str | Unset = UNSET
    backup_cluster_active_server_name: None | str | Unset = UNSET
    backup_cluster_passive_server_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_cluster_id = self.backup_cluster_id

        backup_cluster_name: None | str | Unset
        if isinstance(self.backup_cluster_name, Unset):
            backup_cluster_name = UNSET
        else:
            backup_cluster_name = self.backup_cluster_name

        backup_cluster_status: None | str | Unset
        if isinstance(self.backup_cluster_status, Unset):
            backup_cluster_status = UNSET
        else:
            backup_cluster_status = self.backup_cluster_status

        backup_cluster_active_server_name: None | str | Unset
        if isinstance(self.backup_cluster_active_server_name, Unset):
            backup_cluster_active_server_name = UNSET
        else:
            backup_cluster_active_server_name = self.backup_cluster_active_server_name

        backup_cluster_passive_server_name: None | str | Unset
        if isinstance(self.backup_cluster_passive_server_name, Unset):
            backup_cluster_passive_server_name = UNSET
        else:
            backup_cluster_passive_server_name = self.backup_cluster_passive_server_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_cluster_id is not UNSET:
            field_dict["backupClusterId"] = backup_cluster_id
        if backup_cluster_name is not UNSET:
            field_dict["backupClusterName"] = backup_cluster_name
        if backup_cluster_status is not UNSET:
            field_dict["backupClusterStatus"] = backup_cluster_status
        if backup_cluster_active_server_name is not UNSET:
            field_dict["backupClusterActiveServerName"] = backup_cluster_active_server_name
        if backup_cluster_passive_server_name is not UNSET:
            field_dict["backupClusterPassiveServerName"] = backup_cluster_passive_server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_cluster_id = d.pop("backupClusterId", UNSET)

        def _parse_backup_cluster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_cluster_name = _parse_backup_cluster_name(d.pop("backupClusterName", UNSET))

        def _parse_backup_cluster_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_cluster_status = _parse_backup_cluster_status(d.pop("backupClusterStatus", UNSET))

        def _parse_backup_cluster_active_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_cluster_active_server_name = _parse_backup_cluster_active_server_name(
            d.pop("backupClusterActiveServerName", UNSET)
        )

        def _parse_backup_cluster_passive_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_cluster_passive_server_name = _parse_backup_cluster_passive_server_name(
            d.pop("backupClusterPassiveServerName", UNSET)
        )

        backup_cluster_info = cls(
            backup_cluster_id=backup_cluster_id,
            backup_cluster_name=backup_cluster_name,
            backup_cluster_status=backup_cluster_status,
            backup_cluster_active_server_name=backup_cluster_active_server_name,
            backup_cluster_passive_server_name=backup_cluster_passive_server_name,
        )

        return backup_cluster_info
