from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseUsageTotalUnit")


@_attrs_define
class VeeamOneLicenseUsageTotalUnit:
    """
    Attributes:
        license_unit (None | str | Unset): Type of license units (Points, Sockets or Instances). Example: Instances.
        used (None | str | Unset): Number of consumed license units. Example: 379.
        available (None | str | Unset): Number of available license units. Example: 9621.
        licensed (None | str | Unset): Total number of license units. Example: 10000.
    """

    license_unit: None | str | Unset = UNSET
    used: None | str | Unset = UNSET
    available: None | str | Unset = UNSET
    licensed: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        license_unit: None | str | Unset
        if isinstance(self.license_unit, Unset):
            license_unit = UNSET
        else:
            license_unit = self.license_unit

        used: None | str | Unset
        if isinstance(self.used, Unset):
            used = UNSET
        else:
            used = self.used

        available: None | str | Unset
        if isinstance(self.available, Unset):
            available = UNSET
        else:
            available = self.available

        licensed: None | str | Unset
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

        def _parse_license_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_unit = _parse_license_unit(d.pop("licenseUnit", UNSET))

        def _parse_used(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        used = _parse_used(d.pop("used", UNSET))

        def _parse_available(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        available = _parse_available(d.pop("available", UNSET))

        def _parse_licensed(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        licensed = _parse_licensed(d.pop("licensed", UNSET))

        veeam_one_license_usage_total_unit = cls(
            license_unit=license_unit,
            used=used,
            available=available,
            licensed=licensed,
        )

        return veeam_one_license_usage_total_unit
