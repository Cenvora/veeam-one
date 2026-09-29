from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereHostClusterInfo")


@_attrs_define
class VSphereHostClusterInfo:
    """
    Attributes:
        host_cluster_id (int | Unset): ID assigned to a cluster.
        mo_ref (None | str | Unset): MoRef ID assigned to a cluster in VMware vSphere.
        parent_id (int | None | Unset): ID assigned to a parent object.
        parent_type (None | Unset | VSphereObjectType): Type of a parent object.
        name (None | str | Unset): Name of a cluster.
        is_das_enabled (bool | None | Unset): Indicates whether DAS is used by a cluster.
        is_drs_enabled (bool | None | Unset): Indicates whether DRS is enabled for a cluster.
        cpu_total_mhz (int | None | Unset): Frequency of all CPU cores in a cluster, in MHz.
        total_memory_bytes (int | None | Unset): Amount of memory in all cluster objects.
        cpu_core_count (int | None | Unset): Amount of memory in all cluster objects.
        host_count (int | None | Unset): Number of hosts in a cluster.
        business_view_group_ids (list[int] | None | Unset): Array of Business View groups.
    """

    host_cluster_id: int | Unset = UNSET
    mo_ref: None | str | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET
    name: None | str | Unset = UNSET
    is_das_enabled: bool | None | Unset = UNSET
    is_drs_enabled: bool | None | Unset = UNSET
    cpu_total_mhz: int | None | Unset = UNSET
    total_memory_bytes: int | None | Unset = UNSET
    cpu_core_count: int | None | Unset = UNSET
    host_count: int | None | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_cluster_id = self.host_cluster_id

        mo_ref: None | str | Unset
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_das_enabled: bool | None | Unset
        if isinstance(self.is_das_enabled, Unset):
            is_das_enabled = UNSET
        else:
            is_das_enabled = self.is_das_enabled

        is_drs_enabled: bool | None | Unset
        if isinstance(self.is_drs_enabled, Unset):
            is_drs_enabled = UNSET
        else:
            is_drs_enabled = self.is_drs_enabled

        cpu_total_mhz: int | None | Unset
        if isinstance(self.cpu_total_mhz, Unset):
            cpu_total_mhz = UNSET
        else:
            cpu_total_mhz = self.cpu_total_mhz

        total_memory_bytes: int | None | Unset
        if isinstance(self.total_memory_bytes, Unset):
            total_memory_bytes = UNSET
        else:
            total_memory_bytes = self.total_memory_bytes

        cpu_core_count: int | None | Unset
        if isinstance(self.cpu_core_count, Unset):
            cpu_core_count = UNSET
        else:
            cpu_core_count = self.cpu_core_count

        host_count: int | None | Unset
        if isinstance(self.host_count, Unset):
            host_count = UNSET
        else:
            host_count = self.host_count

        business_view_group_ids: list[int] | None | Unset
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if host_cluster_id is not UNSET:
            field_dict["hostClusterId"] = host_cluster_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if name is not UNSET:
            field_dict["name"] = name
        if is_das_enabled is not UNSET:
            field_dict["isDasEnabled"] = is_das_enabled
        if is_drs_enabled is not UNSET:
            field_dict["isDrsEnabled"] = is_drs_enabled
        if cpu_total_mhz is not UNSET:
            field_dict["cpuTotalMhz"] = cpu_total_mhz
        if total_memory_bytes is not UNSET:
            field_dict["totalMemoryBytes"] = total_memory_bytes
        if cpu_core_count is not UNSET:
            field_dict["cpuCoreCount"] = cpu_core_count
        if host_count is not UNSET:
            field_dict["hostCount"] = host_count
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_cluster_id = d.pop("hostClusterId", UNSET)

        def _parse_mo_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_is_das_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_das_enabled = _parse_is_das_enabled(d.pop("isDasEnabled", UNSET))

        def _parse_is_drs_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_drs_enabled = _parse_is_drs_enabled(d.pop("isDrsEnabled", UNSET))

        def _parse_cpu_total_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_total_mhz = _parse_cpu_total_mhz(d.pop("cpuTotalMhz", UNSET))

        def _parse_total_memory_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_memory_bytes = _parse_total_memory_bytes(d.pop("totalMemoryBytes", UNSET))

        def _parse_cpu_core_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_core_count = _parse_cpu_core_count(d.pop("cpuCoreCount", UNSET))

        def _parse_host_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        host_count = _parse_host_count(d.pop("hostCount", UNSET))

        def _parse_business_view_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        v_sphere_host_cluster_info = cls(
            host_cluster_id=host_cluster_id,
            mo_ref=mo_ref,
            parent_id=parent_id,
            parent_type=parent_type,
            name=name,
            is_das_enabled=is_das_enabled,
            is_drs_enabled=is_drs_enabled,
            cpu_total_mhz=cpu_total_mhz,
            total_memory_bytes=total_memory_bytes,
            cpu_core_count=cpu_core_count,
            host_count=host_count,
            business_view_group_ids=business_view_group_ids,
        )

        return v_sphere_host_cluster_info
