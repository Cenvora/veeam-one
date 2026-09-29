from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.v_sphere_datastore_type import VSphereDatastoreType
from ..models.v_sphere_drs_automation_level import VSphereDrsAutomationLevel
from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereDatastoreClusterInfo")


@_attrs_define
class VSphereDatastoreClusterInfo:
    """
    Attributes:
        datastore_cluster_id (int | Unset): ID assigned to a datastore cluster.
        mo_ref (None | str | Unset): MoRef ID assigned to a datastore cluster in VMware vSphere.
        name (None | str | Unset): Name of a datastore cluster.
        parent_id (int | None | Unset): ID assigned to a parent object.
        parent_type (None | Unset | VSphereObjectType): Type of a parent object.
        capacity_bytes (int | None | Unset): Total capacity of a datastore cluster, in bytes.
        free_space_bytes (int | None | Unset): Amount of available free space on a datastore cluster, in bytes.
        largest_datastore_free_space_bytes (int | None | Unset): Amount of available free space on the largest datastore
            in a cluster, in bytes.
        datastores_type (VSphereDatastoreType | Unset):
        io_metrics_enabled (bool | None | Unset): Indicates whether the IO Metric function is enabled for a datastore
            cluster.
        storage_drs_enabled (bool | None | Unset): Indicates whether Storage DRS is enabled for a datastore cluster.
        drs_automation_level (VSphereDrsAutomationLevel | Unset):
        used_space_threshold_percentage (int | None | Unset): Used space threshold configured for a datastore cluster.
        io_latency_threshold_ms (int | None | Unset): IO latency threshold configured for a datastore cluster, in
            milliseconds.
    """

    datastore_cluster_id: int | Unset = UNSET
    mo_ref: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET
    capacity_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    largest_datastore_free_space_bytes: int | None | Unset = UNSET
    datastores_type: VSphereDatastoreType | Unset = UNSET
    io_metrics_enabled: bool | None | Unset = UNSET
    storage_drs_enabled: bool | None | Unset = UNSET
    drs_automation_level: VSphereDrsAutomationLevel | Unset = UNSET
    used_space_threshold_percentage: int | None | Unset = UNSET
    io_latency_threshold_ms: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        datastore_cluster_id = self.datastore_cluster_id

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

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        largest_datastore_free_space_bytes: int | None | Unset
        if isinstance(self.largest_datastore_free_space_bytes, Unset):
            largest_datastore_free_space_bytes = UNSET
        else:
            largest_datastore_free_space_bytes = self.largest_datastore_free_space_bytes

        datastores_type: str | Unset = UNSET
        if not isinstance(self.datastores_type, Unset):
            datastores_type = self.datastores_type.value

        io_metrics_enabled: bool | None | Unset
        if isinstance(self.io_metrics_enabled, Unset):
            io_metrics_enabled = UNSET
        else:
            io_metrics_enabled = self.io_metrics_enabled

        storage_drs_enabled: bool | None | Unset
        if isinstance(self.storage_drs_enabled, Unset):
            storage_drs_enabled = UNSET
        else:
            storage_drs_enabled = self.storage_drs_enabled

        drs_automation_level: str | Unset = UNSET
        if not isinstance(self.drs_automation_level, Unset):
            drs_automation_level = self.drs_automation_level.value

        used_space_threshold_percentage: int | None | Unset
        if isinstance(self.used_space_threshold_percentage, Unset):
            used_space_threshold_percentage = UNSET
        else:
            used_space_threshold_percentage = self.used_space_threshold_percentage

        io_latency_threshold_ms: int | None | Unset
        if isinstance(self.io_latency_threshold_ms, Unset):
            io_latency_threshold_ms = UNSET
        else:
            io_latency_threshold_ms = self.io_latency_threshold_ms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if datastore_cluster_id is not UNSET:
            field_dict["datastoreClusterId"] = datastore_cluster_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if largest_datastore_free_space_bytes is not UNSET:
            field_dict["largestDatastoreFreeSpaceBytes"] = largest_datastore_free_space_bytes
        if datastores_type is not UNSET:
            field_dict["datastoresType"] = datastores_type
        if io_metrics_enabled is not UNSET:
            field_dict["ioMetricsEnabled"] = io_metrics_enabled
        if storage_drs_enabled is not UNSET:
            field_dict["storageDrsEnabled"] = storage_drs_enabled
        if drs_automation_level is not UNSET:
            field_dict["drsAutomationLevel"] = drs_automation_level
        if used_space_threshold_percentage is not UNSET:
            field_dict["usedSpaceThresholdPercentage"] = used_space_threshold_percentage
        if io_latency_threshold_ms is not UNSET:
            field_dict["ioLatencyThresholdMs"] = io_latency_threshold_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datastore_cluster_id = d.pop("datastoreClusterId", UNSET)

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

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_largest_datastore_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        largest_datastore_free_space_bytes = _parse_largest_datastore_free_space_bytes(
            d.pop("largestDatastoreFreeSpaceBytes", UNSET)
        )

        _datastores_type = d.pop("datastoresType", UNSET)
        datastores_type: VSphereDatastoreType | Unset
        if isinstance(_datastores_type, Unset):
            datastores_type = UNSET
        else:
            datastores_type = VSphereDatastoreType(_datastores_type)

        def _parse_io_metrics_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        io_metrics_enabled = _parse_io_metrics_enabled(d.pop("ioMetricsEnabled", UNSET))

        def _parse_storage_drs_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        storage_drs_enabled = _parse_storage_drs_enabled(d.pop("storageDrsEnabled", UNSET))

        _drs_automation_level = d.pop("drsAutomationLevel", UNSET)
        drs_automation_level: VSphereDrsAutomationLevel | Unset
        if isinstance(_drs_automation_level, Unset):
            drs_automation_level = UNSET
        else:
            drs_automation_level = VSphereDrsAutomationLevel(_drs_automation_level)

        def _parse_used_space_threshold_percentage(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_threshold_percentage = _parse_used_space_threshold_percentage(
            d.pop("usedSpaceThresholdPercentage", UNSET)
        )

        def _parse_io_latency_threshold_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        io_latency_threshold_ms = _parse_io_latency_threshold_ms(d.pop("ioLatencyThresholdMs", UNSET))

        v_sphere_datastore_cluster_info = cls(
            datastore_cluster_id=datastore_cluster_id,
            mo_ref=mo_ref,
            name=name,
            parent_id=parent_id,
            parent_type=parent_type,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            largest_datastore_free_space_bytes=largest_datastore_free_space_bytes,
            datastores_type=datastores_type,
            io_metrics_enabled=io_metrics_enabled,
            storage_drs_enabled=storage_drs_enabled,
            drs_automation_level=drs_automation_level,
            used_space_threshold_percentage=used_space_threshold_percentage,
            io_latency_threshold_ms=io_latency_threshold_ms,
        )

        return v_sphere_datastore_cluster_info
