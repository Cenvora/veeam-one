from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudGatewayPoolInfo")


@_attrs_define
class CloudGatewayPoolInfo:
    """
    Attributes:
        cloud_gateway_pool_id (Union[Unset, int]): ID assigned to a cloud gateway pool.
        cloud_gateway_pool_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a cloud gateway pool in Veeam Cloud
            Connect.
        name (Union[None, Unset, str]): Name of a cloud gateway pool.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Cloud Connect server.
        description (Union[None, Unset, str]): Description of a cloud gateway pool.
        gateway_count (Union[Unset, int]): Number of gateways included in a cloud gateway pool.
    """

    cloud_gateway_pool_id: Union[Unset, int] = UNSET
    cloud_gateway_pool_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    gateway_count: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_gateway_pool_id = self.cloud_gateway_pool_id

        cloud_gateway_pool_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.cloud_gateway_pool_uid_in_vbr, Unset):
            cloud_gateway_pool_uid_in_vbr = UNSET
        elif isinstance(self.cloud_gateway_pool_uid_in_vbr, UUID):
            cloud_gateway_pool_uid_in_vbr = str(self.cloud_gateway_pool_uid_in_vbr)
        else:
            cloud_gateway_pool_uid_in_vbr = self.cloud_gateway_pool_uid_in_vbr

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        description: Union[None, Unset, str]
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

        def _parse_cloud_gateway_pool_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_gateway_pool_uid_in_vbr_type_0 = UUID(data)

                return cloud_gateway_pool_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_gateway_pool_uid_in_vbr = _parse_cloud_gateway_pool_uid_in_vbr(d.pop("cloudGatewayPoolUidInVbr", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

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
