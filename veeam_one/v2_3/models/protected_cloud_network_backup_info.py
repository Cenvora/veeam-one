from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudNetworkBackupInfo")


@_attrs_define
class ProtectedCloudNetworkBackupInfo:
    """
    Attributes:
        backup_uid (UUID | Unset): UID assigned to a backup chain.
        cloud_network_uid_in_vbr (UUID | Unset): UID assigned to a cloud network.
        job_uid (UUID | Unset): UID assigned to a job.
        job_name (None | str | Unset): Name of a job.
        restore_points (int | None | Unset): Number of restore points.
        last_protection_date (datetime.datetime | None | Unset): Date and time when the latest restore point was
            created.
        target (None | str | Unset): Name of a backup repository.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
    """

    backup_uid: UUID | Unset = UNSET
    cloud_network_uid_in_vbr: UUID | Unset = UNSET
    job_uid: UUID | Unset = UNSET
    job_name: None | str | Unset = UNSET
    restore_points: int | None | Unset = UNSET
    last_protection_date: datetime.datetime | None | Unset = UNSET
    target: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_uid: str | Unset = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        cloud_network_uid_in_vbr: str | Unset = UNSET
        if not isinstance(self.cloud_network_uid_in_vbr, Unset):
            cloud_network_uid_in_vbr = str(self.cloud_network_uid_in_vbr)

        job_uid: str | Unset = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

        job_name: None | str | Unset
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        restore_points: int | None | Unset
        if isinstance(self.restore_points, Unset):
            restore_points = UNSET
        else:
            restore_points = self.restore_points

        last_protection_date: None | str | Unset
        if isinstance(self.last_protection_date, Unset):
            last_protection_date = UNSET
        elif isinstance(self.last_protection_date, datetime.datetime):
            last_protection_date = self.last_protection_date.isoformat()
        else:
            last_protection_date = self.last_protection_date

        target: None | str | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        else:
            target = self.target

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
        if cloud_network_uid_in_vbr is not UNSET:
            field_dict["cloudNetworkUidInVbr"] = cloud_network_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
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
        backup_uid: UUID | Unset
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        _cloud_network_uid_in_vbr = d.pop("cloudNetworkUidInVbr", UNSET)
        cloud_network_uid_in_vbr: UUID | Unset
        if isinstance(_cloud_network_uid_in_vbr, Unset):
            cloud_network_uid_in_vbr = UNSET
        else:
            cloud_network_uid_in_vbr = UUID(_cloud_network_uid_in_vbr)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: UUID | Unset
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

        def _parse_job_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        def _parse_restore_points(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        restore_points = _parse_restore_points(d.pop("restorePoints", UNSET))

        def _parse_last_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protection_date = _parse_last_protection_date(d.pop("lastProtectionDate", UNSET))

        def _parse_target(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        target = _parse_target(d.pop("target", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        protected_cloud_network_backup_info = cls(
            backup_uid=backup_uid,
            cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            restore_points=restore_points,
            last_protection_date=last_protection_date,
            target=target,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_cloud_network_backup_info
