from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.backup_platform_type import BackupPlatformType
from ..models.enterprise_manager_connection_state import EnterpriseManagerConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnterpriseManagerServerInfo")


@_attrs_define
class EnterpriseManagerServerInfo:
    """
    Attributes:
        enterprise_manager_server_id (int | Unset): ID assigned to a Veeam Backup Enterprise Manager server.
        backup_server_ids (list[int] | None | Unset): Array of IDs assigned to Veeam Backup & Replication servers that
            are managed by Veeam Backup Enterprise Manager.
        name (None | str | Unset): Name of a Veeam Backup Enterprise Manager server.
        version (None | str | Unset): Veeam Backup Enterprise Manager version.
        connection_error (None | str | Unset): Details on connection failure of a Veeam Backup Enterprise Manager
            server.
        connection_state (EnterpriseManagerConnectionState | Unset):
        platform (BackupPlatformType | Unset):
    """

    enterprise_manager_server_id: int | Unset = UNSET
    backup_server_ids: list[int] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    connection_error: None | str | Unset = UNSET
    connection_state: EnterpriseManagerConnectionState | Unset = UNSET
    platform: BackupPlatformType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        enterprise_manager_server_id = self.enterprise_manager_server_id

        backup_server_ids: list[int] | None | Unset
        if isinstance(self.backup_server_ids, Unset):
            backup_server_ids = UNSET
        elif isinstance(self.backup_server_ids, list):
            backup_server_ids = self.backup_server_ids

        else:
            backup_server_ids = self.backup_server_ids

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        connection_error: None | str | Unset
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enterprise_manager_server_id is not UNSET:
            field_dict["enterpriseManagerServerId"] = enterprise_manager_server_id
        if backup_server_ids is not UNSET:
            field_dict["backupServerIds"] = backup_server_ids
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enterprise_manager_server_id = d.pop("enterpriseManagerServerId", UNSET)

        def _parse_backup_server_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                backup_server_ids_type_0 = cast(list[int], data)

                return backup_server_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        backup_server_ids = _parse_backup_server_ids(d.pop("backupServerIds", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_connection_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: EnterpriseManagerConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = EnterpriseManagerConnectionState(_connection_state)

        _platform = d.pop("platform", UNSET)
        platform: BackupPlatformType | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupPlatformType(_platform)

        enterprise_manager_server_info = cls(
            enterprise_manager_server_id=enterprise_manager_server_id,
            backup_server_ids=backup_server_ids,
            name=name,
            version=version,
            connection_error=connection_error,
            connection_state=connection_state,
            platform=platform,
        )

        return enterprise_manager_server_info
