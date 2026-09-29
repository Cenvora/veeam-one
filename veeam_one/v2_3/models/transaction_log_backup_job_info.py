from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_job_status import BackupJobStatus
from ..models.transaction_log_backup_job_type import TransactionLogBackupJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_log_backup_parent_job import TransactionLogBackupParentJob


T = TypeVar("T", bound="TransactionLogBackupJobInfo")


@_attrs_define
class TransactionLogBackupJobInfo:
    """
    Attributes:
        transaction_job_uid (UUID | Unset): UID assigned to a job in Veeam Backup & Replication.
        name (None | str | Unset): Name of a job.
        type_ (TransactionLogBackupJobType | Unset):
        status (BackupJobStatus | Unset):
        details (list[str] | None | Unset): Job details.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        last_run (datetime.datetime | None | Unset): Date and time of the latest job session.
        last_transferred_data_bytes (int | None | Unset): Amount of data transferred during the latest job session, in
            bytes.
        parent_job (None | TransactionLogBackupParentJob | Unset): Information on a backup job that includes a
            transaction log protection.
    """

    transaction_job_uid: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: TransactionLogBackupJobType | Unset = UNSET
    status: BackupJobStatus | Unset = UNSET
    details: list[str] | None | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_transferred_data_bytes: int | None | Unset = UNSET
    parent_job: None | TransactionLogBackupParentJob | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.transaction_log_backup_parent_job import TransactionLogBackupParentJob  # noqa: PLC0415

        transaction_job_uid: str | Unset = UNSET
        if not isinstance(self.transaction_job_uid, Unset):
            transaction_job_uid = str(self.transaction_job_uid)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

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

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

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

        parent_job: dict[str, Any] | None | Unset
        if isinstance(self.parent_job, Unset):
            parent_job = UNSET
        elif isinstance(self.parent_job, TransactionLogBackupParentJob):
            parent_job = self.parent_job.to_dict()
        else:
            parent_job = self.parent_job

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if transaction_job_uid is not UNSET:
            field_dict["transactionJobUid"] = transaction_job_uid
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_transferred_data_bytes is not UNSET:
            field_dict["lastTransferredDataBytes"] = last_transferred_data_bytes
        if parent_job is not UNSET:
            field_dict["parentJob"] = parent_job

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_log_backup_parent_job import TransactionLogBackupParentJob  # noqa: PLC0415

        d = dict(src_dict)
        _transaction_job_uid = d.pop("transactionJobUid", UNSET)
        transaction_job_uid: UUID | Unset
        if isinstance(_transaction_job_uid, Unset):
            transaction_job_uid = UNSET
        else:
            transaction_job_uid = UUID(_transaction_job_uid)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: TransactionLogBackupJobType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TransactionLogBackupJobType(_type_)

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

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

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

        def _parse_parent_job(data: object) -> None | TransactionLogBackupParentJob | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_job_type_1 = TransactionLogBackupParentJob.from_dict(data)

                return parent_job_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransactionLogBackupParentJob | Unset, data)

        parent_job = _parse_parent_job(d.pop("parentJob", UNSET))

        transaction_log_backup_job_info = cls(
            transaction_job_uid=transaction_job_uid,
            name=name,
            type_=type_,
            status=status,
            details=details,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            last_run=last_run,
            last_transferred_data_bytes=last_transferred_data_bytes,
            parent_job=parent_job,
        )

        return transaction_log_backup_job_info
