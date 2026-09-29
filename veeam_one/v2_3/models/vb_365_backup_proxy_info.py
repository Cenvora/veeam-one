from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_internet_proxy_type import Vb365InternetProxyType
from ..models.vb_365_proxy_status import Vb365ProxyStatus
from ..models.vb_365_proxy_type import Vb365ProxyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupProxyInfo")


@_attrs_define
class Vb365BackupProxyInfo:
    """
    Attributes:
        backup_proxy_id (int | Unset): ID assigned to a backup proxy server.
        backup_proxy_uid_in_vb_365 (None | Unset | UUID): UID assigned to a backup proxy server in Veeam Backup for
            Microsoft 365.
        backup_proxy_pool_uid_in_vb_365 (None | Unset | UUID): UID assigned to a backup proxy pool.
        vb_365_server_id (int | None | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        type_ (Vb365ProxyType | Unset):
        use_internet_proxy (bool | None | Unset): Indicates whether Veeam Backup for Microsoft 365 proxy uses an
            internet proxy server.
        internet_proxy_type (Vb365InternetProxyType | Unset):
        host_name (None | str | Unset): DNS name or IP address of a backup proxy server.
        description (None | str | Unset): Description of a backup proxy server.
        port (int | None | Unset): Port number used to connect to a backup proxy server.
        threads_number (int | None | Unset): Number of threads that a backup proxy server can process.
        enable_network_throttling (bool | None | Unset): Indicates whether network throttling is enabled for a backup
            proxy server.
        status (Vb365ProxyStatus | Unset):
        repository_ids (list[int] | None | Unset): Array of IDs assigned to related Veeam Backup for Microsoft 365
            repositories.
    """

    backup_proxy_id: int | Unset = UNSET
    backup_proxy_uid_in_vb_365: None | Unset | UUID = UNSET
    backup_proxy_pool_uid_in_vb_365: None | Unset | UUID = UNSET
    vb_365_server_id: int | None | Unset = UNSET
    type_: Vb365ProxyType | Unset = UNSET
    use_internet_proxy: bool | None | Unset = UNSET
    internet_proxy_type: Vb365InternetProxyType | Unset = UNSET
    host_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    port: int | None | Unset = UNSET
    threads_number: int | None | Unset = UNSET
    enable_network_throttling: bool | None | Unset = UNSET
    status: Vb365ProxyStatus | Unset = UNSET
    repository_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_proxy_id = self.backup_proxy_id

        backup_proxy_uid_in_vb_365: None | str | Unset
        if isinstance(self.backup_proxy_uid_in_vb_365, Unset):
            backup_proxy_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_proxy_uid_in_vb_365, UUID):
            backup_proxy_uid_in_vb_365 = str(self.backup_proxy_uid_in_vb_365)
        else:
            backup_proxy_uid_in_vb_365 = self.backup_proxy_uid_in_vb_365

        backup_proxy_pool_uid_in_vb_365: None | str | Unset
        if isinstance(self.backup_proxy_pool_uid_in_vb_365, Unset):
            backup_proxy_pool_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_proxy_pool_uid_in_vb_365, UUID):
            backup_proxy_pool_uid_in_vb_365 = str(self.backup_proxy_pool_uid_in_vb_365)
        else:
            backup_proxy_pool_uid_in_vb_365 = self.backup_proxy_pool_uid_in_vb_365

        vb_365_server_id: int | None | Unset
        if isinstance(self.vb_365_server_id, Unset):
            vb_365_server_id = UNSET
        else:
            vb_365_server_id = self.vb_365_server_id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        use_internet_proxy: bool | None | Unset
        if isinstance(self.use_internet_proxy, Unset):
            use_internet_proxy = UNSET
        else:
            use_internet_proxy = self.use_internet_proxy

        internet_proxy_type: str | Unset = UNSET
        if not isinstance(self.internet_proxy_type, Unset):
            internet_proxy_type = self.internet_proxy_type.value

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        port: int | None | Unset
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        threads_number: int | None | Unset
        if isinstance(self.threads_number, Unset):
            threads_number = UNSET
        else:
            threads_number = self.threads_number

        enable_network_throttling: bool | None | Unset
        if isinstance(self.enable_network_throttling, Unset):
            enable_network_throttling = UNSET
        else:
            enable_network_throttling = self.enable_network_throttling

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        repository_ids: list[int] | None | Unset
        if isinstance(self.repository_ids, Unset):
            repository_ids = UNSET
        elif isinstance(self.repository_ids, list):
            repository_ids = self.repository_ids

        else:
            repository_ids = self.repository_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_proxy_id is not UNSET:
            field_dict["backupProxyId"] = backup_proxy_id
        if backup_proxy_uid_in_vb_365 is not UNSET:
            field_dict["backupProxyUidInVb365"] = backup_proxy_uid_in_vb_365
        if backup_proxy_pool_uid_in_vb_365 is not UNSET:
            field_dict["backupProxyPoolUidInVb365"] = backup_proxy_pool_uid_in_vb_365
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if use_internet_proxy is not UNSET:
            field_dict["useInternetProxy"] = use_internet_proxy
        if internet_proxy_type is not UNSET:
            field_dict["internetProxyType"] = internet_proxy_type
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if description is not UNSET:
            field_dict["description"] = description
        if port is not UNSET:
            field_dict["port"] = port
        if threads_number is not UNSET:
            field_dict["threadsNumber"] = threads_number
        if enable_network_throttling is not UNSET:
            field_dict["enableNetworkThrottling"] = enable_network_throttling
        if status is not UNSET:
            field_dict["status"] = status
        if repository_ids is not UNSET:
            field_dict["repositoryIds"] = repository_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_proxy_id = d.pop("backupProxyId", UNSET)

        def _parse_backup_proxy_uid_in_vb_365(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_proxy_uid_in_vb_365_type_0 = UUID(data)

                return backup_proxy_uid_in_vb_365_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        backup_proxy_uid_in_vb_365 = _parse_backup_proxy_uid_in_vb_365(d.pop("backupProxyUidInVb365", UNSET))

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

        def _parse_vb_365_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vb_365_server_id = _parse_vb_365_server_id(d.pop("vb365ServerId", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Vb365ProxyType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365ProxyType(_type_)

        def _parse_use_internet_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_internet_proxy = _parse_use_internet_proxy(d.pop("useInternetProxy", UNSET))

        _internet_proxy_type = d.pop("internetProxyType", UNSET)
        internet_proxy_type: Vb365InternetProxyType | Unset
        if isinstance(_internet_proxy_type, Unset):
            internet_proxy_type = UNSET
        else:
            internet_proxy_type = Vb365InternetProxyType(_internet_proxy_type)

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_port(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_threads_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        threads_number = _parse_threads_number(d.pop("threadsNumber", UNSET))

        def _parse_enable_network_throttling(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_network_throttling = _parse_enable_network_throttling(d.pop("enableNetworkThrottling", UNSET))

        _status = d.pop("status", UNSET)
        status: Vb365ProxyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365ProxyStatus(_status)

        def _parse_repository_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repository_ids_type_0 = cast(list[int], data)

                return repository_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        repository_ids = _parse_repository_ids(d.pop("repositoryIds", UNSET))

        vb_365_backup_proxy_info = cls(
            backup_proxy_id=backup_proxy_id,
            backup_proxy_uid_in_vb_365=backup_proxy_uid_in_vb_365,
            backup_proxy_pool_uid_in_vb_365=backup_proxy_pool_uid_in_vb_365,
            vb_365_server_id=vb_365_server_id,
            type_=type_,
            use_internet_proxy=use_internet_proxy,
            internet_proxy_type=internet_proxy_type,
            host_name=host_name,
            description=description,
            port=port,
            threads_number=threads_number,
            enable_network_throttling=enable_network_throttling,
            status=status,
            repository_ids=repository_ids,
        )

        return vb_365_backup_proxy_info
