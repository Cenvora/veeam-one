import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.application_backup_job_status import ApplicationBackupJobStatus
from ..models.application_job_platform import ApplicationJobPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationBackupJobInfo")


@_attrs_define
class ApplicationBackupJobInfo:
    """
    Attributes:
        application_backup_job_uid (Union[None, UUID, Unset]): UID assigned to a job in Veeam Backup & Replication.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        status (Union[Unset, ApplicationBackupJobStatus]):
        details (Union[None, Unset, list[str]]): Job details.
        name (Union[None, Unset, str]): Name of a job.
        description (Union[None, Unset, str]): Description of a job.
        platform (Union[Unset, ApplicationJobPlatform]):
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest job session.
        last_transferred_data_bytes (Union[None, Unset, int]): Amount of data transferred during the latest job session,
            in bytes.
    """

    application_backup_job_uid: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    status: Union[Unset, ApplicationBackupJobStatus] = UNSET
    details: Union[None, Unset, list[str]] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    platform: Union[Unset, ApplicationJobPlatform] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_transferred_data_bytes: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_backup_job_uid: Union[None, Unset, str]
        if isinstance(self.application_backup_job_uid, Unset):
            application_backup_job_uid = UNSET
        elif isinstance(self.application_backup_job_uid, UUID):
            application_backup_job_uid = str(self.application_backup_job_uid)
        else:
            application_backup_job_uid = self.application_backup_job_uid

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

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_transferred_data_bytes: Union[None, Unset, int]
        if isinstance(self.last_transferred_data_bytes, Unset):
            last_transferred_data_bytes = UNSET
        else:
            last_transferred_data_bytes = self.last_transferred_data_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if application_backup_job_uid is not UNSET:
            field_dict["applicationBackupJobUid"] = application_backup_job_uid
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
        if platform is not UNSET:
            field_dict["platform"] = platform
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_transferred_data_bytes is not UNSET:
            field_dict["lastTransferredDataBytes"] = last_transferred_data_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_application_backup_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_backup_job_uid_type_0 = UUID(data)

                return application_backup_job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        application_backup_job_uid = _parse_application_backup_job_uid(d.pop("applicationBackupJobUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ApplicationBackupJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApplicationBackupJobStatus(_status)

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

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ApplicationJobPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ApplicationJobPlatform(_platform)

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

        def _parse_last_transferred_data_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_transferred_data_bytes = _parse_last_transferred_data_bytes(d.pop("lastTransferredDataBytes", UNSET))

        application_backup_job_info = cls(
            application_backup_job_uid=application_backup_job_uid,
            backup_server_id=backup_server_id,
            status=status,
            details=details,
            name=name,
            description=description,
            platform=platform,
            last_run=last_run,
            last_transferred_data_bytes=last_transferred_data_bytes,
        )

        return application_backup_job_info
