import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.backup_agent_status import BackupAgentStatus
from ..models.computer_operation_mode import ComputerOperationMode
from ..models.computer_platform import ComputerPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_group import ProtectionGroup


T = TypeVar("T", bound="BackupAgentInfo")


@_attrs_define
class BackupAgentInfo:
    """
    Attributes:
        backup_agent_id (Union[Unset, int]): ID assigned to a Veeam backup agent.
        backup_agent_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a Veeam backup agent in Veeam Backup &
            Replication.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server that manages a Veeam
            backup agent.
        protection_groups (Union[None, Unset, list['ProtectionGroup']]): Array of protection groups that include the
            Veeam backup agent.
        name (Union[None, Unset, str]): Name of a Veeam backup agent.
        platform (Union[Unset, ComputerPlatform]):
        operation_mode (Union[Unset, ComputerOperationMode]):
        status (Union[Unset, BackupAgentStatus]):
        version (Union[None, Unset, str]): Version of a Veeam backup agent.
        ip_addresses (Union[None, Unset, list[str]]): Array of IP addresses of a machine on which Veeam backup agent is
            installed.
        last_protected_date (Union[None, Unset, datetime.datetime]): Date and time of the latest successful run of a job
            that protects a Veeam backup agent.
        business_view_group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to the Business View groups.
    """

    backup_agent_id: Union[Unset, int] = UNSET
    backup_agent_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    protection_groups: Union[None, Unset, list["ProtectionGroup"]] = UNSET
    name: Union[None, Unset, str] = UNSET
    platform: Union[Unset, ComputerPlatform] = UNSET
    operation_mode: Union[Unset, ComputerOperationMode] = UNSET
    status: Union[Unset, BackupAgentStatus] = UNSET
    version: Union[None, Unset, str] = UNSET
    ip_addresses: Union[None, Unset, list[str]] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET
    business_view_group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_agent_id = self.backup_agent_id

        backup_agent_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.backup_agent_uid_in_vbr, Unset):
            backup_agent_uid_in_vbr = UNSET
        elif isinstance(self.backup_agent_uid_in_vbr, UUID):
            backup_agent_uid_in_vbr = str(self.backup_agent_uid_in_vbr)
        else:
            backup_agent_uid_in_vbr = self.backup_agent_uid_in_vbr

        backup_server_id = self.backup_server_id

        protection_groups: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.protection_groups, Unset):
            protection_groups = UNSET
        elif isinstance(self.protection_groups, list):
            protection_groups = []
            for protection_groups_type_0_item_data in self.protection_groups:
                protection_groups_type_0_item = protection_groups_type_0_item_data.to_dict()
                protection_groups.append(protection_groups_type_0_item)

        else:
            protection_groups = self.protection_groups

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        ip_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        business_view_group_ids: Union[None, Unset, list[int]]
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_agent_id is not UNSET:
            field_dict["backupAgentId"] = backup_agent_id
        if backup_agent_uid_in_vbr is not UNSET:
            field_dict["backupAgentUidInVbr"] = backup_agent_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_group import ProtectionGroup

        d = dict(src_dict)
        backup_agent_id = d.pop("backupAgentId", UNSET)

        def _parse_backup_agent_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_agent_uid_in_vbr_type_0 = UUID(data)

                return backup_agent_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_agent_uid_in_vbr = _parse_backup_agent_uid_in_vbr(d.pop("backupAgentUidInVbr", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_protection_groups(data: object) -> Union[None, Unset, list["ProtectionGroup"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_groups_type_0 = []
                _protection_groups_type_0 = data
                for protection_groups_type_0_item_data in _protection_groups_type_0:
                    protection_groups_type_0_item = ProtectionGroup.from_dict(protection_groups_type_0_item_data)

                    protection_groups_type_0.append(protection_groups_type_0_item)

                return protection_groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ProtectionGroup"]], data)

        protection_groups = _parse_protection_groups(d.pop("protectionGroups", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ComputerPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ComputerPlatform(_platform)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, ComputerOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = ComputerOperationMode(_operation_mode)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupAgentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupAgentStatus(_status)

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_ip_addresses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        def _parse_last_protected_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = isoparse(data)

                return last_protected_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

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

        backup_agent_info = cls(
            backup_agent_id=backup_agent_id,
            backup_agent_uid_in_vbr=backup_agent_uid_in_vbr,
            backup_server_id=backup_server_id,
            protection_groups=protection_groups,
            name=name,
            platform=platform,
            operation_mode=operation_mode,
            status=status,
            version=version,
            ip_addresses=ip_addresses,
            last_protected_date=last_protected_date,
            business_view_group_ids=business_view_group_ids,
        )

        return backup_agent_info
