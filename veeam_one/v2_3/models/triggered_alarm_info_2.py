from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alarm_status import AlarmStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alarm_source import AlarmSource
    from ..models.remediations import Remediations


T = TypeVar("T", bound="TriggeredAlarmInfo2")


@_attrs_define
class TriggeredAlarmInfo2:
    """
    Attributes:
        triggered_alarm_id (int | Unset): ID assigned to a triggered alarm.
        name (None | str | Unset): Name of an alarm template.
        alarm_template_id (int | Unset): ID assigned to an alarm template.
        predefined_alarm_id (int | None | Unset): Internal ID assigned to a predefined alarm template.
        triggered_time (datetime.datetime | Unset): Date and time when an alarm triggered.
        status (AlarmStatus | Unset):
        description (None | str | Unset): Message containing alarm details.
        comment (None | str | Unset): Comment on a triggered alarm.
        repeat_count (int | Unset): Number of times an alarm was triggered.
        alarm_source (AlarmSource | None | Unset): Object for which an alarm was triggered.
        child_alarms_count (int | Unset): Number of alarm child objects.
        remediation (None | Remediations | Unset): Array of the remediation actions.
    """

    triggered_alarm_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    alarm_template_id: int | Unset = UNSET
    predefined_alarm_id: int | None | Unset = UNSET
    triggered_time: datetime.datetime | Unset = UNSET
    status: AlarmStatus | Unset = UNSET
    description: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    repeat_count: int | Unset = UNSET
    alarm_source: AlarmSource | None | Unset = UNSET
    child_alarms_count: int | Unset = UNSET
    remediation: None | Remediations | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.alarm_source import AlarmSource  # noqa: PLC0415
        from ..models.remediations import Remediations  # noqa: PLC0415

        triggered_alarm_id = self.triggered_alarm_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        alarm_template_id = self.alarm_template_id

        predefined_alarm_id: int | None | Unset
        if isinstance(self.predefined_alarm_id, Unset):
            predefined_alarm_id = UNSET
        else:
            predefined_alarm_id = self.predefined_alarm_id

        triggered_time: str | Unset = UNSET
        if not isinstance(self.triggered_time, Unset):
            triggered_time = self.triggered_time.isoformat()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        repeat_count = self.repeat_count

        alarm_source: dict[str, Any] | None | Unset
        if isinstance(self.alarm_source, Unset):
            alarm_source = UNSET
        elif isinstance(self.alarm_source, AlarmSource):
            alarm_source = self.alarm_source.to_dict()
        else:
            alarm_source = self.alarm_source

        child_alarms_count = self.child_alarms_count

        remediation: dict[str, Any] | None | Unset
        if isinstance(self.remediation, Unset):
            remediation = UNSET
        elif isinstance(self.remediation, Remediations):
            remediation = self.remediation.to_dict()
        else:
            remediation = self.remediation

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if triggered_alarm_id is not UNSET:
            field_dict["triggeredAlarmId"] = triggered_alarm_id
        if name is not UNSET:
            field_dict["name"] = name
        if alarm_template_id is not UNSET:
            field_dict["alarmTemplateId"] = alarm_template_id
        if predefined_alarm_id is not UNSET:
            field_dict["predefinedAlarmId"] = predefined_alarm_id
        if triggered_time is not UNSET:
            field_dict["triggeredTime"] = triggered_time
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if comment is not UNSET:
            field_dict["comment"] = comment
        if repeat_count is not UNSET:
            field_dict["repeatCount"] = repeat_count
        if alarm_source is not UNSET:
            field_dict["alarmSource"] = alarm_source
        if child_alarms_count is not UNSET:
            field_dict["childAlarmsCount"] = child_alarms_count
        if remediation is not UNSET:
            field_dict["remediation"] = remediation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_source import AlarmSource  # noqa: PLC0415
        from ..models.remediations import Remediations  # noqa: PLC0415

        d = dict(src_dict)
        triggered_alarm_id = d.pop("triggeredAlarmId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        alarm_template_id = d.pop("alarmTemplateId", UNSET)

        def _parse_predefined_alarm_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        predefined_alarm_id = _parse_predefined_alarm_id(d.pop("predefinedAlarmId", UNSET))

        _triggered_time = d.pop("triggeredTime", UNSET)
        triggered_time: datetime.datetime | Unset
        if isinstance(_triggered_time, Unset):
            triggered_time = UNSET
        else:
            triggered_time = datetime.datetime.fromisoformat(_triggered_time)

        _status = d.pop("status", UNSET)
        status: AlarmStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AlarmStatus(_status)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        repeat_count = d.pop("repeatCount", UNSET)

        def _parse_alarm_source(data: object) -> AlarmSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alarm_source_type_1 = AlarmSource.from_dict(data)

                return alarm_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AlarmSource | None | Unset, data)

        alarm_source = _parse_alarm_source(d.pop("alarmSource", UNSET))

        child_alarms_count = d.pop("childAlarmsCount", UNSET)

        def _parse_remediation(data: object) -> None | Remediations | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                remediation_type_1 = Remediations.from_dict(data)

                return remediation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Remediations | Unset, data)

        remediation = _parse_remediation(d.pop("remediation", UNSET))

        triggered_alarm_info_2 = cls(
            triggered_alarm_id=triggered_alarm_id,
            name=name,
            alarm_template_id=alarm_template_id,
            predefined_alarm_id=predefined_alarm_id,
            triggered_time=triggered_time,
            status=status,
            description=description,
            comment=comment,
            repeat_count=repeat_count,
            alarm_source=alarm_source,
            child_alarms_count=child_alarms_count,
            remediation=remediation,
        )

        return triggered_alarm_info_2
