from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationVdcNetworkPool")


@_attrs_define
class OrganizationVdcNetworkPool:
    """
    Attributes:
        name (Union[None, Unset, str]): Name of a network pool.
        used_ip_count (Union[Unset, int]): Number of IP addresses used in a network pool.
        total_ip_count (Union[Unset, int]): Number of all available IP addresses.
    """

    name: Union[None, Unset, str] = UNSET
    used_ip_count: Union[Unset, int] = UNSET
    total_ip_count: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        used_ip_count = d.pop("usedIpCount", UNSET)

        total_ip_count = d.pop("totalIpCount", UNSET)

        organization_vdc_network_pool = cls(
            name=name,
            used_ip_count=used_ip_count,
            total_ip_count=total_ip_count,
        )

        return organization_vdc_network_pool
