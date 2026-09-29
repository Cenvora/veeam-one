from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.organization_vdc_allocation_model import OrganizationVdcAllocationModel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_vdc_network_pool import OrganizationVdcNetworkPool


T = TypeVar("T", bound="OrganizationVdcInfo")


@_attrs_define
class OrganizationVdcInfo:
    """
    Attributes:
        organization_vdc_id (int | Unset): ID assigned to an organization VDC.
        href (None | str | Unset): Unique organization VDC identifier in the URL format. Identical to the `href`
            property in VMware Cloud Director API.
        name (None | str | Unset): Name of an organization VDC.
        allocation_model (OrganizationVdcAllocationModel | Unset):
        cpu_allocation_mhz (int | None | Unset): Amount of CPU resources allocated to an organization VDC, in MHz.
        cpu_limit_mhz (int | None | Unset): Maximum amount of CPU resources that can be provided by an organization VDC,
            in MHz.
        cpu_used_mhz (int | None | Unset): Amount of CPU resources consumed on an organization VDC, in MHz.
        memory_allocation_mb (int | None | Unset): Amount of memory resources allocated to an organization VDC, in MB.
        memory_limit_mb (int | None | Unset): Maximum amount of memory resources that can be provided by an organization
            VDC, in MB.
        memory_used_mb (int | None | Unset): Amount of memory resources consumed on an organization VDC, in MB.
        storage_allocation_mb (int | None | Unset): Amount of disk space allocated to an organization VDC, in MB.
        storage_limit_mb (int | None | Unset): Maximum amount of disk space that can be provided by an organization VDC,
            in MB.
        storage_used_mb (int | None | Unset): Amount of disk space consumed on an organization VDC, in MB.
        network_pool (None | OrganizationVdcNetworkPool | Unset): Network pool used by an organization VDC.
        cloud_director_id (int | None | Unset): ID assigned to a VMware Cloud Director server.
        organization_id (int | None | Unset): ID assigned to an organization.
        provider_vdc_id (int | None | Unset): ID assigned to a provider VDC.
    """

    organization_vdc_id: int | Unset = UNSET
    href: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    allocation_model: OrganizationVdcAllocationModel | Unset = UNSET
    cpu_allocation_mhz: int | None | Unset = UNSET
    cpu_limit_mhz: int | None | Unset = UNSET
    cpu_used_mhz: int | None | Unset = UNSET
    memory_allocation_mb: int | None | Unset = UNSET
    memory_limit_mb: int | None | Unset = UNSET
    memory_used_mb: int | None | Unset = UNSET
    storage_allocation_mb: int | None | Unset = UNSET
    storage_limit_mb: int | None | Unset = UNSET
    storage_used_mb: int | None | Unset = UNSET
    network_pool: None | OrganizationVdcNetworkPool | Unset = UNSET
    cloud_director_id: int | None | Unset = UNSET
    organization_id: int | None | Unset = UNSET
    provider_vdc_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_vdc_network_pool import OrganizationVdcNetworkPool  # noqa: PLC0415

        organization_vdc_id = self.organization_vdc_id

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

        allocation_model: str | Unset = UNSET
        if not isinstance(self.allocation_model, Unset):
            allocation_model = self.allocation_model.value

        cpu_allocation_mhz: int | None | Unset
        if isinstance(self.cpu_allocation_mhz, Unset):
            cpu_allocation_mhz = UNSET
        else:
            cpu_allocation_mhz = self.cpu_allocation_mhz

        cpu_limit_mhz: int | None | Unset
        if isinstance(self.cpu_limit_mhz, Unset):
            cpu_limit_mhz = UNSET
        else:
            cpu_limit_mhz = self.cpu_limit_mhz

        cpu_used_mhz: int | None | Unset
        if isinstance(self.cpu_used_mhz, Unset):
            cpu_used_mhz = UNSET
        else:
            cpu_used_mhz = self.cpu_used_mhz

        memory_allocation_mb: int | None | Unset
        if isinstance(self.memory_allocation_mb, Unset):
            memory_allocation_mb = UNSET
        else:
            memory_allocation_mb = self.memory_allocation_mb

        memory_limit_mb: int | None | Unset
        if isinstance(self.memory_limit_mb, Unset):
            memory_limit_mb = UNSET
        else:
            memory_limit_mb = self.memory_limit_mb

        memory_used_mb: int | None | Unset
        if isinstance(self.memory_used_mb, Unset):
            memory_used_mb = UNSET
        else:
            memory_used_mb = self.memory_used_mb

        storage_allocation_mb: int | None | Unset
        if isinstance(self.storage_allocation_mb, Unset):
            storage_allocation_mb = UNSET
        else:
            storage_allocation_mb = self.storage_allocation_mb

        storage_limit_mb: int | None | Unset
        if isinstance(self.storage_limit_mb, Unset):
            storage_limit_mb = UNSET
        else:
            storage_limit_mb = self.storage_limit_mb

        storage_used_mb: int | None | Unset
        if isinstance(self.storage_used_mb, Unset):
            storage_used_mb = UNSET
        else:
            storage_used_mb = self.storage_used_mb

        network_pool: dict[str, Any] | None | Unset
        if isinstance(self.network_pool, Unset):
            network_pool = UNSET
        elif isinstance(self.network_pool, OrganizationVdcNetworkPool):
            network_pool = self.network_pool.to_dict()
        else:
            network_pool = self.network_pool

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

        provider_vdc_id: int | None | Unset
        if isinstance(self.provider_vdc_id, Unset):
            provider_vdc_id = UNSET
        else:
            provider_vdc_id = self.provider_vdc_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_vdc_id is not UNSET:
            field_dict["organizationVdcId"] = organization_vdc_id
        if href is not UNSET:
            field_dict["href"] = href
        if name is not UNSET:
            field_dict["name"] = name
        if allocation_model is not UNSET:
            field_dict["allocationModel"] = allocation_model
        if cpu_allocation_mhz is not UNSET:
            field_dict["cpuAllocationMhz"] = cpu_allocation_mhz
        if cpu_limit_mhz is not UNSET:
            field_dict["cpuLimitMhz"] = cpu_limit_mhz
        if cpu_used_mhz is not UNSET:
            field_dict["cpuUsedMhz"] = cpu_used_mhz
        if memory_allocation_mb is not UNSET:
            field_dict["memoryAllocationMb"] = memory_allocation_mb
        if memory_limit_mb is not UNSET:
            field_dict["memoryLimitMb"] = memory_limit_mb
        if memory_used_mb is not UNSET:
            field_dict["memoryUsedMb"] = memory_used_mb
        if storage_allocation_mb is not UNSET:
            field_dict["storageAllocationMb"] = storage_allocation_mb
        if storage_limit_mb is not UNSET:
            field_dict["storageLimitMb"] = storage_limit_mb
        if storage_used_mb is not UNSET:
            field_dict["storageUsedMb"] = storage_used_mb
        if network_pool is not UNSET:
            field_dict["networkPool"] = network_pool
        if cloud_director_id is not UNSET:
            field_dict["cloudDirectorId"] = cloud_director_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if provider_vdc_id is not UNSET:
            field_dict["providerVdcId"] = provider_vdc_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_vdc_network_pool import OrganizationVdcNetworkPool  # noqa: PLC0415

        d = dict(src_dict)
        organization_vdc_id = d.pop("organizationVdcId", UNSET)

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

        _allocation_model = d.pop("allocationModel", UNSET)
        allocation_model: OrganizationVdcAllocationModel | Unset
        if isinstance(_allocation_model, Unset):
            allocation_model = UNSET
        else:
            allocation_model = OrganizationVdcAllocationModel(_allocation_model)

        def _parse_cpu_allocation_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_allocation_mhz = _parse_cpu_allocation_mhz(d.pop("cpuAllocationMhz", UNSET))

        def _parse_cpu_limit_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_limit_mhz = _parse_cpu_limit_mhz(d.pop("cpuLimitMhz", UNSET))

        def _parse_cpu_used_mhz(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cpu_used_mhz = _parse_cpu_used_mhz(d.pop("cpuUsedMhz", UNSET))

        def _parse_memory_allocation_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_allocation_mb = _parse_memory_allocation_mb(d.pop("memoryAllocationMb", UNSET))

        def _parse_memory_limit_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_limit_mb = _parse_memory_limit_mb(d.pop("memoryLimitMb", UNSET))

        def _parse_memory_used_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        memory_used_mb = _parse_memory_used_mb(d.pop("memoryUsedMb", UNSET))

        def _parse_storage_allocation_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_allocation_mb = _parse_storage_allocation_mb(d.pop("storageAllocationMb", UNSET))

        def _parse_storage_limit_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_limit_mb = _parse_storage_limit_mb(d.pop("storageLimitMb", UNSET))

        def _parse_storage_used_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        storage_used_mb = _parse_storage_used_mb(d.pop("storageUsedMb", UNSET))

        def _parse_network_pool(data: object) -> None | OrganizationVdcNetworkPool | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                network_pool_type_1 = OrganizationVdcNetworkPool.from_dict(data)

                return network_pool_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OrganizationVdcNetworkPool | Unset, data)

        network_pool = _parse_network_pool(d.pop("networkPool", UNSET))

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

        def _parse_provider_vdc_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        provider_vdc_id = _parse_provider_vdc_id(d.pop("providerVdcId", UNSET))

        organization_vdc_info = cls(
            organization_vdc_id=organization_vdc_id,
            href=href,
            name=name,
            allocation_model=allocation_model,
            cpu_allocation_mhz=cpu_allocation_mhz,
            cpu_limit_mhz=cpu_limit_mhz,
            cpu_used_mhz=cpu_used_mhz,
            memory_allocation_mb=memory_allocation_mb,
            memory_limit_mb=memory_limit_mb,
            memory_used_mb=memory_used_mb,
            storage_allocation_mb=storage_allocation_mb,
            storage_limit_mb=storage_limit_mb,
            storage_used_mb=storage_used_mb,
            network_pool=network_pool,
            cloud_director_id=cloud_director_id,
            organization_id=organization_id,
            provider_vdc_id=provider_vdc_id,
        )

        return organization_vdc_info
