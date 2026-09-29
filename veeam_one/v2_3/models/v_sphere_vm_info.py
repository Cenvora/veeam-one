from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.v_sphere_object_type import VSphereObjectType
from ..models.v_sphere_vm_connection_state import VSphereVmConnectionState
from ..models.v_sphere_vm_power_state import VSphereVmPowerState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vm_datastore_usage import VmDatastoreUsage
    from ..models.vm_guest_disk import VmGuestDisk
    from ..models.vm_virtual_disk import VmVirtualDisk


T = TypeVar("T", bound="VSphereVmInfo")


@_attrs_define
class VSphereVmInfo:
    """
    Attributes:
        vm_id (int | Unset): ID assigned to a VM.
        mo_ref (None | str | Unset): MoRef ID assigned to a VM in VMware vSphere.
        parent_id (int | None | Unset): ID assigned to a parent VM.
        parent_type (None | Unset | VSphereObjectType): Type of a parent VM.
        name (None | str | Unset): Name of a VM.
        power_state (VSphereVmPowerState | Unset):
        cpu_count (int | None | Unset): Number of virtual CPUs on a VM.
        guest_dns_name (None | str | Unset): DNS name of a VM.
        memory_size_mb (int | None | Unset): Amount of memory available on a VM.
        guest_disks (list[VmGuestDisk] | None | Unset): Array of guest disks configured in a VM.
        guest_ip_addresses (list[str] | None | Unset): Array of VM IP addresses.
        guest_os (None | str | Unset): Guest OS installed on a VM.
        is_replica (bool | None | Unset): Indicates whether a VM is a replica.
        virtual_disk_count (int | None | Unset): Number of virtual disks configured for a VM.
        virtual_disks (list[VmVirtualDisk] | None | Unset): Array of virtual disks configured for a VM.
        connection_state (VSphereVmConnectionState | Unset):
        notes (None | str | Unset): Additional information on a VM.
        total_disk_capacity_bytes (int | None | Unset): Total disk capacity, in bytes.
        datastore_usage (list[VmDatastoreUsage] | None | Unset): Usage of datastore resources allocated to a VM.
        is_cdp_replica (bool | None | Unset): Indicates whether a VM is a CDP replica.
        virtual_hardware_version (None | str | Unset): Version of VM virtual hardware.
        last_protected_date (datetime.datetime | None | Unset): Date and time of the latest successful VM job.
        vm_protection_job_uids (list[None | UUID] | None | Unset): Array of UIDs assigned to jobs that protect a VM.
        business_view_group_ids (list[int] | None | Unset): Array of Business View groups that a VM is a part of.
    """

    vm_id: int | Unset = UNSET
    mo_ref: None | str | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET
    name: None | str | Unset = UNSET
    power_state: VSphereVmPowerState | Unset = UNSET
    cpu_count: int | None | Unset = UNSET
    guest_dns_name: None | str | Unset = UNSET
    memory_size_mb: int | None | Unset = UNSET
    guest_disks: list[VmGuestDisk] | None | Unset = UNSET
    guest_ip_addresses: list[str] | None | Unset = UNSET
    guest_os: None | str | Unset = UNSET
    is_replica: bool | None | Unset = UNSET
    virtual_disk_count: int | None | Unset = UNSET
    virtual_disks: list[VmVirtualDisk] | None | Unset = UNSET
    connection_state: VSphereVmConnectionState | Unset = UNSET
    notes: None | str | Unset = UNSET
    total_disk_capacity_bytes: int | None | Unset = UNSET
    datastore_usage: list[VmDatastoreUsage] | None | Unset = UNSET
    is_cdp_replica: bool | None | Unset = UNSET
    virtual_hardware_version: None | str | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET
    vm_protection_job_uids: list[None | UUID] | None | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vm_id = self.vm_id

        mo_ref: None | str | Unset
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: None | str | Unset
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        power_state: str | Unset = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        cpu_count: int | None | Unset
        if isinstance(self.cpu_count, Unset):
            cpu_count = UNSET
        else:
            cpu_count = self.cpu_count

        guest_dns_name: None | str | Unset
        if isinstance(self.guest_dns_name, Unset):
            guest_dns_name = UNSET
        else:
            guest_dns_name = self.guest_dns_name

        memory_size_mb: int | None | Unset
        if isinstance(self.memory_size_mb, Unset):
            memory_size_mb = UNSET
        else:
            memory_size_mb = self.memory_size_mb

        guest_disks: list[dict[str, Any]] | None | Unset
        if isinstance(self.guest_disks, Unset):
            guest_disks = UNSET
        elif isinstance(self.guest_disks, list):
            guest_disks = []
            for guest_disks_type_0_item_data in self.guest_disks:
                guest_disks_type_0_item = guest_disks_type_0_item_data.to_dict()
                guest_disks.append(guest_disks_type_0_item)

        else:
            guest_disks = self.guest_disks

        guest_ip_addresses: list[str] | None | Unset
        if isinstance(self.guest_ip_addresses, Unset):
            guest_ip_addresses = UNSET
        elif isinstance(self.guest_ip_addresses, list):
            guest_ip_addresses = self.guest_ip_addresses

        else:
            guest_ip_addresses = self.guest_ip_addresses

        guest_os: None | str | Unset
        if isinstance(self.guest_os, Unset):
            guest_os = UNSET
        else:
            guest_os = self.guest_os

        is_replica: bool | None | Unset
        if isinstance(self.is_replica, Unset):
            is_replica = UNSET
        else:
            is_replica = self.is_replica

        virtual_disk_count: int | None | Unset
        if isinstance(self.virtual_disk_count, Unset):
            virtual_disk_count = UNSET
        else:
            virtual_disk_count = self.virtual_disk_count

        virtual_disks: list[dict[str, Any]] | None | Unset
        if isinstance(self.virtual_disks, Unset):
            virtual_disks = UNSET
        elif isinstance(self.virtual_disks, list):
            virtual_disks = []
            for virtual_disks_type_0_item_data in self.virtual_disks:
                virtual_disks_type_0_item = virtual_disks_type_0_item_data.to_dict()
                virtual_disks.append(virtual_disks_type_0_item)

        else:
            virtual_disks = self.virtual_disks

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        total_disk_capacity_bytes: int | None | Unset
        if isinstance(self.total_disk_capacity_bytes, Unset):
            total_disk_capacity_bytes = UNSET
        else:
            total_disk_capacity_bytes = self.total_disk_capacity_bytes

        datastore_usage: list[dict[str, Any]] | None | Unset
        if isinstance(self.datastore_usage, Unset):
            datastore_usage = UNSET
        elif isinstance(self.datastore_usage, list):
            datastore_usage = []
            for datastore_usage_type_0_item_data in self.datastore_usage:
                datastore_usage_type_0_item = datastore_usage_type_0_item_data.to_dict()
                datastore_usage.append(datastore_usage_type_0_item)

        else:
            datastore_usage = self.datastore_usage

        is_cdp_replica: bool | None | Unset
        if isinstance(self.is_cdp_replica, Unset):
            is_cdp_replica = UNSET
        else:
            is_cdp_replica = self.is_cdp_replica

        virtual_hardware_version: None | str | Unset
        if isinstance(self.virtual_hardware_version, Unset):
            virtual_hardware_version = UNSET
        else:
            virtual_hardware_version = self.virtual_hardware_version

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        vm_protection_job_uids: list[None | str] | None | Unset
        if isinstance(self.vm_protection_job_uids, Unset):
            vm_protection_job_uids = UNSET
        elif isinstance(self.vm_protection_job_uids, list):
            vm_protection_job_uids = []
            for vm_protection_job_uids_type_0_item_data in self.vm_protection_job_uids:
                vm_protection_job_uids_type_0_item: None | str
                if isinstance(vm_protection_job_uids_type_0_item_data, UUID):
                    vm_protection_job_uids_type_0_item = str(vm_protection_job_uids_type_0_item_data)
                else:
                    vm_protection_job_uids_type_0_item = vm_protection_job_uids_type_0_item_data
                vm_protection_job_uids.append(vm_protection_job_uids_type_0_item)

        else:
            vm_protection_job_uids = self.vm_protection_job_uids

        business_view_group_ids: list[int] | None | Unset
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vm_id is not UNSET:
            field_dict["vmId"] = vm_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if name is not UNSET:
            field_dict["name"] = name
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if cpu_count is not UNSET:
            field_dict["cpuCount"] = cpu_count
        if guest_dns_name is not UNSET:
            field_dict["guestDnsName"] = guest_dns_name
        if memory_size_mb is not UNSET:
            field_dict["memorySizeMb"] = memory_size_mb
        if guest_disks is not UNSET:
            field_dict["guestDisks"] = guest_disks
        if guest_ip_addresses is not UNSET:
            field_dict["guestIpAddresses"] = guest_ip_addresses
        if guest_os is not UNSET:
            field_dict["guestOs"] = guest_os
        if is_replica is not UNSET:
            field_dict["isReplica"] = is_replica
        if virtual_disk_count is not UNSET:
            field_dict["virtualDiskCount"] = virtual_disk_count
        if virtual_disks is not UNSET:
            field_dict["virtualDisks"] = virtual_disks
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if notes is not UNSET:
            field_dict["notes"] = notes
        if total_disk_capacity_bytes is not UNSET:
            field_dict["totalDiskCapacityBytes"] = total_disk_capacity_bytes
        if datastore_usage is not UNSET:
            field_dict["datastoreUsage"] = datastore_usage
        if is_cdp_replica is not UNSET:
            field_dict["isCdpReplica"] = is_cdp_replica
        if virtual_hardware_version is not UNSET:
            field_dict["virtualHardwareVersion"] = virtual_hardware_version
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if vm_protection_job_uids is not UNSET:
            field_dict["vmProtectionJobUids"] = vm_protection_job_uids
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vm_datastore_usage import VmDatastoreUsage  # noqa: PLC0415
        from ..models.vm_guest_disk import VmGuestDisk  # noqa: PLC0415
        from ..models.vm_virtual_disk import VmVirtualDisk  # noqa: PLC0415

        d = dict(src_dict)
        vm_id = d.pop("vmId", UNSET)

        def _parse_mo_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_type(data: object) -> None | Unset | VSphereObjectType:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VSphereObjectType, data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _power_state = d.pop("powerState", UNSET)
        power_state: VSphereVmPowerState | Unset
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = VSphereVmPowerState(_power_state)

        def _parse_cpu_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_count = _parse_cpu_count(d.pop("cpuCount", UNSET))

        def _parse_guest_dns_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_dns_name = _parse_guest_dns_name(d.pop("guestDnsName", UNSET))

        def _parse_memory_size_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_size_mb = _parse_memory_size_mb(d.pop("memorySizeMb", UNSET))

        def _parse_guest_disks(data: object) -> list[VmGuestDisk] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guest_disks_type_0 = []
                _guest_disks_type_0 = data
                for guest_disks_type_0_item_data in _guest_disks_type_0:
                    guest_disks_type_0_item = VmGuestDisk.from_dict(guest_disks_type_0_item_data)

                    guest_disks_type_0.append(guest_disks_type_0_item)

                return guest_disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VmGuestDisk] | None | Unset, data)

        guest_disks = _parse_guest_disks(d.pop("guestDisks", UNSET))

        def _parse_guest_ip_addresses(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guest_ip_addresses_type_0 = cast(list[str], data)

                return guest_ip_addresses_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        guest_ip_addresses = _parse_guest_ip_addresses(d.pop("guestIpAddresses", UNSET))

        def _parse_guest_os(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_os = _parse_guest_os(d.pop("guestOs", UNSET))

        def _parse_is_replica(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_replica = _parse_is_replica(d.pop("isReplica", UNSET))

        def _parse_virtual_disk_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        virtual_disk_count = _parse_virtual_disk_count(d.pop("virtualDiskCount", UNSET))

        def _parse_virtual_disks(data: object) -> list[VmVirtualDisk] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                virtual_disks_type_0 = []
                _virtual_disks_type_0 = data
                for virtual_disks_type_0_item_data in _virtual_disks_type_0:
                    virtual_disks_type_0_item = VmVirtualDisk.from_dict(virtual_disks_type_0_item_data)

                    virtual_disks_type_0.append(virtual_disks_type_0_item)

                return virtual_disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VmVirtualDisk] | None | Unset, data)

        virtual_disks = _parse_virtual_disks(d.pop("virtualDisks", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: VSphereVmConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = VSphereVmConnectionState(_connection_state)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_total_disk_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_disk_capacity_bytes = _parse_total_disk_capacity_bytes(d.pop("totalDiskCapacityBytes", UNSET))

        def _parse_datastore_usage(data: object) -> list[VmDatastoreUsage] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                datastore_usage_type_0 = []
                _datastore_usage_type_0 = data
                for datastore_usage_type_0_item_data in _datastore_usage_type_0:
                    datastore_usage_type_0_item = VmDatastoreUsage.from_dict(datastore_usage_type_0_item_data)

                    datastore_usage_type_0.append(datastore_usage_type_0_item)

                return datastore_usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VmDatastoreUsage] | None | Unset, data)

        datastore_usage = _parse_datastore_usage(d.pop("datastoreUsage", UNSET))

        def _parse_is_cdp_replica(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cdp_replica = _parse_is_cdp_replica(d.pop("isCdpReplica", UNSET))

        def _parse_virtual_hardware_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        virtual_hardware_version = _parse_virtual_hardware_version(d.pop("virtualHardwareVersion", UNSET))

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

        def _parse_vm_protection_job_uids(data: object) -> list[None | UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                vm_protection_job_uids_type_0 = []
                _vm_protection_job_uids_type_0 = data
                for vm_protection_job_uids_type_0_item_data in _vm_protection_job_uids_type_0:

                    def _parse_vm_protection_job_uids_type_0_item(data: object) -> None | UUID:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, str):
                                raise TypeError()
                            vm_protection_job_uids_type_0_item_type_0 = UUID(data)

                            return vm_protection_job_uids_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | UUID, data)

                    vm_protection_job_uids_type_0_item = _parse_vm_protection_job_uids_type_0_item(
                        vm_protection_job_uids_type_0_item_data
                    )

                    vm_protection_job_uids_type_0.append(vm_protection_job_uids_type_0_item)

                return vm_protection_job_uids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | UUID] | None | Unset, data)

        vm_protection_job_uids = _parse_vm_protection_job_uids(d.pop("vmProtectionJobUids", UNSET))

        def _parse_business_view_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        v_sphere_vm_info = cls(
            vm_id=vm_id,
            mo_ref=mo_ref,
            parent_id=parent_id,
            parent_type=parent_type,
            name=name,
            power_state=power_state,
            cpu_count=cpu_count,
            guest_dns_name=guest_dns_name,
            memory_size_mb=memory_size_mb,
            guest_disks=guest_disks,
            guest_ip_addresses=guest_ip_addresses,
            guest_os=guest_os,
            is_replica=is_replica,
            virtual_disk_count=virtual_disk_count,
            virtual_disks=virtual_disks,
            connection_state=connection_state,
            notes=notes,
            total_disk_capacity_bytes=total_disk_capacity_bytes,
            datastore_usage=datastore_usage,
            is_cdp_replica=is_cdp_replica,
            virtual_hardware_version=virtual_hardware_version,
            last_protected_date=last_protected_date,
            vm_protection_job_uids=vm_protection_job_uids,
            business_view_group_ids=business_view_group_ids,
        )

        return v_sphere_vm_info
