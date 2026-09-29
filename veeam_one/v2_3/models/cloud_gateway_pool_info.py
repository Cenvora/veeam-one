from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudGatewayPoolInfo")


@_attrs_define
class CloudGatewayPoolInfo:
    """
    Attributes:
        cloud_gateway_pool_id (int | Unset): ID assigned to a cloud gateway pool.
        cloud_gateway_pool_uid_in_vbr (None | Unset | UUID): UID assigned to a cloud gateway pool in Veeam Cloud
            Connect.
        name (None | str | Unset): Name of a cloud gateway pool.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Cloud Connect server.
        description (None | str | Unset): Description of a cloud gateway pool.
        gateway_count (int | Unset): Number of gateways included in a cloud gateway pool.
    """

    cloud_gateway_pool_id: int | Unset = UNSET
    cloud_gateway_pool_uid_in_vbr: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    backup_server_id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    gateway_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_gateway_pool_id = self.cloud_gateway_pool_id

        cloud_gateway_pool_uid_in_vbr: None | str | Unset
        if isinstance(self.cloud_gateway_pool_uid_in_vbr, Unset):
            cloud_gateway_pool_uid_in_vbr = UNSET
        elif isinstance(self.cloud_gateway_pool_uid_in_vbr, UUID):
            cloud_gateway_pool_uid_in_vbr = str(self.cloud_gateway_pool_uid_in_vbr)
        else:
            cloud_gateway_pool_uid_in_vbr = self.cloud_gateway_pool_uid_in_vbr

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        gateway_count = self.gateway_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_gateway_pool_id is not UNSET:
            field_dict["cloudGatewayPoolId"] = cloud_gateway_pool_id
        if cloud_gateway_pool_uid_in_vbr is not UNSET:
            field_dict["cloudGatewayPoolUidInVbr"] = cloud_gateway_pool_uid_in_vbr
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if description is not UNSET:
            field_dict["description"] = description
        if gateway_count is not UNSET:
            field_dict["gatewayCount"] = gateway_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_gateway_pool_id = d.pop("cloudGatewayPoolId", UNSET)

        def _parse_cloud_gateway_pool_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_gateway_pool_uid_in_vbr_type_0 = UUID(data)

                return cloud_gateway_pool_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cloud_gateway_pool_uid_in_vbr = _parse_cloud_gateway_pool_uid_in_vbr(d.pop("cloudGatewayPoolUidInVbr", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        gateway_count = d.pop("gatewayCount", UNSET)

        cloud_gateway_pool_info = cls(
            cloud_gateway_pool_id=cloud_gateway_pool_id,
            cloud_gateway_pool_uid_in_vbr=cloud_gateway_pool_uid_in_vbr,
            name=name,
            backup_server_id=backup_server_id,
            description=description,
            gateway_count=gateway_count,
        )

        return cloud_gateway_pool_info
