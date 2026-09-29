from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.veeam_one_license_usage_total_unit import VeeamOneLicenseUsageTotalUnit


T = TypeVar("T", bound="VeeamOneLicenseUsageTotal")


@_attrs_define
class VeeamOneLicenseUsageTotal:
    """
    Attributes:
        units (Union[None, Unset, list['VeeamOneLicenseUsageTotalUnit']]): Array of license units.
    """

    units: Union[None, Unset, list["VeeamOneLicenseUsageTotalUnit"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        units: Union[None, Unset, list[dict[str, Any]]]
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
        from ..models.veeam_one_license_usage_total_unit import VeeamOneLicenseUsageTotalUnit

        d = dict(src_dict)

        def _parse_units(data: object) -> Union[None, Unset, list["VeeamOneLicenseUsageTotalUnit"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["VeeamOneLicenseUsageTotalUnit"]], data)

        units = _parse_units(d.pop("units", UNSET))

        veeam_one_license_usage_total = cls(
            units=units,
        )

        return veeam_one_license_usage_total
