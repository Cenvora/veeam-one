from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.schedule_session_status import ScheduleSessionStatus
from ..models.sessions_task_types import SessionsTaskTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSessionInfo")


@_attrs_define
class JobSessionInfo:
    """
    Attributes:
        job_session_id (int | Unset): ID assigned to a task session. Example: 1034.
        name (None | str | Unset): Name of a task. Example: Object properties data collection.
        type_ (SessionsTaskTypes | Unset): Type of a data collecion task.
        status (ScheduleSessionStatus | Unset): Task session status.
        status_priority (int | Unset): Number that indicates the list position of all job sessions with the same status.
        start (datetime.datetime | None | Unset): Date and time of a task session start. Example:
            '2021-01-29T11:43:35.69Z'.
        end (datetime.datetime | None | Unset): Date and time of a task session end. Example: '2021-01-29T11:43:36.69Z'.
    """

    job_session_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: SessionsTaskTypes | Unset = UNSET
    status: ScheduleSessionStatus | Unset = UNSET
    status_priority: int | Unset = UNSET
    start: datetime.datetime | None | Unset = UNSET
    end: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        job_session_id = self.job_session_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_priority = self.status_priority

        start: None | str | Unset
        if isinstance(self.start, Unset):
            start = UNSET
        elif isinstance(self.start, datetime.datetime):
            start = self.start.isoformat()
        else:
            start = self.start

        end: None | str | Unset
        if isinstance(self.end, Unset):
            end = UNSET
        elif isinstance(self.end, datetime.datetime):
            end = self.end.isoformat()
        else:
            end = self.end

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if job_session_id is not UNSET:
            field_dict["jobSessionId"] = job_session_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if status_priority is not UNSET:
            field_dict["statusPriority"] = status_priority
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_session_id = d.pop("jobSessionId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: SessionsTaskTypes | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SessionsTaskTypes(_type_)

        _status = d.pop("status", UNSET)
        status: ScheduleSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScheduleSessionStatus(_status)

        status_priority = d.pop("statusPriority", UNSET)

        def _parse_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_type_0 = datetime.datetime.fromisoformat(data)

                return start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start = _parse_start(d.pop("start", UNSET))

        def _parse_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_type_0 = datetime.datetime.fromisoformat(data)

                return end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end = _parse_end(d.pop("end", UNSET))

        job_session_info = cls(
            job_session_id=job_session_id,
            name=name,
            type_=type_,
            status=status,
            status_priority=status_priority,
            start=start,
            end=end,
        )

        return job_session_info
