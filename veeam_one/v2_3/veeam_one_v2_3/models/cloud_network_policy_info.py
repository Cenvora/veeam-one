import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

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
        policy_uid (Union[Unset, UUID]): UID assigned to a policy.
        policy_name (Union[None, Unset, str]): Name of a policy.
        state (Union[Unset, PolicyState]):
        platform (Union[Unset, CloudNetworksPlatform]):
        instance_type (Union[Unset, CloudNetworkInstanceType]):
        backup_server_id (Union[Unset, int]): ID assigned to a Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Backup & Replication server.
        last_backup_date (Union[None, Unset, datetime.datetime]): Date and time when the latest restore point was
            created.
        last_backup_status (Union[Unset, BackupJobStatus]):
    """

    policy_uid: Union[Unset, UUID] = UNSET
    policy_name: Union[None, Unset, str] = UNSET
    state: Union[Unset, PolicyState] = UNSET
    platform: Union[Unset, CloudNetworksPlatform] = UNSET
    instance_type: Union[Unset, CloudNetworkInstanceType] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    last_backup_date: Union[None, Unset, datetime.datetime] = UNSET
    last_backup_status: Union[Unset, BackupJobStatus] = UNSET

    def to_dict(self) -> dict[str, Any]:
        policy_uid: Union[Unset, str] = UNSET
        if not isinstance(self.policy_uid, Unset):
            policy_uid = str(self.policy_uid)

        policy_name: Union[None, Unset, str]
        if isinstance(self.policy_name, Unset):
            policy_name = UNSET
        else:
            policy_name = self.policy_name

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        instance_type: Union[Unset, str] = UNSET
        if not isinstance(self.instance_type, Unset):
            instance_type = self.instance_type.value

        backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        last_backup_date: Union[None, Unset, str]
        if isinstance(self.last_backup_date, Unset):
            last_backup_date = UNSET
        elif isinstance(self.last_backup_date, datetime.datetime):
            last_backup_date = self.last_backup_date.isoformat()
        else:
            last_backup_date = self.last_backup_date

        last_backup_status: Union[Unset, str] = UNSET
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
        policy_uid: Union[Unset, UUID]
        if isinstance(_policy_uid, Unset):
            policy_uid = UNSET
        else:
            policy_uid = UUID(_policy_uid)

        def _parse_policy_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        policy_name = _parse_policy_name(d.pop("policyName", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, PolicyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PolicyState(_state)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, CloudNetworksPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = CloudNetworksPlatform(_platform)

        _instance_type = d.pop("instanceType", UNSET)
        instance_type: Union[Unset, CloudNetworkInstanceType]
        if isinstance(_instance_type, Unset):
            instance_type = UNSET
        else:
            instance_type = CloudNetworkInstanceType(_instance_type)

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_last_backup_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_date_type_0 = isoparse(data)

                return last_backup_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_backup_date = _parse_last_backup_date(d.pop("lastBackupDate", UNSET))

        _last_backup_status = d.pop("lastBackupStatus", UNSET)
        last_backup_status: Union[Unset, BackupJobStatus]
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
