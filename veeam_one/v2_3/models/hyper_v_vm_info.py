from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.hyper_v_vm_power_state import HyperVVmPowerState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hyper_v_integration_service import HyperVIntegrationService
    from ..models.vm_guest_disk import VmGuestDisk


T = TypeVar("T", bound="HyperVVmInfo")


@_attrs_define
class HyperVVmInfo:
    """
    Attributes:
        vm_id (int | Unset): ID assigned to a VM.
        guid (None | str | Unset): Identifier assigned to a VM in Microsoft Hyper-V.
        name (None | str | Unset): Name of a VM.
        power_state (HyperVVmPowerState | Unset):
        cpu_count (int | None | Unset): Number of virtual CPUs on a VM.
        total_datastore_committed_bytes (int | None | Unset): Datastore storage space that is used by a VM, in bytes.
        total_datastore_uncommited_bytes (int | None | Unset): Datastore storage space that can be used by a VM, in
            bytes.
        guest_disks (list[VmGuestDisk] | None | Unset): Array of guest disks configured in a VM.
        ip_addresses (list[str] | None | Unset): Array of VM IP addresses.
        guest_os (None | str | Unset): Guest OS installed on a VM.
        is_replica (bool | None | Unset): Indicates whether a VM is a replica.
        snapshot_folder (None | str | Unset): Path to a folder that contains VM snapshots.
        creation_time (datetime.datetime | None | Unset): Date and time when a VM was created.
        host_id (int | None | Unset): ID assigned to a host on which a VM resides.
        dns_name (None | str | Unset): DNS name of VM.
        dynamic_memory_enabled (bool | None | Unset): Indicates whether Dynamic Memory is configured for a VM.
        assigned_memory_mb (int | None | Unset): Amount of memory currently available to a VM, in MB.
        uptime_ms (int | None | Unset): VM uptime, in milliseconds.
        vm_assigned_memory_mb (int | None | Unset): Amount of memory allocated to a VM.
        integration_services (list[HyperVIntegrationService] | None | Unset): Array of integration services.
        cpu_mhz (int | None | Unset): CPU resource of a VM, in MHz.
        memory_reservation_mb (int | None | Unset): Memory reservation configured for a VM, in MB.
        memory_limit_mb (int | None | Unset): Maximum amount of memory resources that can be allocated to a VM, in MB.
        is_shielded (bool | None | Unset): Indicates whether a VM is shielded.
        last_protected_date (datetime.datetime | None | Unset): Date and time when the latest backup was created for a
            VM.
        business_view_group_ids (list[int] | None | Unset): Array of Business View groups.
    """

    vm_id: int | Unset = UNSET
    guid: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    power_state: HyperVVmPowerState | Unset = UNSET
    cpu_count: int | None | Unset = UNSET
    total_datastore_committed_bytes: int | None | Unset = UNSET
    total_datastore_uncommited_bytes: int | None | Unset = UNSET
    guest_disks: list[VmGuestDisk] | None | Unset = UNSET
    ip_addresses: list[str] | None | Unset = UNSET
    guest_os: None | str | Unset = UNSET
    is_replica: bool | None | Unset = UNSET
    snapshot_folder: None | str | Unset = UNSET
    creation_time: datetime.datetime | None | Unset = UNSET
    host_id: int | None | Unset = UNSET
    dns_name: None | str | Unset = UNSET
    dynamic_memory_enabled: bool | None | Unset = UNSET
    assigned_memory_mb: int | None | Unset = UNSET
    uptime_ms: int | None | Unset = UNSET
    vm_assigned_memory_mb: int | None | Unset = UNSET
    integration_services: list[HyperVIntegrationService] | None | Unset = UNSET
    cpu_mhz: int | None | Unset = UNSET
    memory_reservation_mb: int | None | Unset = UNSET
    memory_limit_mb: int | None | Unset = UNSET
    is_shielded: bool | None | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vm_id = self.vm_id

        guid: None | str | Unset
        if isinstance(self.guid, Unset):
            guid = UNSET
        else:
            guid = self.guid

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

        total_datastore_committed_bytes: int | None | Unset
        if isinstance(self.total_datastore_committed_bytes, Unset):
            total_datastore_committed_bytes = UNSET
        else:
            total_datastore_committed_bytes = self.total_datastore_committed_bytes

        total_datastore_uncommited_bytes: int | None | Unset
        if isinstance(self.total_datastore_uncommited_bytes, Unset):
            total_datastore_uncommited_bytes = UNSET
        else:
            total_datastore_uncommited_bytes = self.total_datastore_uncommited_bytes

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

        ip_addresses: list[str] | None | Unset
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

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

        snapshot_folder: None | str | Unset
        if isinstance(self.snapshot_folder, Unset):
            snapshot_folder = UNSET
        else:
            snapshot_folder = self.snapshot_folder

        creation_time: None | str | Unset
        if isinstance(self.creation_time, Unset):
            creation_time = UNSET
        elif isinstance(self.creation_time, datetime.datetime):
            creation_time = self.creation_time.isoformat()
        else:
            creation_time = self.creation_time

        host_id: int | None | Unset
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        dns_name: None | str | Unset
        if isinstance(self.dns_name, Unset):
            dns_name = UNSET
        else:
            dns_name = self.dns_name

        dynamic_memory_enabled: bool | None | Unset
        if isinstance(self.dynamic_memory_enabled, Unset):
            dynamic_memory_enabled = UNSET
        else:
            dynamic_memory_enabled = self.dynamic_memory_enabled

        assigned_memory_mb: int | None | Unset
        if isinstance(self.assigned_memory_mb, Unset):
            assigned_memory_mb = UNSET
        else:
            assigned_memory_mb = self.assigned_memory_mb

        uptime_ms: int | None | Unset
        if isinstance(self.uptime_ms, Unset):
            uptime_ms = UNSET
        else:
            uptime_ms = self.uptime_ms

        vm_assigned_memory_mb: int | None | Unset
        if isinstance(self.vm_assigned_memory_mb, Unset):
            vm_assigned_memory_mb = UNSET
        else:
            vm_assigned_memory_mb = self.vm_assigned_memory_mb

        integration_services: list[dict[str, Any]] | None | Unset
        if isinstance(self.integration_services, Unset):
            integration_services = UNSET
        elif isinstance(self.integration_services, list):
            integration_services = []
            for integration_services_type_0_item_data in self.integration_services:
                integration_services_type_0_item = integration_services_type_0_item_data.to_dict()
                integration_services.append(integration_services_type_0_item)

        else:
            integration_services = self.integration_services

        cpu_mhz: int | None | Unset
        if isinstance(self.cpu_mhz, Unset):
            cpu_mhz = UNSET
        else:
            cpu_mhz = self.cpu_mhz

        memory_reservation_mb: int | None | Unset
        if isinstance(self.memory_reservation_mb, Unset):
            memory_reservation_mb = UNSET
        else:
            memory_reservation_mb = self.memory_reservation_mb

        memory_limit_mb: int | None | Unset
        if isinstance(self.memory_limit_mb, Unset):
            memory_limit_mb = UNSET
        else:
            memory_limit_mb = self.memory_limit_mb

        is_shielded: bool | None | Unset
        if isinstance(self.is_shielded, Unset):
            is_shielded = UNSET
        else:
            is_shielded = self.is_shielded

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

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
        if guid is not UNSET:
            field_dict["guid"] = guid
        if name is not UNSET:
            field_dict["name"] = name
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if cpu_count is not UNSET:
            field_dict["cpuCount"] = cpu_count
        if total_datastore_committed_bytes is not UNSET:
            field_dict["totalDatastoreCommittedBytes"] = total_datastore_committed_bytes
        if total_datastore_uncommited_bytes is not UNSET:
            field_dict["totalDatastoreUncommitedBytes"] = total_datastore_uncommited_bytes
        if guest_disks is not UNSET:
            field_dict["guestDisks"] = guest_disks
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if guest_os is not UNSET:
            field_dict["guestOs"] = guest_os
        if is_replica is not UNSET:
            field_dict["isReplica"] = is_replica
        if snapshot_folder is not UNSET:
            field_dict["snapshotFolder"] = snapshot_folder
        if creation_time is not UNSET:
            field_dict["creationTime"] = creation_time
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if dns_name is not UNSET:
            field_dict["dnsName"] = dns_name
        if dynamic_memory_enabled is not UNSET:
            field_dict["dynamicMemoryEnabled"] = dynamic_memory_enabled
        if assigned_memory_mb is not UNSET:
            field_dict["assignedMemoryMb"] = assigned_memory_mb
        if uptime_ms is not UNSET:
            field_dict["uptimeMs"] = uptime_ms
        if vm_assigned_memory_mb is not UNSET:
            field_dict["vmAssignedMemoryMb"] = vm_assigned_memory_mb
        if integration_services is not UNSET:
            field_dict["integrationServices"] = integration_services
        if cpu_mhz is not UNSET:
            field_dict["cpuMhz"] = cpu_mhz
        if memory_reservation_mb is not UNSET:
            field_dict["memoryReservationMb"] = memory_reservation_mb
        if memory_limit_mb is not UNSET:
            field_dict["memoryLimitMb"] = memory_limit_mb
        if is_shielded is not UNSET:
            field_dict["isShielded"] = is_shielded
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hyper_v_integration_service import HyperVIntegrationService  # noqa: PLC0415
        from ..models.vm_guest_disk import VmGuestDisk  # noqa: PLC0415

        d = dict(src_dict)
        vm_id = d.pop("vmId", UNSET)

        def _parse_guid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guid = _parse_guid(d.pop("guid", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _power_state = d.pop("powerState", UNSET)
        power_state: HyperVVmPowerState | Unset
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = HyperVVmPowerState(_power_state)

        def _parse_cpu_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_count = _parse_cpu_count(d.pop("cpuCount", UNSET))

        def _parse_total_datastore_committed_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_datastore_committed_bytes = _parse_total_datastore_committed_bytes(
            d.pop("totalDatastoreCommittedBytes", UNSET)
        )

        def _parse_total_datastore_uncommited_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_datastore_uncommited_bytes = _parse_total_datastore_uncommited_bytes(
            d.pop("totalDatastoreUncommitedBytes", UNSET)
        )

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

        def _parse_snapshot_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        snapshot_folder = _parse_snapshot_folder(d.pop("snapshotFolder", UNSET))

        def _parse_creation_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_time_type_0 = datetime.datetime.fromisoformat(data)

                return creation_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        creation_time = _parse_creation_time(d.pop("creationTime", UNSET))

        def _parse_host_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        host_id = _parse_host_id(d.pop("hostId", UNSET))

        def _parse_dns_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dns_name = _parse_dns_name(d.pop("dnsName", UNSET))

        def _parse_dynamic_memory_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        dynamic_memory_enabled = _parse_dynamic_memory_enabled(d.pop("dynamicMemoryEnabled", UNSET))

        def _parse_assigned_memory_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        assigned_memory_mb = _parse_assigned_memory_mb(d.pop("assignedMemoryMb", UNSET))

        def _parse_uptime_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        uptime_ms = _parse_uptime_ms(d.pop("uptimeMs", UNSET))

        def _parse_vm_assigned_memory_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vm_assigned_memory_mb = _parse_vm_assigned_memory_mb(d.pop("vmAssignedMemoryMb", UNSET))

        def _parse_integration_services(data: object) -> list[HyperVIntegrationService] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                integration_services_type_0 = []
                _integration_services_type_0 = data
                for integration_services_type_0_item_data in _integration_services_type_0:
                    integration_services_type_0_item = HyperVIntegrationService.from_dict(
                        integration_services_type_0_item_data
                    )

                    integration_services_type_0.append(integration_services_type_0_item)

                return integration_services_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HyperVIntegrationService] | None | Unset, data)

        integration_services = _parse_integration_services(d.pop("integrationServices", UNSET))

        def _parse_cpu_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_mhz = _parse_cpu_mhz(d.pop("cpuMhz", UNSET))

        def _parse_memory_reservation_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_reservation_mb = _parse_memory_reservation_mb(d.pop("memoryReservationMb", UNSET))

        def _parse_memory_limit_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_limit_mb = _parse_memory_limit_mb(d.pop("memoryLimitMb", UNSET))

        def _parse_is_shielded(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_shielded = _parse_is_shielded(d.pop("isShielded", UNSET))

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

        hyper_v_vm_info = cls(
            vm_id=vm_id,
            guid=guid,
            name=name,
            power_state=power_state,
            cpu_count=cpu_count,
            total_datastore_committed_bytes=total_datastore_committed_bytes,
            total_datastore_uncommited_bytes=total_datastore_uncommited_bytes,
            guest_disks=guest_disks,
            ip_addresses=ip_addresses,
            guest_os=guest_os,
            is_replica=is_replica,
            snapshot_folder=snapshot_folder,
            creation_time=creation_time,
            host_id=host_id,
            dns_name=dns_name,
            dynamic_memory_enabled=dynamic_memory_enabled,
            assigned_memory_mb=assigned_memory_mb,
            uptime_ms=uptime_ms,
            vm_assigned_memory_mb=vm_assigned_memory_mb,
            integration_services=integration_services,
            cpu_mhz=cpu_mhz,
            memory_reservation_mb=memory_reservation_mb,
            memory_limit_mb=memory_limit_mb,
            is_shielded=is_shielded,
            last_protected_date=last_protected_date,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_vm_info
