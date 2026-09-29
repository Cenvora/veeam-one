from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.wan_accelerator_state import WanAcceleratorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="WanAcceleratorInfo")


@_attrs_define
class WanAcceleratorInfo:
    """
    Attributes:
        wan_accelerator_id (Union[Unset, int]): ID assigned to a WAN accelerator.
        wan_accelerator_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a WAN accelerator in Veeam Backup &
            Replication.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup & Replication server.
        name (Union[None, Unset, str]): Name of a WAN accelerator.
        version (Union[None, Unset, str]): WAN accelerator version.
        capacity_bytes (Union[None, Unset, int]): WAN accelerator capacity, in bytes.
        upgrade_required (Union[None, Unset, bool]): Indicates whether a WAN accelerator must be updated.
        state (Union[Unset, WanAcceleratorState]):
        free_space_bytes (Union[None, Unset, int]): WAN accelerator free space, in bytes.
        used_space_bytes (Union[None, Unset, int]): WAN accelerator used space, in bytes.
        cache_path (Union[None, Unset, str]): Path to the folder in which service files and global cache data are
            stored.
        streams (Union[None, Unset, int]): Number of connections that are used to transmit data between WAN
            accelerators.
        traffic_port (Union[None, Unset, int]): Number of the port over which a WAN accelerator communicates with other
            WAN accelerators.
        high_bandwidth_mode (Union[None, Unset, bool]): Indicates whether the high bandwith mode is enabled.
    """

    wan_accelerator_id: Union[Unset, int] = UNSET
    wan_accelerator_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    upgrade_required: Union[None, Unset, bool] = UNSET
    state: Union[Unset, WanAcceleratorState] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    used_space_bytes: Union[None, Unset, int] = UNSET
    cache_path: Union[None, Unset, str] = UNSET
    streams: Union[None, Unset, int] = UNSET
    traffic_port: Union[None, Unset, int] = UNSET
    high_bandwidth_mode: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        wan_accelerator_id = self.wan_accelerator_id

        wan_accelerator_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.wan_accelerator_uid_in_vbr, Unset):
            wan_accelerator_uid_in_vbr = UNSET
        elif isinstance(self.wan_accelerator_uid_in_vbr, UUID):
            wan_accelerator_uid_in_vbr = str(self.wan_accelerator_uid_in_vbr)
        else:
            wan_accelerator_uid_in_vbr = self.wan_accelerator_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        upgrade_required: Union[None, Unset, bool]
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        free_space_bytes: Union[None, Unset, int]
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        used_space_bytes: Union[None, Unset, int]
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        cache_path: Union[None, Unset, str]
        if isinstance(self.cache_path, Unset):
            cache_path = UNSET
        else:
            cache_path = self.cache_path

        streams: Union[None, Unset, int]
        if isinstance(self.streams, Unset):
            streams = UNSET
        else:
            streams = self.streams

        traffic_port: Union[None, Unset, int]
        if isinstance(self.traffic_port, Unset):
            traffic_port = UNSET
        else:
            traffic_port = self.traffic_port

        high_bandwidth_mode: Union[None, Unset, bool]
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

        def _parse_wan_accelerator_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                wan_accelerator_uid_in_vbr_type_0 = UUID(data)

                return wan_accelerator_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        wan_accelerator_uid_in_vbr = _parse_wan_accelerator_uid_in_vbr(d.pop("wanAcceleratorUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_upgrade_required(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, WanAcceleratorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = WanAcceleratorState(_state)

        def _parse_free_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_cache_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cache_path = _parse_cache_path(d.pop("cachePath", UNSET))

        def _parse_streams(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        streams = _parse_streams(d.pop("streams", UNSET))

        def _parse_traffic_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        traffic_port = _parse_traffic_port(d.pop("trafficPort", UNSET))

        def _parse_high_bandwidth_mode(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

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
