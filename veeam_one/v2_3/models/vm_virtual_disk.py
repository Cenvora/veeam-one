from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VmVirtualDisk")


@_attrs_define
class VmVirtualDisk:
    """
    Attributes:
        name (Union[None, Unset, str]): Name of a virtual disk.
        capacity_bytes (Union[Unset, int]): Storage capacity of a virtual disk, in bytes.
    """

    name: Union[None, Unset, str] = UNSET
    capacity_bytes: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        capacity_bytes = self.capacity_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        capacity_bytes = d.pop("capacityBytes", UNSET)

        vm_virtual_disk = cls(
            name=name,
            capacity_bytes=capacity_bytes,
        )

        return vm_virtual_disk
