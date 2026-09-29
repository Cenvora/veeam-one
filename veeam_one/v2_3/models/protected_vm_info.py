import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vm_platform import VmPlatform
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedVmInfo")


@_attrs_define
class ProtectedVmInfo:
    """
    Attributes:
        vm_id (Union[None, Unset, int]): ID assigned to a protected VM.
        vm_uid_in_vbr (Union[Unset, UUID]): UID assigned to a protected VM in Veeam Backup & Replication.
        vm_id_in_hypervisor (Union[None, Unset, str]): MoRef ID or UID assigned to a protected VM by hypervisor.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server that manages VM
            protection.
        backup_server_name (Union[None, Unset, str]):
        name (Union[None, Unset, str]): Name of a protected VM.
        platform (Union[Unset, VmPlatform]):
        parent_host_name (Union[None, Unset, str]): Name of a parent host.
        ip_addresses (Union[None, Unset, list[str]]): IP addresses.
        used_source_size_bytes (Union[None, Unset, int]): Used space on protected VM disks, in bytes.
        provisioned_source_size_bytes (Union[None, Unset, int]): Total space on protected VM disks, in bytes.
        last_protected_date (Union[None, Unset, datetime.datetime]): Time and date of the latest restore point creation.
        job_uid (Union[None, UUID, Unset]): UID assigned to a job that created the latest restore point.
        job_name (Union[None, Unset, str]): Name of a job that created the latest restore point.
    """

    vm_id: Union[None, Unset, int] = UNSET
    vm_uid_in_vbr: Union[Unset, UUID] = UNSET
    vm_id_in_hypervisor: Union[None, Unset, str] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    platform: Union[Unset, VmPlatform] = UNSET
    parent_host_name: Union[None, Unset, str] = UNSET
    ip_addresses: Union[None, Unset, list[str]] = UNSET
    used_source_size_bytes: Union[None, Unset, int] = UNSET
    provisioned_source_size_bytes: Union[None, Unset, int] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        vm_id: Union[None, Unset, int]
        if isinstance(self.vm_id, Unset):
            vm_id = UNSET
        else:
            vm_id = self.vm_id

        vm_uid_in_vbr: Union[Unset, str] = UNSET
        if not isinstance(self.vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = str(self.vm_uid_in_vbr)

        vm_id_in_hypervisor: Union[None, Unset, str]
        if isinstance(self.vm_id_in_hypervisor, Unset):
            vm_id_in_hypervisor = UNSET
        else:
            vm_id_in_hypervisor = self.vm_id_in_hypervisor

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        parent_host_name: Union[None, Unset, str]
        if isinstance(self.parent_host_name, Unset):
            parent_host_name = UNSET
        else:
            parent_host_name = self.parent_host_name

        ip_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        used_source_size_bytes: Union[None, Unset, int]
        if isinstance(self.used_source_size_bytes, Unset):
            used_source_size_bytes = UNSET
        else:
            used_source_size_bytes = self.used_source_size_bytes

        provisioned_source_size_bytes: Union[None, Unset, int]
        if isinstance(self.provisioned_source_size_bytes, Unset):
            provisioned_source_size_bytes = UNSET
        else:
            provisioned_source_size_bytes = self.provisioned_source_size_bytes

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        job_name: Union[None, Unset, str]
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

        def _parse_vm_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vm_id = _parse_vm_id(d.pop("vmId", UNSET))

        _vm_uid_in_vbr = d.pop("vmUidInVbr", UNSET)
        vm_uid_in_vbr: Union[Unset, UUID]
        if isinstance(_vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = UNSET
        else:
            vm_uid_in_vbr = UUID(_vm_uid_in_vbr)

        def _parse_vm_id_in_hypervisor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vm_id_in_hypervisor = _parse_vm_id_in_hypervisor(d.pop("vmIdInHypervisor", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, VmPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = VmPlatform(_platform)

        def _parse_parent_host_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_host_name = _parse_parent_host_name(d.pop("parentHostName", UNSET))

        def _parse_ip_addresses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        def _parse_used_source_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_source_size_bytes = _parse_used_source_size_bytes(d.pop("usedSourceSizeBytes", UNSET))

        def _parse_provisioned_source_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        provisioned_source_size_bytes = _parse_provisioned_source_size_bytes(d.pop("provisionedSourceSizeBytes", UNSET))

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

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_job_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
