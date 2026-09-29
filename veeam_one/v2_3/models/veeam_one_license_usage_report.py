from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.license_usage_report_status import LicenseUsageReportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_report_workload import VeeamOneLicenseUsageReportWorkload


T = TypeVar("T", bound="VeeamOneLicenseUsageReport")


@_attrs_define
class VeeamOneLicenseUsageReport:
    """
    Attributes:
        report_id (int | Unset): ID assigned to a license usage report.
        removal_reason (None | str | Unset): Reason for licensed object removal
        workloads (list[VeeamOneLicenseUsageReportWorkload] | None | Unset): Array of licensed objects.
        date (datetime.datetime | Unset): Date and time of license usage report generation. Example:
            '2021-01-01T00:00:00Z'.
        status (LicenseUsageReportStatus | Unset):
        approval_date (datetime.datetime | None | Unset): Date and time of license usage report approval. Example:
            '2021-01-01T12:21:47Z'.
        total_workloads (int | Unset): Total number of licensed objects. Example: 164.
    """

    report_id: int | Unset = UNSET
    removal_reason: None | str | Unset = UNSET
    workloads: list[VeeamOneLicenseUsageReportWorkload] | None | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    status: LicenseUsageReportStatus | Unset = UNSET
    approval_date: datetime.datetime | None | Unset = UNSET
    total_workloads: int | Unset = UNSET

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

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        approval_date: None | str | Unset
        if isinstance(self.approval_date, Unset):
            approval_date = UNSET
        elif isinstance(self.approval_date, datetime.datetime):
            approval_date = self.approval_date.isoformat()
        else:
            approval_date = self.approval_date

        total_workloads = self.total_workloads

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if removal_reason is not UNSET:
            field_dict["removalReason"] = removal_reason
        if workloads is not UNSET:
            field_dict["workloads"] = workloads
        if date is not UNSET:
            field_dict["date"] = date
        if status is not UNSET:
            field_dict["status"] = status
        if approval_date is not UNSET:
            field_dict["approvalDate"] = approval_date
        if total_workloads is not UNSET:
            field_dict["totalWorkloads"] = total_workloads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.veeam_one_license_usage_report_workload import VeeamOneLicenseUsageReportWorkload  # noqa: PLC0415

        d = dict(src_dict)
        report_id = d.pop("reportId", UNSET)

        def _parse_removal_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        removal_reason = _parse_removal_reason(d.pop("removalReason", UNSET))

        def _parse_workloads(data: object) -> list[VeeamOneLicenseUsageReportWorkload] | None | Unset:
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
                    workloads_type_0_item = VeeamOneLicenseUsageReportWorkload.from_dict(workloads_type_0_item_data)

                    workloads_type_0.append(workloads_type_0_item)

                return workloads_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VeeamOneLicenseUsageReportWorkload] | None | Unset, data)

        workloads = _parse_workloads(d.pop("workloads", UNSET))

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        _status = d.pop("status", UNSET)
        status: LicenseUsageReportStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LicenseUsageReportStatus(_status)

        def _parse_approval_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approval_date_type_0 = datetime.datetime.fromisoformat(data)

                return approval_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approval_date = _parse_approval_date(d.pop("approvalDate", UNSET))

        total_workloads = d.pop("totalWorkloads", UNSET)

        veeam_one_license_usage_report = cls(
            report_id=report_id,
            removal_reason=removal_reason,
            workloads=workloads,
            date=date,
            status=status,
            approval_date=approval_date,
            total_workloads=total_workloads,
        )

        return veeam_one_license_usage_report
