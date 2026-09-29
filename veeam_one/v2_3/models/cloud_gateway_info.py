from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cloud_gateway_state import CloudGatewayState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudGatewayInfo")


@_attrs_define
class CloudGatewayInfo:
    """
    Attributes:
        cloud_gateway_id (int | Unset): ID assigned to a cloud gateway.
        cloud_gateway_uid_in_vbr (None | Unset | UUID): UID assigned to a cloud gateway in Veeam Cloud Connect.
        name (None | str | Unset): Name of a cloud gateway.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Cloud Connect server.
        gateway_pool_id (int | None | Unset): ID assigned to a cloud gateway pool.
        enabled (bool | None | Unset): Indicates whether a cloud gateway is enabled.
        port (int | None | Unset): TCP/UDP port for external connections.
        ip (None | str | Unset): IP address of a cloud gateway.
        state (CloudGatewayState | Unset):
        upgrade_required (bool | None | Unset): Indicates whether a cloud gateway must be updated.
    """

    cloud_gateway_id: int | Unset = UNSET
    cloud_gateway_uid_in_vbr: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    backup_server_id: int | None | Unset = UNSET
    gateway_pool_id: int | None | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    port: int | None | Unset = UNSET
    ip: None | str | Unset = UNSET
    state: CloudGatewayState | Unset = UNSET
    upgrade_required: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cloud_gateway_id = self.cloud_gateway_id

        cloud_gateway_uid_in_vbr: None | str | Unset
        if isinstance(self.cloud_gateway_uid_in_vbr, Unset):
            cloud_gateway_uid_in_vbr = UNSET
        elif isinstance(self.cloud_gateway_uid_in_vbr, UUID):
            cloud_gateway_uid_in_vbr = str(self.cloud_gateway_uid_in_vbr)
        else:
            cloud_gateway_uid_in_vbr = self.cloud_gateway_uid_in_vbr

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

        gateway_pool_id: int | None | Unset
        if isinstance(self.gateway_pool_id, Unset):
            gateway_pool_id = UNSET
        else:
            gateway_pool_id = self.gateway_pool_id

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        upgrade_required: bool | None | Unset
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

        def _parse_cloud_gateway_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cloud_gateway_uid_in_vbr_type_0 = UUID(data)

                return cloud_gateway_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cloud_gateway_uid_in_vbr = _parse_cloud_gateway_uid_in_vbr(d.pop("cloudGatewayUidInVbr", UNSET))

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

        def _parse_gateway_pool_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        gateway_pool_id = _parse_gateway_pool_id(d.pop("gatewayPoolId", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        _state = d.pop("state", UNSET)
        state: CloudGatewayState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = CloudGatewayState(_state)

        def _parse_upgrade_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

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
