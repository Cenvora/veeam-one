from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vm_platform import VmPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVmInfo")


@_attrs_define
class ProtectedVmInfo:
    """
    Attributes:
        vm_id (int | None | Unset): ID assigned to a protected VM.
        vm_uid_in_vbr (UUID | Unset): UID assigned to a protected VM in Veeam Backup & Replication.
        vm_id_in_hypervisor (None | str | Unset): MoRef ID or UID assigned to a protected VM by hypervisor.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server that manages VM protection.
        backup_server_name (None | str | Unset):
        name (None | str | Unset): Name of a protected VM.
        platform (VmPlatform | Unset):
        parent_host_name (None | str | Unset): Name of a parent host.
        ip_addresses (list[str] | None | Unset): IP addresses.
        used_source_size_bytes (int | None | Unset): Used space on protected VM disks, in bytes.
        provisioned_source_size_bytes (int | None | Unset): Total space on protected VM disks, in bytes.
        last_protected_date (datetime.datetime | None | Unset): Time and date of the latest restore point creation.
        job_uid (None | Unset | UUID): UID assigned to a job that created the latest restore point.
        job_name (None | str | Unset): Name of a job that created the latest restore point.
    """

    vm_id: int | None | Unset = UNSET
    vm_uid_in_vbr: UUID | Unset = UNSET
    vm_id_in_hypervisor: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    platform: VmPlatform | Unset = UNSET
    parent_host_name: None | str | Unset = UNSET
    ip_addresses: list[str] | None | Unset = UNSET
    used_source_size_bytes: int | None | Unset = UNSET
    provisioned_source_size_bytes: int | None | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vm_id: int | None | Unset
        if isinstance(self.vm_id, Unset):
            vm_id = UNSET
        else:
            vm_id = self.vm_id

        vm_uid_in_vbr: str | Unset = UNSET
        if not isinstance(self.vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = str(self.vm_uid_in_vbr)

        vm_id_in_hypervisor: None | str | Unset
        if isinstance(self.vm_id_in_hypervisor, Unset):
            vm_id_in_hypervisor = UNSET
        else:
            vm_id_in_hypervisor = self.vm_id_in_hypervisor

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        parent_host_name: None | str | Unset
        if isinstance(self.parent_host_name, Unset):
            parent_host_name = UNSET
        else:
            parent_host_name = self.parent_host_name

        ip_addresses: list[str] | None | Unset
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        used_source_size_bytes: int | None | Unset
        if isinstance(self.used_source_size_bytes, Unset):
            used_source_size_bytes = UNSET
        else:
            used_source_size_bytes = self.used_source_size_bytes

        provisioned_source_size_bytes: int | None | Unset
        if isinstance(self.provisioned_source_size_bytes, Unset):
            provisioned_source_size_bytes = UNSET
        else:
            provisioned_source_size_bytes = self.provisioned_source_size_bytes

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vm_id is not UNSET:
            field_dict["vmId"] = vm_id
        if vm_uid_in_vbr is not UNSET:
            field_dict["vmUidInVbr"] = vm_uid_in_vbr
        if vm_id_in_hypervisor is not UNSET:
            field_dict["vmIdInHypervisor"] = vm_id_in_hypervisor
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if parent_host_name is not UNSET:
            field_dict["parentHostName"] = parent_host_name
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if used_source_size_bytes is not UNSET:
            field_dict["usedSourceSizeBytes"] = used_source_size_bytes
        if provisioned_source_size_bytes is not UNSET:
            field_dict["provisionedSourceSizeBytes"] = provisioned_source_size_bytes
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_vm_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vm_id = _parse_vm_id(d.pop("vmId", UNSET))

        _vm_uid_in_vbr = d.pop("vmUidInVbr", UNSET)
        vm_uid_in_vbr: UUID | Unset
        if isinstance(_vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = UNSET
        else:
            vm_uid_in_vbr = UUID(_vm_uid_in_vbr)

        def _parse_vm_id_in_hypervisor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vm_id_in_hypervisor = _parse_vm_id_in_hypervisor(d.pop("vmIdInHypervisor", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: VmPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = VmPlatform(_platform)

        def _parse_parent_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_host_name = _parse_parent_host_name(d.pop("parentHostName", UNSET))

        def _parse_ip_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        def _parse_used_source_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_source_size_bytes = _parse_used_source_size_bytes(d.pop("usedSourceSizeBytes", UNSET))

        def _parse_provisioned_source_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        provisioned_source_size_bytes = _parse_provisioned_source_size_bytes(d.pop("provisionedSourceSizeBytes", UNSET))

        def _parse_last_protected_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protected_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

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

        protected_vm_info = cls(
            vm_id=vm_id,
            vm_uid_in_vbr=vm_uid_in_vbr,
            vm_id_in_hypervisor=vm_id_in_hypervisor,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            name=name,
            platform=platform,
            parent_host_name=parent_host_name,
            ip_addresses=ip_addresses,
            used_source_size_bytes=used_source_size_bytes,
            provisioned_source_size_bytes=provisioned_source_size_bytes,
            last_protected_date=last_protected_date,
            job_uid=job_uid,
            job_name=job_name,
        )

        return protected_vm_info
