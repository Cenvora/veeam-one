from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseSettings")


@_attrs_define
class VeeamOneLicenseSettings:
    """
    Attributes:
        auto_update_enabled (bool | Unset): Indicates whether auto-update is enabled for a license. Example: True.
        managed_mode (bool | Unset): Indicates whether some other service provides statistics instead of Veeam ONE.
            Example: False.
    """

    auto_update_enabled: bool | Unset = UNSET
    managed_mode: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        auto_update_enabled = self.auto_update_enabled

        managed_mode = self.managed_mode

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if auto_update_enabled is not UNSET:
            field_dict["autoUpdateEnabled"] = auto_update_enabled
        if managed_mode is not UNSET:
            field_dict["managedMode"] = managed_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_update_enabled = d.pop("autoUpdateEnabled", UNSET)

        managed_mode = d.pop("managedMode", UNSET)

        veeam_one_license_settings = cls(
            auto_update_enabled=auto_update_enabled,
            managed_mode=managed_mode,
        )

        return veeam_one_license_settings
