from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseUsageTotalUnit")


@_attrs_define
class VeeamOneLicenseUsageTotalUnit:
    """
    Attributes:
        license_unit (Union[None, Unset, str]): Type of license units (Points, Sockets or Instances). Example:
            Instances.
        used (Union[None, Unset, str]): Number of consumed license units. Example: 379.
        available (Union[None, Unset, str]): Number of available license units. Example: 9621.
        licensed (Union[None, Unset, str]): Total number of license units. Example: 10000.
    """

    license_unit: Union[None, Unset, str] = UNSET
    used: Union[None, Unset, str] = UNSET
    available: Union[None, Unset, str] = UNSET
    licensed: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        license_unit: Union[None, Unset, str]
        if isinstance(self.license_unit, Unset):
            license_unit = UNSET
        else:
            license_unit = self.license_unit

        used: Union[None, Unset, str]
        if isinstance(self.used, Unset):
            used = UNSET
        else:
            used = self.used

        available: Union[None, Unset, str]
        if isinstance(self.available, Unset):
            available = UNSET
        else:
            available = self.available

        licensed: Union[None, Unset, str]
        if isinstance(self.licensed, Unset):
            licensed = UNSET
        else:
            licensed = self.licensed

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if license_unit is not UNSET:
            field_dict["licenseUnit"] = license_unit
        if used is not UNSET:
            field_dict["used"] = used
        if available is not UNSET:
            field_dict["available"] = available
        if licensed is not UNSET:
            field_dict["licensed"] = licensed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_license_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_unit = _parse_license_unit(d.pop("licenseUnit", UNSET))

        def _parse_used(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        used = _parse_used(d.pop("used", UNSET))

        def _parse_available(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        available = _parse_available(d.pop("available", UNSET))

        def _parse_licensed(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        licensed = _parse_licensed(d.pop("licensed", UNSET))

        veeam_one_license_usage_total_unit = cls(
            license_unit=license_unit,
            used=used,
            available=available,
            licensed=licensed,
        )

        return veeam_one_license_usage_total_unit
