from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.memory_shares_level import MemorySharesLevel
from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereResourcePoolInfo")


@_attrs_define
class VSphereResourcePoolInfo:
    """
    Attributes:
        resource_pool_id (int | Unset): ID assigned to a resource pool.
        mo_ref (None | str | Unset): MoRef ID assigned to a resource pool in VMware vSphere.
        name (None | str | Unset): Name of a resource pool.
        parent_id (int | None | Unset): ID assigned to a parent object.
        parent_type (None | Unset | VSphereObjectType): Type of a parent object.
        cpu_reservation_mhz (int | None | Unset): CPU reservation configured for a resource pool, in MHz.
        is_cpu_expandable (bool | None | Unset): Indicates whether a resource pool CPU reservation is expandable.
        cpu_limit_mhz (int | None | Unset): Maximum amount of CPU resources that can be allocated to a resource pool, in
            MHz.
        cpu_shares (int | None | Unset): CPU share value.
        cpu_usage_mhz (int | None | Unset): Number of actively used CPU resources, in MHz.
        memory_reservation_mb (int | None | Unset): Memory reservation configured for a resource pool, in MB.
        memory_shares_level (MemorySharesLevel | Unset):
        is_memory_expandable (bool | None | Unset): Indicates whether a resource pool memory reservation is expandable.
        memory_limit_mb (int | None | Unset): Maximum amount of memory resources that can be allocated to a resource
            pool, in MB.
        memory_shares (int | None | Unset): Memory share value.
        memory_usage_bytes (int | None | Unset): Amount of actively used memory resources, in bytes.
        cpu_unreserved_mhz (int | None | Unset): Amount of unreserved CPU resources, in MHz.
        memory_unreserved_bytes (int | None | Unset): Amoount of unreserved memory resources, in bytes.
    """

    resource_pool_id: int | Unset = UNSET
    mo_ref: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET
    cpu_reservation_mhz: int | None | Unset = UNSET
    is_cpu_expandable: bool | None | Unset = UNSET
    cpu_limit_mhz: int | None | Unset = UNSET
    cpu_shares: int | None | Unset = UNSET
    cpu_usage_mhz: int | None | Unset = UNSET
    memory_reservation_mb: int | None | Unset = UNSET
    memory_shares_level: MemorySharesLevel | Unset = UNSET
    is_memory_expandable: bool | None | Unset = UNSET
    memory_limit_mb: int | None | Unset = UNSET
    memory_shares: int | None | Unset = UNSET
    memory_usage_bytes: int | None | Unset = UNSET
    cpu_unreserved_mhz: int | None | Unset = UNSET
    memory_unreserved_bytes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        resource_pool_id = self.resource_pool_id

        mo_ref: None | str | Unset
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: None | str | Unset
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        cpu_reservation_mhz: int | None | Unset
        if isinstance(self.cpu_reservation_mhz, Unset):
            cpu_reservation_mhz = UNSET
        else:
            cpu_reservation_mhz = self.cpu_reservation_mhz

        is_cpu_expandable: bool | None | Unset
        if isinstance(self.is_cpu_expandable, Unset):
            is_cpu_expandable = UNSET
        else:
            is_cpu_expandable = self.is_cpu_expandable

        cpu_limit_mhz: int | None | Unset
        if isinstance(self.cpu_limit_mhz, Unset):
            cpu_limit_mhz = UNSET
        else:
            cpu_limit_mhz = self.cpu_limit_mhz

        cpu_shares: int | None | Unset
        if isinstance(self.cpu_shares, Unset):
            cpu_shares = UNSET
        else:
            cpu_shares = self.cpu_shares

        cpu_usage_mhz: int | None | Unset
        if isinstance(self.cpu_usage_mhz, Unset):
            cpu_usage_mhz = UNSET
        else:
            cpu_usage_mhz = self.cpu_usage_mhz

        memory_reservation_mb: int | None | Unset
        if isinstance(self.memory_reservation_mb, Unset):
            memory_reservation_mb = UNSET
        else:
            memory_reservation_mb = self.memory_reservation_mb

        memory_shares_level: str | Unset = UNSET
        if not isinstance(self.memory_shares_level, Unset):
            memory_shares_level = self.memory_shares_level.value

        is_memory_expandable: bool | None | Unset
        if isinstance(self.is_memory_expandable, Unset):
            is_memory_expandable = UNSET
        else:
            is_memory_expandable = self.is_memory_expandable

        memory_limit_mb: int | None | Unset
        if isinstance(self.memory_limit_mb, Unset):
            memory_limit_mb = UNSET
        else:
            memory_limit_mb = self.memory_limit_mb

        memory_shares: int | None | Unset
        if isinstance(self.memory_shares, Unset):
            memory_shares = UNSET
        else:
            memory_shares = self.memory_shares

        memory_usage_bytes: int | None | Unset
        if isinstance(self.memory_usage_bytes, Unset):
            memory_usage_bytes = UNSET
        else:
            memory_usage_bytes = self.memory_usage_bytes

        cpu_unreserved_mhz: int | None | Unset
        if isinstance(self.cpu_unreserved_mhz, Unset):
            cpu_unreserved_mhz = UNSET
        else:
            cpu_unreserved_mhz = self.cpu_unreserved_mhz

        memory_unreserved_bytes: int | None | Unset
        if isinstance(self.memory_unreserved_bytes, Unset):
            memory_unreserved_bytes = UNSET
        else:
            memory_unreserved_bytes = self.memory_unreserved_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if resource_pool_id is not UNSET:
            field_dict["resourcePoolId"] = resource_pool_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if cpu_reservation_mhz is not UNSET:
            field_dict["cpuReservationMhz"] = cpu_reservation_mhz
        if is_cpu_expandable is not UNSET:
            field_dict["isCpuExpandable"] = is_cpu_expandable
        if cpu_limit_mhz is not UNSET:
            field_dict["cpuLimitMhz"] = cpu_limit_mhz
        if cpu_shares is not UNSET:
            field_dict["cpuShares"] = cpu_shares
        if cpu_usage_mhz is not UNSET:
            field_dict["cpuUsageMhz"] = cpu_usage_mhz
        if memory_reservation_mb is not UNSET:
            field_dict["memoryReservationMb"] = memory_reservation_mb
        if memory_shares_level is not UNSET:
            field_dict["memorySharesLevel"] = memory_shares_level
        if is_memory_expandable is not UNSET:
            field_dict["isMemoryExpandable"] = is_memory_expandable
        if memory_limit_mb is not UNSET:
            field_dict["memoryLimitMb"] = memory_limit_mb
        if memory_shares is not UNSET:
            field_dict["memoryShares"] = memory_shares
        if memory_usage_bytes is not UNSET:
            field_dict["memoryUsageBytes"] = memory_usage_bytes
        if cpu_unreserved_mhz is not UNSET:
            field_dict["cpuUnreservedMhz"] = cpu_unreserved_mhz
        if memory_unreserved_bytes is not UNSET:
            field_dict["memoryUnreservedBytes"] = memory_unreserved_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource_pool_id = d.pop("resourcePoolId", UNSET)

        def _parse_mo_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_type(data: object) -> None | Unset | VSphereObjectType:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VSphereObjectType, data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        def _parse_cpu_reservation_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_reservation_mhz = _parse_cpu_reservation_mhz(d.pop("cpuReservationMhz", UNSET))

        def _parse_is_cpu_expandable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cpu_expandable = _parse_is_cpu_expandable(d.pop("isCpuExpandable", UNSET))

        def _parse_cpu_limit_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_limit_mhz = _parse_cpu_limit_mhz(d.pop("cpuLimitMhz", UNSET))

        def _parse_cpu_shares(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_shares = _parse_cpu_shares(d.pop("cpuShares", UNSET))

        def _parse_cpu_usage_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_usage_mhz = _parse_cpu_usage_mhz(d.pop("cpuUsageMhz", UNSET))

        def _parse_memory_reservation_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_reservation_mb = _parse_memory_reservation_mb(d.pop("memoryReservationMb", UNSET))

        _memory_shares_level = d.pop("memorySharesLevel", UNSET)
        memory_shares_level: MemorySharesLevel | Unset
        if isinstance(_memory_shares_level, Unset):
            memory_shares_level = UNSET
        else:
            memory_shares_level = MemorySharesLevel(_memory_shares_level)

        def _parse_is_memory_expandable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_memory_expandable = _parse_is_memory_expandable(d.pop("isMemoryExpandable", UNSET))

        def _parse_memory_limit_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_limit_mb = _parse_memory_limit_mb(d.pop("memoryLimitMb", UNSET))

        def _parse_memory_shares(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_shares = _parse_memory_shares(d.pop("memoryShares", UNSET))

        def _parse_memory_usage_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_usage_bytes = _parse_memory_usage_bytes(d.pop("memoryUsageBytes", UNSET))

        def _parse_cpu_unreserved_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_unreserved_mhz = _parse_cpu_unreserved_mhz(d.pop("cpuUnreservedMhz", UNSET))

        def _parse_memory_unreserved_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_unreserved_bytes = _parse_memory_unreserved_bytes(d.pop("memoryUnreservedBytes", UNSET))

        v_sphere_resource_pool_info = cls(
            resource_pool_id=resource_pool_id,
            mo_ref=mo_ref,
            name=name,
            parent_id=parent_id,
            parent_type=parent_type,
            cpu_reservation_mhz=cpu_reservation_mhz,
            is_cpu_expandable=is_cpu_expandable,
            cpu_limit_mhz=cpu_limit_mhz,
            cpu_shares=cpu_shares,
            cpu_usage_mhz=cpu_usage_mhz,
            memory_reservation_mb=memory_reservation_mb,
            memory_shares_level=memory_shares_level,
            is_memory_expandable=is_memory_expandable,
            memory_limit_mb=memory_limit_mb,
            memory_shares=memory_shares,
            memory_usage_bytes=memory_usage_bytes,
            cpu_unreserved_mhz=cpu_unreserved_mhz,
            memory_unreserved_bytes=memory_unreserved_bytes,
        )

        return v_sphere_resource_pool_info
