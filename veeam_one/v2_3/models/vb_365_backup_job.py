from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_backup_type import Vb365BackupType
from ..models.vb_365_job_status import Vb365JobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupJob")


@_attrs_define
class Vb365BackupJob:
    """
    Attributes:
        backup_job_uid (UUID | Unset): UID assigned to a backup job.
        name (None | str | Unset): Name of a backup job.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365.
        status (Vb365JobStatus | Unset):
        details (list[str] | None | Unset): Backup job details.
        description (None | str | Unset): Description of a backup job.
        backup_type (Vb365BackupType | Unset):
        is_enabled (bool | Unset): Indicates whether a backup job is enabled.
        organization_uid (None | Unset | UUID): UID assigned to a Microsoft 365 organization.
        organization_name (None | str | Unset): Name of a Microsoft 365 organization.
        repository_uid (None | Unset | UUID): UID assigned to a backup repository.
        repository_name (None | str | Unset): Name of a backup repository.
        proxy_uid (None | Unset | UUID): UID assigned to a backup proxy.
        proxy_name (None | str | Unset): Name of a backup proxy.
        last_run (datetime.datetime | None | Unset): Date and time when the latest backup job session started.
        last_run_duration_sec (int | None | Unset): Duration of the latest backup job session, in seconds.
        last_transferred_data_bytes (int | None | Unset): Size of tha data transferred during the latest backup job
            session, in bytes.
        processed_items (int | None | Unset): Number of processed items.
    """

    backup_job_uid: UUID | Unset = UNSET
    name: None | str | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    status: Vb365JobStatus | Unset = UNSET
    details: list[str] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    backup_type: Vb365BackupType | Unset = UNSET
    is_enabled: bool | Unset = UNSET
    organization_uid: None | Unset | UUID = UNSET
    organization_name: None | str | Unset = UNSET
    repository_uid: None | Unset | UUID = UNSET
    repository_name: None | str | Unset = UNSET
    proxy_uid: None | Unset | UUID = UNSET
    proxy_name: None | str | Unset = UNSET
    last_run: datetime.datetime | None | Unset = UNSET
    last_run_duration_sec: int | None | Unset = UNSET
    last_transferred_data_bytes: int | None | Unset = UNSET
    processed_items: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_job_uid: str | Unset = UNSET
        if not isinstance(self.backup_job_uid, Unset):
            backup_job_uid = str(self.backup_job_uid)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vb_365_server_id = self.vb_365_server_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: list[str] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        else:
            details = self.details

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        backup_type: str | Unset = UNSET
        if not isinstance(self.backup_type, Unset):
            backup_type = self.backup_type.value

        is_enabled = self.is_enabled

        organization_uid: None | str | Unset
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        organization_name: None | str | Unset
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        repository_uid: None | str | Unset
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        proxy_uid: None | str | Unset
        if isinstance(self.proxy_uid, Unset):
            proxy_uid = UNSET
        elif isinstance(self.proxy_uid, UUID):
            proxy_uid = str(self.proxy_uid)
        else:
            proxy_uid = self.proxy_uid

        proxy_name: None | str | Unset
        if isinstance(self.proxy_name, Unset):
            proxy_name = UNSET
        else:
            proxy_name = self.proxy_name

        last_run: None | str | Unset
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_run_duration_sec: int | None | Unset
        if isinstance(self.last_run_duration_sec, Unset):
            last_run_duration_sec = UNSET
        else:
            last_run_duration_sec = self.last_run_duration_sec

        last_transferred_data_bytes: int | None | Unset
        if isinstance(self.last_transferred_data_bytes, Unset):
            last_transferred_data_bytes = UNSET
        else:
            last_transferred_data_bytes = self.last_transferred_data_bytes

        processed_items: int | None | Unset
        if isinstance(self.processed_items, Unset):
            processed_items = UNSET
        else:
            processed_items = self.processed_items

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_job_uid is not UNSET:
            field_dict["backupJobUid"] = backup_job_uid
        if name is not UNSET:
            field_dict["name"] = name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if description is not UNSET:
            field_dict["description"] = description
        if backup_type is not UNSET:
            field_dict["backupType"] = backup_type
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
        if proxy_uid is not UNSET:
            field_dict["proxyUid"] = proxy_uid
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
        _backup_job_uid = d.pop("backupJobUid", UNSET)
        backup_job_uid: UUID | Unset
        if isinstance(_backup_job_uid, Unset):
            backup_job_uid = UNSET
        else:
            backup_job_uid = UUID(_backup_job_uid)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Vb365JobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365JobStatus(_status)

        def _parse_details(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _backup_type = d.pop("backupType", UNSET)
        backup_type: Vb365BackupType | Unset
        if isinstance(_backup_type, Unset):
            backup_type = UNSET
        else:
            backup_type = Vb365BackupType(_backup_type)

        is_enabled = d.pop("isEnabled", UNSET)

        def _parse_organization_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        def _parse_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        def _parse_repository_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        def _parse_proxy_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_uid_type_0 = UUID(data)

                return proxy_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_uid = _parse_proxy_uid(d.pop("proxyUid", UNSET))

        def _parse_proxy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        proxy_name = _parse_proxy_name(d.pop("proxyName", UNSET))

        def _parse_last_run(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = datetime.datetime.fromisoformat(data)

                return last_run_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        def _parse_last_run_duration_sec(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_run_duration_sec = _parse_last_run_duration_sec(d.pop("lastRunDurationSec", UNSET))

        def _parse_last_transferred_data_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_transferred_data_bytes = _parse_last_transferred_data_bytes(d.pop("lastTransferredDataBytes", UNSET))

        def _parse_processed_items(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        processed_items = _parse_processed_items(d.pop("processedItems", UNSET))

        vb_365_backup_job = cls(
            backup_job_uid=backup_job_uid,
            name=name,
            vb_365_server_id=vb_365_server_id,
            status=status,
            details=details,
            description=description,
            backup_type=backup_type,
            is_enabled=is_enabled,
            organization_uid=organization_uid,
            organization_name=organization_name,
            repository_uid=repository_uid,
            repository_name=repository_name,
            proxy_uid=proxy_uid,
            proxy_name=proxy_name,
            last_run=last_run,
            last_run_duration_sec=last_run_duration_sec,
            last_transferred_data_bytes=last_transferred_data_bytes,
            processed_items=processed_items,
        )

        return vb_365_backup_job
