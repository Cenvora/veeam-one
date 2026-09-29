from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_job_status import BackupJobStatus
from ..models.cloud_platform import CloudPlatform
from ..models.cloud_vm_instance_type import CloudVmInstanceType
from ..models.policy_state import PolicyState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cloud_instance import CloudInstance


T = TypeVar("T", bound="CloudVmPolicyInfo")


@_attrs_define
class CloudVmPolicyInfo:
    """
    Attributes:
        policy_uid (UUID | Unset): UID assigned to a policy.
        policy_name (None | str | Unset): Name of a policy.
        state (PolicyState | Unset):
        instances (list[CloudInstance] | None | Unset): Array of cloud VMs included in a policy.
        instances_count (int | Unset): Number of cloud VMs included in a policy.
        platform (CloudPlatform | Unset):
        instance_type (CloudVmInstanceType | Unset):
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        last_snapshot_date (datetime.datetime | None | Unset): Date and time when the latest snapshot was created.
        last_snapshot_status (BackupJobStatus | Unset):
        last_backup_date (datetime.datetime | None | Unset): Date and time when the latest backup restore point was
            created.
        last_backup_status (BackupJobStatus | Unset):
        last_replication_date (datetime.datetime | None | Unset): Date and time when the latest replica was created.
        last_replication_status (BackupJobStatus | Unset):
        last_archive_date (datetime.datetime | None | Unset): Date and time when the latest archive restore point was
            created.
        last_archive_status (BackupJobStatus | Unset):
    """

    policy_uid: UUID | Unset = UNSET
    policy_name: None | str | Unset = UNSET
    state: PolicyState | Unset = UNSET
    instances: list[CloudInstance] | None | Unset = UNSET
    instances_count: int | Unset = UNSET
    platform: CloudPlatform | Unset = UNSET
    instance_type: CloudVmInstanceType | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    last_snapshot_date: datetime.datetime | None | Unset = UNSET
    last_snapshot_status: BackupJobStatus | Unset = UNSET
    last_backup_date: datetime.datetime | None | Unset = UNSET
    last_backup_status: BackupJobStatus | Unset = UNSET
    last_replication_date: datetime.datetime | None | Unset = UNSET
    last_replication_status: BackupJobStatus | Unset = UNSET
    last_archive_date: datetime.datetime | None | Unset = UNSET
    last_archive_status: BackupJobStatus | Unset = UNSET

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

        instances: list[dict[str, Any]] | None | Unset
        if isinstance(self.instances, Unset):
            instances = UNSET
        elif isinstance(self.instances, list):
            instances = []
            for instances_type_0_item_data in self.instances:
                instances_type_0_item = instances_type_0_item_data.to_dict()
                instances.append(instances_type_0_item)

        else:
            instances = self.instances

        instances_count = self.instances_count

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

        last_snapshot_date: None | str | Unset
        if isinstance(self.last_snapshot_date, Unset):
            last_snapshot_date = UNSET
        elif isinstance(self.last_snapshot_date, datetime.datetime):
            last_snapshot_date = self.last_snapshot_date.isoformat()
        else:
            last_snapshot_date = self.last_snapshot_date

        last_snapshot_status: str | Unset = UNSET
        if not isinstance(self.last_snapshot_status, Unset):
            last_snapshot_status = self.last_snapshot_status.value

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

        last_replication_date: None | str | Unset
        if isinstance(self.last_replication_date, Unset):
            last_replication_date = UNSET
        elif isinstance(self.last_replication_date, datetime.datetime):
            last_replication_date = self.last_replication_date.isoformat()
        else:
            last_replication_date = self.last_replication_date

        last_replication_status: str | Unset = UNSET
        if not isinstance(self.last_replication_status, Unset):
            last_replication_status = self.last_replication_status.value

        last_archive_date: None | str | Unset
        if isinstance(self.last_archive_date, Unset):
            last_archive_date = UNSET
        elif isinstance(self.last_archive_date, datetime.datetime):
            last_archive_date = self.last_archive_date.isoformat()
        else:
            last_archive_date = self.last_archive_date

        last_archive_status: str | Unset = UNSET
        if not isinstance(self.last_archive_status, Unset):
            last_archive_status = self.last_archive_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if policy_uid is not UNSET:
            field_dict["policyUid"] = policy_uid
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if state is not UNSET:
            field_dict["state"] = state
        if instances is not UNSET:
            field_dict["instances"] = instances
        if instances_count is not UNSET:
            field_dict["instancesCount"] = instances_count
        if platform is not UNSET:
            field_dict["platform"] = platform
        if instance_type is not UNSET:
            field_dict["instanceType"] = instance_type
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if last_snapshot_date is not UNSET:
            field_dict["lastSnapshotDate"] = last_snapshot_date
        if last_snapshot_status is not UNSET:
            field_dict["lastSnapshotStatus"] = last_snapshot_status
        if last_backup_date is not UNSET:
            field_dict["lastBackupDate"] = last_backup_date
        if last_backup_status is not UNSET:
            field_dict["lastBackupStatus"] = last_backup_status
        if last_replication_date is not UNSET:
            field_dict["lastReplicationDate"] = last_replication_date
        if last_replication_status is not UNSET:
            field_dict["lastReplicationStatus"] = last_replication_status
        if last_archive_date is not UNSET:
            field_dict["lastArchiveDate"] = last_archive_date
        if last_archive_status is not UNSET:
            field_dict["lastArchiveStatus"] = last_archive_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cloud_instance import CloudInstance  # noqa: PLC0415

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

        def _parse_instances(data: object) -> list[CloudInstance] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instances_type_0 = []
                _instances_type_0 = data
                for instances_type_0_item_data in _instances_type_0:
                    instances_type_0_item = CloudInstance.from_dict(instances_type_0_item_data)

                    instances_type_0.append(instances_type_0_item)

                return instances_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CloudInstance] | None | Unset, data)

        instances = _parse_instances(d.pop("instances", UNSET))

        instances_count = d.pop("instancesCount", UNSET)

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

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_last_snapshot_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_snapshot_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_snapshot_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_snapshot_date = _parse_last_snapshot_date(d.pop("lastSnapshotDate", UNSET))

        _last_snapshot_status = d.pop("lastSnapshotStatus", UNSET)
        last_snapshot_status: BackupJobStatus | Unset
        if isinstance(_last_snapshot_status, Unset):
            last_snapshot_status = UNSET
        else:
            last_snapshot_status = BackupJobStatus(_last_snapshot_status)

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

        def _parse_last_replication_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_replication_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_replication_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_replication_date = _parse_last_replication_date(d.pop("lastReplicationDate", UNSET))

        _last_replication_status = d.pop("lastReplicationStatus", UNSET)
        last_replication_status: BackupJobStatus | Unset
        if isinstance(_last_replication_status, Unset):
            last_replication_status = UNSET
        else:
            last_replication_status = BackupJobStatus(_last_replication_status)

        def _parse_last_archive_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_archive_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_archive_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_archive_date = _parse_last_archive_date(d.pop("lastArchiveDate", UNSET))

        _last_archive_status = d.pop("lastArchiveStatus", UNSET)
        last_archive_status: BackupJobStatus | Unset
        if isinstance(_last_archive_status, Unset):
            last_archive_status = UNSET
        else:
            last_archive_status = BackupJobStatus(_last_archive_status)

        cloud_vm_policy_info = cls(
            policy_uid=policy_uid,
            policy_name=policy_name,
            state=state,
            instances=instances,
            instances_count=instances_count,
            platform=platform,
            instance_type=instance_type,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            last_snapshot_date=last_snapshot_date,
            last_snapshot_status=last_snapshot_status,
            last_backup_date=last_backup_date,
            last_backup_status=last_backup_status,
            last_replication_date=last_replication_date,
            last_replication_status=last_replication_status,
            last_archive_date=last_archive_date,
            last_archive_status=last_archive_status,
        )

        return cloud_vm_policy_info
