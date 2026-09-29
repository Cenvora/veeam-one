from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseUsageReportWorkload")


@_attrs_define
class VeeamOneLicenseUsageReportWorkload:
    """
    Attributes:
        workload_type (None | str | Unset): Type of licensed objects. Example: Virtual Machines.
        used_objects (int | Unset): Number of licensed objects. Example: 376.
        new_objects (int | None | Unset): Number of new objects. Example: 2.
        used_units (float | Unset): Number of consumed license units. Example: 376.
        new_units (float | None | Unset): Number of license units that new objects will consume. Example: 2.
        multiplier (int | Unset): License unit multiplier. Example: 1.
        removed_objects (int | Unset): Number of removed objects.
        removed_units (int | None | Unset): Number of license units consumed by removed objects.
    """

    workload_type: None | str | Unset = UNSET
    used_objects: int | Unset = UNSET
    new_objects: int | None | Unset = UNSET
    used_units: float | Unset = UNSET
    new_units: float | None | Unset = UNSET
    multiplier: int | Unset = UNSET
    removed_objects: int | Unset = UNSET
    removed_units: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workload_type: None | str | Unset
        if isinstance(self.workload_type, Unset):
            workload_type = UNSET
        else:
            workload_type = self.workload_type

        used_objects = self.used_objects

        new_objects: int | None | Unset
        if isinstance(self.new_objects, Unset):
            new_objects = UNSET
        else:
            new_objects = self.new_objects

        used_units = self.used_units

        new_units: float | None | Unset
        if isinstance(self.new_units, Unset):
            new_units = UNSET
        else:
            new_units = self.new_units

        multiplier = self.multiplier

        removed_objects = self.removed_objects

        removed_units: int | None | Unset
        if isinstance(self.removed_units, Unset):
            removed_units = UNSET
        else:
            removed_units = self.removed_units

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if workload_type is not UNSET:
            field_dict["workloadType"] = workload_type
        if used_objects is not UNSET:
            field_dict["usedObjects"] = used_objects
        if new_objects is not UNSET:
            field_dict["newObjects"] = new_objects
        if used_units is not UNSET:
            field_dict["usedUnits"] = used_units
        if new_units is not UNSET:
            field_dict["newUnits"] = new_units
        if multiplier is not UNSET:
            field_dict["multiplier"] = multiplier
        if removed_objects is not UNSET:
            field_dict["removedObjects"] = removed_objects
        if removed_units is not UNSET:
            field_dict["removedUnits"] = removed_units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workload_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        workload_type = _parse_workload_type(d.pop("workloadType", UNSET))

        used_objects = d.pop("usedObjects", UNSET)

        def _parse_new_objects(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_objects = _parse_new_objects(d.pop("newObjects", UNSET))

        used_units = d.pop("usedUnits", UNSET)

        def _parse_new_units(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        new_units = _parse_new_units(d.pop("newUnits", UNSET))

        multiplier = d.pop("multiplier", UNSET)

        removed_objects = d.pop("removedObjects", UNSET)

        def _parse_removed_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        removed_units = _parse_removed_units(d.pop("removedUnits", UNSET))

        veeam_one_license_usage_report_workload = cls(
            workload_type=workload_type,
            used_objects=used_objects,
            new_objects=new_objects,
            used_units=used_units,
            new_units=new_units,
            multiplier=multiplier,
            removed_objects=removed_objects,
            removed_units=removed_units,
        )

        return veeam_one_license_usage_report_workload
