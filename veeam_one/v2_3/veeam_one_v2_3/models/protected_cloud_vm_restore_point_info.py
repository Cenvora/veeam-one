import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudVmRestorePointInfo")


@_attrs_define
class ProtectedCloudVmRestorePointInfo:
    """
    Attributes:
        restore_point_uid (Union[None, UUID, Unset]): UID assigned to a restore point.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup chain.
        cloud_vm_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected cloud VM.
        job_uid (Union[None, UUID, Unset]): UID assigned to a job.
        job_name (Union[None, Unset, str]): Name of a job.
        target (Union[None, Unset, str]): Name of a backup repository.
        original_size_bytes (Union[None, Unset, int]): Used space on protected cloud VM disks, in bytes.
        backup_size_bytes (Union[None, Unset, int]): Backup size, in bytes.
        creation_time (Union[None, Unset, datetime.datetime]): Time and date when a restore point was created.
        immutable_till (Union[None, Unset, datetime.datetime]): Date and time till which a restore point remains
            immutable.
    """

    restore_point_uid: Union[None, UUID, Unset] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    cloud_vm_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    target: Union[None, Unset, str] = UNSET
    original_size_bytes: Union[None, Unset, int] = UNSET
    backup_size_bytes: Union[None, Unset, int] = UNSET
    creation_time: Union[None, Unset, datetime.datetime] = UNSET
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

        cloud_vm_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.cloud_vm_uid_in_vbr, Unset):
            cloud_vm_uid_in_vbr = UNSET
        elif isinstance(self.cloud_vm_uid_in_vbr, UUID):
            cloud_vm_uid_in_vbr = str(self.cloud_vm_uid_in_vbr)
        else:
            cloud_vm_uid_in_vbr = self.cloud_vm_uid_in_vbr

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

        target: Union[None, Unset, str]
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        original_size_bytes: Union[None, Unset, int]
        if isinstance(self.original_size_bytes, Unset):
            original_size_bytes = UNSET
        else:
            original_size_bytes = self.original_size_bytes

        backup_size_bytes: Union[None, Unset, int]
        if isinstance(self.backup_size_bytes, Unset):
            backup_size_bytes = UNSET
        else:
            backup_size_bytes = self.backup_size_bytes

        creation_time: Union[None, Unset, str]
        if isinstance(self.creation_time, Unset):
            creation_time = UNSET
        elif isinstance(self.creation_time, datetime.datetime):
            creation_time = self.creation_time.isoformat()
        else:
            creation_time = self.creation_time

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
        if cloud_vm_uid_in_vbr is not UNSET:
            field_dict["cloudVmUidInVbr"] = cloud_vm_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if target is not UNSET:
            field_dict["target"] = target
        if original_size_bytes is not UNSET:
            field_dict["originalSizeBytes"] = original_size_bytes
        if backup_size_bytes is not UNSET:
            field_dict["backupSizeBytes"] = backup_size_bytes
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
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

        def _parse_cloud_vm_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_vm_uid_in_vbr_type_0 = UUID(data)

                return cloud_vm_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_vm_uid_in_vbr = _parse_cloud_vm_uid_in_vbr(d.pop("cloudVmUidInVbr", UNSET))

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

        def _parse_target(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target = _parse_target(d.pop("target", UNSET))

        def _parse_original_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        original_size_bytes = _parse_original_size_bytes(d.pop("originalSizeBytes", UNSET))

        def _parse_backup_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_size_bytes = _parse_backup_size_bytes(d.pop("backupSizeBytes", UNSET))

        def _parse_creation_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_time_type_0 = isoparse(data)

                return creation_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_time = _parse_creation_time(d.pop("creationTime", UNSET))

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

        protected_cloud_vm_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            backup_uid=backup_uid,
            cloud_vm_uid_in_vbr=cloud_vm_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            target=target,
            original_size_bytes=original_size_bytes,
            backup_size_bytes=backup_size_bytes,
            creation_time=creation_time,
            immutable_till=immutable_till,
        )

        return protected_cloud_vm_restore_point_info
