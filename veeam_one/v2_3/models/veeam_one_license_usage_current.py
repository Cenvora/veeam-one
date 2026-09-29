from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.veeam_one_license_usage_unit_type import VeeamOneLicenseUsageUnitType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_common_workload import VeeamOneLicenseUsageCommonWorkload


T = TypeVar("T", bound="VeeamOneLicenseUsageCurrent")


@_attrs_define
class VeeamOneLicenseUsageCurrent:
    """
    Attributes:
        units_type (VeeamOneLicenseUsageUnitType | Unset): Type of license units.
        workloads (list[VeeamOneLicenseUsageCommonWorkload] | None | Unset): Array of licensed objects.
    """

    units_type: VeeamOneLicenseUsageUnitType | Unset = UNSET
    workloads: list[VeeamOneLicenseUsageCommonWorkload] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        units_type: str | Unset = UNSET
        if not isinstance(self.units_type, Unset):
            units_type = self.units_type.value

        workloads: list[dict[str, Any]] | None | Unset
        if isinstance(self.workloads, Unset):
            workloads = UNSET
        elif isinstance(self.workloads, list):
            workloads = []
            for workloads_type_0_item_data in self.workloads:
                workloads_type_0_item = workloads_type_0_item_data.to_dict()
                workloads.append(workloads_type_0_item)

        else:
            workloads = self.workloads

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if units_type is not UNSET:
            field_dict["unitsType"] = units_type
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.veeam_one_license_usage_common_workload import VeeamOneLicenseUsageCommonWorkload  # noqa: PLC0415

        d = dict(src_dict)
        _units_type = d.pop("unitsType", UNSET)
        units_type: VeeamOneLicenseUsageUnitType | Unset
        if isinstance(_units_type, Unset):
            units_type = UNSET
        else:
            units_type = VeeamOneLicenseUsageUnitType(_units_type)

        def _parse_workloads(data: object) -> list[VeeamOneLicenseUsageCommonWorkload] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                workloads_type_0 = []
                _workloads_type_0 = data
                for workloads_type_0_item_data in _workloads_type_0:
                    workloads_type_0_item = VeeamOneLicenseUsageCommonWorkload.from_dict(workloads_type_0_item_data)

                    workloads_type_0.append(workloads_type_0_item)

                return workloads_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VeeamOneLicenseUsageCommonWorkload] | None | Unset, data)

        workloads = _parse_workloads(d.pop("workloads", UNSET))

        veeam_one_license_usage_current = cls(
            units_type=units_type,
            workloads=workloads,
        )

        return veeam_one_license_usage_current
