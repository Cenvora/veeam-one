from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationVdcNetworkPool")


@_attrs_define
class OrganizationVdcNetworkPool:
    """
    Attributes:
        name (None | str | Unset): Name of a network pool.
        used_ip_count (int | Unset): Number of IP addresses used in a network pool.
        total_ip_count (int | Unset): Number of all available IP addresses.
    """

    name: None | str | Unset = UNSET
    used_ip_count: int | Unset = UNSET
    total_ip_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        used_ip_count = self.used_ip_count

        total_ip_count = self.total_ip_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if used_ip_count is not UNSET:
            field_dict["usedIpCount"] = used_ip_count
        if total_ip_count is not UNSET:
            field_dict["totalIpCount"] = total_ip_count

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

        used_ip_count = d.pop("usedIpCount", UNSET)

        total_ip_count = d.pop("totalIpCount", UNSET)

        organization_vdc_network_pool = cls(
            name=name,
            used_ip_count=used_ip_count,
            total_ip_count=total_ip_count,
        )

        return organization_vdc_network_pool
