from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.hyper_v_connection_state import HyperVConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVClusterInfo")


@_attrs_define
class HyperVClusterInfo:
    """
    Attributes:
        host_cluster_id (Union[Unset, int]): ID assigned to a cluster.
        name (Union[None, Unset, str]): Name of a cluster.
        scvmm_server_id (Union[None, Unset, int]): ID assigned to an SCVMM server.
        connection_error (Union[None, Unset, str]): Datails on cluster connection failure.
        connection_state (Union[Unset, HyperVConnectionState]):
        business_view_group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to the Business View groups.
    """

    host_cluster_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    scvmm_server_id: Union[None, Unset, int] = UNSET
    connection_error: Union[None, Unset, str] = UNSET
    connection_state: Union[Unset, HyperVConnectionState] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_cluster_id = self.host_cluster_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        scvmm_server_id: Union[None, Unset, int]
        if isinstance(self.scvmm_server_id, Unset):
            scvmm_server_id = UNSET
        else:
            scvmm_server_id = self.scvmm_server_id

        connection_error: Union[None, Unset, str]
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if host_cluster_id is not UNSET:
            field_dict["hostClusterId"] = host_cluster_id
        if name is not UNSET:
            field_dict["name"] = name
        if scvmm_server_id is not UNSET:
            field_dict["scvmmServerId"] = scvmm_server_id
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_cluster_id = d.pop("hostClusterId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_scvmm_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scvmm_server_id = _parse_scvmm_server_id(d.pop("scvmmServerId", UNSET))

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

        def _parse_business_view_group_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        hyper_v_cluster_info = cls(
            host_cluster_id=host_cluster_id,
            name=name,
            scvmm_server_id=scvmm_server_id,
            connection_error=connection_error,
            connection_state=connection_state,
            business_view_group_ids=business_view_group_ids,
        )

        return hyper_v_cluster_info
