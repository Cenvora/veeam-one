from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.vb_365_server_connection_state import Vb365ServerConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ServerInfo")


@_attrs_define
class Vb365ServerInfo:
    """
    Attributes:
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        name (Union[None, Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        version (Union[None, Unset, str]): Version of Veeam Backup for Microsoft 365 installed on a server.
        port (Union[None, Unset, int]): Port used by Veeam Backup for Microsoft 365.
        connection_error (Union[None, Unset, str]): Datails on Veeam Backup for Microsoft 365 server connection failure.
        connection_state (Union[Unset, Vb365ServerConnectionState]):
    """

    vb_365_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, Vb365ServerConnectionState] = UNSET

    def to_dict(self) -> dict[str, Any]:
        vb_365_server_id = self.vb_365_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        connection_error: Union[None, Unset, str]
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: Union[Unset, str] = UNSET
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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_connection_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, Vb365ServerConnectionState]
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
