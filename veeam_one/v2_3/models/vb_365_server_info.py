from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.vb_365_server_connection_state import Vb365ServerConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ServerInfo")


@_attrs_define
class Vb365ServerInfo:
    """
    Attributes:
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        name (None | str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        version (None | str | Unset): Version of Veeam Backup for Microsoft 365 installed on a server.
        port (int | None | Unset): Port used by Veeam Backup for Microsoft 365.
        connection_error (None | str | Unset): Datails on Veeam Backup for Microsoft 365 server connection failure.
        connection_state (Vb365ServerConnectionState | Unset):
    """

    vb_365_server_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    connection_error: None | str | Unset = UNSET
    connection_state: Vb365ServerConnectionState | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        vb_365_server_id = self.vb_365_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if port is not UNSET:
            field_dict["port"] = port
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

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
        connection_state: Vb365ServerConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = Vb365ServerConnectionState(_connection_state)

        vb_365_server_info = cls(
            vb_365_server_id=vb_365_server_id,
            name=name,
            version=version,
            port=port,
            connection_error=connection_error,
            connection_state=connection_state,
        )

        return vb_365_server_info
