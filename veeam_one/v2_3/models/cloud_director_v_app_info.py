from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.v_app_power_state import VAppPowerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDirectorVAppInfo")


@_attrs_define
class CloudDirectorVAppInfo:
    """
    Attributes:
        v_app_id (int | Unset): ID assigned to a vApp.
        href (None | str | Unset): Unique vApp identifier in the URL format. Identical to the `href` property in VMware
            Cloud Director API.
        name (None | str | Unset): Name of a vApp.
        cpu_allocation_mhz (int | None | Unset): Amount of allocated CPU, in MHz.
        memory_allocation_mb (int | None | Unset): Amount of allocated memory, in MB.
        storage_kb (int | None | Unset): Amount of storage capacity, in kB.
        lease_expiration_date (datetime.datetime | None | Unset): Date and time when a vApp must be deleted
            automaticaly.
        power_state (VAppPowerState | Unset):
        is_expired (bool | None | Unset): Indicates whether the vApp lease has expired.
        auto_undeploy_time (datetime.datetime | None | Unset): Date and time when a vApp must be undeployed.
        cloud_director_id (int | None | Unset): ID assigned to a VMware Cloud Director.
        organization_id (int | None | Unset): ID assigned to an organization.
        organization_vdc_id (int | None | Unset): ID assigned to an organization VDC.
    """

    v_app_id: int | Unset = UNSET
    href: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    cpu_allocation_mhz: int | None | Unset = UNSET
    memory_allocation_mb: int | None | Unset = UNSET
    storage_kb: int | None | Unset = UNSET
    lease_expiration_date: datetime.datetime | None | Unset = UNSET
    power_state: VAppPowerState | Unset = UNSET
    is_expired: bool | None | Unset = UNSET
    auto_undeploy_time: datetime.datetime | None | Unset = UNSET
    cloud_director_id: int | None | Unset = UNSET
    organization_id: int | None | Unset = UNSET
    organization_vdc_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        v_app_id = self.v_app_id

        href: None | str | Unset
        if isinstance(self.href, Unset):
            href = UNSET
        else:
            href = self.href

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cpu_allocation_mhz: int | None | Unset
        if isinstance(self.cpu_allocation_mhz, Unset):
            cpu_allocation_mhz = UNSET
        else:
            cpu_allocation_mhz = self.cpu_allocation_mhz

        memory_allocation_mb: int | None | Unset
        if isinstance(self.memory_allocation_mb, Unset):
            memory_allocation_mb = UNSET
        else:
            memory_allocation_mb = self.memory_allocation_mb

        storage_kb: int | None | Unset
        if isinstance(self.storage_kb, Unset):
            storage_kb = UNSET
        else:
            storage_kb = self.storage_kb

        lease_expiration_date: None | str | Unset
        if isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        elif isinstance(self.lease_expiration_date, datetime.datetime):
            lease_expiration_date = self.lease_expiration_date.isoformat()
        else:
            lease_expiration_date = self.lease_expiration_date

        power_state: str | Unset = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        is_expired: bool | None | Unset
        if isinstance(self.is_expired, Unset):
            is_expired = UNSET
        else:
            is_expired = self.is_expired

        auto_undeploy_time: None | str | Unset
        if isinstance(self.auto_undeploy_time, Unset):
            auto_undeploy_time = UNSET
        elif isinstance(self.auto_undeploy_time, datetime.datetime):
            auto_undeploy_time = self.auto_undeploy_time.isoformat()
        else:
            auto_undeploy_time = self.auto_undeploy_time

        cloud_director_id: int | None | Unset
        if isinstance(self.cloud_director_id, Unset):
            cloud_director_id = UNSET
        else:
            cloud_director_id = self.cloud_director_id

        organization_id: int | None | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        organization_vdc_id: int | None | Unset
        if isinstance(self.organization_vdc_id, Unset):
            organization_vdc_id = UNSET
        else:
            organization_vdc_id = self.organization_vdc_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if v_app_id is not UNSET:
            field_dict["vAppId"] = v_app_id
        if href is not UNSET:
            field_dict["href"] = href
        if name is not UNSET:
            field_dict["name"] = name
        if cpu_allocation_mhz is not UNSET:
            field_dict["cpuAllocationMhz"] = cpu_allocation_mhz
        if memory_allocation_mb is not UNSET:
            field_dict["memoryAllocationMb"] = memory_allocation_mb
        if storage_kb is not UNSET:
            field_dict["storageKb"] = storage_kb
        if lease_expiration_date is not UNSET:
            field_dict["leaseExpirationDate"] = lease_expiration_date
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if is_expired is not UNSET:
            field_dict["isExpired"] = is_expired
        if auto_undeploy_time is not UNSET:
            field_dict["autoUndeployTime"] = auto_undeploy_time
        if cloud_director_id is not UNSET:
            field_dict["cloudDirectorId"] = cloud_director_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization_vdc_id is not UNSET:
            field_dict["organizationVdcId"] = organization_vdc_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v_app_id = d.pop("vAppId", UNSET)

        def _parse_href(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        href = _parse_href(d.pop("href", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_cpu_allocation_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_allocation_mhz = _parse_cpu_allocation_mhz(d.pop("cpuAllocationMhz", UNSET))

        def _parse_memory_allocation_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_allocation_mb = _parse_memory_allocation_mb(d.pop("memoryAllocationMb", UNSET))

        def _parse_storage_kb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_kb = _parse_storage_kb(d.pop("storageKb", UNSET))

        def _parse_lease_expiration_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_expiration_date_type_0 = datetime.datetime.fromisoformat(data)

                return lease_expiration_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        lease_expiration_date = _parse_lease_expiration_date(d.pop("leaseExpirationDate", UNSET))

        _power_state = d.pop("powerState", UNSET)
        power_state: VAppPowerState | Unset
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = VAppPowerState(_power_state)

        def _parse_is_expired(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_expired = _parse_is_expired(d.pop("isExpired", UNSET))

        def _parse_auto_undeploy_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auto_undeploy_time_type_0 = datetime.datetime.fromisoformat(data)

                return auto_undeploy_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        auto_undeploy_time = _parse_auto_undeploy_time(d.pop("autoUndeployTime", UNSET))

        def _parse_cloud_director_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_director_id = _parse_cloud_director_id(d.pop("cloudDirectorId", UNSET))

        def _parse_organization_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        def _parse_organization_vdc_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        organization_vdc_id = _parse_organization_vdc_id(d.pop("organizationVdcId", UNSET))

        cloud_director_v_app_info = cls(
            v_app_id=v_app_id,
            href=href,
            name=name,
            cpu_allocation_mhz=cpu_allocation_mhz,
            memory_allocation_mb=memory_allocation_mb,
            storage_kb=storage_kb,
            lease_expiration_date=lease_expiration_date,
            power_state=power_state,
            is_expired=is_expired,
            auto_undeploy_time=auto_undeploy_time,
            cloud_director_id=cloud_director_id,
            organization_id=organization_id,
            organization_vdc_id=organization_vdc_id,
        )

        return cloud_director_v_app_info
