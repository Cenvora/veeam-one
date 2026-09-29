import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.protected_object_storage_type import ProtectedObjectStorageType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job import Job


T = TypeVar("T", bound="ProtectedObjectStorageInfo")


@_attrs_define
class ProtectedObjectStorageInfo:
    """
    Attributes:
        object_storage_uid_in_vbr (Union[Unset, UUID]): UID assigned to an object storage in Veeam Backup & Replication.
        name (Union[None, Unset, str]): Name of an object storage.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
        type_ (Union[Unset, ProtectedObjectStorageType]):
        jobs (Union[None, Unset, list['Job']]): Array of jobs protecting object storage.
        last_protected_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
    """

    object_storage_uid_in_vbr: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, ProtectedObjectStorageType] = UNSET
    jobs: Union[None, Unset, list["Job"]] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_storage_uid_in_vbr: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_uid_in_vbr, Unset):
            object_storage_uid_in_vbr = str(self.object_storage_uid_in_vbr)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        jobs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.jobs, Unset):
            jobs = UNSET
        elif isinstance(self.jobs, list):
            jobs = []
            for jobs_type_0_item_data in self.jobs:
                jobs_type_0_item = jobs_type_0_item_data.to_dict()
                jobs.append(jobs_type_0_item)

        else:
            jobs = self.jobs

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_storage_uid_in_vbr is not UNSET:
            field_dict["objectStorageUidInVbr"] = object_storage_uid_in_vbr
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if jobs is not UNSET:
            field_dict["jobs"] = jobs
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job import Job

        d = dict(src_dict)
        _object_storage_uid_in_vbr = d.pop("objectStorageUidInVbr", UNSET)
        object_storage_uid_in_vbr: Union[Unset, UUID]
        if isinstance(_object_storage_uid_in_vbr, Unset):
            object_storage_uid_in_vbr = UNSET
        else:
            object_storage_uid_in_vbr = UUID(_object_storage_uid_in_vbr)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ProtectedObjectStorageType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ProtectedObjectStorageType(_type_)

        def _parse_jobs(data: object) -> Union[None, Unset, list["Job"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                jobs_type_0 = []
                _jobs_type_0 = data
                for jobs_type_0_item_data in _jobs_type_0:
                    jobs_type_0_item = Job.from_dict(jobs_type_0_item_data)

                    jobs_type_0.append(jobs_type_0_item)

                return jobs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Job"]], data)

        jobs = _parse_jobs(d.pop("jobs", UNSET))

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

        protected_object_storage_info = cls(
            object_storage_uid_in_vbr=object_storage_uid_in_vbr,
            name=name,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            type_=type_,
            jobs=jobs,
            last_protected_date=last_protected_date,
        )

        return protected_object_storage_info
