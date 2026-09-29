from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_report_approve_workload import VeeamOneLicenseUsageReportApproveWorkload


T = TypeVar("T", bound="VeeamOneLicenseUsageReportApprove")


@_attrs_define
class VeeamOneLicenseUsageReportApprove:
    """
    Attributes:
        report_id (int | Unset): ID assigned to a license usage report.
        removal_reason (None | str | Unset): Reason for the removal of a licensed object.
        workloads (list[VeeamOneLicenseUsageReportApproveWorkload] | None | Unset): Array of managed workloads.
    """

    report_id: int | Unset = UNSET
    removal_reason: None | str | Unset = UNSET
    workloads: list[VeeamOneLicenseUsageReportApproveWorkload] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        removal_reason: None | str | Unset
        if isinstance(self.removal_reason, Unset):
            removal_reason = UNSET
        else:
            removal_reason = self.removal_reason

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
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason
        if workloads is not UNSET:
            field_dict["workloads"] = workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.veeam_one_license_usage_report_approve_workload import (
            VeeamOneLicenseUsageReportApproveWorkload,  # noqa: PLC0415
        )

        d = dict(src_dict)
        report_id = d.pop("reportId", UNSET)

        def _parse_removal_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removal_reason = _parse_removal_reason(d.pop("removalReason", UNSET))

        def _parse_workloads(data: object) -> list[VeeamOneLicenseUsageReportApproveWorkload] | None | Unset:
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
                    workloads_type_0_item = VeeamOneLicenseUsageReportApproveWorkload.from_dict(
                        workloads_type_0_item_data
                    )

                    workloads_type_0.append(workloads_type_0_item)

                return workloads_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VeeamOneLicenseUsageReportApproveWorkload] | None | Unset, data)

        workloads = _parse_workloads(d.pop("workloads", UNSET))

        veeam_one_license_usage_report_approve = cls(
            report_id=report_id,
            removal_reason=removal_reason,
            workloads=workloads,
        )

        return veeam_one_license_usage_report_approve
