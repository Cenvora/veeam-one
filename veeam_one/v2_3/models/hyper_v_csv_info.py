from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVCsvInfo")


@_attrs_define
class HyperVCsvInfo:
    """
    Attributes:
        csv_disk_id (int | Unset): ID assigned to a CSV disk.
        cluster_id (int | None | Unset): ID assigned to a cluster.
        name (None | str | Unset): Name of a CSV disk.
        capacity_mb (int | None | Unset): Capacity of a CSV disk, in MB.
        free_space_mb (int | None | Unset): Amount of available free space on a CSV disk, in MB.
        provisioned_mb (int | None | Unset): Amount of provisioned space on a CSV disk, in MB.
        path (None | str | Unset): Path to a storage location in a CSV disk.
        business_view_group_ids (list[int] | None | Unset): Array of IDs assigned to the Business View groups.
    """

    csv_disk_id: int | Unset = UNSET
    cluster_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    capacity_mb: int | None | Unset = UNSET
    free_space_mb: int | None | Unset = UNSET
    provisioned_mb: int | None | Unset = UNSET
    path: None | str | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        csv_disk_id = self.csv_disk_id

        cluster_id: int | None | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        capacity_mb: int | None | Unset
        if isinstance(self.capacity_mb, Unset):
            capacity_mb = UNSET
        else:
            capacity_mb = self.capacity_mb

        free_space_mb: int | None | Unset
        if isinstance(self.free_space_mb, Unset):
            free_space_mb = UNSET
        else:
            free_space_mb = self.free_space_mb

        provisioned_mb: int | None | Unset
        if isinstance(self.provisioned_mb, Unset):
            provisioned_mb = UNSET
        else:
            provisioned_mb = self.provisioned_mb

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        business_view_group_ids: list[int] | None | Unset
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

        def _parse_cluster_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cluster_id = _parse_cluster_id(d.pop("clusterId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_capacity_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_mb = _parse_capacity_mb(d.pop("capacityMb", UNSET))

        def _parse_free_space_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_mb = _parse_free_space_mb(d.pop("freeSpaceMb", UNSET))

        def _parse_provisioned_mb(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        provisioned_mb = _parse_provisioned_mb(d.pop("provisionedMb", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

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
