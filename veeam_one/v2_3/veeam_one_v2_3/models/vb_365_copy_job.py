import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vb_365_copy_job_schedule_type import Vb365CopyJobScheduleType
from ..models.vb_365_job_status import Vb365JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365CopyJob")


@_attrs_define
class Vb365CopyJob:
    """
    Attributes:
        copy_job_uid (Union[Unset, UUID]): UID assigned to a backup copy job.
        name (Union[None, Unset, str]): Name of a backup copy job.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        status (Union[Unset, Vb365JobStatus]):
        details (Union[None, Unset, list[str]]): Backup copy job details.
        schedule_type (Union[Unset, Vb365CopyJobScheduleType]):
        is_enabled (Union[Unset, bool]): Indicates whether a backup copy job is enabled.
        organization_uid (Union[None, UUID, Unset]): UID assigned to a Microsoft 365 organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft 365 organization.
        repository_uid (Union[None, UUID, Unset]): UID assigned to a backup repository.
        repository_name (Union[None, Unset, str]): Name of a backup repository.
        proxy_id (Union[None, UUID, Unset]): UID assigned to a backup proxy.
        proxy_name (Union[None, Unset, str]): Name of a backup proxy.
        last_run (Union[None, Unset, datetime.datetime]): Date and time when the latest backup copy job session started.
        last_run_duration_sec (Union[None, Unset, int]): Duration of the latest backup copy job session, in seconds.
        last_transferred_data_bytes (Union[None, Unset, int]): Size of tha data transferred during the latest backup
            copy job session, in bytes.
        processed_items (Union[None, Unset, int]): Number of processed items.
    """

    copy_job_uid: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    status: Union[Unset, Vb365JobStatus] = UNSET
    details: Union[None, Unset, list[str]] = UNSET
    schedule_type: Union[Unset, Vb365CopyJobScheduleType] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    organization_uid: Union[None, UUID, Unset] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    repository_uid: Union[None, UUID, Unset] = UNSET
    repository_name: Union[None, Unset, str] = UNSET
    proxy_id: Union[None, UUID, Unset] = UNSET
    proxy_name: Union[None, Unset, str] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_run_duration_sec: Union[None, Unset, int] = UNSET
    last_transferred_data_bytes: Union[None, Unset, int] = UNSET
    processed_items: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        copy_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.copy_job_uid, Unset):
            copy_job_uid = str(self.copy_job_uid)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vb_365_server_id = self.vb_365_server_id

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

        schedule_type: Union[Unset, str] = UNSET
        if not isinstance(self.schedule_type, Unset):
            schedule_type = self.schedule_type.value

        is_enabled = self.is_enabled

        organization_uid: Union[None, Unset, str]
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        repository_uid: Union[None, Unset, str]
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        repository_name: Union[None, Unset, str]
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        proxy_id: Union[None, Unset, str]
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        elif isinstance(self.proxy_id, UUID):
            proxy_id = str(self.proxy_id)
        else:
            proxy_id = self.proxy_id

        proxy_name: Union[None, Unset, str]
        if isinstance(self.proxy_name, Unset):
            proxy_name = UNSET
        else:
            proxy_name = self.proxy_name

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_run_duration_sec: Union[None, Unset, int]
        if isinstance(self.last_run_duration_sec, Unset):
            last_run_duration_sec = UNSET
        else:
            last_run_duration_sec = self.last_run_duration_sec

        last_transferred_data_bytes: Union[None, Unset, int]
        if isinstance(self.last_transferred_data_bytes, Unset):
            last_transferred_data_bytes = UNSET
        else:
            last_transferred_data_bytes = self.last_transferred_data_bytes

        processed_items: Union[None, Unset, int]
        if isinstance(self.processed_items, Unset):
            processed_items = UNSET
        else:
            processed_items = self.processed_items

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if copy_job_uid is not UNSET:
            field_dict["copyJobUid"] = copy_job_uid
        if name is not UNSET:
            field_dict["name"] = name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if schedule_type is not UNSET:
            field_dict["scheduleType"] = schedule_type
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if proxy_name is not UNSET:
            field_dict["proxyName"] = proxy_name
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_run_duration_sec is not UNSET:
            field_dict["lastRunDurationSec"] = last_run_duration_sec
        if last_transferred_data_bytes is not UNSET:
            field_dict["lastTransferredDataBytes"] = last_transferred_data_bytes
        if processed_items is not UNSET:
            field_dict["processedItems"] = processed_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _copy_job_uid = d.pop("copyJobUid", UNSET)
        copy_job_uid: Union[Unset, UUID]
        if isinstance(_copy_job_uid, Unset):
            copy_job_uid = UNSET
        else:
            copy_job_uid = UUID(_copy_job_uid)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, Vb365JobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365JobStatus(_status)

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

        _schedule_type = d.pop("scheduleType", UNSET)
        schedule_type: Union[Unset, Vb365CopyJobScheduleType]
        if isinstance(_schedule_type, Unset):
            schedule_type = UNSET
        else:
            schedule_type = Vb365CopyJobScheduleType(_schedule_type)

        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        def _parse_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        def _parse_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_repository_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        def _parse_proxy_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_id_type_0 = UUID(data)

                return proxy_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))

        def _parse_proxy_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        proxy_name = _parse_proxy_name(d.pop("proxyName", UNSET))

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

        def _parse_last_run_duration_sec(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_run_duration_sec = _parse_last_run_duration_sec(d.pop("lastRunDurationSec", UNSET))

        def _parse_last_transferred_data_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_transferred_data_bytes = _parse_last_transferred_data_bytes(d.pop("lastTransferredDataBytes", UNSET))

        def _parse_processed_items(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        processed_items = _parse_processed_items(d.pop("processedItems", UNSET))

        vb_365_copy_job = cls(
            copy_job_uid=copy_job_uid,
            name=name,
            vb_365_server_id=vb_365_server_id,
            status=status,
            details=details,
            schedule_type=schedule_type,
            is_enabled=is_enabled,
            organization_uid=organization_uid,
            organization_name=organization_name,
            repository_uid=repository_uid,
            repository_name=repository_name,
            proxy_id=proxy_id,
            proxy_name=proxy_name,
            last_run=last_run,
            last_run_duration_sec=last_run_duration_sec,
            last_transferred_data_bytes=last_transferred_data_bytes,
            processed_items=processed_items,
        )

        return vb_365_copy_job
