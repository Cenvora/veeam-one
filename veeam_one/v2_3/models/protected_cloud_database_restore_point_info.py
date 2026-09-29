from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudDatabaseRestorePointInfo")


@_attrs_define
class ProtectedCloudDatabaseRestorePointInfo:
    """
    Attributes:
        restore_point_uid (None | Unset | UUID): UID assigned to a restore point.
        backup_uid (None | Unset | UUID): UID assigned to a backup chain.
        cloud_database_uid_in_vbr (None | Unset | UUID): UID assigned to a cloud database in Veeam Backup & Replication.
        job_uid (None | Unset | UUID): UID assigned to a job.
        job_name (None | str | Unset): Name of a job.
        target (None | str | Unset): Name of a backup repository.
        creation_time (datetime.datetime | None | Unset): Date and time when a restore point was created.
    """

    restore_point_uid: None | Unset | UUID = UNSET
    backup_uid: None | Unset | UUID = UNSET
    cloud_database_uid_in_vbr: None | Unset | UUID = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET
    target: None | str | Unset = UNSET
    creation_time: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_uid: None | str | Unset
        if isinstance(self.restore_point_uid, Unset):
            restore_point_uid = UNSET
        elif isinstance(self.restore_point_uid, UUID):
            restore_point_uid = str(self.restore_point_uid)
        else:
            restore_point_uid = self.restore_point_uid

        backup_uid: None | str | Unset
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        cloud_database_uid_in_vbr: None | str | Unset
        if isinstance(self.cloud_database_uid_in_vbr, Unset):
            cloud_database_uid_in_vbr = UNSET
        elif isinstance(self.cloud_database_uid_in_vbr, UUID):
            cloud_database_uid_in_vbr = str(self.cloud_database_uid_in_vbr)
        else:
            cloud_database_uid_in_vbr = self.cloud_database_uid_in_vbr

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

        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

        creation_time: None | str | Unset
        if isinstance(self.creation_time, Unset):
            creation_time = UNSET
        elif isinstance(self.creation_time, datetime.datetime):
            creation_time = self.creation_time.isoformat()
        else:
            creation_time = self.creation_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_uid is not UNSET:
            field_dict["restorePointUid"] = restore_point_uid
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if cloud_database_uid_in_vbr is not UNSET:
            field_dict["cloudDatabaseUidInVbr"] = cloud_database_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if target is not UNSET:
            field_dict["target"] = target
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_restore_point_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                restore_point_uid_type_0 = UUID(data)

                return restore_point_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        restore_point_uid = _parse_restore_point_uid(d.pop("restorePointUid", UNSET))

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

        def _parse_cloud_database_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_database_uid_in_vbr_type_0 = UUID(data)

                return cloud_database_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cloud_database_uid_in_vbr = _parse_cloud_database_uid_in_vbr(d.pop("cloudDatabaseUidInVbr", UNSET))

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

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))

        def _parse_creation_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_time_type_0 = datetime.datetime.fromisoformat(data)

                return creation_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        creation_time = _parse_creation_time(d.pop("creationTime", UNSET))

        protected_cloud_database_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            backup_uid=backup_uid,
            cloud_database_uid_in_vbr=cloud_database_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            target=target,
            creation_time=creation_time,
        )

        return protected_cloud_database_restore_point_info
