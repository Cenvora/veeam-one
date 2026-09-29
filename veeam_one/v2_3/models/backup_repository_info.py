from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.regular_repository_type import RegularRepositoryType
from ..models.repository_state import RepositoryState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupRepositoryInfo")


@_attrs_define
class BackupRepositoryInfo:
    """
    Attributes:
        repository_id (Union[Unset, int]): ID assigned to a backup repository.
        repository_uid_in_vbr (Union[None, UUID, Unset]): ID assigned to a backup repository in Veeam Backup &
            Replication.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup & Replication server.
        name (Union[None, Unset, str]): Name of a backup repository.
        type_ (Union[Unset, RegularRepositoryType]):
        capacity_bytes (Union[None, Unset, int]): Storage capacity of a backup repository, in bytes.
        free_space_bytes (Union[None, Unset, int]): Amount of free storage space on the repository, in bytes.
        running_tasks (Union[None, Unset, int]): Number of tasks that are currently running on a backup repository.
        max_concurrent_tasks (Union[None, Unset, int]): Maximum number of concurrent tasks allowed for a backup proxy.
        upgrade_required (Union[None, Unset, bool]): Indicates whether a backup repository must be updated.
        out_of_space_in_days (Union[None, Unset, int]): Number of days before a backup repository runs out of free
            space.
        state (Union[Unset, RepositoryState]):
        path (Union[None, Unset, str]): Path to the folder where backup files are stored.
        one_backup_file_per_vm (Union[None, Unset, bool]): Indicates whether a separate backup file is created for every
            machine in a job.
        is_re_fs (Union[None, Unset, bool]): Indicates whether a backup repository stores files in the ReFS format.
        is_immutable (Union[None, Unset, bool]): Indicates whether immutability is enabled for a backup repository.
        immutability_interval_days (Union[None, Unset, int]): Immutability period, in days.
    """

    repository_id: Union[Unset, int] = UNSET
    repository_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, RegularRepositoryType] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    running_tasks: Union[None, Unset, int] = UNSET
    max_concurrent_tasks: Union[None, Unset, int] = UNSET
    upgrade_required: Union[None, Unset, bool] = UNSET
    out_of_space_in_days: Union[None, Unset, int] = UNSET
    state: Union[Unset, RepositoryState] = UNSET
    path: Union[None, Unset, str] = UNSET
    one_backup_file_per_vm: Union[None, Unset, bool] = UNSET
    is_re_fs: Union[None, Unset, bool] = UNSET
    is_immutable: Union[None, Unset, bool] = UNSET
    immutability_interval_days: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_id = self.repository_id

        repository_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.repository_uid_in_vbr, Unset):
            repository_uid_in_vbr = UNSET
        elif isinstance(self.repository_uid_in_vbr, UUID):
            repository_uid_in_vbr = str(self.repository_uid_in_vbr)
        else:
            repository_uid_in_vbr = self.repository_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: Union[None, Unset, int]
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        running_tasks: Union[None, Unset, int]
        if isinstance(self.running_tasks, Unset):
            running_tasks = UNSET
        else:
            running_tasks = self.running_tasks

        max_concurrent_tasks: Union[None, Unset, int]
        if isinstance(self.max_concurrent_tasks, Unset):
            max_concurrent_tasks = UNSET
        else:
            max_concurrent_tasks = self.max_concurrent_tasks

        upgrade_required: Union[None, Unset, bool]
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        out_of_space_in_days: Union[None, Unset, int]
        if isinstance(self.out_of_space_in_days, Unset):
            out_of_space_in_days = UNSET
        else:
            out_of_space_in_days = self.out_of_space_in_days

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        one_backup_file_per_vm: Union[None, Unset, bool]
        if isinstance(self.one_backup_file_per_vm, Unset):
            one_backup_file_per_vm = UNSET
        else:
            one_backup_file_per_vm = self.one_backup_file_per_vm

        is_re_fs: Union[None, Unset, bool]
        if isinstance(self.is_re_fs, Unset):
            is_re_fs = UNSET
        else:
            is_re_fs = self.is_re_fs

        is_immutable: Union[None, Unset, bool]
        if isinstance(self.is_immutable, Unset):
            is_immutable = UNSET
        else:
            is_immutable = self.is_immutable

        immutability_interval_days: Union[None, Unset, int]
        if isinstance(self.immutability_interval_days, Unset):
            immutability_interval_days = UNSET
        else:
            immutability_interval_days = self.immutability_interval_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_uid_in_vbr is not UNSET:
            field_dict["repositoryUidInVbr"] = repository_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if running_tasks is not UNSET:
            field_dict["runningTasks"] = running_tasks
        if max_concurrent_tasks is not UNSET:
            field_dict["maxConcurrentTasks"] = max_concurrent_tasks
        if upgrade_required is not UNSET:
            field_dict["upgradeRequired"] = upgrade_required
        if out_of_space_in_days is not UNSET:
            field_dict["outOfSpaceInDays"] = out_of_space_in_days
        if state is not UNSET:
            field_dict["state"] = state
        if path is not UNSET:
            field_dict["path"] = path
        if one_backup_file_per_vm is not UNSET:
            field_dict["oneBackupFilePerVm"] = one_backup_file_per_vm
        if is_re_fs is not UNSET:
            field_dict["isReFs"] = is_re_fs
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable
        if immutability_interval_days is not UNSET:
            field_dict["immutabilityIntervalDays"] = immutability_interval_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        repository_id = d.pop("repositoryId", UNSET)

        def _parse_repository_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_in_vbr_type_0 = UUID(data)

                return repository_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        repository_uid_in_vbr = _parse_repository_uid_in_vbr(d.pop("repositoryUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RegularRepositoryType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RegularRepositoryType(_type_)

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_running_tasks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        running_tasks = _parse_running_tasks(d.pop("runningTasks", UNSET))

        def _parse_max_concurrent_tasks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_concurrent_tasks = _parse_max_concurrent_tasks(d.pop("maxConcurrentTasks", UNSET))

        def _parse_upgrade_required(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        def _parse_out_of_space_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        out_of_space_in_days = _parse_out_of_space_in_days(d.pop("outOfSpaceInDays", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, RepositoryState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RepositoryState(_state)

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_one_backup_file_per_vm(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        one_backup_file_per_vm = _parse_one_backup_file_per_vm(d.pop("oneBackupFilePerVm", UNSET))

        def _parse_is_re_fs(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_re_fs = _parse_is_re_fs(d.pop("isReFs", UNSET))

        def _parse_is_immutable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_immutable = _parse_is_immutable(d.pop("isImmutable", UNSET))

        def _parse_immutability_interval_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        immutability_interval_days = _parse_immutability_interval_days(d.pop("immutabilityIntervalDays", UNSET))

        backup_repository_info = cls(
            repository_id=repository_id,
            repository_uid_in_vbr=repository_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            type_=type_,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            running_tasks=running_tasks,
            max_concurrent_tasks=max_concurrent_tasks,
            upgrade_required=upgrade_required,
            out_of_space_in_days=out_of_space_in_days,
            state=state,
            path=path,
            one_backup_file_per_vm=one_backup_file_per_vm,
            is_re_fs=is_re_fs,
            is_immutable=is_immutable,
            immutability_interval_days=immutability_interval_days,
        )

        return backup_repository_info
