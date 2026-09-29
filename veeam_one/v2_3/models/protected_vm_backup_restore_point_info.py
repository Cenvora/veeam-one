import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVmBackupRestorePointInfo")


@_attrs_define
class ProtectedVmBackupRestorePointInfo:
    """
    Attributes:
        restore_point_uid (Union[None, UUID, Unset]): UID assigned to a restore point.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup chain.
        vm_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected VM.
        job_uid (Union[None, UUID, Unset]): UID assigned to a job.
        job_name (Union[None, Unset, str]): Name of a job.
        repository_uid (Union[None, UUID, Unset]): UID assigned to a repository on which a restore point resides.
        size_bytes (Union[None, Unset, int]): Size of a restore point, in bytes.
        provisioned_source_size_bytes (Union[None, Unset, int]): Total size of protected VM disks, in bytes.
        used_source_size_bytes (Union[None, Unset, int]): Used space on protected VM disks, in bytes.
        file_creation_date (Union[None, Unset, datetime.datetime]): Time and date when a restore point was created.
        is_incremental (Union[None, Unset, bool]): Indicates whether a restore point is an increment.
        immutable_till (Union[None, Unset, datetime.datetime]): Date and time till which a restore point remains
            immutable.
    """

    restore_point_uid: Union[None, UUID, Unset] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    vm_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    repository_uid: Union[None, UUID, Unset] = UNSET
    size_bytes: Union[None, Unset, int] = UNSET
    provisioned_source_size_bytes: Union[None, Unset, int] = UNSET
    used_source_size_bytes: Union[None, Unset, int] = UNSET
    file_creation_date: Union[None, Unset, datetime.datetime] = UNSET
    is_incremental: Union[None, Unset, bool] = UNSET
    immutable_till: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_uid: Union[None, Unset, str]
        if isinstance(self.restore_point_uid, Unset):
            restore_point_uid = UNSET
        elif isinstance(self.restore_point_uid, UUID):
            restore_point_uid = str(self.restore_point_uid)
        else:
            restore_point_uid = self.restore_point_uid

        backup_uid: Union[None, Unset, str]
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

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

        repository_uid: Union[None, Unset, str]
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        size_bytes: Union[None, Unset, int]
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        provisioned_source_size_bytes: Union[None, Unset, int]
        if isinstance(self.provisioned_source_size_bytes, Unset):
            provisioned_source_size_bytes = UNSET
        else:
            provisioned_source_size_bytes = self.provisioned_source_size_bytes

        used_source_size_bytes: Union[None, Unset, int]
        if isinstance(self.used_source_size_bytes, Unset):
            used_source_size_bytes = UNSET
        else:
            used_source_size_bytes = self.used_source_size_bytes

        file_creation_date: Union[None, Unset, str]
        if isinstance(self.file_creation_date, Unset):
            file_creation_date = UNSET
        elif isinstance(self.file_creation_date, datetime.datetime):
            file_creation_date = self.file_creation_date.isoformat()
        else:
            file_creation_date = self.file_creation_date

        is_incremental: Union[None, Unset, bool]
        if isinstance(self.is_incremental, Unset):
            is_incremental = UNSET
        else:
            is_incremental = self.is_incremental

        immutable_till: Union[None, Unset, str]
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_uid is not UNSET:
            field_dict["restorePointUid"] = restore_point_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if vm_uid_in_vbr is not UNSET:
            field_dict["vmUidInVbr"] = vm_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if provisioned_source_size_bytes is not UNSET:
            field_dict["provisionedSourceSizeBytes"] = provisioned_source_size_bytes
        if used_source_size_bytes is not UNSET:
            field_dict["usedSourceSizeBytes"] = used_source_size_bytes
        if file_creation_date is not UNSET:
            field_dict["fileCreationDate"] = file_creation_date
        if is_incremental is not UNSET:
            field_dict["isIncremental"] = is_incremental
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_restore_point_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_uid_type_0 = UUID(data)

                return restore_point_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        restore_point_uid = _parse_restore_point_uid(d.pop("restorePointUid", UNSET))

        def _parse_backup_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_uid_type_0 = UUID(data)

                return backup_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_uid = _parse_backup_uid(d.pop("backupUid", UNSET))

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

        def _parse_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        def _parse_provisioned_source_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        provisioned_source_size_bytes = _parse_provisioned_source_size_bytes(d.pop("provisionedSourceSizeBytes", UNSET))

        def _parse_used_source_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_source_size_bytes = _parse_used_source_size_bytes(d.pop("usedSourceSizeBytes", UNSET))

        def _parse_file_creation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_creation_date_type_0 = isoparse(data)

                return file_creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        file_creation_date = _parse_file_creation_date(d.pop("fileCreationDate", UNSET))

        def _parse_is_incremental(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_incremental = _parse_is_incremental(d.pop("isIncremental", UNSET))

        def _parse_immutable_till(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutable_till_type_0 = isoparse(data)

                return immutable_till_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        immutable_till = _parse_immutable_till(d.pop("immutableTill", UNSET))

        protected_vm_backup_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            backup_uid=backup_uid,
            vm_uid_in_vbr=vm_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            repository_uid=repository_uid,
            size_bytes=size_bytes,
            provisioned_source_size_bytes=provisioned_source_size_bytes,
            used_source_size_bytes=used_source_size_bytes,
            file_creation_date=file_creation_date,
            is_incremental=is_incremental,
            immutable_till=immutable_till,
        )

        return protected_vm_backup_restore_point_info
