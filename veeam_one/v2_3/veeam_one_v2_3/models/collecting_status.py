import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.schedule_session_status import ScheduleSessionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CollectingStatus")


@_attrs_define
class CollectingStatus:
    """
    Attributes:
        progress (Union[None, Unset, int]): Data collection session progress, in percent. Example: 100.
        status (Union[Unset, ScheduleSessionStatus]): Task session status.
        manually_start (Union[Unset, bool]): Indicates whether a data collection session must be initiated manually.
        next_run (Union[None, Unset, datetime.datetime]): Date and time of the next data collection session start.
            Example: '2021-02-10T19:00:00Z'.
        tasks_success (Union[Unset, int]): Number of successful data collection sessions. Example: 10.
        tasks_warning (Union[Unset, int]): Number of data collection sessions that ended with warnings. Example: 2.
        tasks_failed (Union[Unset, int]): Number of failed data collection sessions. Example: 1.
        tasks_stopped (Union[Unset, int]): Number of canceled data collection sessions. Example: 2.
    """

    progress: Union[None, Unset, int] = UNSET
    status: Union[Unset, ScheduleSessionStatus] = UNSET
    manually_start: Union[Unset, bool] = UNSET
    next_run: Union[None, Unset, datetime.datetime] = UNSET
    tasks_success: Union[Unset, int] = UNSET
    tasks_warning: Union[Unset, int] = UNSET
    tasks_failed: Union[Unset, int] = UNSET
    tasks_stopped: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        progress: Union[None, Unset, int]
        if isinstance(self.progress, Unset):
            progress = UNSET
        else:
            progress = self.progress

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        manually_start = self.manually_start

        next_run: Union[None, Unset, str]
        if isinstance(self.next_run, Unset):
            next_run = UNSET
        elif isinstance(self.next_run, datetime.datetime):
            next_run = self.next_run.isoformat()
        else:
            next_run = self.next_run

        tasks_success = self.tasks_success

        tasks_warning = self.tasks_warning

        tasks_failed = self.tasks_failed

        tasks_stopped = self.tasks_stopped

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status is not UNSET:
            field_dict["status"] = status
        if manually_start is not UNSET:
            field_dict["manuallyStart"] = manually_start
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if tasks_success is not UNSET:
            field_dict["tasksSuccess"] = tasks_success
        if tasks_warning is not UNSET:
            field_dict["tasksWarning"] = tasks_warning
        if tasks_failed is not UNSET:
            field_dict["tasksFailed"] = tasks_failed
        if tasks_stopped is not UNSET:
            field_dict["tasksStopped"] = tasks_stopped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_progress(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        progress = _parse_progress(d.pop("progress", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ScheduleSessionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ScheduleSessionStatus(_status)

        manually_start = d.pop("manuallyStart", UNSET)

        def _parse_next_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_run_type_0 = isoparse(data)

                return next_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_run = _parse_next_run(d.pop("nextRun", UNSET))

        tasks_success = d.pop("tasksSuccess", UNSET)

        tasks_warning = d.pop("tasksWarning", UNSET)

        tasks_failed = d.pop("tasksFailed", UNSET)

        tasks_stopped = d.pop("tasksStopped", UNSET)

        collecting_status = cls(
            progress=progress,
            status=status,
            manually_start=manually_start,
            next_run=next_run,
            tasks_success=tasks_success,
            tasks_warning=tasks_warning,
            tasks_failed=tasks_failed,
            tasks_stopped=tasks_stopped,
        )

        return collecting_status
