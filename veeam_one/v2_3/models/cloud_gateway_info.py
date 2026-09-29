from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cloud_gateway_state import CloudGatewayState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudGatewayInfo")


@_attrs_define
class CloudGatewayInfo:
    """
    Attributes:
        cloud_gateway_id (Union[Unset, int]): ID assigned to a cloud gateway.
        cloud_gateway_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a cloud gateway in Veeam Cloud Connect.
        name (Union[None, Unset, str]): Name of a cloud gateway.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Cloud Connect server.
        gateway_pool_id (Union[None, Unset, int]): ID assigned to a cloud gateway pool.
        enabled (Union[None, Unset, bool]): Indicates whether a cloud gateway is enabled.
        port (Union[None, Unset, int]): TCP/UDP port for external connections.
        ip (Union[None, Unset, str]): IP address of a cloud gateway.
        state (Union[Unset, CloudGatewayState]):
        upgrade_required (Union[None, Unset, bool]): Indicates whether a cloud gateway must be updated.
    """

    cloud_gateway_id: Union[Unset, int] = UNSET
    cloud_gateway_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    gateway_pool_id: Union[None, Unset, int] = UNSET
    enabled: Union[None, Unset, bool] = UNSET
    port: Union[None, Unset, int] = UNSET
    ip: Union[None, Unset, str] = UNSET
    state: Union[Unset, CloudGatewayState] = UNSET
    upgrade_required: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_gateway_id = self.cloud_gateway_id

        cloud_gateway_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.cloud_gateway_uid_in_vbr, Unset):
            cloud_gateway_uid_in_vbr = UNSET
        elif isinstance(self.cloud_gateway_uid_in_vbr, UUID):
            cloud_gateway_uid_in_vbr = str(self.cloud_gateway_uid_in_vbr)
        else:
            cloud_gateway_uid_in_vbr = self.cloud_gateway_uid_in_vbr

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

        gateway_pool_id: Union[None, Unset, int]
        if isinstance(self.gateway_pool_id, Unset):
            gateway_pool_id = UNSET
        else:
            gateway_pool_id = self.gateway_pool_id

        enabled: Union[None, Unset, bool]
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        ip: Union[None, Unset, str]
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        upgrade_required: Union[None, Unset, bool]
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cloud_gateway_id is not UNSET:
            field_dict["cloudGatewayId"] = cloud_gateway_id
        if cloud_gateway_uid_in_vbr is not UNSET:
            field_dict["cloudGatewayUidInVbr"] = cloud_gateway_uid_in_vbr
        if name is not UNSET:
            field_dict["name"] = name
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if gateway_pool_id is not UNSET:
            field_dict["gatewayPoolId"] = gateway_pool_id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if port is not UNSET:
            field_dict["port"] = port
        if ip is not UNSET:
            field_dict["ip"] = ip
        if state is not UNSET:
            field_dict["state"] = state
        if upgrade_required is not UNSET:
            field_dict["upgradeRequired"] = upgrade_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_gateway_id = d.pop("cloudGatewayId", UNSET)

        def _parse_cloud_gateway_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_gateway_uid_in_vbr_type_0 = UUID(data)

                return cloud_gateway_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        cloud_gateway_uid_in_vbr = _parse_cloud_gateway_uid_in_vbr(d.pop("cloudGatewayUidInVbr", UNSET))

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

        def _parse_gateway_pool_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        gateway_pool_id = _parse_gateway_pool_id(d.pop("gatewayPoolId", UNSET))

        def _parse_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_ip(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ip = _parse_ip(d.pop("ip", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, CloudGatewayState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CloudGatewayState(_state)

        def _parse_upgrade_required(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        cloud_gateway_info = cls(
            cloud_gateway_id=cloud_gateway_id,
            cloud_gateway_uid_in_vbr=cloud_gateway_uid_in_vbr,
            name=name,
            backup_server_id=backup_server_id,
            gateway_pool_id=gateway_pool_id,
            enabled=enabled,
            port=port,
            ip=ip,
            state=state,
            upgrade_required=upgrade_required,
        )

        return cloud_gateway_info
