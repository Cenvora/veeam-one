import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.schedule_type import ScheduleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_plan_daily import SchedulePlanDaily
    from ..models.schedule_plan_monthly_days import SchedulePlanMonthlyDays
    from ..models.schedule_plan_monthly_week_days import SchedulePlanMonthlyWeekDays
    from ..models.schedule_plan_periodical import SchedulePlanPeriodical


T = TypeVar("T", bound="SchedulePlan")


@_attrs_define
class SchedulePlan:
    """
    Attributes:
        start_time (datetime.datetime): Time and date of the data collection session start. Example:
            '2021-01-12T11:44:42.09Z'.
        schedule_type (ScheduleType): Type of a data collection schedule.
        time_zone_id (Union[None, Unset, str]): ID assigned to a time zone.
        disabled (Union[Unset, bool]): Indicates whether a data collection schedule is enabled.
        periodically (Union['SchedulePlanPeriodical', None, Unset]): Settings for periodic scheduling.
        daily (Union['SchedulePlanDaily', None, Unset]): Settings for daily scheduling.
        monthly_days (Union['SchedulePlanMonthlyDays', None, Unset]): Scheduling settings for monthly data collection on
            specific date.
        monthly_week_days (Union['SchedulePlanMonthlyWeekDays', None, Unset]): Scheduling settings for monthly data
            collection on specific week days.
    """

    start_time: datetime.datetime
    schedule_type: ScheduleType
    time_zone_id: Union[None, Unset, str] = UNSET
    disabled: Union[Unset, bool] = UNSET
    periodically: Union["SchedulePlanPeriodical", None, Unset] = UNSET
    daily: Union["SchedulePlanDaily", None, Unset] = UNSET
    monthly_days: Union["SchedulePlanMonthlyDays", None, Unset] = UNSET
    monthly_week_days: Union["SchedulePlanMonthlyWeekDays", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.schedule_plan_daily import SchedulePlanDaily
        from ..models.schedule_plan_monthly_days import SchedulePlanMonthlyDays
        from ..models.schedule_plan_monthly_week_days import SchedulePlanMonthlyWeekDays
        from ..models.schedule_plan_periodical import SchedulePlanPeriodical

        start_time = self.start_time.isoformat()

        schedule_type = self.schedule_type.value

        time_zone_id: Union[None, Unset, str]
        if isinstance(self.time_zone_id, Unset):
            time_zone_id = UNSET
        else:
            time_zone_id = self.time_zone_id

        disabled = self.disabled

        periodically: Union[None, Unset, dict[str, Any]]
        if isinstance(self.periodically, Unset):
            periodically = UNSET
        elif isinstance(self.periodically, SchedulePlanPeriodical):
            periodically = self.periodically.to_dict()
        else:
            periodically = self.periodically

        daily: Union[None, Unset, dict[str, Any]]
        if isinstance(self.daily, Unset):
            daily = UNSET
        elif isinstance(self.daily, SchedulePlanDaily):
            daily = self.daily.to_dict()
        else:
            daily = self.daily

        monthly_days: Union[None, Unset, dict[str, Any]]
        if isinstance(self.monthly_days, Unset):
            monthly_days = UNSET
        elif isinstance(self.monthly_days, SchedulePlanMonthlyDays):
            monthly_days = self.monthly_days.to_dict()
        else:
            monthly_days = self.monthly_days

        monthly_week_days: Union[None, Unset, dict[str, Any]]
        if isinstance(self.monthly_week_days, Unset):
            monthly_week_days = UNSET
        elif isinstance(self.monthly_week_days, SchedulePlanMonthlyWeekDays):
            monthly_week_days = self.monthly_week_days.to_dict()
        else:
            monthly_week_days = self.monthly_week_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "startTime": start_time,
                "scheduleType": schedule_type,
            }
        )
        if time_zone_id is not UNSET:
            field_dict["timeZoneId"] = time_zone_id
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if periodically is not UNSET:
            field_dict["periodically"] = periodically
        if daily is not UNSET:
            field_dict["daily"] = daily
        if monthly_days is not UNSET:
            field_dict["monthlyDays"] = monthly_days
        if monthly_week_days is not UNSET:
            field_dict["monthlyWeekDays"] = monthly_week_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_plan_daily import SchedulePlanDaily
        from ..models.schedule_plan_monthly_days import SchedulePlanMonthlyDays
        from ..models.schedule_plan_monthly_week_days import SchedulePlanMonthlyWeekDays
        from ..models.schedule_plan_periodical import SchedulePlanPeriodical

        d = dict(src_dict)
        start_time = isoparse(d.pop("startTime"))

        schedule_type = ScheduleType(d.pop("scheduleType"))

        def _parse_time_zone_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone_id = _parse_time_zone_id(d.pop("timeZoneId", UNSET))

        disabled = d.pop("disabled", UNSET)

        def _parse_periodically(data: object) -> Union["SchedulePlanPeriodical", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                periodically_type_1 = SchedulePlanPeriodical.from_dict(data)

                return periodically_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SchedulePlanPeriodical", None, Unset], data)

        periodically = _parse_periodically(d.pop("periodically", UNSET))

        def _parse_daily(data: object) -> Union["SchedulePlanDaily", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                daily_type_1 = SchedulePlanDaily.from_dict(data)

                return daily_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SchedulePlanDaily", None, Unset], data)

        daily = _parse_daily(d.pop("daily", UNSET))

        def _parse_monthly_days(data: object) -> Union["SchedulePlanMonthlyDays", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monthly_days_type_1 = SchedulePlanMonthlyDays.from_dict(data)

                return monthly_days_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SchedulePlanMonthlyDays", None, Unset], data)

        monthly_days = _parse_monthly_days(d.pop("monthlyDays", UNSET))

        def _parse_monthly_week_days(data: object) -> Union["SchedulePlanMonthlyWeekDays", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                monthly_week_days_type_1 = SchedulePlanMonthlyWeekDays.from_dict(data)

                return monthly_week_days_type_1
            except:  # noqa: E722
                pass
            return cast(Union["SchedulePlanMonthlyWeekDays", None, Unset], data)

        monthly_week_days = _parse_monthly_week_days(d.pop("monthlyWeekDays", UNSET))

        schedule_plan = cls(
            start_time=start_time,
            schedule_type=schedule_type,
            time_zone_id=time_zone_id,
            disabled=disabled,
            periodically=periodically,
            daily=daily,
            monthly_days=monthly_days,
            monthly_week_days=monthly_week_days,
        )

        return schedule_plan
