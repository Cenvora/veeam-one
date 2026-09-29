import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.v_app_power_state import VAppPowerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDirectorVAppInfo")


@_attrs_define
class CloudDirectorVAppInfo:
    """
    Attributes:
        v_app_id (Union[Unset, int]): ID assigned to a vApp.
        href (Union[None, Unset, str]): Unique vApp identifier in the URL format. Identical to the `href` property in
            VMware Cloud Director API.
        name (Union[None, Unset, str]): Name of a vApp.
        cpu_allocation_mhz (Union[None, Unset, int]): Amount of allocated CPU, in MHz.
        memory_allocation_mb (Union[None, Unset, int]): Amount of allocated memory, in MB.
        storage_kb (Union[None, Unset, int]): Amount of storage capacity, in kB.
        lease_expiration_date (Union[None, Unset, datetime.datetime]): Date and time when a vApp must be deleted
            automaticaly.
        power_state (Union[Unset, VAppPowerState]):
        is_expired (Union[None, Unset, bool]): Indicates whether the vApp lease has expired.
        auto_undeploy_time (Union[None, Unset, datetime.datetime]): Date and time when a vApp must be undeployed.
        cloud_director_id (Union[None, Unset, int]): ID assigned to a VMware Cloud Director.
        organization_id (Union[None, Unset, int]): ID assigned to an organization.
        organization_vdc_id (Union[None, Unset, int]): ID assigned to an organization VDC.
    """

    v_app_id: Union[Unset, int] = UNSET
    href: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    cpu_allocation_mhz: Union[None, Unset, int] = UNSET
    memory_allocation_mb: Union[None, Unset, int] = UNSET
    storage_kb: Union[None, Unset, int] = UNSET
    lease_expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    power_state: Union[Unset, VAppPowerState] = UNSET
    is_expired: Union[None, Unset, bool] = UNSET
    auto_undeploy_time: Union[None, Unset, datetime.datetime] = UNSET
    cloud_director_id: Union[None, Unset, int] = UNSET
    organization_id: Union[None, Unset, int] = UNSET
    organization_vdc_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        v_app_id = self.v_app_id

        href: Union[None, Unset, str]
        if isinstance(self.href, Unset):
            href = UNSET
        else:
            href = self.href

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cpu_allocation_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_allocation_mhz, Unset):
            cpu_allocation_mhz = UNSET
        else:
            cpu_allocation_mhz = self.cpu_allocation_mhz

        memory_allocation_mb: Union[None, Unset, int]
        if isinstance(self.memory_allocation_mb, Unset):
            memory_allocation_mb = UNSET
        else:
            memory_allocation_mb = self.memory_allocation_mb

        storage_kb: Union[None, Unset, int]
        if isinstance(self.storage_kb, Unset):
            storage_kb = UNSET
        else:
            storage_kb = self.storage_kb

        lease_expiration_date: Union[None, Unset, str]
        if isinstance(self.lease_expiration_date, Unset):
            lease_expiration_date = UNSET
        elif isinstance(self.lease_expiration_date, datetime.datetime):
            lease_expiration_date = self.lease_expiration_date.isoformat()
        else:
            lease_expiration_date = self.lease_expiration_date

        power_state: Union[Unset, str] = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        is_expired: Union[None, Unset, bool]
        if isinstance(self.is_expired, Unset):
            is_expired = UNSET
        else:
            is_expired = self.is_expired

        auto_undeploy_time: Union[None, Unset, str]
        if isinstance(self.auto_undeploy_time, Unset):
            auto_undeploy_time = UNSET
        elif isinstance(self.auto_undeploy_time, datetime.datetime):
            auto_undeploy_time = self.auto_undeploy_time.isoformat()
        else:
            auto_undeploy_time = self.auto_undeploy_time

        cloud_director_id: Union[None, Unset, int]
        if isinstance(self.cloud_director_id, Unset):
            cloud_director_id = UNSET
        else:
            cloud_director_id = self.cloud_director_id

        organization_id: Union[None, Unset, int]
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        organization_vdc_id: Union[None, Unset, int]
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

        def _parse_href(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        href = _parse_href(d.pop("href", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_cpu_allocation_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_allocation_mhz = _parse_cpu_allocation_mhz(d.pop("cpuAllocationMhz", UNSET))

        def _parse_memory_allocation_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_allocation_mb = _parse_memory_allocation_mb(d.pop("memoryAllocationMb", UNSET))

        def _parse_storage_kb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        storage_kb = _parse_storage_kb(d.pop("storageKb", UNSET))

        def _parse_lease_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                lease_expiration_date_type_0 = isoparse(data)

                return lease_expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        lease_expiration_date = _parse_lease_expiration_date(d.pop("leaseExpirationDate", UNSET))

        _power_state = d.pop("powerState", UNSET)
        power_state: Union[Unset, VAppPowerState]
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = VAppPowerState(_power_state)

        def _parse_is_expired(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_expired = _parse_is_expired(d.pop("isExpired", UNSET))

        def _parse_auto_undeploy_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                auto_undeploy_time_type_0 = isoparse(data)

                return auto_undeploy_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        auto_undeploy_time = _parse_auto_undeploy_time(d.pop("autoUndeployTime", UNSET))

        def _parse_cloud_director_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cloud_director_id = _parse_cloud_director_id(d.pop("cloudDirectorId", UNSET))

        def _parse_organization_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        def _parse_organization_vdc_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

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
