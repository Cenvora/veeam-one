from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.infrequent_access import InfrequentAccess
from ..models.object_storage_type import ObjectStorageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjectStorageInfo")


@_attrs_define
class ObjectStorageInfo:
    """
    Attributes:
        object_storage_id (int | None | Unset): ID assigned to an object storage repository.
        object_storage_uid_in_vbr (None | Unset | UUID): UID assigned to an object storage repository in Veeam Backup &
            Replication.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication.
        name (None | str | Unset): Name of an object storage repository.
        type_ (ObjectStorageType | Unset):
        running_tasks (int | None | Unset): Number of tasks that are currently running on a backup repository.
        description (None | str | Unset): Description of an object storage repository.
        region (None | str | Unset): Region at which an object storage repository is located
        bucket (None | str | Unset): Name of bucket or container.
        capacity_bytes (int | None | Unset): Object storage capacity, in bytes.
        used_space_bytes (int | None | Unset): Amount of used storage space, in bytes.
        consumption_limit_gb (int | None | Unset): Soft limit for object storage consumption, in GB.
        is_immutable (bool | None | Unset): Indicates whether immutability is enabled for an object storage repository.
        immutability_interval_days (int | None | Unset): Immutability period, in days.
        concurrent_jobs_max (int | None | Unset): Maximum number of concurrent jobs.
        concurrent_jobs_now (int | None | Unset): Number of currently running concurrent jobs.
        infrequent_access_storage (InfrequentAccess | Unset):
    """

    object_storage_id: int | None | Unset = UNSET
    object_storage_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: ObjectStorageType | Unset = UNSET
    running_tasks: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    region: None | str | Unset = UNSET
    bucket: None | str | Unset = UNSET
    capacity_bytes: int | None | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    consumption_limit_gb: int | None | Unset = UNSET
    is_immutable: bool | None | Unset = UNSET
    immutability_interval_days: int | None | Unset = UNSET
    concurrent_jobs_max: int | None | Unset = UNSET
    concurrent_jobs_now: int | None | Unset = UNSET
    infrequent_access_storage: InfrequentAccess | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_storage_id: int | None | Unset
        if isinstance(self.object_storage_id, Unset):
            object_storage_id = UNSET
        else:
            object_storage_id = self.object_storage_id

        object_storage_uid_in_vbr: None | str | Unset
        if isinstance(self.object_storage_uid_in_vbr, Unset):
            object_storage_uid_in_vbr = UNSET
        elif isinstance(self.object_storage_uid_in_vbr, UUID):
            object_storage_uid_in_vbr = str(self.object_storage_uid_in_vbr)
        else:
            object_storage_uid_in_vbr = self.object_storage_uid_in_vbr

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        running_tasks: int | None | Unset
        if isinstance(self.running_tasks, Unset):
            running_tasks = UNSET
        else:
            running_tasks = self.running_tasks

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        bucket: None | str | Unset
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        used_space_bytes: int | None | Unset
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        consumption_limit_gb: int | None | Unset
        if isinstance(self.consumption_limit_gb, Unset):
            consumption_limit_gb = UNSET
        else:
            consumption_limit_gb = self.consumption_limit_gb

        is_immutable: bool | None | Unset
        if isinstance(self.is_immutable, Unset):
            is_immutable = UNSET
        else:
            is_immutable = self.is_immutable

        immutability_interval_days: int | None | Unset
        if isinstance(self.immutability_interval_days, Unset):
            immutability_interval_days = UNSET
        else:
            immutability_interval_days = self.immutability_interval_days

        concurrent_jobs_max: int | None | Unset
        if isinstance(self.concurrent_jobs_max, Unset):
            concurrent_jobs_max = UNSET
        else:
            concurrent_jobs_max = self.concurrent_jobs_max

        concurrent_jobs_now: int | None | Unset
        if isinstance(self.concurrent_jobs_now, Unset):
            concurrent_jobs_now = UNSET
        else:
            concurrent_jobs_now = self.concurrent_jobs_now

        infrequent_access_storage: str | Unset = UNSET
        if not isinstance(self.infrequent_access_storage, Unset):
            infrequent_access_storage = self.infrequent_access_storage.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_storage_id is not UNSET:
            field_dict["objectStorageId"] = object_storage_id
        if object_storage_uid_in_vbr is not UNSET:
            field_dict["objectStorageUidInVbr"] = object_storage_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if running_tasks is not UNSET:
            field_dict["runningTasks"] = running_tasks
        if description is not UNSET:
            field_dict["description"] = description
        if region is not UNSET:
            field_dict["region"] = region
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if consumption_limit_gb is not UNSET:
            field_dict["consumptionLimitGb"] = consumption_limit_gb
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable
        if immutability_interval_days is not UNSET:
            field_dict["immutabilityIntervalDays"] = immutability_interval_days
        if concurrent_jobs_max is not UNSET:
            field_dict["concurrentJobsMax"] = concurrent_jobs_max
        if concurrent_jobs_now is not UNSET:
            field_dict["concurrentJobsNow"] = concurrent_jobs_now
        if infrequent_access_storage is not UNSET:
            field_dict["infrequentAccessStorage"] = infrequent_access_storage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_object_storage_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        object_storage_id = _parse_object_storage_id(d.pop("objectStorageId", UNSET))

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

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: ObjectStorageType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ObjectStorageType(_type_)

        def _parse_running_tasks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        running_tasks = _parse_running_tasks(d.pop("runningTasks", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_consumption_limit_gb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        consumption_limit_gb = _parse_consumption_limit_gb(d.pop("consumptionLimitGb", UNSET))

        def _parse_is_immutable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_immutable = _parse_is_immutable(d.pop("isImmutable", UNSET))

        def _parse_immutability_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        immutability_interval_days = _parse_immutability_interval_days(d.pop("immutabilityIntervalDays", UNSET))

        def _parse_concurrent_jobs_max(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrent_jobs_max = _parse_concurrent_jobs_max(d.pop("concurrentJobsMax", UNSET))

        def _parse_concurrent_jobs_now(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        concurrent_jobs_now = _parse_concurrent_jobs_now(d.pop("concurrentJobsNow", UNSET))

        _infrequent_access_storage = d.pop("infrequentAccessStorage", UNSET)
        infrequent_access_storage: InfrequentAccess | Unset
        if isinstance(_infrequent_access_storage, Unset):
            infrequent_access_storage = UNSET
        else:
            infrequent_access_storage = InfrequentAccess(_infrequent_access_storage)

        object_storage_info = cls(
            object_storage_id=object_storage_id,
            object_storage_uid_in_vbr=object_storage_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            type_=type_,
            running_tasks=running_tasks,
            description=description,
            region=region,
            bucket=bucket,
            capacity_bytes=capacity_bytes,
            used_space_bytes=used_space_bytes,
            consumption_limit_gb=consumption_limit_gb,
            is_immutable=is_immutable,
            immutability_interval_days=immutability_interval_days,
            concurrent_jobs_max=concurrent_jobs_max,
            concurrent_jobs_now=concurrent_jobs_now,
            infrequent_access_storage=infrequent_access_storage,
        )

        return object_storage_info
