from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.hyper_v_connection_state import HyperVConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVScVmmServerInfo")


@_attrs_define
class HyperVScVmmServerInfo:
    """
    Attributes:
        scvmm_server_id (int | Unset): ID assigned to SCVMM server.
        name (None | str | Unset): Name of a SCVMM server.
        port (int | None | Unset): Port that is used to access a SCVMM server.
        connection_error (None | str | Unset): Datails on SCVMM server connection failure.
        connection_state (HyperVConnectionState | Unset):
        version (None | str | Unset): Version of a SCVMM server.
    """

    scvmm_server_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    connection_error: None | str | Unset = UNSET
    connection_state: HyperVConnectionState | Unset = UNSET
    version: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scvmm_server_id = self.scvmm_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        connection_error: None | str | Unset
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scvmm_server_id is not UNSET:
            field_dict["scvmmServerId"] = scvmm_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if port is not UNSET:
            field_dict["port"] = port
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scvmm_server_id = d.pop("scvmmServerId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_connection_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: HyperVConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = HyperVConnectionState(_connection_state)

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        hyper_v_sc_vmm_server_info = cls(
            scvmm_server_id=scvmm_server_id,
            name=name,
            port=port,
            connection_error=connection_error,
            connection_state=connection_state,
            version=version,
        )

        return hyper_v_sc_vmm_server_info
