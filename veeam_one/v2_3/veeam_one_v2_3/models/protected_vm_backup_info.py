import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vm_backup_type import VmBackupType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo


T = TypeVar("T", bound="ProtectedVmBackupInfo")


@_attrs_define
class ProtectedVmBackupInfo:
    """
    Attributes:
        backup_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        vm_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a VM.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job.
        job_name (Union[None, Unset, str]): Name of a backup job.
        type_ (Union[Unset, VmBackupType]):
        total_restore_point_size_bytes (Union[None, Unset, int]): Total size of all restore points, in bytes.
        latest_restore_point_size_bytes (Union[None, Unset, int]): Size of the latest restore point, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        last_protected_date (Union[None, Unset, datetime.datetime]): Time and date of the latest restore point creation.
        repository (Union['ProtectedDataRepositoryInfo', None, Unset]): Information on a target backup repository.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
        total_unique_restore_points_size_bytes (Union[None, Unset, int]): Total size of all unique restore points, in
            bytes.
        unique_restore_points (Union[None, Unset, int]): Number of unique restore points.
    """

    backup_uid: Union[Unset, UUID] = UNSET
    vm_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, VmBackupType] = UNSET
    total_restore_point_size_bytes: Union[None, Unset, int] = UNSET
    latest_restore_point_size_bytes: Union[None, Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET
    repository: Union["ProtectedDataRepositoryInfo", None, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    total_unique_restore_points_size_bytes: Union[None, Unset, int] = UNSET
    unique_restore_points: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo

        backup_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        vm_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = UNSET
        elif isinstance(self.vm_uid_in_vbr, UUID):
            vm_uid_in_vbr = str(self.vm_uid_in_vbr)
        else:
            vm_uid_in_vbr = self.vm_uid_in_vbr

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        job_name: Union[None, Unset, str]
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        total_restore_point_size_bytes: Union[None, Unset, int]
        if isinstance(self.total_restore_point_size_bytes, Unset):
            total_restore_point_size_bytes = UNSET
        else:
            total_restore_point_size_bytes = self.total_restore_point_size_bytes

        latest_restore_point_size_bytes: Union[None, Unset, int]
        if isinstance(self.latest_restore_point_size_bytes, Unset):
            latest_restore_point_size_bytes = UNSET
        else:
            latest_restore_point_size_bytes = self.latest_restore_point_size_bytes

        restore_points = self.restore_points

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        repository: Union[None, Unset, dict[str, Any]]
        if isinstance(self.repository, Unset):
            repository = UNSET
        elif isinstance(self.repository, ProtectedDataRepositoryInfo):
            repository = self.repository.to_dict()
        else:
            repository = self.repository

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        total_unique_restore_points_size_bytes: Union[None, Unset, int]
        if isinstance(self.total_unique_restore_points_size_bytes, Unset):
            total_unique_restore_points_size_bytes = UNSET
        else:
            total_unique_restore_points_size_bytes = self.total_unique_restore_points_size_bytes

        unique_restore_points: Union[None, Unset, int]
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
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo

        d = dict(src_dict)
        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: Union[Unset, UUID]
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        def _parse_vm_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vm_uid_in_vbr_type_0 = UUID(data)

                return vm_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        vm_uid_in_vbr = _parse_vm_uid_in_vbr(d.pop("vmUidInVbr", UNSET))

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_job_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, VmBackupType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VmBackupType(_type_)

        def _parse_total_restore_point_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_restore_point_size_bytes = _parse_total_restore_point_size_bytes(
            d.pop("totalRestorePointSizeBytes", UNSET)
        )

        def _parse_latest_restore_point_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        latest_restore_point_size_bytes = _parse_latest_restore_point_size_bytes(
            d.pop("latestRestorePointSizeBytes", UNSET)
        )

        restore_points = d.pop("restorePoints", UNSET)

        def _parse_last_protected_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = isoparse(data)

                return last_protected_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

        def _parse_repository(data: object) -> Union["ProtectedDataRepositoryInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repository_type_1 = ProtectedDataRepositoryInfo.from_dict(data)

                return repository_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProtectedDataRepositoryInfo", None, Unset], data)

        repository = _parse_repository(d.pop("repository", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_total_unique_restore_points_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_unique_restore_points_size_bytes = _parse_total_unique_restore_points_size_bytes(
            d.pop("totalUniqueRestorePointsSizeBytes", UNSET)
        )

        def _parse_unique_restore_points(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

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
