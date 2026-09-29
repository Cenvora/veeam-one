from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GuestSettingsRequest")


@_attrs_define
class GuestSettingsRequest:
    """
    Attributes:
        ssh_port (int | Unset): SSH port.
        ssh_skip_verification (bool | Unset): Indicates whether SSH certificate fingerprint check is skipped.
        propagate (bool | None | Unset): Indicates whether child objects are accessed using the same credential set.
    """

    ssh_port: int | Unset = UNSET
    ssh_skip_verification: bool | Unset = UNSET
    propagate: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        ssh_port = self.ssh_port

        ssh_skip_verification = self.ssh_skip_verification

        propagate: bool | None | Unset
        if isinstance(self.propagate, Unset):
            propagate = UNSET
        else:
            propagate = self.propagate

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if ssh_port is not UNSET:
            field_dict["sshPort"] = ssh_port
        if ssh_skip_verification is not UNSET:
            field_dict["sshSkipVerification"] = ssh_skip_verification
        if propagate is not UNSET:
            field_dict["propagate"] = propagate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ssh_port = d.pop("sshPort", UNSET)

        ssh_skip_verification = d.pop("sshSkipVerification", UNSET)

        def _parse_propagate(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        propagate = _parse_propagate(d.pop("propagate", UNSET))

        guest_settings_request = cls(
            ssh_port=ssh_port,
            ssh_skip_verification=ssh_skip_verification,
            propagate=propagate,
        )

        return guest_settings_request
