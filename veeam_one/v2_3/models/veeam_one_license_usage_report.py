import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.license_usage_report_status import LicenseUsageReportStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_report_workload import VeeamOneLicenseUsageReportWorkload


T = TypeVar("T", bound="VeeamOneLicenseUsageReport")


@_attrs_define
class VeeamOneLicenseUsageReport:
    """
    Attributes:
        report_id (Union[Unset, int]): ID assigned to a license usage report.
        removal_reason (Union[None, Unset, str]): Reason for licensed object removal
        workloads (Union[None, Unset, list['VeeamOneLicenseUsageReportWorkload']]): Array of licensed objects.
        date (Union[Unset, datetime.datetime]): Date and time of license usage report generation. Example:
            '2021-01-01T00:00:00Z'.
        status (Union[Unset, LicenseUsageReportStatus]):
        approval_date (Union[None, Unset, datetime.datetime]): Date and time of license usage report approval. Example:
            '2021-01-01T12:21:47Z'.
        total_workloads (Union[Unset, int]): Total number of licensed objects. Example: 164.
    """

    report_id: Union[Unset, int] = UNSET
    removal_reason: Union[None, Unset, str] = UNSET
    workloads: Union[None, Unset, list["VeeamOneLicenseUsageReportWorkload"]] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, LicenseUsageReportStatus] = UNSET
    approval_date: Union[None, Unset, datetime.datetime] = UNSET
    total_workloads: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        report_id = self.report_id

        removal_reason: Union[None, Unset, str]
        if isinstance(self.removal_reason, Unset):
            removal_reason = UNSET
        else:
            removal_reason = self.removal_reason

        workloads: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.workloads, Unset):
            workloads = UNSET
        elif isinstance(self.workloads, list):
            workloads = []
            for workloads_type_0_item_data in self.workloads:
                workloads_type_0_item = workloads_type_0_item_data.to_dict()
                workloads.append(workloads_type_0_item)

        else:
            workloads = self.workloads

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        approval_date: Union[None, Unset, str]
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
        from ..models.veeam_one_license_usage_report_workload import VeeamOneLicenseUsageReportWorkload

        d = dict(src_dict)
        report_id = d.pop("reportId", UNSET)

        def _parse_removal_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        removal_reason = _parse_removal_reason(d.pop("removalReason", UNSET))

        def _parse_workloads(data: object) -> Union[None, Unset, list["VeeamOneLicenseUsageReportWorkload"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["VeeamOneLicenseUsageReportWorkload"]], data)

        workloads = _parse_workloads(d.pop("workloads", UNSET))

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LicenseUsageReportStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LicenseUsageReportStatus(_status)

        def _parse_approval_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approval_date_type_0 = isoparse(data)

                return approval_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

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
