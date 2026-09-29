import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudNetworkRestorePointInfo")


@_attrs_define
class ProtectedCloudNetworkRestorePointInfo:
    """
    Attributes:
        restore_point_uid (Union[Unset, UUID]): UID assigned to a restore point.
        backup_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        instance_uid (Union[Unset, UUID]): UID assigned to a backup chain.
        job_uid (Union[Unset, UUID]): UID assigned to a job.
        job_name (Union[None, Unset, str]): Name of a job.
        target (Union[None, Unset, str]): Name of a backup repository.
        creation_time (Union[None, Unset, datetime.datetime]): Date and time when a restore point was created.
    """

    restore_point_uid: Union[Unset, UUID] = UNSET
    backup_uid: Union[Unset, UUID] = UNSET
    instance_uid: Union[Unset, UUID] = UNSET
    job_uid: Union[Unset, UUID] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    target: Union[None, Unset, str] = UNSET
    creation_time: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_uid: Union[Unset, str] = UNSET
        if not isinstance(self.restore_point_uid, Unset):
            restore_point_uid = str(self.restore_point_uid)

        backup_uid: Union[Unset, str] = UNSET
        if not isinstance(self.backup_uid, Unset):
            backup_uid = str(self.backup_uid)

        instance_uid: Union[Unset, str] = UNSET
        if not isinstance(self.instance_uid, Unset):
            instance_uid = str(self.instance_uid)

        job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.job_uid, Unset):
            job_uid = str(self.job_uid)

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

        creation_time: Union[None, Unset, str]
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
        if instance_uid is not UNSET:
            field_dict["instanceUid"] = instance_uid
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
        _restore_point_uid = d.pop("restorePointUid", UNSET)
        restore_point_uid: Union[Unset, UUID]
        if isinstance(_restore_point_uid, Unset):
            restore_point_uid = UNSET
        else:
            restore_point_uid = UUID(_restore_point_uid)

        _backup_uid = d.pop("backupUid", UNSET)
        backup_uid: Union[Unset, UUID]
        if isinstance(_backup_uid, Unset):
            backup_uid = UNSET
        else:
            backup_uid = UUID(_backup_uid)

        _instance_uid = d.pop("instanceUid", UNSET)
        instance_uid: Union[Unset, UUID]
        if isinstance(_instance_uid, Unset):
            instance_uid = UNSET
        else:
            instance_uid = UUID(_instance_uid)

        _job_uid = d.pop("jobUid", UNSET)
        job_uid: Union[Unset, UUID]
        if isinstance(_job_uid, Unset):
            job_uid = UNSET
        else:
            job_uid = UUID(_job_uid)

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

        protected_cloud_network_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            backup_uid=backup_uid,
            instance_uid=instance_uid,
            job_uid=job_uid,
            job_name=job_name,
            target=target,
            creation_time=creation_time,
        )

        return protected_cloud_network_restore_point_info
