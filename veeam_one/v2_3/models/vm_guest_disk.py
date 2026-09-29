from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VmGuestDisk")


@_attrs_define
class VmGuestDisk:
    """
    Attributes:
        name (None | str | Unset): Name of a guest disk.
        capacity_bytes (int | Unset): Storage capacity of a guest disk, in bytes.
        free_space_bytes (int | Unset): Free storage space of a guest disk, in bytes.
    """

    name: None | str | Unset = UNSET
    capacity_bytes: int | Unset = UNSET
    free_space_bytes: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        capacity_bytes = self.capacity_bytes

        free_space_bytes = self.free_space_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        capacity_bytes = d.pop("capacityBytes", UNSET)

        free_space_bytes = d.pop("freeSpaceBytes", UNSET)

        vm_guest_disk = cls(
            name=name,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
        )

        return vm_guest_disk
