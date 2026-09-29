from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.child_alarm_status import ChildAlarmStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggeredChildAlarmInfo")


@_attrs_define
class TriggeredChildAlarmInfo:
    """
    Attributes:
        child_alarm_id (int | Unset): ID assigned to an alarm that triggered for a child object.
        triggered_alarm_id (int | Unset): ID assigned to a triggered alarm.
        triggered_time (datetime.datetime | Unset): Date and time when an alarm triggered.
        status (ChildAlarmStatus | Unset):
        source (None | str | Unset): Name of the infrastructure object that caused the alarm.
        description (None | str | Unset): Message containing alarm details.
        repeat_count (int | Unset): Number of times an alarm was triggered.
        comment (None | str | Unset): Alarm comment.
    """

    child_alarm_id: int | Unset = UNSET
    triggered_alarm_id: int | Unset = UNSET
    triggered_time: datetime.datetime | Unset = UNSET
    status: ChildAlarmStatus | Unset = UNSET
    source: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    repeat_count: int | Unset = UNSET
    comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        child_alarm_id = self.child_alarm_id

        triggered_alarm_id = self.triggered_alarm_id

        triggered_time: str | Unset = UNSET
        if not isinstance(self.triggered_time, Unset):
            triggered_time = self.triggered_time.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        repeat_count = self.repeat_count

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if child_alarm_id is not UNSET:
            field_dict["childAlarmId"] = child_alarm_id
        if triggered_alarm_id is not UNSET:
            field_dict["triggeredAlarmId"] = triggered_alarm_id
        if triggered_time is not UNSET:
            field_dict["triggeredTime"] = triggered_time
        if status is not UNSET:
            field_dict["status"] = status
        if source is not UNSET:
            field_dict["source"] = source
        if description is not UNSET:
            field_dict["description"] = description
        if repeat_count is not UNSET:
            field_dict["repeatCount"] = repeat_count
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        child_alarm_id = d.pop("childAlarmId", UNSET)

        triggered_alarm_id = d.pop("triggeredAlarmId", UNSET)

        _triggered_time = d.pop("triggeredTime", UNSET)
        triggered_time: datetime.datetime | Unset
        if isinstance(_triggered_time, Unset):
            triggered_time = UNSET
        else:
            triggered_time = datetime.datetime.fromisoformat(_triggered_time)

        _status = d.pop("status", UNSET)
        status: ChildAlarmStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ChildAlarmStatus(_status)

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        repeat_count = d.pop("repeatCount", UNSET)

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        triggered_child_alarm_info = cls(
            child_alarm_id=child_alarm_id,
            triggered_alarm_id=triggered_alarm_id,
            triggered_time=triggered_time,
            status=status,
            source=source,
            description=description,
            repeat_count=repeat_count,
            comment=comment,
        )

        return triggered_child_alarm_info
