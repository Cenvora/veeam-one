from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupProxyPoolInfo")


@_attrs_define
class Vb365BackupProxyPoolInfo:
    """
    Attributes:
        backup_proxy_pool_id (int | Unset): ID assigned to a backup proxy pool.
        backup_proxy_pool_uid_in_vb_365 (None | Unset | UUID): UID assigned to a backup proxy pool in Veeam Backup for
            Microsoft 365.
        name (None | str | Unset): Name of a backup proxy pool.
        vb_365_server_id (int | None | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
    """

    backup_proxy_pool_id: int | Unset = UNSET
    backup_proxy_pool_uid_in_vb_365: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    vb_365_server_id: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_proxy_pool_id = self.backup_proxy_pool_id

        backup_proxy_pool_uid_in_vb_365: None | str | Unset
        if isinstance(self.backup_proxy_pool_uid_in_vb_365, Unset):
            backup_proxy_pool_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_proxy_pool_uid_in_vb_365, UUID):
            backup_proxy_pool_uid_in_vb_365 = str(self.backup_proxy_pool_uid_in_vb_365)
        else:
            backup_proxy_pool_uid_in_vb_365 = self.backup_proxy_pool_uid_in_vb_365

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vb_365_server_id: int | None | Unset
        if isinstance(self.vb_365_server_id, Unset):
            vb_365_server_id = UNSET
        else:
            vb_365_server_id = self.vb_365_server_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_proxy_pool_id is not UNSET:
            field_dict["backupProxyPoolId"] = backup_proxy_pool_id
        if backup_proxy_pool_uid_in_vb_365 is not UNSET:
            field_dict["backupProxyPoolUidInVb365"] = backup_proxy_pool_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_proxy_pool_id = d.pop("backupProxyPoolId", UNSET)

        def _parse_backup_proxy_pool_uid_in_vb_365(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_proxy_pool_uid_in_vb_365_type_0 = UUID(data)

                return backup_proxy_pool_uid_in_vb_365_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_proxy_pool_uid_in_vb_365 = _parse_backup_proxy_pool_uid_in_vb_365(
            d.pop("backupProxyPoolUidInVb365", UNSET)
        )

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_vb_365_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vb_365_server_id = _parse_vb_365_server_id(d.pop("vb365ServerId", UNSET))

        vb_365_backup_proxy_pool_info = cls(
            backup_proxy_pool_id=backup_proxy_pool_id,
            backup_proxy_pool_uid_in_vb_365=backup_proxy_pool_uid_in_vb_365,
            name=name,
            vb_365_server_id=vb_365_server_id,
        )

        return vb_365_backup_proxy_pool_info
