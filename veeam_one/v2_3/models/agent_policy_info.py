from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.agent_backup_job_platform import AgentBackupJobPlatform
from ..models.backup_job_status import BackupJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentPolicyInfo")


@_attrs_define
class AgentPolicyInfo:
    """
    Attributes:
        agent_policy_uid (None | Unset | UUID): UID assigned to a backup policy in Veeam Backup & Replication.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        status (BackupJobStatus | Unset):
        details (list[str] | None | Unset): Additional information on a backup policy.
        name (None | str | Unset): Name of a backup policy.
        description (None | str | Unset): Backup policy description.
        platform (AgentBackupJobPlatform | Unset):
        child_job_uids (list[UUID] | None | Unset): Array of UIDs assigned to child jobs.
    """

    agent_policy_uid: None | Unset | UUID = UNSET
    backup_server_id: int | Unset = UNSET
    status: BackupJobStatus | Unset = UNSET
    details: list[str] | None | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    platform: AgentBackupJobPlatform | Unset = UNSET
    child_job_uids: list[UUID] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_policy_uid: None | str | Unset
        if isinstance(self.agent_policy_uid, Unset):
            agent_policy_uid = UNSET
        elif isinstance(self.agent_policy_uid, UUID):
            agent_policy_uid = str(self.agent_policy_uid)
        else:
            agent_policy_uid = self.agent_policy_uid

        backup_server_id = self.backup_server_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: list[str] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        else:
            details = self.details

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        child_job_uids: list[str] | None | Unset
        if isinstance(self.child_job_uids, Unset):
            child_job_uids = UNSET
        elif isinstance(self.child_job_uids, list):
            child_job_uids = []
            for child_job_uids_type_0_item_data in self.child_job_uids:
                child_job_uids_type_0_item = str(child_job_uids_type_0_item_data)
                child_job_uids.append(child_job_uids_type_0_item)

        else:
            child_job_uids = self.child_job_uids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if agent_policy_uid is not UNSET:
            field_dict["agentPolicyUid"] = agent_policy_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if platform is not UNSET:
            field_dict["platform"] = platform
        if child_job_uids is not UNSET:
            field_dict["childJobUids"] = child_job_uids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_agent_policy_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_policy_uid_type_0 = UUID(data)

                return agent_policy_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_policy_uid = _parse_agent_policy_uid(d.pop("agentPolicyUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: BackupJobStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupJobStatus(_status)

        def _parse_details(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: AgentBackupJobPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = AgentBackupJobPlatform(_platform)

        def _parse_child_job_uids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                child_job_uids_type_0 = []
                _child_job_uids_type_0 = data
                for child_job_uids_type_0_item_data in _child_job_uids_type_0:
                    child_job_uids_type_0_item = UUID(child_job_uids_type_0_item_data)

                    child_job_uids_type_0.append(child_job_uids_type_0_item)

                return child_job_uids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        child_job_uids = _parse_child_job_uids(d.pop("childJobUids", UNSET))

        agent_policy_info = cls(
            agent_policy_uid=agent_policy_uid,
            backup_server_id=backup_server_id,
            status=status,
            details=details,
            name=name,
            description=description,
            platform=platform,
            child_job_uids=child_job_uids,
        )

        return agent_policy_info
