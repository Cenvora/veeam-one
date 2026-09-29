from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.cloud_director_connection_state import CloudDirectorConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudDirectorInfo")


@_attrs_define
class CloudDirectorInfo:
    """
    Attributes:
        cloud_director_server_id (Union[Unset, int]): ID assigned to a VMware Cloud Director server.
        name (Union[None, Unset, str]): Name of a VMware Cloud Director.
        connection_state (Union[Unset, CloudDirectorConnectionState]):
        connection_error (Union[None, Unset, str]): Datails on VMware Cloud Director server connection failure.
        version (Union[None, Unset, str]): VMware Cloud Director version.
    """

    cloud_director_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, CloudDirectorConnectionState] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_director_server_id = self.cloud_director_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        connection_error: Union[None, Unset, str]
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_director_server_id is not UNSET:
            field_dict["cloudDirectorServerId"] = cloud_director_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_director_server_id = d.pop("cloudDirectorServerId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, CloudDirectorConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = CloudDirectorConnectionState(_connection_state)

        def _parse_connection_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        cloud_director_info = cls(
            cloud_director_server_id=cloud_director_server_id,
            name=name,
            connection_state=connection_state,
            connection_error=connection_error,
            version=version,
        )

        return cloud_director_info
