from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialAssignHostRequest")


@_attrs_define
class CredentialAssignHostRequest:
    """
    Attributes:
        object_id (int | Unset): ID assigned to a host
        propagate (bool | Unset): Defines whether credentials must be propagated to host child objects.
        port (int | None | Unset): Host connection port.
    """

    object_id: int | Unset = UNSET
    propagate: bool | Unset = UNSET
    port: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        propagate = self.propagate

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if propagate is not UNSET:
            field_dict["propagate"] = propagate
        if port is not UNSET:
            field_dict["port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("objectId", UNSET)

        propagate = d.pop("propagate", UNSET)

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        credential_assign_host_request = cls(
            object_id=object_id,
            propagate=propagate,
            port=port,
        )

        return credential_assign_host_request
