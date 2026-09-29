from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedComputerBackupRestorePointInfo")


@_attrs_define
class ProtectedComputerBackupRestorePointInfo:
    """
    Attributes:
        restore_point_uid (UUID | Unset): UID assigned to a restore point.
        computer_uid_in_vbr (None | Unset | UUID): UID assigned to a protected computer.
        backup_uid (None | Unset | UUID): UID assigned to a backup chain.
        job_uid (None | Unset | UUID): UID assigned to a backup job.
        job_name (None | str | Unset): Name of a backup job.
        repository_uid (None | Unset | UUID): UID assigned to a repository on which a restore point resides.
        size_bytes (int | None | Unset): Size of a restore point, in bytes.
        source_size_bytes (int | None | Unset): Total size of protected computer disks included in a restore point, in
            bytes.
        original_size_bytes (int | None | Unset): Initial size of protected data, in bytes.
        backup_creation_date (datetime.datetime | None | Unset): Time and date when backup was created.
        is_incremental (bool | None | Unset): Indicates whether a restore point is an increment.
        immutable_till (datetime.datetime | None | Unset): Date and time till which a restore point is immutable.
        file_creation_time (datetime.datetime | None | Unset): Date and time when a restore point was created.
    """

    restore_point_uid: UUID | Unset = UNSET
    computer_uid_in_vbr: None | Unset | UUID = UNSET
    backup_uid: None | Unset | UUID = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET
    repository_uid: None | Unset | UUID = UNSET
    size_bytes: int | None | Unset = UNSET
    source_size_bytes: int | None | Unset = UNSET
    original_size_bytes: int | None | Unset = UNSET
    backup_creation_date: datetime.datetime | None | Unset = UNSET
    is_incremental: bool | None | Unset = UNSET
    immutable_till: datetime.datetime | None | Unset = UNSET
    file_creation_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_uid: str | Unset = UNSET
        if not isinstance(self.restore_point_uid, Unset):
            restore_point_uid = str(self.restore_point_uid)

        computer_uid_in_vbr: None | str | Unset
        if isinstance(self.computer_uid_in_vbr, Unset):
            computer_uid_in_vbr = UNSET
        elif isinstance(self.computer_uid_in_vbr, UUID):
            computer_uid_in_vbr = str(self.computer_uid_in_vbr)
        else:
            computer_uid_in_vbr = self.computer_uid_in_vbr

        backup_uid: None | str | Unset
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        job_uid: None | str | Unset
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        job_name: None | str | Unset
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        repository_uid: None | str | Unset
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        source_size_bytes: int | None | Unset
        if isinstance(self.source_size_bytes, Unset):
            source_size_bytes = UNSET
        else:
            source_size_bytes = self.source_size_bytes

        original_size_bytes: int | None | Unset
        if isinstance(self.original_size_bytes, Unset):
            original_size_bytes = UNSET
        else:
            original_size_bytes = self.original_size_bytes

        backup_creation_date: None | str | Unset
        if isinstance(self.backup_creation_date, Unset):
            backup_creation_date = UNSET
        elif isinstance(self.backup_creation_date, datetime.datetime):
            backup_creation_date = self.backup_creation_date.isoformat()
        else:
            backup_creation_date = self.backup_creation_date

        is_incremental: bool | None | Unset
        if isinstance(self.is_incremental, Unset):
            is_incremental = UNSET
        else:
            is_incremental = self.is_incremental

        immutable_till: None | str | Unset
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

        file_creation_time: None | str | Unset
        if isinstance(self.file_creation_time, Unset):
            file_creation_time = UNSET
        elif isinstance(self.file_creation_time, datetime.datetime):
            file_creation_time = self.file_creation_time.isoformat()
        else:
            file_creation_time = self.file_creation_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_uid is not UNSET:
            field_dict["restorePointUid"] = restore_point_uid
        if computer_uid_in_vbr is not UNSET:
            field_dict["computerUidInVbr"] = computer_uid_in_vbr
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if source_size_bytes is not UNSET:
            field_dict["sourceSizeBytes"] = source_size_bytes
        if original_size_bytes is not UNSET:
            field_dict["originalSizeBytes"] = original_size_bytes
        if backup_creation_date is not UNSET:
            field_dict["backupCreationDate"] = backup_creation_date
        if is_incremental is not UNSET:
            field_dict["isIncremental"] = is_incremental
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till
        if file_creation_time is not UNSET:
            field_dict["fileCreationTime"] = file_creation_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _restore_point_uid = d.pop("restorePointUid", UNSET)
        restore_point_uid: UUID | Unset
        if isinstance(_restore_point_uid, Unset):
            restore_point_uid = UNSET
        else:
            restore_point_uid = UUID(_restore_point_uid)

        def _parse_computer_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                computer_uid_in_vbr_type_0 = UUID(data)

                return computer_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        computer_uid_in_vbr = _parse_computer_uid_in_vbr(d.pop("computerUidInVbr", UNSET))

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

        def _parse_job_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_job_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        def _parse_repository_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        def _parse_source_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_size_bytes = _parse_source_size_bytes(d.pop("sourceSizeBytes", UNSET))

        def _parse_original_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        original_size_bytes = _parse_original_size_bytes(d.pop("originalSizeBytes", UNSET))

        def _parse_backup_creation_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_creation_date_type_0 = datetime.datetime.fromisoformat(data)

                return backup_creation_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        backup_creation_date = _parse_backup_creation_date(d.pop("backupCreationDate", UNSET))

        def _parse_is_incremental(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_incremental = _parse_is_incremental(d.pop("isIncremental", UNSET))

        def _parse_immutable_till(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutable_till_type_0 = datetime.datetime.fromisoformat(data)

                return immutable_till_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        immutable_till = _parse_immutable_till(d.pop("immutableTill", UNSET))

        def _parse_file_creation_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_creation_time_type_0 = datetime.datetime.fromisoformat(data)

                return file_creation_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        file_creation_time = _parse_file_creation_time(d.pop("fileCreationTime", UNSET))

        protected_computer_backup_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            computer_uid_in_vbr=computer_uid_in_vbr,
            backup_uid=backup_uid,
            job_uid=job_uid,
            job_name=job_name,
            repository_uid=repository_uid,
            size_bytes=size_bytes,
            source_size_bytes=source_size_bytes,
            original_size_bytes=original_size_bytes,
            backup_creation_date=backup_creation_date,
            is_incremental=is_incremental,
            immutable_till=immutable_till,
            file_creation_time=file_creation_time,
        )

        return protected_computer_backup_restore_point_info
