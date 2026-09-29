import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.cloud_database_backup_type import CloudDatabaseBackupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudDatabaseBackupInfo")


@_attrs_define
class ProtectedCloudDatabaseBackupInfo:
    """
    Attributes:
        backup_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        cloud_database_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a cloud database in Veeam Backup &
            Replication.
        job_uid (Union[None, UUID, Unset]): UID assigned to a job.
        job_name (Union[None, Unset, str]): Name of a job.
        type_ (Union[Unset, CloudDatabaseBackupType]):
        restore_points (Union[Unset, int]): Number of restore points.
        last_protection_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
        target (Union[None, Unset, str]): Name of a backup repository.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
    """

    backup_uid: Union[Unset, UUID] = UNSET
    cloud_database_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, CloudDatabaseBackupType] = UNSET
    restore_points: Union[Unset, int] = UNSET
    last_protection_date: Union[None, Unset, datetime.datetime] = UNSET
    target: Union[None, Unset, str] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        cloud_database_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.cloud_database_uid_in_vbr, Unset):
            cloud_database_uid_in_vbr = UNSET
        elif isinstance(self.cloud_database_uid_in_vbr, UUID):
            cloud_database_uid_in_vbr = str(self.cloud_database_uid_in_vbr)
        else:
            cloud_database_uid_in_vbr = self.cloud_database_uid_in_vbr

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

        restore_points = self.restore_points

        last_protection_date: Union[None, Unset, str]
        if isinstance(self.last_protection_date, Unset):
            last_protection_date = UNSET
        elif isinstance(self.last_protection_date, datetime.datetime):
            last_protection_date = self.last_protection_date.isoformat()
        else:
            last_protection_date = self.last_protection_date

        target: Union[None, Unset, str]
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if cloud_database_uid_in_vbr is not UNSET:
            field_dict["cloudDatabaseUidInVbr"] = cloud_database_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if last_protection_date is not UNSET:
            field_dict["lastProtectionDate"] = last_protection_date
        if target is not UNSET:
            field_dict["target"] = target
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: Union[Unset, UUID]
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        def _parse_cloud_database_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_database_uid_in_vbr_type_0 = UUID(data)

                return cloud_database_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_database_uid_in_vbr = _parse_cloud_database_uid_in_vbr(d.pop("cloudDatabaseUidInVbr", UNSET))

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
        type_: Union[Unset, CloudDatabaseBackupType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CloudDatabaseBackupType(_type_)

        restore_points = d.pop("restorePoints", UNSET)

        def _parse_last_protection_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protection_date_type_0 = isoparse(data)

                return last_protection_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_protection_date = _parse_last_protection_date(d.pop("lastProtectionDate", UNSET))

        def _parse_target(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        target = _parse_target(d.pop("target", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        protected_cloud_database_backup_info = cls(
            backup_uid=backup_uid,
            cloud_database_uid_in_vbr=cloud_database_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            type_=type_,
            restore_points=restore_points,
            last_protection_date=last_protection_date,
            target=target,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_cloud_database_backup_info
