from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.v_app_power_state import VAppPowerState
from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereVAppInfo")


@_attrs_define
class VSphereVAppInfo:
    """
    Attributes:
        v_app_id (Union[Unset, int]): ID assigned to a vApp.
        mo_ref (Union[None, Unset, str]): MoRef ID assigned to a vApp in VMware vSphere.
        name (Union[None, Unset, str]): Name of a vApp.
        parent_id (Union[None, Unset, int]): ID assigned to a parent object.
        parent_type (Union[None, Unset, VSphereObjectType]): Type of a parent object.
        product_name (Union[None, Unset, str]): Name of a product associated with a vApp.
        product_version (Union[None, Unset, str]): Version of a product associated with a vApp.
        product_vendor (Union[None, Unset, str]): Name of a product vendor.
        power_state (Union[Unset, VAppPowerState]):
        cpu_reservation_mhz (Union[None, Unset, int]): CPU reservation configured for a vApp, in MHz.
        cpu_unreserved_mhz (Union[None, Unset, int]): Amount of unreserved CPU resources, in MHz.
        is_cpu_expandable (Union[None, Unset, bool]): Indicates whether a vApp CPU reservation is expandable.
        cpu_limit_mhz (Union[None, Unset, int]): Maximum amount of CPU resources that can be allocated to a vApp, in
            MHz.
        cpu_shares (Union[None, Unset, int]): CPU share value.
        cpu_usage_mhz (Union[None, Unset, int]): Number of actively used CPU resource, in MHz.
        memory_reservation_mb (Union[None, Unset, int]): Memory reservation configured for a vApp, in MB.
        memory_unreserved_bytes (Union[None, Unset, int]): Amount of unreserved memory resources, in bytes.
        is_memory_expandable (Union[None, Unset, bool]): Indicates whether a vApp memory reservation is expandable.
        memory_limit_mb (Union[None, Unset, int]): Maximum amount of memory resources that can be allocated to a vApp,
            in MB.
        memory_shares (Union[None, Unset, int]): Memory share value.
        memory_usage_bytes (Union[None, Unset, int]): Amount of actively used memory resources, in bytes.
    """

    v_app_id: Union[Unset, int] = UNSET
    mo_ref: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    parent_type: Union[None, Unset, VSphereObjectType] = UNSET
    product_name: Union[None, Unset, str] = UNSET
    product_version: Union[None, Unset, str] = UNSET
    product_vendor: Union[None, Unset, str] = UNSET
    power_state: Union[Unset, VAppPowerState] = UNSET
    cpu_reservation_mhz: Union[None, Unset, int] = UNSET
    cpu_unreserved_mhz: Union[None, Unset, int] = UNSET
    is_cpu_expandable: Union[None, Unset, bool] = UNSET
    cpu_limit_mhz: Union[None, Unset, int] = UNSET
    cpu_shares: Union[None, Unset, int] = UNSET
    cpu_usage_mhz: Union[None, Unset, int] = UNSET
    memory_reservation_mb: Union[None, Unset, int] = UNSET
    memory_unreserved_bytes: Union[None, Unset, int] = UNSET
    is_memory_expandable: Union[None, Unset, bool] = UNSET
    memory_limit_mb: Union[None, Unset, int] = UNSET
    memory_shares: Union[None, Unset, int] = UNSET
    memory_usage_bytes: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        v_app_id = self.v_app_id

        mo_ref: Union[None, Unset, str]
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: Union[None, Unset, str]
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        product_name: Union[None, Unset, str]
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        product_version: Union[None, Unset, str]
        if isinstance(self.product_version, Unset):
            product_version = UNSET
        else:
            product_version = self.product_version

        product_vendor: Union[None, Unset, str]
        if isinstance(self.product_vendor, Unset):
            product_vendor = UNSET
        else:
            product_vendor = self.product_vendor

        power_state: Union[Unset, str] = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        cpu_reservation_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_reservation_mhz, Unset):
            cpu_reservation_mhz = UNSET
        else:
            cpu_reservation_mhz = self.cpu_reservation_mhz

        cpu_unreserved_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_unreserved_mhz, Unset):
            cpu_unreserved_mhz = UNSET
        else:
            cpu_unreserved_mhz = self.cpu_unreserved_mhz

        is_cpu_expandable: Union[None, Unset, bool]
        if isinstance(self.is_cpu_expandable, Unset):
            is_cpu_expandable = UNSET
        else:
            is_cpu_expandable = self.is_cpu_expandable

        cpu_limit_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_limit_mhz, Unset):
            cpu_limit_mhz = UNSET
        else:
            cpu_limit_mhz = self.cpu_limit_mhz

        cpu_shares: Union[None, Unset, int]
        if isinstance(self.cpu_shares, Unset):
            cpu_shares = UNSET
        else:
            cpu_shares = self.cpu_shares

        cpu_usage_mhz: Union[None, Unset, int]
        if isinstance(self.cpu_usage_mhz, Unset):
            cpu_usage_mhz = UNSET
        else:
            cpu_usage_mhz = self.cpu_usage_mhz

        memory_reservation_mb: Union[None, Unset, int]
        if isinstance(self.memory_reservation_mb, Unset):
            memory_reservation_mb = UNSET
        else:
            memory_reservation_mb = self.memory_reservation_mb

        memory_unreserved_bytes: Union[None, Unset, int]
        if isinstance(self.memory_unreserved_bytes, Unset):
            memory_unreserved_bytes = UNSET
        else:
            memory_unreserved_bytes = self.memory_unreserved_bytes

        is_memory_expandable: Union[None, Unset, bool]
        if isinstance(self.is_memory_expandable, Unset):
            is_memory_expandable = UNSET
        else:
            is_memory_expandable = self.is_memory_expandable

        memory_limit_mb: Union[None, Unset, int]
        if isinstance(self.memory_limit_mb, Unset):
            memory_limit_mb = UNSET
        else:
            memory_limit_mb = self.memory_limit_mb

        memory_shares: Union[None, Unset, int]
        if isinstance(self.memory_shares, Unset):
            memory_shares = UNSET
        else:
            memory_shares = self.memory_shares

        memory_usage_bytes: Union[None, Unset, int]
        if isinstance(self.memory_usage_bytes, Unset):
            memory_usage_bytes = UNSET
        else:
            memory_usage_bytes = self.memory_usage_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if v_app_id is not UNSET:
            field_dict["vAppId"] = v_app_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if product_version is not UNSET:
            field_dict["productVersion"] = product_version
        if product_vendor is not UNSET:
            field_dict["productVendor"] = product_vendor
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if cpu_reservation_mhz is not UNSET:
            field_dict["cpuReservationMhz"] = cpu_reservation_mhz
        if cpu_unreserved_mhz is not UNSET:
            field_dict["cpuUnreservedMhz"] = cpu_unreserved_mhz
        if is_cpu_expandable is not UNSET:
            field_dict["isCpuExpandable"] = is_cpu_expandable
        if cpu_limit_mhz is not UNSET:
            field_dict["cpuLimitMhz"] = cpu_limit_mhz
        if cpu_shares is not UNSET:
            field_dict["cpuShares"] = cpu_shares
        if cpu_usage_mhz is not UNSET:
            field_dict["cpuUsageMhz"] = cpu_usage_mhz
        if memory_reservation_mb is not UNSET:
            field_dict["memoryReservationMb"] = memory_reservation_mb
        if memory_unreserved_bytes is not UNSET:
            field_dict["memoryUnreservedBytes"] = memory_unreserved_bytes
        if is_memory_expandable is not UNSET:
            field_dict["isMemoryExpandable"] = is_memory_expandable
        if memory_limit_mb is not UNSET:
            field_dict["memoryLimitMb"] = memory_limit_mb
        if memory_shares is not UNSET:
            field_dict["memoryShares"] = memory_shares
        if memory_usage_bytes is not UNSET:
            field_dict["memoryUsageBytes"] = memory_usage_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v_app_id = d.pop("vAppId", UNSET)

        def _parse_mo_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_type(data: object) -> Union[None, Unset, VSphereObjectType]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, VSphereObjectType], data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        def _parse_product_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_name = _parse_product_name(d.pop("productName", UNSET))

        def _parse_product_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_version = _parse_product_version(d.pop("productVersion", UNSET))

        def _parse_product_vendor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_vendor = _parse_product_vendor(d.pop("productVendor", UNSET))

        _power_state = d.pop("powerState", UNSET)
        power_state: Union[Unset, VAppPowerState]
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = VAppPowerState(_power_state)

        def _parse_cpu_reservation_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_reservation_mhz = _parse_cpu_reservation_mhz(d.pop("cpuReservationMhz", UNSET))

        def _parse_cpu_unreserved_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_unreserved_mhz = _parse_cpu_unreserved_mhz(d.pop("cpuUnreservedMhz", UNSET))

        def _parse_is_cpu_expandable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_cpu_expandable = _parse_is_cpu_expandable(d.pop("isCpuExpandable", UNSET))

        def _parse_cpu_limit_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_limit_mhz = _parse_cpu_limit_mhz(d.pop("cpuLimitMhz", UNSET))

        def _parse_cpu_shares(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_shares = _parse_cpu_shares(d.pop("cpuShares", UNSET))

        def _parse_cpu_usage_mhz(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cpu_usage_mhz = _parse_cpu_usage_mhz(d.pop("cpuUsageMhz", UNSET))

        def _parse_memory_reservation_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_reservation_mb = _parse_memory_reservation_mb(d.pop("memoryReservationMb", UNSET))

        def _parse_memory_unreserved_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_unreserved_bytes = _parse_memory_unreserved_bytes(d.pop("memoryUnreservedBytes", UNSET))

        def _parse_is_memory_expandable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_memory_expandable = _parse_is_memory_expandable(d.pop("isMemoryExpandable", UNSET))

        def _parse_memory_limit_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_limit_mb = _parse_memory_limit_mb(d.pop("memoryLimitMb", UNSET))

        def _parse_memory_shares(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_shares = _parse_memory_shares(d.pop("memoryShares", UNSET))

        def _parse_memory_usage_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        memory_usage_bytes = _parse_memory_usage_bytes(d.pop("memoryUsageBytes", UNSET))

        v_sphere_v_app_info = cls(
            v_app_id=v_app_id,
            mo_ref=mo_ref,
            name=name,
            parent_id=parent_id,
            parent_type=parent_type,
            product_name=product_name,
            product_version=product_version,
            product_vendor=product_vendor,
            power_state=power_state,
            cpu_reservation_mhz=cpu_reservation_mhz,
            cpu_unreserved_mhz=cpu_unreserved_mhz,
            is_cpu_expandable=is_cpu_expandable,
            cpu_limit_mhz=cpu_limit_mhz,
            cpu_shares=cpu_shares,
            cpu_usage_mhz=cpu_usage_mhz,
            memory_reservation_mb=memory_reservation_mb,
            memory_unreserved_bytes=memory_unreserved_bytes,
            is_memory_expandable=is_memory_expandable,
            memory_limit_mb=memory_limit_mb,
            memory_shares=memory_shares,
            memory_usage_bytes=memory_usage_bytes,
        )

        return v_sphere_v_app_info
