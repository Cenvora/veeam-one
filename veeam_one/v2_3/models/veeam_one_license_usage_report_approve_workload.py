from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseUsageReportApproveWorkload")


@_attrs_define
class VeeamOneLicenseUsageReportApproveWorkload:
    """
    Attributes:
        workload_type (None | str | Unset): Type of managed workloads.
        used_objects (int | Unset): Number of managed workloads.
    """

    workload_type: None | str | Unset = UNSET
    used_objects: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        workload_type: None | str | Unset
        if isinstance(self.workload_type, Unset):
            workload_type = UNSET
        else:
            workload_type = self.workload_type

        used_objects = self.used_objects

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if workload_type is not UNSET:
            field_dict["workloadType"] = workload_type
        if used_objects is not UNSET:
            field_dict["usedObjects"] = used_objects

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

        veeam_one_license_usage_report_approve_workload = cls(
            workload_type=workload_type,
            used_objects=used_objects,
        )

        return veeam_one_license_usage_report_approve_workload
