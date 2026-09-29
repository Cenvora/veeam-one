from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.day_of_week import DayOfWeek
from ..models.day_of_week_appearance import DayOfWeekAppearance
from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulePlanMonthlyWeekDays")


@_attrs_define
class SchedulePlanMonthlyWeekDays:
    """Scheduling settings for monthly data collection on specific week days.

    Attributes:
        months (list[Month] | None | Unset): Array of months.
        day_of_week_appearance (list[DayOfWeekAppearance] | None | Unset): Ordinal numeral.
        days_of_week (list[DayOfWeek] | None | Unset): Week day.
    """

    months: list[Month] | None | Unset = UNSET
    day_of_week_appearance: list[DayOfWeekAppearance] | None | Unset = UNSET
    days_of_week: list[DayOfWeek] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        months: list[str] | None | Unset
        if isinstance(self.months, Unset):
            months = UNSET
        elif isinstance(self.months, list):
            months = []
            for months_type_0_item_data in self.months:
                months_type_0_item = months_type_0_item_data.value
                months.append(months_type_0_item)

        else:
            months = self.months

        day_of_week_appearance: list[str] | None | Unset
        if isinstance(self.day_of_week_appearance, Unset):
            day_of_week_appearance = UNSET
        elif isinstance(self.day_of_week_appearance, list):
            day_of_week_appearance = []
            for day_of_week_appearance_type_0_item_data in self.day_of_week_appearance:
                day_of_week_appearance_type_0_item = day_of_week_appearance_type_0_item_data.value
                day_of_week_appearance.append(day_of_week_appearance_type_0_item)

        else:
            day_of_week_appearance = self.day_of_week_appearance

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
        if months is not UNSET:
            field_dict["months"] = months
        if day_of_week_appearance is not UNSET:
            field_dict["dayOfWeekAppearance"] = day_of_week_appearance
        if days_of_week is not UNSET:
            field_dict["daysOfWeek"] = days_of_week

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_months(data: object) -> list[Month] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                months_type_0 = []
                _months_type_0 = data
                for months_type_0_item_data in _months_type_0:
                    months_type_0_item = Month(months_type_0_item_data)

                    months_type_0.append(months_type_0_item)

                return months_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Month] | None | Unset, data)

        months = _parse_months(d.pop("months", UNSET))

        def _parse_day_of_week_appearance(data: object) -> list[DayOfWeekAppearance] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                day_of_week_appearance_type_0 = []
                _day_of_week_appearance_type_0 = data
                for day_of_week_appearance_type_0_item_data in _day_of_week_appearance_type_0:
                    day_of_week_appearance_type_0_item = DayOfWeekAppearance(day_of_week_appearance_type_0_item_data)

                    day_of_week_appearance_type_0.append(day_of_week_appearance_type_0_item)

                return day_of_week_appearance_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DayOfWeekAppearance] | None | Unset, data)

        day_of_week_appearance = _parse_day_of_week_appearance(d.pop("dayOfWeekAppearance", UNSET))

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

        schedule_plan_monthly_week_days = cls(
            months=months,
            day_of_week_appearance=day_of_week_appearance,
            days_of_week=days_of_week,
        )

        return schedule_plan_monthly_week_days
