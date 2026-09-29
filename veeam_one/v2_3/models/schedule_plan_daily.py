from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulePlanDaily")


@_attrs_define
class SchedulePlanDaily:
    """Settings for daily scheduling.

    Attributes:
        days_of_week (list[DayOfWeek] | None | Unset): Array of week days.
    """

    days_of_week: list[DayOfWeek] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        days_of_week: list[str] | None | Unset
        if isinstance(self.days_of_week, Unset):
            days_of_week = UNSET
        elif isinstance(self.days_of_week, list):
            days_of_week = []
            for days_of_week_type_0_item_data in self.days_of_week:
                days_of_week_type_0_item = days_of_week_type_0_item_data.value
                days_of_week.append(days_of_week_type_0_item)

        else:
            days_of_week = self.days_of_week

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if days_of_week is not UNSET:
            field_dict["daysOfWeek"] = days_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_days_of_week(data: object) -> list[DayOfWeek] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_of_week_type_0 = []
                _days_of_week_type_0 = data
                for days_of_week_type_0_item_data in _days_of_week_type_0:
                    days_of_week_type_0_item = DayOfWeek(days_of_week_type_0_item_data)

                    days_of_week_type_0.append(days_of_week_type_0_item)

                return days_of_week_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DayOfWeek] | None | Unset, data)

        days_of_week = _parse_days_of_week(d.pop("daysOfWeek", UNSET))

        schedule_plan_daily = cls(
            days_of_week=days_of_week,
        )

        return schedule_plan_daily
