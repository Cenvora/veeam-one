import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.backup_job_status import BackupJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupCopyJobInfo")


@_attrs_define
class BackupCopyJobInfo:
    """
    Attributes:
        backup_copy_job_uid (Union[None, UUID, Unset]): UID assigned to a job in Veeam Backup & Replication.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        status (Union[Unset, BackupJobStatus]):
        details (Union[None, Unset, list[str]]): Job details.
        name (Union[None, Unset, str]): Name of a job.
        description (Union[None, Unset, str]): Job description.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest job session.
    """

    backup_copy_job_uid: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    status: Union[Unset, BackupJobStatus] = UNSET
    details: Union[None, Unset, list[str]] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_copy_job_uid: Union[None, Unset, str]
        if isinstance(self.backup_copy_job_uid, Unset):
            backup_copy_job_uid = UNSET
        elif isinstance(self.backup_copy_job_uid, UUID):
            backup_copy_job_uid = str(self.backup_copy_job_uid)
        else:
            backup_copy_job_uid = self.backup_copy_job_uid

        backup_server_id = self.backup_server_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: Union[None, Unset, list[str]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        else:
            details = self.details

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_copy_job_uid is not UNSET:
            field_dict["backupCopyJobUid"] = backup_copy_job_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_backup_copy_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_copy_job_uid_type_0 = UUID(data)

                return backup_copy_job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_copy_job_uid = _parse_backup_copy_job_uid(d.pop("backupCopyJobUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupJobStatus(_status)

        def _parse_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_last_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)

                return last_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        backup_copy_job_info = cls(
            backup_copy_job_uid=backup_copy_job_uid,
            backup_server_id=backup_server_id,
            status=status,
            details=details,
            name=name,
            description=description,
            last_run=last_run,
        )

        return backup_copy_job_info
