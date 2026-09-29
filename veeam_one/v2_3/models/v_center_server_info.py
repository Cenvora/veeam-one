from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.v_center_connection_state import VCenterConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="VCenterServerInfo")


@_attrs_define
class VCenterServerInfo:
    """
    Attributes:
        v_center_server_id (Union[Unset, int]): ID assigned to a vCenter server.
        name (Union[None, Unset, str]): Name of a vCenter server.
        connection_state (Union[Unset, VCenterConnectionState]):
        port (Union[None, Unset, int]): Connection port of a vCenter server.
        connection_error (Union[None, Unset, str]): Datails on vCenter server connection failure.
        product_name (Union[None, Unset, str]): Product name.
        version (Union[None, Unset, str]): Version of a vCenter server.
        os_type (Union[None, Unset, str]): Type of OS installed on a vCenter server.
        cloud_director_id (Union[None, Unset, int]): ID asigned to a VMware Cloud Director.
    """

    v_center_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, VCenterConnectionState] = UNSET
    port: Union[None, Unset, int] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    product_name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    os_type: Union[None, Unset, str] = UNSET
    cloud_director_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        v_center_server_id = self.v_center_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

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

        product_name: Union[None, Unset, str]
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        os_type: Union[None, Unset, str]
        if isinstance(self.os_type, Unset):
            os_type = UNSET
        else:
            os_type = self.os_type

        cloud_director_id: Union[None, Unset, int]
        if isinstance(self.cloud_director_id, Unset):
            cloud_director_id = UNSET
        else:
            cloud_director_id = self.cloud_director_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if v_center_server_id is not UNSET:
            field_dict["vCenterServerId"] = v_center_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if port is not UNSET:
            field_dict["port"] = port
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if version is not UNSET:
            field_dict["version"] = version
        if os_type is not UNSET:
            field_dict["osType"] = os_type
        if cloud_director_id is not UNSET:
            field_dict["cloudDirectorId"] = cloud_director_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        v_center_server_id = d.pop("vCenterServerId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, VCenterConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = VCenterConnectionState(_connection_state)

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

        def _parse_product_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_name = _parse_product_name(d.pop("productName", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_os_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        os_type = _parse_os_type(d.pop("osType", UNSET))

        def _parse_cloud_director_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cloud_director_id = _parse_cloud_director_id(d.pop("cloudDirectorId", UNSET))

        v_center_server_info = cls(
            v_center_server_id=v_center_server_id,
            name=name,
            connection_state=connection_state,
            port=port,
            connection_error=connection_error,
            product_name=product_name,
            version=version,
            os_type=os_type,
            cloud_director_id=cloud_director_id,
        )

        return v_center_server_info
