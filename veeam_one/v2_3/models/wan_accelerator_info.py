from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.wan_accelerator_state import WanAcceleratorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="WanAcceleratorInfo")


@_attrs_define
class WanAcceleratorInfo:
    """
    Attributes:
        wan_accelerator_id (int | Unset): ID assigned to a WAN accelerator.
        wan_accelerator_uid_in_vbr (None | Unset | UUID): UID assigned to a WAN accelerator in Veeam Backup &
            Replication.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        name (None | str | Unset): Name of a WAN accelerator.
        version (None | str | Unset): WAN accelerator version.
        capacity_bytes (int | None | Unset): WAN accelerator capacity, in bytes.
        upgrade_required (bool | None | Unset): Indicates whether a WAN accelerator must be updated.
        state (WanAcceleratorState | Unset):
        free_space_bytes (int | None | Unset): WAN accelerator free space, in bytes.
        used_space_bytes (int | None | Unset): WAN accelerator used space, in bytes.
        cache_path (None | str | Unset): Path to the folder in which service files and global cache data are stored.
        streams (int | None | Unset): Number of connections that are used to transmit data between WAN accelerators.
        traffic_port (int | None | Unset): Number of the port over which a WAN accelerator communicates with other WAN
            accelerators.
        high_bandwidth_mode (bool | None | Unset): Indicates whether the high bandwith mode is enabled.
    """

    wan_accelerator_id: int | Unset = UNSET
    wan_accelerator_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    capacity_bytes: int | None | Unset = UNSET
    upgrade_required: bool | None | Unset = UNSET
    state: WanAcceleratorState | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    cache_path: None | str | Unset = UNSET
    streams: int | None | Unset = UNSET
    traffic_port: int | None | Unset = UNSET
    high_bandwidth_mode: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        wan_accelerator_id = self.wan_accelerator_id

        wan_accelerator_uid_in_vbr: None | str | Unset
        if isinstance(self.wan_accelerator_uid_in_vbr, Unset):
            wan_accelerator_uid_in_vbr = UNSET
        elif isinstance(self.wan_accelerator_uid_in_vbr, UUID):
            wan_accelerator_uid_in_vbr = str(self.wan_accelerator_uid_in_vbr)
        else:
            wan_accelerator_uid_in_vbr = self.wan_accelerator_uid_in_vbr

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

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        upgrade_required: bool | None | Unset
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        used_space_bytes: int | None | Unset
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        cache_path: None | str | Unset
        if isinstance(self.cache_path, Unset):
            cache_path = UNSET
        else:
            cache_path = self.cache_path

        streams: int | None | Unset
        if isinstance(self.streams, Unset):
            streams = UNSET
        else:
            streams = self.streams

        traffic_port: int | None | Unset
        if isinstance(self.traffic_port, Unset):
            traffic_port = UNSET
        else:
            traffic_port = self.traffic_port

        high_bandwidth_mode: bool | None | Unset
        if isinstance(self.high_bandwidth_mode, Unset):
            high_bandwidth_mode = UNSET
        else:
            high_bandwidth_mode = self.high_bandwidth_mode

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if wan_accelerator_id is not UNSET:
            field_dict["wanAcceleratorId"] = wan_accelerator_id
        if wan_accelerator_uid_in_vbr is not UNSET:
            field_dict["wanAcceleratorUidInVbr"] = wan_accelerator_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if upgrade_required is not UNSET:
            field_dict["upgradeRequired"] = upgrade_required
        if state is not UNSET:
            field_dict["state"] = state
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if cache_path is not UNSET:
            field_dict["cachePath"] = cache_path
        if streams is not UNSET:
            field_dict["streams"] = streams
        if traffic_port is not UNSET:
            field_dict["trafficPort"] = traffic_port
        if high_bandwidth_mode is not UNSET:
            field_dict["highBandwidthMode"] = high_bandwidth_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wan_accelerator_id = d.pop("wanAcceleratorId", UNSET)

        def _parse_wan_accelerator_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wan_accelerator_uid_in_vbr_type_0 = UUID(data)

                return wan_accelerator_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        wan_accelerator_uid_in_vbr = _parse_wan_accelerator_uid_in_vbr(d.pop("wanAcceleratorUidInVbr", UNSET))

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

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_upgrade_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        _state = d.pop("state", UNSET)
        state: WanAcceleratorState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WanAcceleratorState(_state)

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_cache_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cache_path = _parse_cache_path(d.pop("cachePath", UNSET))

        def _parse_streams(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        streams = _parse_streams(d.pop("streams", UNSET))

        def _parse_traffic_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        traffic_port = _parse_traffic_port(d.pop("trafficPort", UNSET))

        def _parse_high_bandwidth_mode(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        high_bandwidth_mode = _parse_high_bandwidth_mode(d.pop("highBandwidthMode", UNSET))

        wan_accelerator_info = cls(
            wan_accelerator_id=wan_accelerator_id,
            wan_accelerator_uid_in_vbr=wan_accelerator_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            version=version,
            capacity_bytes=capacity_bytes,
            upgrade_required=upgrade_required,
            state=state,
            free_space_bytes=free_space_bytes,
            used_space_bytes=used_space_bytes,
            cache_path=cache_path,
            streams=streams,
            traffic_port=traffic_port,
            high_bandwidth_mode=high_bandwidth_mode,
        )

        return wan_accelerator_info
