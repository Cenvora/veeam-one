from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.hyper_v_connection_state import HyperVConnectionState
from ..models.hyper_v_host_power_state import HyperVHostPowerState
from ..models.hyper_v_object_type import HyperVObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVHostInfo")


@_attrs_define
class HyperVHostInfo:
    """
    Attributes:
        host_id (Union[Unset, int]): ID assigned to a host.
        name (Union[None, Unset, str]): Name of a host.
        connection_error (Union[None, Unset, str]): Datails on host connection failure.
        connection_state (Union[Unset, HyperVConnectionState]):
        power_state (Union[Unset, HyperVHostPowerState]):
        memory_size_bytes (Union[None, Unset, int]): Amount of memory available on a host, in bytes.
        cpu_count (Union[None, Unset, int]): Number of CPU cores on a host.
        cpu_frequency_mhz (Union[None, Unset, int]): Host CPU frequency, in MHz.
        cpu_model (Union[None, Unset, str]): Host CPU model.
        socket_count (Union[None, Unset, int]): Number of CPU sockets on a host.
        memory_reserve_mb (Union[None, Unset, int]): Size of memory reserve, in MB.
        version (Union[None, Unset, str]): Version of OS installed on a host.
        parent_id (Union[None, Unset, int]): ID assigned to a parent object.
        parent_type (Union[Unset, HyperVObjectType]):
        business_view_group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to the Business View groups.
    """

    host_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, HyperVConnectionState] = UNSET
    power_state: Union[Unset, HyperVHostPowerState] = UNSET
    memory_size_bytes: Union[None, Unset, int] = UNSET
    cpu_count: Union[None, Unset, int] = UNSET
    cpu_frequency_mhz: Union[None, Unset, int] = UNSET
    cpu_model: Union[None, Unset, str] = UNSET
    socket_count: Union[None, Unset, int] = UNSET
    memory_reserve_mb: Union[None, Unset, int] = UNSET
    version: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    parent_type: Union[Unset, HyperVObjectType] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_id = self.host_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        connection_error: Union[None, Unset, str]
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        power_state: Union[Unset, str] = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        memory_size_bytes: Union[None, Unset, int]
        if isinstance(self.memory_size_bytes, Unset):
            memory_size_bytes = UNSET
        else:
            memory_size_bytes = self.memory_size_bytes

        cpu_count: Union[None, Unset, int]
        if isinstance(self.cpu_count, Unset):
            cpu_count = UNSET
        else:
            cpu_count = self.cpu_count

        cpu_frequency_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_frequency_mhz, Unset):
            cpu_frequency_mhz = UNSET
        else:
            cpu_frequency_mhz = self.cpu_frequency_mhz

        cpu_model: Union[None, Unset, str]
        if isinstance(self.cpu_model, Unset):
            cpu_model = UNSET
        else:
            cpu_model = self.cpu_model

        socket_count: Union[None, Unset, int]
        if isinstance(self.socket_count, Unset):
            socket_count = UNSET
        else:
            socket_count = self.socket_count

        memory_reserve_mb: Union[None, Unset, int]
        if isinstance(self.memory_reserve_mb, Unset):
            memory_reserve_mb = UNSET
        else:
            memory_reserve_mb = self.memory_reserve_mb

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if name is not UNSET:
            field_dict["name"] = name
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if memory_size_bytes is not UNSET:
            field_dict["memorySizeBytes"] = memory_size_bytes
        if cpu_count is not UNSET:
            field_dict["cpuCount"] = cpu_count
        if cpu_frequency_mhz is not UNSET:
            field_dict["cpuFrequencyMhz"] = cpu_frequency_mhz
        if cpu_model is not UNSET:
            field_dict["cpuModel"] = cpu_model
        if socket_count is not UNSET:
            field_dict["socketCount"] = socket_count
        if memory_reserve_mb is not UNSET:
            field_dict["memoryReserveMb"] = memory_reserve_mb
        if version is not UNSET:
            field_dict["version"] = version
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_id = d.pop("hostId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_connection_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, HyperVConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = HyperVConnectionState(_connection_state)

        _power_state = d.pop("powerState", UNSET)
        power_state: Union[Unset, HyperVHostPowerState]
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = HyperVHostPowerState(_power_state)

        def _parse_memory_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_size_bytes = _parse_memory_size_bytes(d.pop("memorySizeBytes", UNSET))

        def _parse_cpu_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_count = _parse_cpu_count(d.pop("cpuCount", UNSET))

        def _parse_cpu_frequency_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_frequency_mhz = _parse_cpu_frequency_mhz(d.pop("cpuFrequencyMhz", UNSET))

        def _parse_cpu_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cpu_model = _parse_cpu_model(d.pop("cpuModel", UNSET))

        def _parse_socket_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        socket_count = _parse_socket_count(d.pop("socketCount", UNSET))

        def _parse_memory_reserve_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_reserve_mb = _parse_memory_reserve_mb(d.pop("memoryReserveMb", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        _parent_type = d.pop("parentType", UNSET)
        parent_type: Union[Unset, HyperVObjectType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = HyperVObjectType(_parent_type)

        def _parse_business_view_group_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        hyper_v_host_info = cls(
            host_id=host_id,
            name=name,
            connection_error=connection_error,
            connection_state=connection_state,
            power_state=power_state,
            memory_size_bytes=memory_size_bytes,
            cpu_count=cpu_count,
            cpu_frequency_mhz=cpu_frequency_mhz,
            cpu_model=cpu_model,
            socket_count=socket_count,
            memory_reserve_mb=memory_reserve_mb,
            version=version,
            parent_id=parent_id,
            parent_type=parent_type,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_host_info
