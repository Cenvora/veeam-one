from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVCsvInfo")


@_attrs_define
class HyperVCsvInfo:
    """
    Attributes:
        csv_disk_id (Union[Unset, int]): ID assigned to a CSV disk.
        cluster_id (Union[None, Unset, int]): ID assigned to a cluster.
        name (Union[None, Unset, str]): Name of a CSV disk.
        capacity_mb (Union[None, Unset, int]): Capacity of a CSV disk, in MB.
        free_space_mb (Union[None, Unset, int]): Amount of available free space on a CSV disk, in MB.
        provisioned_mb (Union[None, Unset, int]): Amount of provisioned space on a CSV disk, in MB.
        path (Union[None, Unset, str]): Path to a storage location in a CSV disk.
        business_view_group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to the Business View groups.
    """

    csv_disk_id: Union[Unset, int] = UNSET
    cluster_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    capacity_mb: Union[None, Unset, int] = UNSET
    free_space_mb: Union[None, Unset, int] = UNSET
    provisioned_mb: Union[None, Unset, int] = UNSET
    path: Union[None, Unset, str] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        csv_disk_id = self.csv_disk_id

        cluster_id: Union[None, Unset, int]
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        capacity_mb: Union[None, Unset, int]
        if isinstance(self.capacity_mb, Unset):
            capacity_mb = UNSET
        else:
            capacity_mb = self.capacity_mb

        free_space_mb: Union[None, Unset, int]
        if isinstance(self.free_space_mb, Unset):
            free_space_mb = UNSET
        else:
            free_space_mb = self.free_space_mb

        provisioned_mb: Union[None, Unset, int]
        if isinstance(self.provisioned_mb, Unset):
            provisioned_mb = UNSET
        else:
            provisioned_mb = self.provisioned_mb

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if csv_disk_id is not UNSET:
            field_dict["csvDiskId"] = csv_disk_id
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id
        if name is not UNSET:
            field_dict["name"] = name
        if capacity_mb is not UNSET:
            field_dict["capacityMb"] = capacity_mb
        if free_space_mb is not UNSET:
            field_dict["freeSpaceMb"] = free_space_mb
        if provisioned_mb is not UNSET:
            field_dict["provisionedMb"] = provisioned_mb
        if path is not UNSET:
            field_dict["path"] = path
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        csv_disk_id = d.pop("csvDiskId", UNSET)

        def _parse_cluster_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cluster_id = _parse_cluster_id(d.pop("clusterId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_capacity_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_mb = _parse_capacity_mb(d.pop("capacityMb", UNSET))

        def _parse_free_space_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_mb = _parse_free_space_mb(d.pop("freeSpaceMb", UNSET))

        def _parse_provisioned_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        provisioned_mb = _parse_provisioned_mb(d.pop("provisionedMb", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

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

        hyper_v_csv_info = cls(
            csv_disk_id=csv_disk_id,
            cluster_id=cluster_id,
            name=name,
            capacity_mb=capacity_mb,
            free_space_mb=free_space_mb,
            provisioned_mb=provisioned_mb,
            path=path,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_csv_info
