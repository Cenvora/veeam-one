from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="InstallVeeamOneLicenseRequest")


@_attrs_define
class InstallVeeamOneLicenseRequest:
    """
    Attributes:
        license_ (str): License file in the Base64 format.
    """

    license_: str

    def to_dict(self) -> dict[str, Any]:
        license_ = self.license_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "license": license_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        license_ = d.pop("license")

        install_veeam_one_license_request = cls(
            license_=license_,
        )

        return install_veeam_one_license_request
