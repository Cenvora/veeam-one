from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

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
        alarm_template_id (Union[Unset, int]): ID assigned to an alarm template.
        name (Union[None, Unset, str]): Name of an alarm.
        type_ (Union[Unset, AlarmTemplateType]):
        predefined_alarm_id (Union[None, Unset, int]): Internal ID assigned to a predefined alarm template.
        knowledge_summary (Union[None, Unset, str]): Description of an alarm.
        knowledge_cause (Union[None, Unset, str]): Possible cause of a problem that triggered an alarm.
        knowledge_resolution (Union[None, Unset, str]): Instructions for alarm resolution.
        knowledge_custom (Union[None, Unset, str]): Additional alarm details.
        knowledge_external (Union[None, Unset, str]): Links to external resources containing reference information.
        is_enabled (Union[Unset, bool]): Indicates whether an alarm is enabled.
        is_predefined (Union[None, Unset, bool]): Indicates whether an alarm is predefined.
        assignments (Union[None, Unset, list['AlarmAssignment']]): Array of objects to which an alarm is assigned.
        exclusions (Union[None, Unset, list['AlarmAssignment']]): Array of objects excluded from the alarm scope.
    """

    alarm_template_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, AlarmTemplateType] = UNSET
    predefined_alarm_id: Union[None, Unset, int] = UNSET
    knowledge_summary: Union[None, Unset, str] = UNSET
    knowledge_cause: Union[None, Unset, str] = UNSET
    knowledge_resolution: Union[None, Unset, str] = UNSET
    knowledge_custom: Union[None, Unset, str] = UNSET
    knowledge_external: Union[None, Unset, str] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_predefined: Union[None, Unset, bool] = UNSET
    assignments: Union[None, Unset, list["AlarmAssignment"]] = UNSET
    exclusions: Union[None, Unset, list["AlarmAssignment"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        alarm_template_id = self.alarm_template_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        predefined_alarm_id: Union[None, Unset, int]
        if isinstance(self.predefined_alarm_id, Unset):
            predefined_alarm_id = UNSET
        else:
            predefined_alarm_id = self.predefined_alarm_id

        knowledge_summary: Union[None, Unset, str]
        if isinstance(self.knowledge_summary, Unset):
            knowledge_summary = UNSET
        else:
            knowledge_summary = self.knowledge_summary

        knowledge_cause: Union[None, Unset, str]
        if isinstance(self.knowledge_cause, Unset):
            knowledge_cause = UNSET
        else:
            knowledge_cause = self.knowledge_cause

        knowledge_resolution: Union[None, Unset, str]
        if isinstance(self.knowledge_resolution, Unset):
            knowledge_resolution = UNSET
        else:
            knowledge_resolution = self.knowledge_resolution

        knowledge_custom: Union[None, Unset, str]
        if isinstance(self.knowledge_custom, Unset):
            knowledge_custom = UNSET
        else:
            knowledge_custom = self.knowledge_custom

        knowledge_external: Union[None, Unset, str]
        if isinstance(self.knowledge_external, Unset):
            knowledge_external = UNSET
        else:
            knowledge_external = self.knowledge_external

        is_enabled = self.is_enabled

        is_predefined: Union[None, Unset, bool]
        if isinstance(self.is_predefined, Unset):
            is_predefined = UNSET
        else:
            is_predefined = self.is_predefined

        assignments: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.assignments, Unset):
            assignments = UNSET
        elif isinstance(self.assignments, list):
            assignments = []
            for assignments_type_0_item_data in self.assignments:
                assignments_type_0_item = assignments_type_0_item_data.to_dict()
                assignments.append(assignments_type_0_item)

        else:
            assignments = self.assignments

        exclusions: Union[None, Unset, list[dict[str, Any]]]
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
        from ..models.alarm_assignment import AlarmAssignment

        d = dict(src_dict)
        alarm_template_id = d.pop("alarmTemplateId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AlarmTemplateType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = AlarmTemplateType(_type_)

        def _parse_predefined_alarm_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        predefined_alarm_id = _parse_predefined_alarm_id(d.pop("predefinedAlarmId", UNSET))

        def _parse_knowledge_summary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        knowledge_summary = _parse_knowledge_summary(d.pop("knowledgeSummary", UNSET))

        def _parse_knowledge_cause(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        knowledge_cause = _parse_knowledge_cause(d.pop("knowledgeCause", UNSET))

        def _parse_knowledge_resolution(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        knowledge_resolution = _parse_knowledge_resolution(d.pop("knowledgeResolution", UNSET))

        def _parse_knowledge_custom(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        knowledge_custom = _parse_knowledge_custom(d.pop("knowledgeCustom", UNSET))

        def _parse_knowledge_external(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        knowledge_external = _parse_knowledge_external(d.pop("knowledgeExternal", UNSET))

        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_is_predefined(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_predefined = _parse_is_predefined(d.pop("isPredefined", UNSET))

        def _parse_assignments(data: object) -> Union[None, Unset, list["AlarmAssignment"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlarmAssignment"]], data)

        assignments = _parse_assignments(d.pop("assignments", UNSET))

        def _parse_exclusions(data: object) -> Union[None, Unset, list["AlarmAssignment"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["AlarmAssignment"]], data)

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
