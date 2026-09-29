from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.repository_state import RepositoryState
from ..models.scaleout_repository_policy import ScaleoutRepositoryPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScaleoutRepositoryInfo")


@_attrs_define
class ScaleoutRepositoryInfo:
    """
    Attributes:
        scaleout_repository_id (int | Unset): ID assigned to a scale-out backup repository.
        scaleout_repository_uid_in_vbr (None | Unset | UUID): UID assigned to a scale-out backup repository in Veeam
            Bakcup & Replication.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        name (None | str | Unset): Name of a scale-out backup repository.
        capacity_bytes (int | None | Unset): Storage capacity of a scale-out backup repository, in bytes.
        free_space_bytes (int | None | Unset): Amount of free storage space on a scale-out backup repository, in bytes.
        running_tasks (int | Unset): Number of currently running tasks on a scale-out backup repository.
        out_of_space_in_days (int | None | Unset): Estimated number of days before a scale-out backup repository runs
            out of free space.
        state (RepositoryState | Unset):
        scaleout_repository_policy (ScaleoutRepositoryPolicy | Unset):
        copy_policy (bool | None | Unset): Indicates whether all backups are copied to object storage as soon as they
            are created.
        move_policy_in_days (int | None | Unset): Period after which inactive backup chains on a performance extent are
            moved to a capacity extent, in days.
        archiving_policy_in_days (int | None | Unset): Period after which inactive backup chains on a capacity extent
            are moved to an archive extent, in days.
        encrypt_archived_data (bool | None | Unset): Indicates whether encryption is enabled for the archived data.
    """

    scaleout_repository_id: int | Unset = UNSET
    scaleout_repository_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    capacity_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    running_tasks: int | Unset = UNSET
    out_of_space_in_days: int | None | Unset = UNSET
    state: RepositoryState | Unset = UNSET
    scaleout_repository_policy: ScaleoutRepositoryPolicy | Unset = UNSET
    copy_policy: bool | None | Unset = UNSET
    move_policy_in_days: int | None | Unset = UNSET
    archiving_policy_in_days: int | None | Unset = UNSET
    encrypt_archived_data: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        scaleout_repository_id = self.scaleout_repository_id

        scaleout_repository_uid_in_vbr: None | str | Unset
        if isinstance(self.scaleout_repository_uid_in_vbr, Unset):
            scaleout_repository_uid_in_vbr = UNSET
        elif isinstance(self.scaleout_repository_uid_in_vbr, UUID):
            scaleout_repository_uid_in_vbr = str(self.scaleout_repository_uid_in_vbr)
        else:
            scaleout_repository_uid_in_vbr = self.scaleout_repository_uid_in_vbr

        backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        running_tasks = self.running_tasks

        out_of_space_in_days: int | None | Unset
        if isinstance(self.out_of_space_in_days, Unset):
            out_of_space_in_days = UNSET
        else:
            out_of_space_in_days = self.out_of_space_in_days

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        scaleout_repository_policy: str | Unset = UNSET
        if not isinstance(self.scaleout_repository_policy, Unset):
            scaleout_repository_policy = self.scaleout_repository_policy.value

        copy_policy: bool | None | Unset
        if isinstance(self.copy_policy, Unset):
            copy_policy = UNSET
        else:
            copy_policy = self.copy_policy

        move_policy_in_days: int | None | Unset
        if isinstance(self.move_policy_in_days, Unset):
            move_policy_in_days = UNSET
        else:
            move_policy_in_days = self.move_policy_in_days

        archiving_policy_in_days: int | None | Unset
        if isinstance(self.archiving_policy_in_days, Unset):
            archiving_policy_in_days = UNSET
        else:
            archiving_policy_in_days = self.archiving_policy_in_days

        encrypt_archived_data: bool | None | Unset
        if isinstance(self.encrypt_archived_data, Unset):
            encrypt_archived_data = UNSET
        else:
            encrypt_archived_data = self.encrypt_archived_data

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if scaleout_repository_id is not UNSET:
            field_dict["scaleoutRepositoryId"] = scaleout_repository_id
        if scaleout_repository_uid_in_vbr is not UNSET:
            field_dict["scaleoutRepositoryUidInVbr"] = scaleout_repository_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if running_tasks is not UNSET:
            field_dict["runningTasks"] = running_tasks
        if out_of_space_in_days is not UNSET:
            field_dict["outOfSpaceInDays"] = out_of_space_in_days
        if state is not UNSET:
            field_dict["state"] = state
        if scaleout_repository_policy is not UNSET:
            field_dict["scaleoutRepositoryPolicy"] = scaleout_repository_policy
        if copy_policy is not UNSET:
            field_dict["copyPolicy"] = copy_policy
        if move_policy_in_days is not UNSET:
            field_dict["movePolicyInDays"] = move_policy_in_days
        if archiving_policy_in_days is not UNSET:
            field_dict["archivingPolicyInDays"] = archiving_policy_in_days
        if encrypt_archived_data is not UNSET:
            field_dict["encryptArchivedData"] = encrypt_archived_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scaleout_repository_id = d.pop("scaleoutRepositoryId", UNSET)

        def _parse_scaleout_repository_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scaleout_repository_uid_in_vbr_type_0 = UUID(data)

                return scaleout_repository_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        scaleout_repository_uid_in_vbr = _parse_scaleout_repository_uid_in_vbr(
            d.pop("scaleoutRepositoryUidInVbr", UNSET)
        )

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        running_tasks = d.pop("runningTasks", UNSET)

        def _parse_out_of_space_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        out_of_space_in_days = _parse_out_of_space_in_days(d.pop("outOfSpaceInDays", UNSET))

        _state = d.pop("state", UNSET)
        state: RepositoryState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryState(_state)

        _scaleout_repository_policy = d.pop("scaleoutRepositoryPolicy", UNSET)
        scaleout_repository_policy: ScaleoutRepositoryPolicy | Unset
        if isinstance(_scaleout_repository_policy, Unset):
            scaleout_repository_policy = UNSET
        else:
            scaleout_repository_policy = ScaleoutRepositoryPolicy(_scaleout_repository_policy)

        def _parse_copy_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_policy = _parse_copy_policy(d.pop("copyPolicy", UNSET))

        def _parse_move_policy_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        move_policy_in_days = _parse_move_policy_in_days(d.pop("movePolicyInDays", UNSET))

        def _parse_archiving_policy_in_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        archiving_policy_in_days = _parse_archiving_policy_in_days(d.pop("archivingPolicyInDays", UNSET))

        def _parse_encrypt_archived_data(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        encrypt_archived_data = _parse_encrypt_archived_data(d.pop("encryptArchivedData", UNSET))

        scaleout_repository_info = cls(
            scaleout_repository_id=scaleout_repository_id,
            scaleout_repository_uid_in_vbr=scaleout_repository_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            running_tasks=running_tasks,
            out_of_space_in_days=out_of_space_in_days,
            state=state,
            scaleout_repository_policy=scaleout_repository_policy,
            copy_policy=copy_policy,
            move_policy_in_days=move_policy_in_days,
            archiving_policy_in_days=archiving_policy_in_days,
            encrypt_archived_data=encrypt_archived_data,
        )

        return scaleout_repository_info
