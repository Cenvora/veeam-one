from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_total_unit import VeeamOneLicenseUsageTotalUnit


T = TypeVar("T", bound="VeeamOneLicenseUsageTotal")


@_attrs_define
class VeeamOneLicenseUsageTotal:
    """
    Attributes:
        units (list[VeeamOneLicenseUsageTotalUnit] | None | Unset): Array of license units.
    """

    units: list[VeeamOneLicenseUsageTotalUnit] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        units: list[dict[str, Any]] | None | Unset
        if isinstance(self.units, Unset):
            units = UNSET
        elif isinstance(self.units, list):
            units = []
            for units_type_0_item_data in self.units:
                units_type_0_item = units_type_0_item_data.to_dict()
                units.append(units_type_0_item)

        else:
            units = self.units

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if units is not UNSET:
            field_dict["units"] = units

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.veeam_one_license_usage_total_unit import VeeamOneLicenseUsageTotalUnit  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_units(data: object) -> list[VeeamOneLicenseUsageTotalUnit] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                units_type_0 = []
                _units_type_0 = data
                for units_type_0_item_data in _units_type_0:
                    units_type_0_item = VeeamOneLicenseUsageTotalUnit.from_dict(units_type_0_item_data)

                    units_type_0.append(units_type_0_item)

                return units_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[VeeamOneLicenseUsageTotalUnit] | None | Unset, data)

        units = _parse_units(d.pop("units", UNSET))

        veeam_one_license_usage_total = cls(
            units=units,
        )

        return veeam_one_license_usage_total
