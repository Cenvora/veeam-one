from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.hyper_v_connection_state import HyperVConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVScVmmServerInfo")


@_attrs_define
class HyperVScVmmServerInfo:
    """
    Attributes:
        scvmm_server_id (Union[Unset, int]): ID assigned to SCVMM server.
        name (Union[None, Unset, str]): Name of a SCVMM server.
        port (Union[None, Unset, int]): Port that is used to access a SCVMM server.
        connection_error (Union[None, Unset, str]): Datails on SCVMM server connection failure.
        connection_state (Union[Unset, HyperVConnectionState]):
        version (Union[None, Unset, str]): Version of a SCVMM server.
    """

    scvmm_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, HyperVConnectionState] = UNSET
    version: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        scvmm_server_id = self.scvmm_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        version: Union[None, Unset, str]
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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

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
        connection_state: Union[Unset, HyperVConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = HyperVConnectionState(_connection_state)

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
