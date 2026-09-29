from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alarm_template_type import AlarmTemplateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alarm_assignment import AlarmAssignment


T = TypeVar("T", bound="AlarmTemplateInfo")


@_attrs_define
class AlarmTemplateInfo:
    """
    Attributes:
        alarm_template_id (int | Unset): ID assigned to an alarm template.
        name (None | str | Unset): Name of an alarm.
        type_ (AlarmTemplateType | Unset):
        predefined_alarm_id (int | None | Unset): Internal ID assigned to a predefined alarm template.
        knowledge_summary (None | str | Unset): Description of an alarm.
        knowledge_cause (None | str | Unset): Possible cause of a problem that triggered an alarm.
        knowledge_resolution (None | str | Unset): Instructions for alarm resolution.
        knowledge_custom (None | str | Unset): Additional alarm details.
        knowledge_external (None | str | Unset): Links to external resources containing reference information.
        is_enabled (bool | Unset): Indicates whether an alarm is enabled.
        is_predefined (bool | None | Unset): Indicates whether an alarm is predefined.
        assignments (list[AlarmAssignment] | None | Unset): Array of objects to which an alarm is assigned.
        exclusions (list[AlarmAssignment] | None | Unset): Array of objects excluded from the alarm scope.
    """

    alarm_template_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: AlarmTemplateType | Unset = UNSET
    predefined_alarm_id: int | None | Unset = UNSET
    knowledge_summary: None | str | Unset = UNSET
    knowledge_cause: None | str | Unset = UNSET
    knowledge_resolution: None | str | Unset = UNSET
    knowledge_custom: None | str | Unset = UNSET
    knowledge_external: None | str | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    is_predefined: bool | None | Unset = UNSET
    assignments: list[AlarmAssignment] | None | Unset = UNSET
    exclusions: list[AlarmAssignment] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        alarm_template_id = self.alarm_template_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        predefined_alarm_id: int | None | Unset
        if isinstance(self.predefined_alarm_id, Unset):
            predefined_alarm_id = UNSET
        else:
            predefined_alarm_id = self.predefined_alarm_id

        knowledge_summary: None | str | Unset
        if isinstance(self.knowledge_summary, Unset):
            knowledge_summary = UNSET
        else:
            knowledge_summary = self.knowledge_summary

        knowledge_cause: None | str | Unset
        if isinstance(self.knowledge_cause, Unset):
            knowledge_cause = UNSET
        else:
            knowledge_cause = self.knowledge_cause

        knowledge_resolution: None | str | Unset
        if isinstance(self.knowledge_resolution, Unset):
            knowledge_resolution = UNSET
        else:
            knowledge_resolution = self.knowledge_resolution

        knowledge_custom: None | str | Unset
        if isinstance(self.knowledge_custom, Unset):
            knowledge_custom = UNSET
        else:
            knowledge_custom = self.knowledge_custom

        knowledge_external: None | str | Unset
        if isinstance(self.knowledge_external, Unset):
            knowledge_external = UNSET
        else:
            knowledge_external = self.knowledge_external

        is_enabled = self.is_enabled

        is_predefined: bool | None | Unset
        if isinstance(self.is_predefined, Unset):
            is_predefined = UNSET
        else:
            is_predefined = self.is_predefined

        assignments: list[dict[str, Any]] | None | Unset
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item = assignments_type_0_item_data.to_dict()
                assignments.append(assignments_type_0_item)

        else:
            assignments = self.assignments

        exclusions: list[dict[str, Any]] | None | Unset
        if isinstance(self.exclusions, Unset):
            exclusions = UNSET
        elif isinstance(self.exclusions, list):
            exclusions = []
            for exclusions_type_0_item_data in self.exclusions:
                exclusions_type_0_item = exclusions_type_0_item_data.to_dict()
                exclusions.append(exclusions_type_0_item)

        else:
            exclusions = self.exclusions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alarm_template_id is not UNSET:
            field_dict["alarmTemplateId"] = alarm_template_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if predefined_alarm_id is not UNSET:
            field_dict["predefinedAlarmId"] = predefined_alarm_id
        if knowledge_summary is not UNSET:
            field_dict["knowledgeSummary"] = knowledge_summary
        if knowledge_cause is not UNSET:
            field_dict["knowledgeCause"] = knowledge_cause
        if knowledge_resolution is not UNSET:
            field_dict["knowledgeResolution"] = knowledge_resolution
        if knowledge_custom is not UNSET:
            field_dict["knowledgeCustom"] = knowledge_custom
        if knowledge_external is not UNSET:
            field_dict["knowledgeExternal"] = knowledge_external
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if is_predefined is not UNSET:
            field_dict["isPredefined"] = is_predefined
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alarm_assignment import AlarmAssignment  # noqa: PLC0415

        d = dict(src_dict)
        alarm_template_id = d.pop("alarmTemplateId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: AlarmTemplateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AlarmTemplateType(_type_)

        def _parse_predefined_alarm_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        predefined_alarm_id = _parse_predefined_alarm_id(d.pop("predefinedAlarmId", UNSET))

        def _parse_knowledge_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_summary = _parse_knowledge_summary(d.pop("knowledgeSummary", UNSET))

        def _parse_knowledge_cause(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_cause = _parse_knowledge_cause(d.pop("knowledgeCause", UNSET))

        def _parse_knowledge_resolution(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_resolution = _parse_knowledge_resolution(d.pop("knowledgeResolution", UNSET))

        def _parse_knowledge_custom(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_custom = _parse_knowledge_custom(d.pop("knowledgeCustom", UNSET))

        def _parse_knowledge_external(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        knowledge_external = _parse_knowledge_external(d.pop("knowledgeExternal", UNSET))

        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_is_predefined(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_predefined = _parse_is_predefined(d.pop("isPredefined", UNSET))

        def _parse_assignments(data: object) -> list[AlarmAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assignments_type_0 = []
                _assignments_type_0 = data
                for assignments_type_0_item_data in _assignments_type_0:
                    assignments_type_0_item = AlarmAssignment.from_dict(assignments_type_0_item_data)

                    assignments_type_0.append(assignments_type_0_item)

                return assignments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AlarmAssignment] | None | Unset, data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))

        def _parse_exclusions(data: object) -> list[AlarmAssignment] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusions_type_0 = []
                _exclusions_type_0 = data
                for exclusions_type_0_item_data in _exclusions_type_0:
                    exclusions_type_0_item = AlarmAssignment.from_dict(exclusions_type_0_item_data)

                    exclusions_type_0.append(exclusions_type_0_item)

                return exclusions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AlarmAssignment] | None | Unset, data)

        exclusions = _parse_exclusions(d.pop("exclusions", UNSET))

        alarm_template_info = cls(
            alarm_template_id=alarm_template_id,
            name=name,
            type_=type_,
            predefined_alarm_id=predefined_alarm_id,
            knowledge_summary=knowledge_summary,
            knowledge_cause=knowledge_cause,
            knowledge_resolution=knowledge_resolution,
            knowledge_custom=knowledge_custom,
            knowledge_external=knowledge_external,
            is_enabled=is_enabled,
            is_predefined=is_predefined,
            assignments=assignments,
            exclusions=exclusions,
        )

        return alarm_template_info
