from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderVdc")


@_attrs_define
class ProviderVdc:
    """
    Attributes:
        provider_vdc_id (int | Unset): ID assigned to a provider VDC.
        name (None | str | Unset): Name of a provider VDC.
    """

    provider_vdc_id: int | Unset = UNSET
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider_vdc_id = self.provider_vdc_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if provider_vdc_id is not UNSET:
            field_dict["providerVdcId"] = provider_vdc_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider_vdc_id = d.pop("providerVdcId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        provider_vdc = cls(
            provider_vdc_id=provider_vdc_id,
            name=name,
        )

        return provider_vdc
