from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_proxy_state import BackupProxyState
from ..models.backup_proxy_transport_mode import BackupProxyTransportMode
from ..models.backup_proxy_type import BackupProxyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupProxyInfo")


@_attrs_define
class BackupProxyInfo:
    """
    Attributes:
        backup_proxy_id (int | Unset): ID assigned to a backup proxy.
        proxy_uid_in_vbr (None | Unset | UUID): UID assigned to a backup proxy in Veeam Backup & Replication.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        name (None | str | Unset): Name of a backup proxy.
        enabled (bool | None | Unset): Indicates whether a backup proxy is enabled.
        version (None | str | Unset): Version of a backup proxy.
        type_ (BackupProxyType | Unset):
        state (BackupProxyState | Unset):
        running_tasks (int | None | Unset): Number of tasks that a backup proxy is currently processing.
        max_concurrent_tasks (int | None | Unset): Maximum number of concurrent tasks.
        upgrade_required (bool | None | Unset): Indicates whether a backup proxy must be updated.
        transport_mode (BackupProxyTransportMode | Unset):
        throttling_enabled (bool | None | Unset): Indicates whether traffic throttling is enabled for a backup proxy.
    """

    backup_proxy_id: int | Unset = UNSET
    proxy_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    version: None | str | Unset = UNSET
    type_: BackupProxyType | Unset = UNSET
    state: BackupProxyState | Unset = UNSET
    running_tasks: int | None | Unset = UNSET
    max_concurrent_tasks: int | None | Unset = UNSET
    upgrade_required: bool | None | Unset = UNSET
    transport_mode: BackupProxyTransportMode | Unset = UNSET
    throttling_enabled: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_proxy_id = self.backup_proxy_id

        proxy_uid_in_vbr: None | str | Unset
        if isinstance(self.proxy_uid_in_vbr, Unset):
            proxy_uid_in_vbr = UNSET
        elif isinstance(self.proxy_uid_in_vbr, UUID):
            proxy_uid_in_vbr = str(self.proxy_uid_in_vbr)
        else:
            proxy_uid_in_vbr = self.proxy_uid_in_vbr

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        running_tasks: int | None | Unset
        if isinstance(self.running_tasks, Unset):
            running_tasks = UNSET
        else:
            running_tasks = self.running_tasks

        max_concurrent_tasks: int | None | Unset
        if isinstance(self.max_concurrent_tasks, Unset):
            max_concurrent_tasks = UNSET
        else:
            max_concurrent_tasks = self.max_concurrent_tasks

        upgrade_required: bool | None | Unset
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        transport_mode: str | Unset = UNSET
        if not isinstance(self.transport_mode, Unset):
            transport_mode = self.transport_mode.value

        throttling_enabled: bool | None | Unset
        if isinstance(self.throttling_enabled, Unset):
            throttling_enabled = UNSET
        else:
            throttling_enabled = self.throttling_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_proxy_id is not UNSET:
            field_dict["backupProxyId"] = backup_proxy_id
        if proxy_uid_in_vbr is not UNSET:
            field_dict["proxyUidInVbr"] = proxy_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if version is not UNSET:
            field_dict["version"] = version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if state is not UNSET:
            field_dict["state"] = state
        if running_tasks is not UNSET:
            field_dict["runningTasks"] = running_tasks
        if max_concurrent_tasks is not UNSET:
            field_dict["maxConcurrentTasks"] = max_concurrent_tasks
        if upgrade_required is not UNSET:
            field_dict["upgradeRequired"] = upgrade_required
        if transport_mode is not UNSET:
            field_dict["transportMode"] = transport_mode
        if throttling_enabled is not UNSET:
            field_dict["throttlingEnabled"] = throttling_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_proxy_id = d.pop("backupProxyId", UNSET)

        def _parse_proxy_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_uid_in_vbr_type_0 = UUID(data)

                return proxy_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_uid_in_vbr = _parse_proxy_uid_in_vbr(d.pop("proxyUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: BackupProxyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupProxyType(_type_)

        _state = d.pop("state", UNSET)
        state: BackupProxyState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BackupProxyState(_state)

        def _parse_running_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        running_tasks = _parse_running_tasks(d.pop("runningTasks", UNSET))

        def _parse_max_concurrent_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_concurrent_tasks = _parse_max_concurrent_tasks(d.pop("maxConcurrentTasks", UNSET))

        def _parse_upgrade_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        _transport_mode = d.pop("transportMode", UNSET)
        transport_mode: BackupProxyTransportMode | Unset
        if isinstance(_transport_mode, Unset):
            transport_mode = UNSET
        else:
            transport_mode = BackupProxyTransportMode(_transport_mode)

        def _parse_throttling_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        throttling_enabled = _parse_throttling_enabled(d.pop("throttlingEnabled", UNSET))

        backup_proxy_info = cls(
            backup_proxy_id=backup_proxy_id,
            proxy_uid_in_vbr=proxy_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            enabled=enabled,
            version=version,
            type_=type_,
            state=state,
            running_tasks=running_tasks,
            max_concurrent_tasks=max_concurrent_tasks,
            upgrade_required=upgrade_required,
            transport_mode=transport_mode,
            throttling_enabled=throttling_enabled,
        )

        return backup_proxy_info
