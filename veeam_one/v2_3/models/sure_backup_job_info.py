from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_job_status import BackupJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SureBackupJobInfo")


@_attrs_define
class SureBackupJobInfo:
    """
    Attributes:
        sure_backup_job_uid (UUID | Unset): UID assigned to a job.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication.
        name (None | str | Unset): Name of a job.
        status (BackupJobStatus | Unset):
        details (list[str] | None | Unset): Job details.
        created_by (None | str | Unset): Name of a user that created a job.
        last_run (datetime.datetime | None | Unset): Date and time of the latest job session.
        last_run_duration_sec (int | None | Unset): Duration of the latest job session, in seconds.
        avg_duration_sec (int | None | Unset): Average duration of a job session, in seconds.
    """

    sure_backup_job_uid: UUID | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    status: BackupJobStatus | Unset = UNSET
    details: list[str] | None | Unset = UNSET
    created_by: None | str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_run_duration_sec: int | None | Unset = UNSET
    avg_duration_sec: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        sure_backup_job_uid: str | Unset = UNSET
        if not isinstance(self.sure_backup_job_uid, Unset):
            sure_backup_job_uid = str(self.sure_backup_job_uid)

        backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: list[str] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        else:
            details = self.details

        created_by: None | str | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        else:
            created_by = self.created_by

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_run_duration_sec: int | None | Unset
        if isinstance(self.last_run_duration_sec, Unset):
            last_run_duration_sec = UNSET
        else:
            last_run_duration_sec = self.last_run_duration_sec

        avg_duration_sec: int | None | Unset
        if isinstance(self.avg_duration_sec, Unset):
            avg_duration_sec = UNSET
        else:
            avg_duration_sec = self.avg_duration_sec

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sure_backup_job_uid is not UNSET:
            field_dict["sureBackupJobUid"] = sure_backup_job_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_run_duration_sec is not UNSET:
            field_dict["lastRunDurationSec"] = last_run_duration_sec
        if avg_duration_sec is not UNSET:
            field_dict["avgDurationSec"] = avg_duration_sec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sure_backup_job_uid = d.pop("sureBackupJobUid", UNSET)
        sure_backup_job_uid: UUID | Unset
        if isinstance(_sure_backup_job_uid, Unset):
            sure_backup_job_uid = UNSET
        else:
            sure_backup_job_uid = UUID(_sure_backup_job_uid)

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _status = d.pop("status", UNSET)
        status: BackupJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupJobStatus(_status)

        def _parse_details(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_created_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_by = _parse_created_by(d.pop("createdBy", UNSET))

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        def _parse_last_run_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_run_duration_sec = _parse_last_run_duration_sec(d.pop("lastRunDurationSec", UNSET))

        def _parse_avg_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        avg_duration_sec = _parse_avg_duration_sec(d.pop("avgDurationSec", UNSET))

        sure_backup_job_info = cls(
            sure_backup_job_uid=sure_backup_job_uid,
            backup_server_id=backup_server_id,
            name=name,
            status=status,
            details=details,
            created_by=created_by,
            last_run=last_run,
            last_run_duration_sec=last_run_duration_sec,
            avg_duration_sec=avg_duration_sec,
        )

        return sure_backup_job_info
