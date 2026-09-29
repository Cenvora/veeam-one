from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseUsageCommonWorkload")


@_attrs_define
class VeeamOneLicenseUsageCommonWorkload:
    """
    Attributes:
        workload_type (Union[None, Unset, str]): Type of licensed objects. Example: Virtual Machines.
        used_objects (Union[Unset, int]): Number of licensed objects. Example: 376.
        new_objects (Union[None, Unset, int]): Number of new objects. Example: 2.
        used_units (Union[Unset, float]): Number of consumed license units. Example: 376.
        new_units (Union[None, Unset, float]): Number of license units that new objects will consume. Example: 2.
        multiplier (Union[Unset, int]): License unit multiplier. Example: 1.
    """

    workload_type: Union[None, Unset, str] = UNSET
    used_objects: Union[Unset, int] = UNSET
    new_objects: Union[None, Unset, int] = UNSET
    used_units: Union[Unset, float] = UNSET
    new_units: Union[None, Unset, float] = UNSET
    multiplier: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        workload_type: Union[None, Unset, str]
        if isinstance(self.workload_type, Unset):
            workload_type = UNSET
        else:
            workload_type = self.workload_type

        used_objects = self.used_objects

        new_objects: Union[None, Unset, int]
        if isinstance(self.new_objects, Unset):
            new_objects = UNSET
        else:
            new_objects = self.new_objects

        used_units = self.used_units

        new_units: Union[None, Unset, float]
        if isinstance(self.new_units, Unset):
            new_units = UNSET
        else:
            new_units = self.new_units

        multiplier = self.multiplier

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workload_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        workload_type = _parse_workload_type(d.pop("workloadType", UNSET))

        used_objects = d.pop("usedObjects", UNSET)

        def _parse_new_objects(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        new_objects = _parse_new_objects(d.pop("newObjects", UNSET))

        used_units = d.pop("usedUnits", UNSET)

        def _parse_new_units(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        new_units = _parse_new_units(d.pop("newUnits", UNSET))

        multiplier = d.pop("multiplier", UNSET)

        veeam_one_license_usage_common_workload = cls(
            workload_type=workload_type,
            used_objects=used_objects,
            new_objects=new_objects,
            used_units=used_units,
            new_units=new_units,
            multiplier=multiplier,
        )

        return veeam_one_license_usage_common_workload
