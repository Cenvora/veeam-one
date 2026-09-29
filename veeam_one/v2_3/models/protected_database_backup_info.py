from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.protected_application_platform import ProtectedApplicationPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo


T = TypeVar("T", bound="ProtectedDatabaseBackupInfo")


@_attrs_define
class ProtectedDatabaseBackupInfo:
    """
    Attributes:
        backup_uid (None | Unset | UUID): UID assigned to an application database backup in Veeam Backup & Replication.
        database_uid_in_vbr (None | Unset | UUID): UID assigned to an application database in Veeam Backup &
            Replication.
        database_name (None | str | Unset): Name of an application database.
        application_uid_in_vbr (None | Unset | UUID): UID assigned to an application in Veeam Backup & Replication.
        application_name (None | str | Unset): Name of an application.
        application_platform (ProtectedApplicationPlatform | Unset):
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        job_uid (UUID | Unset): UID assigned to a backup job in Veeam Backup & Replication.
        job_name (None | str | Unset): Name of a backup job.
        session_tasks (int | None | Unset): Total number of backup sessions.
        success_session_tasks (int | None | Unset): Number of successful backup sessions.
        failed_session_tasks (int | None | Unset): Number of failed backup sessions.
        warning_sessiontasks (int | None | Unset): Number of backup sessions that completed with warnings.
        last_database_protection_date (datetime.datetime | None | Unset): Date and time when the latest successful job
            session protecting application database started.
        last_log_protection_date (datetime.datetime | None | Unset): Date and time when the latest successful job
            session protecting application database logs started.
        repository (None | ProtectedDataRepositoryInfo | Unset): Information on backup repository.
        backup_size (int | Unset): Size of a backup chain, in bytes.
    """

    backup_uid: None | Unset | UUID = UNSET
    database_uid_in_vbr: None | Unset | UUID = UNSET
    database_name: None | str | Unset = UNSET
    application_uid_in_vbr: None | Unset | UUID = UNSET
    application_name: None | str | Unset = UNSET
    application_platform: ProtectedApplicationPlatform | Unset = UNSET
    backup_server_id: int | None | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    job_uid: UUID | Unset = UNSET
    job_name: None | str | Unset = UNSET
    session_tasks: int | None | Unset = UNSET
    success_session_tasks: int | None | Unset = UNSET
    failed_session_tasks: int | None | Unset = UNSET
    warning_sessiontasks: int | None | Unset = UNSET
    last_database_protection_date: datetime.datetime | None | Unset = UNSET
    last_log_protection_date: datetime.datetime | None | Unset = UNSET
    repository: None | ProtectedDataRepositoryInfo | Unset = UNSET
    backup_size: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo  # noqa: PLC0415

        backup_uid: None | str | Unset
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        database_uid_in_vbr: None | str | Unset
        if isinstance(self.database_uid_in_vbr, Unset):
            database_uid_in_vbr = UNSET
        elif isinstance(self.database_uid_in_vbr, UUID):
            database_uid_in_vbr = str(self.database_uid_in_vbr)
        else:
            database_uid_in_vbr = self.database_uid_in_vbr

        database_name: None | str | Unset
        if isinstance(self.database_name, Unset):
            database_name = UNSET
        else:
            database_name = self.database_name

        application_uid_in_vbr: None | str | Unset
        if isinstance(self.application_uid_in_vbr, Unset):
            application_uid_in_vbr = UNSET
        elif isinstance(self.application_uid_in_vbr, UUID):
            application_uid_in_vbr = str(self.application_uid_in_vbr)
        else:
            application_uid_in_vbr = self.application_uid_in_vbr

        application_name: None | str | Unset
        if isinstance(self.application_name, Unset):
            application_name = UNSET
        else:
            application_name = self.application_name

        application_platform: str | Unset = UNSET
        if not isinstance(self.application_platform, Unset):
            application_platform = self.application_platform.value

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        job_name: None | str | Unset
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        session_tasks: int | None | Unset
        if isinstance(self.session_tasks, Unset):
            session_tasks = UNSET
        else:
            session_tasks = self.session_tasks

        success_session_tasks: int | None | Unset
        if isinstance(self.success_session_tasks, Unset):
            success_session_tasks = UNSET
        else:
            success_session_tasks = self.success_session_tasks

        failed_session_tasks: int | None | Unset
        if isinstance(self.failed_session_tasks, Unset):
            failed_session_tasks = UNSET
        else:
            failed_session_tasks = self.failed_session_tasks

        warning_sessiontasks: int | None | Unset
        if isinstance(self.warning_sessiontasks, Unset):
            warning_sessiontasks = UNSET
        else:
            warning_sessiontasks = self.warning_sessiontasks

        last_database_protection_date: None | str | Unset
        if isinstance(self.last_database_protection_date, Unset):
            last_database_protection_date = UNSET
        elif isinstance(self.last_database_protection_date, datetime.datetime):
            last_database_protection_date = self.last_database_protection_date.isoformat()
        else:
            last_database_protection_date = self.last_database_protection_date

        last_log_protection_date: None | str | Unset
        if isinstance(self.last_log_protection_date, Unset):
            last_log_protection_date = UNSET
        elif isinstance(self.last_log_protection_date, datetime.datetime):
            last_log_protection_date = self.last_log_protection_date.isoformat()
        else:
            last_log_protection_date = self.last_log_protection_date

        repository: dict[str, Any] | None | Unset
        if isinstance(self.repository, Unset):
            repository = UNSET
        elif isinstance(self.repository, ProtectedDataRepositoryInfo):
            repository = self.repository.to_dict()
        else:
            repository = self.repository

        backup_size = self.backup_size

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if database_uid_in_vbr is not UNSET:
            field_dict["databaseUidInVbr"] = database_uid_in_vbr
        if database_name is not UNSET:
            field_dict["databaseName"] = database_name
        if application_uid_in_vbr is not UNSET:
            field_dict["applicationUidInVbr"] = application_uid_in_vbr
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if application_platform is not UNSET:
            field_dict["applicationPlatform"] = application_platform
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if session_tasks is not UNSET:
            field_dict["sessionTasks"] = session_tasks
        if success_session_tasks is not UNSET:
            field_dict["successSessionTasks"] = success_session_tasks
        if failed_session_tasks is not UNSET:
            field_dict["failedSessionTasks"] = failed_session_tasks
        if warning_sessiontasks is not UNSET:
            field_dict["warningSessiontasks"] = warning_sessiontasks
        if last_database_protection_date is not UNSET:
            field_dict["lastDatabaseProtectionDate"] = last_database_protection_date
        if last_log_protection_date is not UNSET:
            field_dict["lastLogProtectionDate"] = last_log_protection_date
        if repository is not UNSET:
            field_dict["repository"] = repository
        if backup_size is not UNSET:
            field_dict["backupSize"] = backup_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_backup_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_uid_type_0 = UUID(data)

                return backup_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_uid = _parse_backup_uid(d.pop("backupUid", UNSET))

        def _parse_database_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                database_uid_in_vbr_type_0 = UUID(data)

                return database_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        database_uid_in_vbr = _parse_database_uid_in_vbr(d.pop("databaseUidInVbr", UNSET))

        def _parse_database_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        database_name = _parse_database_name(d.pop("databaseName", UNSET))

        def _parse_application_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_uid_in_vbr_type_0 = UUID(data)

                return application_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_uid_in_vbr = _parse_application_uid_in_vbr(d.pop("applicationUidInVbr", UNSET))

        def _parse_application_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        application_name = _parse_application_name(d.pop("applicationName", UNSET))

        _application_platform = d.pop("applicationPlatform", UNSET)
        application_platform: ProtectedApplicationPlatform | Unset
        if isinstance(_application_platform, Unset):
            application_platform = UNSET
        else:
            application_platform = ProtectedApplicationPlatform(_application_platform)

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        def _parse_job_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        def _parse_session_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        session_tasks = _parse_session_tasks(d.pop("sessionTasks", UNSET))

        def _parse_success_session_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        success_session_tasks = _parse_success_session_tasks(d.pop("successSessionTasks", UNSET))

        def _parse_failed_session_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        failed_session_tasks = _parse_failed_session_tasks(d.pop("failedSessionTasks", UNSET))

        def _parse_warning_sessiontasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        warning_sessiontasks = _parse_warning_sessiontasks(d.pop("warningSessiontasks", UNSET))

        def _parse_last_database_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_database_protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_database_protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_database_protection_date = _parse_last_database_protection_date(d.pop("lastDatabaseProtectionDate", UNSET))

        def _parse_last_log_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_log_protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_log_protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_log_protection_date = _parse_last_log_protection_date(d.pop("lastLogProtectionDate", UNSET))

        def _parse_repository(data: object) -> None | ProtectedDataRepositoryInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repository_type_1 = ProtectedDataRepositoryInfo.from_dict(data)

                return repository_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectedDataRepositoryInfo | Unset, data)

        repository = _parse_repository(d.pop("repository", UNSET))

        backup_size = d.pop("backupSize", UNSET)

        protected_database_backup_info = cls(
            backup_uid=backup_uid,
            database_uid_in_vbr=database_uid_in_vbr,
            database_name=database_name,
            application_uid_in_vbr=application_uid_in_vbr,
            application_name=application_name,
            application_platform=application_platform,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            job_uid=job_uid,
            job_name=job_name,
            session_tasks=session_tasks,
            success_session_tasks=success_session_tasks,
            failed_session_tasks=failed_session_tasks,
            warning_sessiontasks=warning_sessiontasks,
            last_database_protection_date=last_database_protection_date,
            last_log_protection_date=last_log_protection_date,
            repository=repository,
            backup_size=backup_size,
        )

        return protected_database_backup_info
