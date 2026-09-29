from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vm_backup_type import VmBackupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo


T = TypeVar("T", bound="ProtectedVmBackupInfo")


@_attrs_define
class ProtectedVmBackupInfo:
    """
    Attributes:
        backup_uid (UUID | Unset): UID assigned to a backup chain.
        vm_uid_in_vbr (None | Unset | UUID): UID assigned to a VM.
        job_uid (None | Unset | UUID): UID assigned to a backup job.
        job_name (None | str | Unset): Name of a backup job.
        type_ (VmBackupType | Unset):
        total_restore_point_size_bytes (int | None | Unset): Total size of all restore points, in bytes.
        latest_restore_point_size_bytes (int | None | Unset): Size of the latest restore point, in bytes.
        restore_points (int | Unset): Number of restore points.
        last_protected_date (datetime.datetime | None | Unset): Time and date of the latest restore point creation.
        repository (None | ProtectedDataRepositoryInfo | Unset): Information on a target backup repository.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        total_unique_restore_points_size_bytes (int | None | Unset): Total size of all unique restore points, in bytes.
        unique_restore_points (int | None | Unset): Number of unique restore points.
    """

    backup_uid: UUID | Unset = UNSET
    vm_uid_in_vbr: None | Unset | UUID = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET
    type_: VmBackupType | Unset = UNSET
    total_restore_point_size_bytes: int | None | Unset = UNSET
    latest_restore_point_size_bytes: int | None | Unset = UNSET
    restore_points: int | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET
    repository: None | ProtectedDataRepositoryInfo | Unset = UNSET
    backup_server_id: int | None | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    total_unique_restore_points_size_bytes: int | None | Unset = UNSET
    unique_restore_points: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo  # noqa: PLC0415

        backup_uid: str | Unset = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        vm_uid_in_vbr: None | str | Unset
        if isinstance(self.vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = UNSET
        elif isinstance(self.vm_uid_in_vbr, UUID):
            vm_uid_in_vbr = str(self.vm_uid_in_vbr)
        else:
            vm_uid_in_vbr = self.vm_uid_in_vbr

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

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        total_restore_point_size_bytes: int | None | Unset
        if isinstance(self.total_restore_point_size_bytes, Unset):
            total_restore_point_size_bytes = UNSET
        else:
            total_restore_point_size_bytes = self.total_restore_point_size_bytes

        latest_restore_point_size_bytes: int | None | Unset
        if isinstance(self.latest_restore_point_size_bytes, Unset):
            latest_restore_point_size_bytes = UNSET
        else:
            latest_restore_point_size_bytes = self.latest_restore_point_size_bytes

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

        total_unique_restore_points_size_bytes: int | None | Unset
        if isinstance(self.total_unique_restore_points_size_bytes, Unset):
            total_unique_restore_points_size_bytes = UNSET
        else:
            total_unique_restore_points_size_bytes = self.total_unique_restore_points_size_bytes

        unique_restore_points: int | None | Unset
        if isinstance(self.unique_restore_points, Unset):
            unique_restore_points = UNSET
        else:
            unique_restore_points = self.unique_restore_points

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if vm_uid_in_vbr is not UNSET:
            field_dict["vmUidInVbr"] = vm_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if total_restore_point_size_bytes is not UNSET:
            field_dict["totalRestorePointSizeBytes"] = total_restore_point_size_bytes
        if latest_restore_point_size_bytes is not UNSET:
            field_dict["latestRestorePointSizeBytes"] = latest_restore_point_size_bytes
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if repository is not UNSET:
            field_dict["repository"] = repository
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if total_unique_restore_points_size_bytes is not UNSET:
            field_dict["totalUniqueRestorePointsSizeBytes"] = total_unique_restore_points_size_bytes
        if unique_restore_points is not UNSET:
            field_dict["uniqueRestorePoints"] = unique_restore_points

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo  # noqa: PLC0415

        d = dict(src_dict)
        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: UUID | Unset
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        def _parse_vm_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vm_uid_in_vbr_type_0 = UUID(data)

                return vm_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        vm_uid_in_vbr = _parse_vm_uid_in_vbr(d.pop("vmUidInVbr", UNSET))

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

        _type_ = d.pop("type", UNSET)
        type_: VmBackupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VmBackupType(_type_)

        def _parse_total_restore_point_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_restore_point_size_bytes = _parse_total_restore_point_size_bytes(
            d.pop("totalRestorePointSizeBytes", UNSET)
        )

        def _parse_latest_restore_point_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_restore_point_size_bytes = _parse_latest_restore_point_size_bytes(
            d.pop("latestRestorePointSizeBytes", UNSET)
        )

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

        def _parse_total_unique_restore_points_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_unique_restore_points_size_bytes = _parse_total_unique_restore_points_size_bytes(
            d.pop("totalUniqueRestorePointsSizeBytes", UNSET)
        )

        def _parse_unique_restore_points(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_restore_points = _parse_unique_restore_points(d.pop("uniqueRestorePoints", UNSET))

        protected_vm_backup_info = cls(
            backup_uid=backup_uid,
            vm_uid_in_vbr=vm_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            type_=type_,
            total_restore_point_size_bytes=total_restore_point_size_bytes,
            latest_restore_point_size_bytes=latest_restore_point_size_bytes,
            restore_points=restore_points,
            last_protected_date=last_protected_date,
            repository=repository,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            total_unique_restore_points_size_bytes=total_unique_restore_points_size_bytes,
            unique_restore_points=unique_restore_points,
        )

        return protected_vm_backup_info
