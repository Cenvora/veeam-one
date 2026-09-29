from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.schedule_interval_type import ScheduleIntervalType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulePlanPeriodical")


@_attrs_define
class SchedulePlanPeriodical:
    """Settings for periodic scheduling.

    Attributes:
        period (Union[Unset, int]): Time interval value. Example: 1.
        interval (Union[Unset, ScheduleIntervalType]): Measurement units configured for interval.
    """

    period: Union[Unset, int] = UNSET
    interval: Union[Unset, ScheduleIntervalType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        period = self.period

        interval: Union[Unset, str] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if period is not UNSET:
            field_dict["period"] = period
        if interval is not UNSET:
            field_dict["interval"] = interval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        period = d.pop("period", UNSET)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, ScheduleIntervalType]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = ScheduleIntervalType(_interval)

        schedule_plan_periodical = cls(
            period=period,
            interval=interval,
        )

        return schedule_plan_periodical
