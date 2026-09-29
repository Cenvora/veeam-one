import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSessionDetailsInfo")


@_attrs_define
class JobSessionDetailsInfo:
    """
    Attributes:
        session_record_id (Union[Unset, int]): ID assigned to a log record that was generated for an operation.
        details (Union[None, Unset, str]): Operation details. Example: Veeam ONE is installed successfully. Root objects
            are collected..
        log_date_time (Union[None, Unset, datetime.datetime]): Date and time when the log record was generated for an
            operation. Example: '2021-01-27T11:54:31.84Z'.
    """

    session_record_id: Union[Unset, int] = UNSET
    details: Union[None, Unset, str] = UNSET
    log_date_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_record_id = self.session_record_id

        details: Union[None, Unset, str]
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        log_date_time: Union[None, Unset, str]
        if isinstance(self.log_date_time, Unset):
            log_date_time = UNSET
        elif isinstance(self.log_date_time, datetime.datetime):
            log_date_time = self.log_date_time.isoformat()
        else:
            log_date_time = self.log_date_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_record_id is not UNSET:
            field_dict["sessionRecordId"] = session_record_id
        if details is not UNSET:
            field_dict["details"] = details
        if log_date_time is not UNSET:
            field_dict["logDateTime"] = log_date_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_record_id = d.pop("sessionRecordId", UNSET)

        def _parse_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_log_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                log_date_time_type_0 = isoparse(data)

                return log_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        log_date_time = _parse_log_date_time(d.pop("logDateTime", UNSET))

        job_session_details_info = cls(
            session_record_id=session_record_id,
            details=details,
            log_date_time=log_date_time,
        )

        return job_session_details_info
