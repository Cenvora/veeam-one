from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVFileShareInfo")


@_attrs_define
class HyperVFileShareInfo:
    """
    Attributes:
        file_share_id (Union[Unset, int]): ID assigned to a file share.
        name (Union[None, Unset, str]): Name of a file share
        file_server_id (Union[Unset, int]): ID assigned to a file server.
        is_ha (Union[None, Unset, bool]): Indicates whether a share is Highly Available.
        capacity_bytes (Union[None, Unset, int]): Disk capacity of a file share, in bytes.
        free_space_bytes (Union[None, Unset, int]): Amount of available free space on a file share, in bytes.
        provisioned_bytes (Union[None, Unset, int]): Amount of provisioned space on a file share, in bytes.
        business_view_group_ids (Union[None, Unset, list[int]]): Array of Business View groups.
    """

    file_share_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    file_server_id: Union[Unset, int] = UNSET
    is_ha: Union[None, Unset, bool] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    provisioned_bytes: Union[None, Unset, int] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_share_id = self.file_share_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        file_server_id = self.file_server_id

        is_ha: Union[None, Unset, bool]
        if isinstance(self.is_ha, Unset):
            is_ha = UNSET
        else:
            is_ha = self.is_ha

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

        provisioned_bytes: Union[None, Unset, int]
        if isinstance(self.provisioned_bytes, Unset):
            provisioned_bytes = UNSET
        else:
            provisioned_bytes = self.provisioned_bytes

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_share_id is not UNSET:
            field_dict["fileShareId"] = file_share_id
        if name is not UNSET:
            field_dict["name"] = name
        if file_server_id is not UNSET:
            field_dict["fileServerId"] = file_server_id
        if is_ha is not UNSET:
            field_dict["isHa"] = is_ha
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if provisioned_bytes is not UNSET:
            field_dict["provisionedBytes"] = provisioned_bytes
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_share_id = d.pop("fileShareId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        file_server_id = d.pop("fileServerId", UNSET)

        def _parse_is_ha(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_ha = _parse_is_ha(d.pop("isHa", UNSET))

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

        def _parse_provisioned_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        provisioned_bytes = _parse_provisioned_bytes(d.pop("provisionedBytes", UNSET))

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

        hyper_v_file_share_info = cls(
            file_share_id=file_share_id,
            name=name,
            file_server_id=file_server_id,
            is_ha=is_ha,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            provisioned_bytes=provisioned_bytes,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_file_share_info
