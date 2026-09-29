from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.resolve_type import ResolveType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResolveMultipleTriggeredChildAlarmsRequest")


@_attrs_define
class ResolveMultipleTriggeredChildAlarmsRequest:
    """
    Attributes:
        triggered_child_alarm_ids (list[int]): List of IDs assigned to triggered child alarms that you want to resolve.
        comment (str): Additional information.
        resolve_type (Union[Unset, ResolveType]):
    """

    triggered_child_alarm_ids: list[int]
    comment: str
    resolve_type: Union[Unset, ResolveType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        triggered_child_alarm_ids = self.triggered_child_alarm_ids

        comment = self.comment

        resolve_type: Union[Unset, str] = UNSET
        if not isinstance(self.resolve_type, Unset):
            resolve_type = self.resolve_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "triggeredChildAlarmIds": triggered_child_alarm_ids,
                "comment": comment,
            }
        )
        if resolve_type is not UNSET:
            field_dict["resolveType"] = resolve_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        triggered_child_alarm_ids = cast(list[int], d.pop("triggeredChildAlarmIds"))

        comment = d.pop("comment")

        _resolve_type = d.pop("resolveType", UNSET)
        resolve_type: Union[Unset, ResolveType]
        if isinstance(_resolve_type, Unset):
            resolve_type = UNSET
        else:
            resolve_type = ResolveType(_resolve_type)

        resolve_multiple_triggered_child_alarms_request = cls(
            triggered_child_alarm_ids=triggered_child_alarm_ids,
            comment=comment,
            resolve_type=resolve_type,
        )

        return resolve_multiple_triggered_child_alarms_request
