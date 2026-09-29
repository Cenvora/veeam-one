from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.month import Month
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulePlanMonthlyDays")


@_attrs_define
class SchedulePlanMonthlyDays:
    """Scheduling settings for monthly data collection on specific date.

    Attributes:
        months (Union[None, Unset, list[Month]]): Array of months.
        days (Union[None, Unset, list[int]]): Array of dates.
    """

    months: Union[None, Unset, list[Month]] = UNSET
    days: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        months: Union[None, Unset, list[str]]
        if isinstance(self.months, Unset):
            months = UNSET
        elif isinstance(self.months, list):
            months = []
            for months_type_0_item_data in self.months:
                months_type_0_item = months_type_0_item_data.value
                months.append(months_type_0_item)

        else:
            months = self.months

        days: Union[None, Unset, list[int]]
        if isinstance(self.days, Unset):
            days = UNSET
        elif isinstance(self.days, list):
            days = self.days

        else:
            days = self.days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if months is not UNSET:
            field_dict["months"] = months
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_months(data: object) -> Union[None, Unset, list[Month]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Month]], data)

        months = _parse_months(d.pop("months", UNSET))

        def _parse_days(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                days_type_0 = cast(list[int], data)

                return days_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        days = _parse_days(d.pop("days", UNSET))

        schedule_plan_monthly_days = cls(
            months=months,
            days=days,
        )

        return schedule_plan_monthly_days
