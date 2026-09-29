from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.v_sphere_host_connection_state import VSphereHostConnectionState
from ..models.v_sphere_host_power_state import VSphereHostPowerState
from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereHostInfo")


@_attrs_define
class VSphereHostInfo:
    """
    Attributes:
        host_id (Union[Unset, int]): ID assigned to a host.
        mo_ref (Union[None, Unset, str]): MoRef ID assigned to a host in VMware vSphere.
        name (Union[None, Unset, str]): Name of a host.
        parent_id (Union[None, Unset, int]): ID assigned to a parent object.
        parent_type (Union[None, Unset, VSphereObjectType]): Type of a parent object.
        port (Union[None, Unset, int]): Port used to access a host.
        connection_state (Union[Unset, VSphereHostConnectionState]):
        power_state (Union[Unset, VSphereHostPowerState]):
        vendor (Union[None, Unset, str]): Host vendor.
        model (Union[None, Unset, str]): Host model.
        socket_count (Union[None, Unset, int]): Number of CPU sockets on a host.
        cpu_package_count (Union[None, Unset, int]): Number of CPU packages on a host.
        cpu_core_count (Union[None, Unset, int]): Number of CPU cores on a host.
        cpu_model (Union[None, Unset, str]): Model of a host CPU.
        cpu_mhz (Union[None, Unset, int]): Host CPU frequency, in MHz.
        memory_size_bytes (Union[None, Unset, int]): Amount of memory available on a host, in bytes.
        nic_count (Union[None, Unset, int]): Number of network interface controllers connected to a host.
        is_maintenance_mode_enabled (Union[None, Unset, bool]): Indicates whether a host is in the maintenance mode.
        memory_usage_mb (Union[None, Unset, int]): Host memory usage, in MB.
        cpu_usage_mhz (Union[None, Unset, int]): Host CPU usage, in MHz.
        is_vmotion_enabled (Union[None, Unset, bool]): Indicates whether VMware vSphere vMotion is enabled for a host.
        connection_error (Union[None, Unset, str]): Error message for failed connection.
        version (Union[None, Unset, str]): Version of a host.
        business_view_group_ids (Union[None, Unset, list[int]]): Array of Business View groups.
    """

    host_id: Union[Unset, int] = UNSET
    mo_ref: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    parent_type: Union[None, Unset, VSphereObjectType] = UNSET
    port: Union[None, Unset, int] = UNSET
    connection_state: Union[Unset, VSphereHostConnectionState] = UNSET
    power_state: Union[Unset, VSphereHostPowerState] = UNSET
    vendor: Union[None, Unset, str] = UNSET
    model: Union[None, Unset, str] = UNSET
    socket_count: Union[None, Unset, int] = UNSET
    cpu_package_count: Union[None, Unset, int] = UNSET
    cpu_core_count: Union[None, Unset, int] = UNSET
    cpu_model: Union[None, Unset, str] = UNSET
    cpu_mhz: Union[None, Unset, int] = UNSET
    memory_size_bytes: Union[None, Unset, int] = UNSET
    nic_count: Union[None, Unset, int] = UNSET
    is_maintenance_mode_enabled: Union[None, Unset, bool] = UNSET
    memory_usage_mb: Union[None, Unset, int] = UNSET
    cpu_usage_mhz: Union[None, Unset, int] = UNSET
    is_vmotion_enabled: Union[None, Unset, bool] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_id = self.host_id

        mo_ref: Union[None, Unset, str]
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: Union[None, Unset, str]
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        power_state: Union[Unset, str] = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        vendor: Union[None, Unset, str]
        if isinstance(self.vendor, Unset):
            vendor = UNSET
        else:
            vendor = self.vendor

        model: Union[None, Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        socket_count: Union[None, Unset, int]
        if isinstance(self.socket_count, Unset):
            socket_count = UNSET
        else:
            socket_count = self.socket_count

        cpu_package_count: Union[None, Unset, int]
        if isinstance(self.cpu_package_count, Unset):
            cpu_package_count = UNSET
        else:
            cpu_package_count = self.cpu_package_count

        cpu_core_count: Union[None, Unset, int]
        if isinstance(self.cpu_core_count, Unset):
            cpu_core_count = UNSET
        else:
            cpu_core_count = self.cpu_core_count

        cpu_model: Union[None, Unset, str]
        if isinstance(self.cpu_model, Unset):
            cpu_model = UNSET
        else:
            cpu_model = self.cpu_model

        cpu_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_mhz, Unset):
            cpu_mhz = UNSET
        else:
            cpu_mhz = self.cpu_mhz

        memory_size_bytes: Union[None, Unset, int]
        if isinstance(self.memory_size_bytes, Unset):
            memory_size_bytes = UNSET
        else:
            memory_size_bytes = self.memory_size_bytes

        nic_count: Union[None, Unset, int]
        if isinstance(self.nic_count, Unset):
            nic_count = UNSET
        else:
            nic_count = self.nic_count

        is_maintenance_mode_enabled: Union[None, Unset, bool]
        if isinstance(self.is_maintenance_mode_enabled, Unset):
            is_maintenance_mode_enabled = UNSET
        else:
            is_maintenance_mode_enabled = self.is_maintenance_mode_enabled

        memory_usage_mb: Union[None, Unset, int]
        if isinstance(self.memory_usage_mb, Unset):
            memory_usage_mb = UNSET
        else:
            memory_usage_mb = self.memory_usage_mb

        cpu_usage_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_usage_mhz, Unset):
            cpu_usage_mhz = UNSET
        else:
            cpu_usage_mhz = self.cpu_usage_mhz

        is_vmotion_enabled: Union[None, Unset, bool]
        if isinstance(self.is_vmotion_enabled, Unset):
            is_vmotion_enabled = UNSET
        else:
            is_vmotion_enabled = self.is_vmotion_enabled

        connection_error: Union[None, Unset, str]
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

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
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if port is not UNSET:
            field_dict["port"] = port
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if socket_count is not UNSET:
            field_dict["socketCount"] = socket_count
        if cpu_package_count is not UNSET:
            field_dict["cpuPackageCount"] = cpu_package_count
        if cpu_core_count is not UNSET:
            field_dict["cpuCoreCount"] = cpu_core_count
        if cpu_model is not UNSET:
            field_dict["cpuModel"] = cpu_model
        if cpu_mhz is not UNSET:
            field_dict["cpuMhz"] = cpu_mhz
        if memory_size_bytes is not UNSET:
            field_dict["memorySizeBytes"] = memory_size_bytes
        if nic_count is not UNSET:
            field_dict["nicCount"] = nic_count
        if is_maintenance_mode_enabled is not UNSET:
            field_dict["isMaintenanceModeEnabled"] = is_maintenance_mode_enabled
        if memory_usage_mb is not UNSET:
            field_dict["memoryUsageMb"] = memory_usage_mb
        if cpu_usage_mhz is not UNSET:
            field_dict["cpuUsageMhz"] = cpu_usage_mhz
        if is_vmotion_enabled is not UNSET:
            field_dict["isVmotionEnabled"] = is_vmotion_enabled
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if version is not UNSET:
            field_dict["version"] = version
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_id = d.pop("hostId", UNSET)

        def _parse_mo_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_type(data: object) -> Union[None, Unset, VSphereObjectType]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, VSphereObjectType], data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, VSphereHostConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = VSphereHostConnectionState(_connection_state)

        _power_state = d.pop("powerState", UNSET)
        power_state: Union[Unset, VSphereHostPowerState]
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = VSphereHostPowerState(_power_state)

        def _parse_vendor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vendor = _parse_vendor(d.pop("vendor", UNSET))

        def _parse_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        def _parse_socket_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        socket_count = _parse_socket_count(d.pop("socketCount", UNSET))

        def _parse_cpu_package_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_package_count = _parse_cpu_package_count(d.pop("cpuPackageCount", UNSET))

        def _parse_cpu_core_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_core_count = _parse_cpu_core_count(d.pop("cpuCoreCount", UNSET))

        def _parse_cpu_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cpu_model = _parse_cpu_model(d.pop("cpuModel", UNSET))

        def _parse_cpu_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_mhz = _parse_cpu_mhz(d.pop("cpuMhz", UNSET))

        def _parse_memory_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_size_bytes = _parse_memory_size_bytes(d.pop("memorySizeBytes", UNSET))

        def _parse_nic_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nic_count = _parse_nic_count(d.pop("nicCount", UNSET))

        def _parse_is_maintenance_mode_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_maintenance_mode_enabled = _parse_is_maintenance_mode_enabled(d.pop("isMaintenanceModeEnabled", UNSET))

        def _parse_memory_usage_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_usage_mb = _parse_memory_usage_mb(d.pop("memoryUsageMb", UNSET))

        def _parse_cpu_usage_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_usage_mhz = _parse_cpu_usage_mhz(d.pop("cpuUsageMhz", UNSET))

        def _parse_is_vmotion_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_vmotion_enabled = _parse_is_vmotion_enabled(d.pop("isVmotionEnabled", UNSET))

        def _parse_connection_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

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

        v_sphere_host_info = cls(
            host_id=host_id,
            mo_ref=mo_ref,
            name=name,
            parent_id=parent_id,
            parent_type=parent_type,
            port=port,
            connection_state=connection_state,
            power_state=power_state,
            vendor=vendor,
            model=model,
            socket_count=socket_count,
            cpu_package_count=cpu_package_count,
            cpu_core_count=cpu_core_count,
            cpu_model=cpu_model,
            cpu_mhz=cpu_mhz,
            memory_size_bytes=memory_size_bytes,
            nic_count=nic_count,
            is_maintenance_mode_enabled=is_maintenance_mode_enabled,
            memory_usage_mb=memory_usage_mb,
            cpu_usage_mhz=cpu_usage_mhz,
            is_vmotion_enabled=is_vmotion_enabled,
            connection_error=connection_error,
            version=version,
            business_view_group_ids=business_view_group_ids,
        )

        return v_sphere_host_info
