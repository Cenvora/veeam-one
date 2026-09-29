import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.child_alarm_status import ChildAlarmStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="TriggeredChildAlarmInfo")


@_attrs_define
class TriggeredChildAlarmInfo:
    """
    Attributes:
        child_alarm_id (Union[Unset, int]): ID assigned to an alarm that triggered for a child object.
        triggered_alarm_id (Union[Unset, int]): ID assigned to a triggered alarm.
        triggered_time (Union[Unset, datetime.datetime]): Date and time when an alarm triggered.
        status (Union[Unset, ChildAlarmStatus]):
        source (Union[None, Unset, str]): Name of the infrastructure object that caused the alarm.
        description (Union[None, Unset, str]): Message containing alarm details.
        repeat_count (Union[Unset, int]): Number of times an alarm was triggered.
        comment (Union[None, Unset, str]): Alarm comment.
    """

    child_alarm_id: Union[Unset, int] = UNSET
    triggered_alarm_id: Union[Unset, int] = UNSET
    triggered_time: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, ChildAlarmStatus] = UNSET
    source: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    repeat_count: Union[Unset, int] = UNSET
    comment: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        child_alarm_id = self.child_alarm_id

        triggered_alarm_id = self.triggered_alarm_id

        triggered_time: Union[Unset, str] = UNSET
        if not isinstance(self.triggered_time, Unset):
            triggered_time = self.triggered_time.isoformat()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        source: Union[None, Unset, str]
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        repeat_count = self.repeat_count

        comment: Union[None, Unset, str]
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
        triggered_time: Union[Unset, datetime.datetime]
        if isinstance(_triggered_time, Unset):
            triggered_time = UNSET
        else:
            triggered_time = isoparse(_triggered_time)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ChildAlarmStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ChildAlarmStatus(_status)

        def _parse_source(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        repeat_count = d.pop("repeatCount", UNSET)

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
