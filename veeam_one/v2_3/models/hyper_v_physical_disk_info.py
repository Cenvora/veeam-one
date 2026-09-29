from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVPhysicalDiskInfo")


@_attrs_define
class HyperVPhysicalDiskInfo:
    """
    Attributes:
        physical_disk_id (Union[Unset, int]): ID assigned to a physical disk.
        capacity_bytes (Union[None, Unset, int]): Physical disk capacity, in bytes.
        free_space_bytes (Union[None, Unset, int]): Amount of free space on physical disk, in bytes.
        host_id (Union[None, Unset, int]): ID assigned to a host.
        provisioned_bytes (Union[None, Unset, int]): Amount of provisioned space on a physical disk, in bytes.
        path (Union[None, Unset, str]): Paths to logical disks.
        name (Union[None, Unset, str]): Name of a physical disk.
        business_view_group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to the Business View groups.
    """

    physical_disk_id: Union[Unset, int] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    host_id: Union[None, Unset, int] = UNSET
    provisioned_bytes: Union[None, Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        physical_disk_id = self.physical_disk_id

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: Union[None, Unset, int]
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        host_id: Union[None, Unset, int]
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        provisioned_bytes: Union[None, Unset, int]
        if isinstance(self.provisioned_bytes, Unset):
            provisioned_bytes = UNSET
        else:
            provisioned_bytes = self.provisioned_bytes

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if physical_disk_id is not UNSET:
            field_dict["physicalDiskId"] = physical_disk_id
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if provisioned_bytes is not UNSET:
            field_dict["provisionedBytes"] = provisioned_bytes
        if path is not UNSET:
            field_dict["path"] = path
        if name is not UNSET:
            field_dict["name"] = name
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        physical_disk_id = d.pop("physicalDiskId", UNSET)

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_host_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        host_id = _parse_host_id(d.pop("hostId", UNSET))

        def _parse_provisioned_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        provisioned_bytes = _parse_provisioned_bytes(d.pop("provisionedBytes", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_business_view_group_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        hyper_v_physical_disk_info = cls(
            physical_disk_id=physical_disk_id,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            host_id=host_id,
            provisioned_bytes=provisioned_bytes,
            path=path,
            name=name,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_physical_disk_info
