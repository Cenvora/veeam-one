from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.hyper_v_connection_state import HyperVConnectionState
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVClusterInfo")


@_attrs_define
class HyperVClusterInfo:
    """
    Attributes:
        host_cluster_id (int | Unset): ID assigned to a cluster.
        name (None | str | Unset): Name of a cluster.
        scvmm_server_id (int | None | Unset): ID assigned to an SCVMM server.
        connection_error (None | str | Unset): Datails on cluster connection failure.
        connection_state (HyperVConnectionState | Unset):
        business_view_group_ids (list[int] | None | Unset): Array of IDs assigned to the Business View groups.
    """

    host_cluster_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    scvmm_server_id: int | None | Unset = UNSET
    connection_error: None | str | Unset = UNSET
    connection_state: HyperVConnectionState | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_cluster_id = self.host_cluster_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        scvmm_server_id: int | None | Unset
        if isinstance(self.scvmm_server_id, Unset):
            scvmm_server_id = UNSET
        else:
            scvmm_server_id = self.scvmm_server_id

        connection_error: None | str | Unset
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        business_view_group_ids: list[int] | None | Unset
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_scvmm_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scvmm_server_id = _parse_scvmm_server_id(d.pop("scvmmServerId", UNSET))

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

        def _parse_business_view_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

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
