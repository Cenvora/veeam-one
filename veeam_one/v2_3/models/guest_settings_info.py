from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GuestSettingsInfo")


@_attrs_define
class GuestSettingsInfo:
    """
    Attributes:
        ssh_port (int | Unset): SSH port.
        ssh_skip_verification (bool | Unset): Indicates whether SSH fingerprint check is skipped.
    """

    ssh_port: int | Unset = UNSET
    ssh_skip_verification: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ssh_port = self.ssh_port

        ssh_skip_verification = self.ssh_skip_verification

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ssh_port is not UNSET:
            field_dict["sshPort"] = ssh_port
        if ssh_skip_verification is not UNSET:
            field_dict["sshSkipVerification"] = ssh_skip_verification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssh_port = d.pop("sshPort", UNSET)

        ssh_skip_verification = d.pop("sshSkipVerification", UNSET)

        guest_settings_info = cls(
            ssh_port=ssh_port,
            ssh_skip_verification=ssh_skip_verification,
        )

        return guest_settings_info
