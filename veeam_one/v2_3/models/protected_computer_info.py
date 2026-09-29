import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.protected_computer_operation_mode import ProtectedComputerOperationMode
from ..models.protected_computer_platform import ProtectedComputerPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_group import ProtectionGroup


T = TypeVar("T", bound="ProtectedComputerInfo")


@_attrs_define
class ProtectedComputerInfo:
    """
    Attributes:
        computer_id (Union[None, Unset, int]): ID assigned to a protected computer.
        computer_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected computer in Veeam Backup &
            Replication.
        backup_server_id (Union[None, Unset, int]): UID assigned to a Veeam Backup & Replication server that manages
            computer protection.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
        protection_groups (Union[None, Unset, list['ProtectionGroup']]): Array of protection groups that include a
            protected computer.
        name (Union[None, Unset, str]): Host name of a protected computer.
        ip_addresses (Union[None, Unset, list[str]]): IP addresses of a protected computer.
        platform (Union[Unset, ProtectedComputerPlatform]):
        operation_mode (Union[Unset, ProtectedComputerOperationMode]):
        last_protected_date (Union[None, Unset, datetime.datetime]): Time and date of the latest restore point creation.
    """

    computer_id: Union[None, Unset, int] = UNSET
    computer_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    protection_groups: Union[None, Unset, list["ProtectionGroup"]] = UNSET
    name: Union[None, Unset, str] = UNSET
    ip_addresses: Union[None, Unset, list[str]] = UNSET
    platform: Union[Unset, ProtectedComputerPlatform] = UNSET
    operation_mode: Union[Unset, ProtectedComputerOperationMode] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        computer_id: Union[None, Unset, int]
        if isinstance(self.computer_id, Unset):
            computer_id = UNSET
        else:
            computer_id = self.computer_id

        computer_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.computer_uid_in_vbr, Unset):
            computer_uid_in_vbr = UNSET
        elif isinstance(self.computer_uid_in_vbr, UUID):
            computer_uid_in_vbr = str(self.computer_uid_in_vbr)
        else:
            computer_uid_in_vbr = self.computer_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

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

        ip_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        operation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.operation_mode, Unset):
            operation_mode = self.operation_mode.value

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if computer_id is not UNSET:
            field_dict["computerId"] = computer_id
        if computer_uid_in_vbr is not UNSET:
            field_dict["computerUidInVbr"] = computer_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if name is not UNSET:
            field_dict["name"] = name
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if platform is not UNSET:
            field_dict["platform"] = platform
        if operation_mode is not UNSET:
            field_dict["operationMode"] = operation_mode
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_group import ProtectionGroup

        d = dict(src_dict)

        def _parse_computer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        computer_id = _parse_computer_id(d.pop("computerId", UNSET))

        def _parse_computer_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                computer_uid_in_vbr_type_0 = UUID(data)

                return computer_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        computer_uid_in_vbr = _parse_computer_uid_in_vbr(d.pop("computerUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

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

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ProtectedComputerPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProtectedComputerPlatform(_platform)

        _operation_mode = d.pop("operationMode", UNSET)
        operation_mode: Union[Unset, ProtectedComputerOperationMode]
        if isinstance(_operation_mode, Unset):
            operation_mode = UNSET
        else:
            operation_mode = ProtectedComputerOperationMode(_operation_mode)

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

        protected_computer_info = cls(
            computer_id=computer_id,
            computer_uid_in_vbr=computer_uid_in_vbr,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            protection_groups=protection_groups,
            name=name,
            ip_addresses=ip_addresses,
            platform=platform,
            operation_mode=operation_mode,
            last_protected_date=last_protected_date,
        )

        return protected_computer_info
