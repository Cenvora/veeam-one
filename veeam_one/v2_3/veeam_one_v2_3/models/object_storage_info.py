from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        object_storage_id (Union[None, Unset, int]): ID assigned to an object storage repository.
        object_storage_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to an object storage repository in Veeam
            Backup & Replication.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup & Replication.
        name (Union[None, Unset, str]): Name of an object storage repository.
        type_ (Union[Unset, ObjectStorageType]):
        running_tasks (Union[None, Unset, int]): Number of tasks that are currently running on a backup repository.
        description (Union[None, Unset, str]): Description of an object storage repository.
        region (Union[None, Unset, str]): Region at which an object storage repository is located
        bucket (Union[None, Unset, str]): Name of bucket or container.
        capacity_bytes (Union[None, Unset, int]): Object storage capacity, in bytes.
        used_space_bytes (Union[None, Unset, int]): Amount of used storage space, in bytes.
        consumption_limit_gb (Union[None, Unset, int]): Soft limit for object storage consumption, in GB.
        is_immutable (Union[None, Unset, bool]): Indicates whether immutability is enabled for an object storage
            repository.
        immutability_interval_days (Union[None, Unset, int]): Immutability period, in days.
        concurrent_jobs_max (Union[None, Unset, int]): Maximum number of concurrent jobs.
        concurrent_jobs_now (Union[None, Unset, int]): Number of currently running concurrent jobs.
        infrequent_access_storage (Union[Unset, InfrequentAccess]):
    """

    object_storage_id: Union[None, Unset, int] = UNSET
    object_storage_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, ObjectStorageType] = UNSET
    running_tasks: Union[None, Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    region: Union[None, Unset, str] = UNSET
    bucket: Union[None, Unset, str] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    used_space_bytes: Union[None, Unset, int] = UNSET
    consumption_limit_gb: Union[None, Unset, int] = UNSET
    is_immutable: Union[None, Unset, bool] = UNSET
    immutability_interval_days: Union[None, Unset, int] = UNSET
    concurrent_jobs_max: Union[None, Unset, int] = UNSET
    concurrent_jobs_now: Union[None, Unset, int] = UNSET
    infrequent_access_storage: Union[Unset, InfrequentAccess] = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_storage_id: Union[None, Unset, int]
        if isinstance(self.object_storage_id, Unset):
            object_storage_id = UNSET
        else:
            object_storage_id = self.object_storage_id

        object_storage_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.object_storage_uid_in_vbr, Unset):
            object_storage_uid_in_vbr = UNSET
        elif isinstance(self.object_storage_uid_in_vbr, UUID):
            object_storage_uid_in_vbr = str(self.object_storage_uid_in_vbr)
        else:
            object_storage_uid_in_vbr = self.object_storage_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        running_tasks: Union[None, Unset, int]
        if isinstance(self.running_tasks, Unset):
            running_tasks = UNSET
        else:
            running_tasks = self.running_tasks

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        bucket: Union[None, Unset, str]
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        used_space_bytes: Union[None, Unset, int]
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        consumption_limit_gb: Union[None, Unset, int]
        if isinstance(self.consumption_limit_gb, Unset):
            consumption_limit_gb = UNSET
        else:
            consumption_limit_gb = self.consumption_limit_gb

        is_immutable: Union[None, Unset, bool]
        if isinstance(self.is_immutable, Unset):
            is_immutable = UNSET
        else:
            is_immutable = self.is_immutable

        immutability_interval_days: Union[None, Unset, int]
        if isinstance(self.immutability_interval_days, Unset):
            immutability_interval_days = UNSET
        else:
            immutability_interval_days = self.immutability_interval_days

        concurrent_jobs_max: Union[None, Unset, int]
        if isinstance(self.concurrent_jobs_max, Unset):
            concurrent_jobs_max = UNSET
        else:
            concurrent_jobs_max = self.concurrent_jobs_max

        concurrent_jobs_now: Union[None, Unset, int]
        if isinstance(self.concurrent_jobs_now, Unset):
            concurrent_jobs_now = UNSET
        else:
            concurrent_jobs_now = self.concurrent_jobs_now

        infrequent_access_storage: Union[Unset, str] = UNSET
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

        def _parse_object_storage_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        object_storage_id = _parse_object_storage_id(d.pop("objectStorageId", UNSET))

        def _parse_object_storage_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_storage_uid_in_vbr_type_0 = UUID(data)

                return object_storage_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        object_storage_uid_in_vbr = _parse_object_storage_uid_in_vbr(d.pop("objectStorageUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ObjectStorageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ObjectStorageType(_type_)

        def _parse_running_tasks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        running_tasks = _parse_running_tasks(d.pop("runningTasks", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_bucket(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_consumption_limit_gb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        consumption_limit_gb = _parse_consumption_limit_gb(d.pop("consumptionLimitGb", UNSET))

        def _parse_is_immutable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_immutable = _parse_is_immutable(d.pop("isImmutable", UNSET))

        def _parse_immutability_interval_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        immutability_interval_days = _parse_immutability_interval_days(d.pop("immutabilityIntervalDays", UNSET))

        def _parse_concurrent_jobs_max(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        concurrent_jobs_max = _parse_concurrent_jobs_max(d.pop("concurrentJobsMax", UNSET))

        def _parse_concurrent_jobs_now(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        concurrent_jobs_now = _parse_concurrent_jobs_now(d.pop("concurrentJobsNow", UNSET))

        _infrequent_access_storage = d.pop("infrequentAccessStorage", UNSET)
        infrequent_access_storage: Union[Unset, InfrequentAccess]
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
