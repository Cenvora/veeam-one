from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.collecting_object_type import CollectingObjectType
from ..models.schedule_session_status import ScheduleSessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectingSessionInfo")


@_attrs_define
class CollectingSessionInfo:
    """
    Attributes:
        session_id (int | Unset): ID assigned to a data collection session. Example: 1255.
        task_id (int | Unset): ID assigned to a data collection task. Example: 1255.
        name (None | str | Unset): Name of an infrastructure server from which data is collected. Example: bckp_srv3.
        status (ScheduleSessionStatus | Unset): Task session status.
        status_priority (int | Unset): Number assigned to a task status that defines task position in the list.
        modified (datetime.datetime | None | Unset): Date and time of the latest data collection task modification.
            Example: '2021-01-10T11:44:42.09Z'.
        last_run (datetime.datetime | None | Unset): Date and time of the latest data collection session. Example:
            '2021-01-12T11:44:42.09Z'.
        collecting_type (CollectingObjectType | Unset): Type of the collected data.
    """

    session_id: int | Unset = UNSET
    task_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    status: ScheduleSessionStatus | Unset = UNSET
    status_priority: int | Unset = UNSET
    modified: datetime.datetime | None | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    collecting_type: CollectingObjectType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        task_id = self.task_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_priority = self.status_priority

        modified: None | str | Unset
        if isinstance(self.modified, Unset):
            modified = UNSET
        elif isinstance(self.modified, datetime.datetime):
            modified = self.modified.isoformat()
        else:
            modified = self.modified

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        collecting_type: str | Unset = UNSET
        if not isinstance(self.collecting_type, Unset):
            collecting_type = self.collecting_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_priority is not UNSET:
            field_dict["statusPriority"] = status_priority
        if modified is not UNSET:
            field_dict["modified"] = modified
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if collecting_type is not UNSET:
            field_dict["collectingType"] = collecting_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId", UNSET)

        task_id = d.pop("taskId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _status = d.pop("status", UNSET)
        status: ScheduleSessionStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScheduleSessionStatus(_status)

        status_priority = d.pop("statusPriority", UNSET)

        def _parse_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modified_type_0 = datetime.datetime.fromisoformat(data)

                return modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        modified = _parse_modified(d.pop("modified", UNSET))

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        _collecting_type = d.pop("collectingType", UNSET)
        collecting_type: CollectingObjectType | Unset
        if isinstance(_collecting_type, Unset):
            collecting_type = UNSET
        else:
            collecting_type = CollectingObjectType(_collecting_type)

        collecting_session_info = cls(
            session_id=session_id,
            task_id=task_id,
            name=name,
            status=status,
            status_priority=status_priority,
            modified=modified,
            last_run=last_run,
            collecting_type=collecting_type,
        )

        return collecting_session_info
