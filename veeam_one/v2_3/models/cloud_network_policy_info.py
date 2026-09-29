from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_job_status import BackupJobStatus
from ..models.cloud_network_instance_type import CloudNetworkInstanceType
from ..models.cloud_networks_platform import CloudNetworksPlatform
from ..models.policy_state import PolicyState
from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudNetworkPolicyInfo")


@_attrs_define
class CloudNetworkPolicyInfo:
    """
    Attributes:
        policy_uid (UUID | Unset): UID assigned to a policy.
        policy_name (None | str | Unset): Name of a policy.
        state (PolicyState | Unset):
        platform (CloudNetworksPlatform | Unset):
        instance_type (CloudNetworkInstanceType | Unset):
        backup_server_id (int | Unset): ID assigned to a Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Backup & Replication server.
        last_backup_date (datetime.datetime | None | Unset): Date and time when the latest restore point was created.
        last_backup_status (BackupJobStatus | Unset):
    """

    policy_uid: UUID | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    state: PolicyState | Unset = UNSET
    platform: CloudNetworksPlatform | Unset = UNSET
    instance_type: CloudNetworkInstanceType | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    last_backup_date: datetime.datetime | None | Unset = UNSET
    last_backup_status: BackupJobStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_uid: str | Unset = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name: None | str | Unset
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        instance_type: str | Unset = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.value

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        last_backup_date: None | str | Unset
        if isinstance(self.last_backup_date, Unset):
            last_backup_date = UNSET
        elif isinstance(self.last_backup_date, datetime.datetime):
            last_backup_date = self.last_backup_date.isoformat()
        else:
            last_backup_date = self.last_backup_date

        last_backup_status: str | Unset = UNSET
        if not isinstance(self.last_backup_status, Unset):
            last_backup_status = self.last_backup_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if state is not UNSET:
            field_dict["state"] = state
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if last_backup_date is not UNSET:
            field_dict["lastBackupDate"] = last_backup_date
        if last_backup_status is not UNSET:
            field_dict["lastBackupStatus"] = last_backup_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _policy_uid = d.pop("policyUid", UNSET)
        policy_uid: UUID | Unset
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        def _parse_policy_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _state = d.pop("state", UNSET)
        state: PolicyState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PolicyState(_state)

        _platform = d.pop("platform", UNSET)
        platform: CloudNetworksPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudNetworksPlatform(_platform)

        _instance_type = d.pop("instanceType", UNSET)
        instance_type: CloudNetworkInstanceType | Unset
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = CloudNetworkInstanceType(_instance_type)

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_last_backup_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_backup_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_backup_date = _parse_last_backup_date(d.pop("lastBackupDate", UNSET))

        _last_backup_status = d.pop("lastBackupStatus", UNSET)
        last_backup_status: BackupJobStatus | Unset
        if isinstance(_last_backup_status, Unset):
            last_backup_status = UNSET
        else:
            last_backup_status = BackupJobStatus(_last_backup_status)

        cloud_network_policy_info = cls(
            policy_uid=policy_uid,
            policy_name=policy_name,
            state=state,
            platform=platform,
            instance_type=instance_type,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            last_backup_date=last_backup_date,
            last_backup_status=last_backup_status,
        )

        return cloud_network_policy_info
