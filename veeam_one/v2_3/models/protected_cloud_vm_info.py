from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cloud_platform import CloudPlatform
from ..models.cloud_vm_instance_type import CloudVmInstanceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedCloudVmInfo")


@_attrs_define
class ProtectedCloudVmInfo:
    """
    Attributes:
        instance_id (None | str | Unset): Resource of a cloud VM.
        name (None | str | Unset): Name of a cloud VM.
        cloud_vm_uid_in_vbr (UUID | Unset): ID assigned to a cloud VM in Veeam Backup & Replication.
        platform (CloudPlatform | Unset):
        instance_type (CloudVmInstanceType | Unset):
        region (None | str | Unset): Region of a cloud VM.
        ip_addresses (None | str | Unset): IP address of a cloud VM.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server that manages cloud VM
            protection.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        last_protection_date (datetime.datetime | None | Unset): Date and time when the latest restore point was
            created.
        size_bytes (int | None | Unset): Size of a VM, in bytes.
        aws_account_id (None | str | Unset): ID of an AWS account.
        aws_account_alias (None | str | Unset): Alias of an AWS account.
    """

    instance_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    cloud_vm_uid_in_vbr: UUID | Unset = UNSET
    platform: CloudPlatform | Unset = UNSET
    instance_type: CloudVmInstanceType | Unset = UNSET
    region: None | str | Unset = UNSET
    ip_addresses: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    last_protection_date: datetime.datetime | None | Unset = UNSET
    size_bytes: int | None | Unset = UNSET
    aws_account_id: None | str | Unset = UNSET
    aws_account_alias: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        instance_id: None | str | Unset
        if isinstance(self.instance_id, Unset):
            instance_id = UNSET
        else:
            instance_id = self.instance_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        cloud_vm_uid_in_vbr: str | Unset = UNSET
        if not isinstance(self.cloud_vm_uid_in_vbr, Unset):
            cloud_vm_uid_in_vbr = str(self.cloud_vm_uid_in_vbr)

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        instance_type: str | Unset = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.value

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        ip_addresses: None | str | Unset
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        else:
            ip_addresses = self.ip_addresses

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        last_protection_date: None | str | Unset
        if isinstance(self.last_protection_date, Unset):
            last_protection_date = UNSET
        elif isinstance(self.last_protection_date, datetime.datetime):
            last_protection_date = self.last_protection_date.isoformat()
        else:
            last_protection_date = self.last_protection_date

        size_bytes: int | None | Unset
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        aws_account_id: None | str | Unset
        if isinstance(self.aws_account_id, Unset):
            aws_account_id = UNSET
        else:
            aws_account_id = self.aws_account_id

        aws_account_alias: None | str | Unset
        if isinstance(self.aws_account_alias, Unset):
            aws_account_alias = UNSET
        else:
            aws_account_alias = self.aws_account_alias

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if name is not UNSET:
            field_dict["name"] = name
        if cloud_vm_uid_in_vbr is not UNSET:
            field_dict["cloudVmUidInVbr"] = cloud_vm_uid_in_vbr
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if region is not UNSET:
            field_dict["region"] = region
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if last_protection_date is not UNSET:
            field_dict["lastProtectionDate"] = last_protection_date
        if size_bytes is not UNSET:
            field_dict["sizeBytes"] = size_bytes
        if aws_account_id is not UNSET:
            field_dict["awsAccountID"] = aws_account_id
        if aws_account_alias is not UNSET:
            field_dict["awsAccountAlias"] = aws_account_alias

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_instance_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance_id = _parse_instance_id(d.pop("instanceId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _cloud_vm_uid_in_vbr = d.pop("cloudVmUidInVbr", UNSET)
        cloud_vm_uid_in_vbr: UUID | Unset
        if isinstance(_cloud_vm_uid_in_vbr, Unset):
            cloud_vm_uid_in_vbr = UNSET
        else:
            cloud_vm_uid_in_vbr = UUID(_cloud_vm_uid_in_vbr)

        _platform = d.pop("platform", UNSET)
        platform: CloudPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudPlatform(_platform)

        _instance_type = d.pop("instanceType", UNSET)
        instance_type: CloudVmInstanceType | Unset
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = CloudVmInstanceType(_instance_type)

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_ip_addresses(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_last_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protection_date = _parse_last_protection_date(d.pop("lastProtectionDate", UNSET))

        def _parse_size_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_bytes = _parse_size_bytes(d.pop("sizeBytes", UNSET))

        def _parse_aws_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_account_id = _parse_aws_account_id(d.pop("awsAccountID", UNSET))

        def _parse_aws_account_alias(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        aws_account_alias = _parse_aws_account_alias(d.pop("awsAccountAlias", UNSET))

        protected_cloud_vm_info = cls(
            instance_id=instance_id,
            name=name,
            cloud_vm_uid_in_vbr=cloud_vm_uid_in_vbr,
            platform=platform,
            instance_type=instance_type,
            region=region,
            ip_addresses=ip_addresses,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            last_protection_date=last_protection_date,
            size_bytes=size_bytes,
            aws_account_id=aws_account_id,
            aws_account_alias=aws_account_alias,
        )

        return protected_cloud_vm_info
