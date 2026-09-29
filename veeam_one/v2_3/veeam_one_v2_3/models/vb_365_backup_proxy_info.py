from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
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
        backup_proxy_id (Union[Unset, int]): ID assigned to a backup proxy server.
        backup_proxy_uid_in_vb_365 (Union[None, UUID, Unset]): UID assigned to a backup proxy server in Veeam Backup for
            Microsoft 365.
        backup_proxy_pool_uid_in_vb_365 (Union[None, UUID, Unset]): UID assigned to a backup proxy pool.
        vb_365_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        type_ (Union[Unset, Vb365ProxyType]):
        use_internet_proxy (Union[None, Unset, bool]): Indicates whether Veeam Backup for Microsoft 365 proxy uses an
            internet proxy server.
        internet_proxy_type (Union[Unset, Vb365InternetProxyType]):
        host_name (Union[None, Unset, str]): DNS name or IP address of a backup proxy server.
        description (Union[None, Unset, str]): Description of a backup proxy server.
        port (Union[None, Unset, int]): Port number used to connect to a backup proxy server.
        threads_number (Union[None, Unset, int]): Number of threads that a backup proxy server can process.
        enable_network_throttling (Union[None, Unset, bool]): Indicates whether network throttling is enabled for a
            backup proxy server.
        status (Union[Unset, Vb365ProxyStatus]):
        repository_ids (Union[None, Unset, list[int]]): Array of IDs assigned to related Veeam Backup for Microsoft 365
            repositories.
    """

    backup_proxy_id: Union[Unset, int] = UNSET
    backup_proxy_uid_in_vb_365: Union[None, UUID, Unset] = UNSET
    backup_proxy_pool_uid_in_vb_365: Union[None, UUID, Unset] = UNSET
    vb_365_server_id: Union[None, Unset, int] = UNSET
    type_: Union[Unset, Vb365ProxyType] = UNSET
    use_internet_proxy: Union[None, Unset, bool] = UNSET
    internet_proxy_type: Union[Unset, Vb365InternetProxyType] = UNSET
    host_name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    port: Union[None, Unset, int] = UNSET
    threads_number: Union[None, Unset, int] = UNSET
    enable_network_throttling: Union[None, Unset, bool] = UNSET
    status: Union[Unset, Vb365ProxyStatus] = UNSET
    repository_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_proxy_id = self.backup_proxy_id

        backup_proxy_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.backup_proxy_uid_in_vb_365, Unset):
            backup_proxy_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_proxy_uid_in_vb_365, UUID):
            backup_proxy_uid_in_vb_365 = str(self.backup_proxy_uid_in_vb_365)
        else:
            backup_proxy_uid_in_vb_365 = self.backup_proxy_uid_in_vb_365

        backup_proxy_pool_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.backup_proxy_pool_uid_in_vb_365, Unset):
            backup_proxy_pool_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_proxy_pool_uid_in_vb_365, UUID):
            backup_proxy_pool_uid_in_vb_365 = str(self.backup_proxy_pool_uid_in_vb_365)
        else:
            backup_proxy_pool_uid_in_vb_365 = self.backup_proxy_pool_uid_in_vb_365

        vb_365_server_id: Union[None, Unset, int]
        if isinstance(self.vb_365_server_id, Unset):
            vb_365_server_id = UNSET
        else:
            vb_365_server_id = self.vb_365_server_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        use_internet_proxy: Union[None, Unset, bool]
        if isinstance(self.use_internet_proxy, Unset):
            use_internet_proxy = UNSET
        else:
            use_internet_proxy = self.use_internet_proxy

        internet_proxy_type: Union[Unset, str] = UNSET
        if not isinstance(self.internet_proxy_type, Unset):
            internet_proxy_type = self.internet_proxy_type.value

        host_name: Union[None, Unset, str]
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        port: Union[None, Unset, int]
        if isinstance(self.port, Unset):
            port = UNSET
        else:
            port = self.port

        threads_number: Union[None, Unset, int]
        if isinstance(self.threads_number, Unset):
            threads_number = UNSET
        else:
            threads_number = self.threads_number

        enable_network_throttling: Union[None, Unset, bool]
        if isinstance(self.enable_network_throttling, Unset):
            enable_network_throttling = UNSET
        else:
            enable_network_throttling = self.enable_network_throttling

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        repository_ids: Union[None, Unset, list[int]]
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

        def _parse_backup_proxy_uid_in_vb_365(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_proxy_uid_in_vb_365_type_0 = UUID(data)

                return backup_proxy_uid_in_vb_365_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_proxy_uid_in_vb_365 = _parse_backup_proxy_uid_in_vb_365(d.pop("backupProxyUidInVb365", UNSET))

        def _parse_backup_proxy_pool_uid_in_vb_365(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_proxy_pool_uid_in_vb_365_type_0 = UUID(data)

                return backup_proxy_pool_uid_in_vb_365_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_proxy_pool_uid_in_vb_365 = _parse_backup_proxy_pool_uid_in_vb_365(
            d.pop("backupProxyPoolUidInVb365", UNSET)
        )

        def _parse_vb_365_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vb_365_server_id = _parse_vb_365_server_id(d.pop("vb365ServerId", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, Vb365ProxyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365ProxyType(_type_)

        def _parse_use_internet_proxy(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        use_internet_proxy = _parse_use_internet_proxy(d.pop("useInternetProxy", UNSET))

        _internet_proxy_type = d.pop("internetProxyType", UNSET)
        internet_proxy_type: Union[Unset, Vb365InternetProxyType]
        if isinstance(_internet_proxy_type, Unset):
            internet_proxy_type = UNSET
        else:
            internet_proxy_type = Vb365InternetProxyType(_internet_proxy_type)

        def _parse_host_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_port(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        port = _parse_port(d.pop("port", UNSET))

        def _parse_threads_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        threads_number = _parse_threads_number(d.pop("threadsNumber", UNSET))

        def _parse_enable_network_throttling(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enable_network_throttling = _parse_enable_network_throttling(d.pop("enableNetworkThrottling", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, Vb365ProxyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = Vb365ProxyStatus(_status)

        def _parse_repository_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                repository_ids_type_0 = cast(list[int], data)

                return repository_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

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
