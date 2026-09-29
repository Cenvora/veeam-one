from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialAssignHostRequest")


@_attrs_define
class CredentialAssignHostRequest:
    """
    Attributes:
        object_id (Union[Unset, int]): ID assigned to a host
        propagate (Union[Unset, bool]): Defines whether credentials must be propagated to host child objects.
        port (Union[None, Unset, int]): Host connection port.
    """

    object_id: Union[Unset, int] = UNSET
    propagate: Union[Unset, bool] = UNSET
    port: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        propagate = self.propagate

        port: Union[None, Unset, int]
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

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        credential_assign_host_request = cls(
            object_id=object_id,
            propagate=propagate,
            port=port,
        )

        return credential_assign_host_request
