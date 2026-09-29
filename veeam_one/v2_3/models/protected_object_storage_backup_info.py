from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.object_storage_backup_job_type import ObjectStorageBackupJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo


T = TypeVar("T", bound="ProtectedObjectStorageBackupInfo")


@_attrs_define
class ProtectedObjectStorageBackupInfo:
    """
    Attributes:
        backup_uid (None | Unset | UUID): UID assigned to a backup chain.
        object_storage_uid_in_vbr (None | Unset | UUID): UID assigned to an object storage in Veeam Backup &
            Replication.
        job_uid (None | Unset | UUID): UID assigned to a backup job.
        job_name (None | str | Unset): Name of a backup job.
        job_type (ObjectStorageBackupJobType | Unset):
        backup_size (int | None | Unset): Size of a backup, in bytes.
        archive_size (int | None | Unset): Size of an archived backup, in bytes.
        restore_points (int | Unset): Number of restore points.
        last_protected_date (datetime.datetime | None | Unset): Time and date of the latest restore point creation.
        repository (None | ProtectedDataRepositoryInfo | Unset): Information on a target backup repository.
        archive_repository (None | ProtectedDataRepositoryInfo | Unset): Information on an archive repository.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset):
    """

    backup_uid: None | Unset | UUID = UNSET
    object_storage_uid_in_vbr: None | Unset | UUID = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET
    job_type: ObjectStorageBackupJobType | Unset = UNSET
    backup_size: int | None | Unset = UNSET
    archive_size: int | None | Unset = UNSET
    restore_points: int | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET
    repository: None | ProtectedDataRepositoryInfo | Unset = UNSET
    archive_repository: None | ProtectedDataRepositoryInfo | Unset = UNSET
    backup_server_id: int | None | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo  # noqa: PLC0415

        backup_uid: None | str | Unset
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        object_storage_uid_in_vbr: None | str | Unset
        if isinstance(self.object_storage_uid_in_vbr, Unset):
            object_storage_uid_in_vbr = UNSET
        elif isinstance(self.object_storage_uid_in_vbr, UUID):
            object_storage_uid_in_vbr = str(self.object_storage_uid_in_vbr)
        else:
            object_storage_uid_in_vbr = self.object_storage_uid_in_vbr

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

        job_type: str | Unset = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        backup_size: int | None | Unset
        if isinstance(self.backup_size, Unset):
            backup_size = UNSET
        else:
            backup_size = self.backup_size

        archive_size: int | None | Unset
        if isinstance(self.archive_size, Unset):
            archive_size = UNSET
        else:
            archive_size = self.archive_size

        restore_points = self.restore_points

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        repository: dict[str, Any] | None | Unset
        if isinstance(self.repository, Unset):
            repository = UNSET
        elif isinstance(self.repository, ProtectedDataRepositoryInfo):
            repository = self.repository.to_dict()
        else:
            repository = self.repository

        archive_repository: dict[str, Any] | None | Unset
        if isinstance(self.archive_repository, Unset):
            archive_repository = UNSET
        elif isinstance(self.archive_repository, ProtectedDataRepositoryInfo):
            archive_repository = self.archive_repository.to_dict()
        else:
            archive_repository = self.archive_repository

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if object_storage_uid_in_vbr is not UNSET:
            field_dict["objectStorageUidInVbr"] = object_storage_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if backup_size is not UNSET:
            field_dict["backupSize"] = backup_size
        if archive_size is not UNSET:
            field_dict["archiveSize"] = archive_size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if repository is not UNSET:
            field_dict["repository"] = repository
        if archive_repository is not UNSET:
            field_dict["archiveRepository"] = archive_repository
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name

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

        def _parse_object_storage_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_storage_uid_in_vbr_type_0 = UUID(data)

                return object_storage_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_storage_uid_in_vbr = _parse_object_storage_uid_in_vbr(d.pop("objectStorageUidInVbr", UNSET))

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

        _job_type = d.pop("jobType", UNSET)
        job_type: ObjectStorageBackupJobType | Unset
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = ObjectStorageBackupJobType(_job_type)

        def _parse_backup_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_size = _parse_backup_size(d.pop("backupSize", UNSET))

        def _parse_archive_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archive_size = _parse_archive_size(d.pop("archiveSize", UNSET))

        restore_points = d.pop("restorePoints", UNSET)

        def _parse_last_protected_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protected_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

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

        def _parse_archive_repository(data: object) -> None | ProtectedDataRepositoryInfo | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                archive_repository_type_1 = ProtectedDataRepositoryInfo.from_dict(data)

                return archive_repository_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectedDataRepositoryInfo | Unset, data)

        archive_repository = _parse_archive_repository(d.pop("archiveRepository", UNSET))

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

        protected_object_storage_backup_info = cls(
            backup_uid=backup_uid,
            object_storage_uid_in_vbr=object_storage_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            job_type=job_type,
            backup_size=backup_size,
            archive_size=archive_size,
            restore_points=restore_points,
            last_protected_date=last_protected_date,
            repository=repository,
            archive_repository=archive_repository,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_object_storage_backup_info
