from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.application_job_platform import ApplicationJobPlatform
from ..models.backup_job_status import BackupJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationTransactionLogBackupJobInfo")


@_attrs_define
class ApplicationTransactionLogBackupJobInfo:
    """
    Attributes:
        application_transaction_log_backup_job_uid (None | Unset | UUID): UID assigned to a transaction log backup job
            in Veeam Backup & Replication.
        parent_application_job_uid (None | Unset | UUID): UID assigned to an Enterprise Application backup job that
            includes the transaction log protection.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        status (BackupJobStatus | Unset):
        details (list[str] | None | Unset): Job details.
        name (None | str | Unset): Name of a transaction log backup job.
        description (None | str | Unset): Description of a transaction log backup job.
        platform (ApplicationJobPlatform | Unset):
        last_run (datetime.datetime | None | Unset): Time and date of the latest transaction log backup job session.
        last_transferred_data_bytes (int | None | Unset): Amount of data transferred during the latest job session, in
            bytes.
    """

    application_transaction_log_backup_job_uid: None | Unset | UUID = UNSET
    parent_application_job_uid: None | Unset | UUID = UNSET
    backup_server_id: int | Unset = UNSET
    status: BackupJobStatus | Unset = UNSET
    details: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    platform: ApplicationJobPlatform | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_transferred_data_bytes: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_transaction_log_backup_job_uid: None | str | Unset
        if isinstance(self.application_transaction_log_backup_job_uid, Unset):
            application_transaction_log_backup_job_uid = UNSET
        elif isinstance(self.application_transaction_log_backup_job_uid, UUID):
            application_transaction_log_backup_job_uid = str(self.application_transaction_log_backup_job_uid)
        else:
            application_transaction_log_backup_job_uid = self.application_transaction_log_backup_job_uid

        parent_application_job_uid: None | str | Unset
        if isinstance(self.parent_application_job_uid, Unset):
            parent_application_job_uid = UNSET
        elif isinstance(self.parent_application_job_uid, UUID):
            parent_application_job_uid = str(self.parent_application_job_uid)
        else:
            parent_application_job_uid = self.parent_application_job_uid

        backup_server_id = self.backup_server_id

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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_transferred_data_bytes: int | None | Unset
        if isinstance(self.last_transferred_data_bytes, Unset):
            last_transferred_data_bytes = UNSET
        else:
            last_transferred_data_bytes = self.last_transferred_data_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if application_transaction_log_backup_job_uid is not UNSET:
            field_dict["applicationTransactionLogBackupJobUid"] = application_transaction_log_backup_job_uid
        if parent_application_job_uid is not UNSET:
            field_dict["parentApplicationJobUid"] = parent_application_job_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if platform is not UNSET:
            field_dict["platform"] = platform
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_transferred_data_bytes is not UNSET:
            field_dict["lastTransferredDataBytes"] = last_transferred_data_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_application_transaction_log_backup_job_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_transaction_log_backup_job_uid_type_0 = UUID(data)

                return application_transaction_log_backup_job_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_transaction_log_backup_job_uid = _parse_application_transaction_log_backup_job_uid(
            d.pop("applicationTransactionLogBackupJobUid", UNSET)
        )

        def _parse_parent_application_job_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_application_job_uid_type_0 = UUID(data)

                return parent_application_job_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_application_job_uid = _parse_parent_application_job_uid(d.pop("parentApplicationJobUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: ApplicationJobPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ApplicationJobPlatform(_platform)

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

        def _parse_last_transferred_data_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_transferred_data_bytes = _parse_last_transferred_data_bytes(d.pop("lastTransferredDataBytes", UNSET))

        application_transaction_log_backup_job_info = cls(
            application_transaction_log_backup_job_uid=application_transaction_log_backup_job_uid,
            parent_application_job_uid=parent_application_job_uid,
            backup_server_id=backup_server_id,
            status=status,
            details=details,
            name=name,
            description=description,
            platform=platform,
            last_run=last_run,
            last_transferred_data_bytes=last_transferred_data_bytes,
        )

        return application_transaction_log_backup_job_info
