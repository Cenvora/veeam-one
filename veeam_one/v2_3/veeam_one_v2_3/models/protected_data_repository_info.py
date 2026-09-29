from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.backup_repository_type import BackupRepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectedDataRepositoryInfo")


@_attrs_define
class ProtectedDataRepositoryInfo:
    """
    Attributes:
        repository_id (Union[Unset, int]): ID assigned to a backup repository.
        repository_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a backup repository in Veeam Backup &
            Replication.
        type_ (Union[Unset, BackupRepositoryType]):
        name (Union[None, Unset, str]): Name of a backup repository.
    """

    repository_id: Union[Unset, int] = UNSET
    repository_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    type_: Union[Unset, BackupRepositoryType] = UNSET
    name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        repository_id = self.repository_id

        repository_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.repository_uid_in_vbr, Unset):
            repository_uid_in_vbr = UNSET
        elif isinstance(self.repository_uid_in_vbr, UUID):
            repository_uid_in_vbr = str(self.repository_uid_in_vbr)
        else:
            repository_uid_in_vbr = self.repository_uid_in_vbr

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repositoryId"] = repository_id
        if repository_uid_in_vbr is not UNSET:
            field_dict["repositoryUidInVbr"] = repository_uid_in_vbr
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name

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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BackupRepositoryType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BackupRepositoryType(_type_)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        protected_data_repository_info = cls(
            repository_id=repository_id,
            repository_uid_in_vbr=repository_uid_in_vbr,
            type_=type_,
            name=name,
        )

        return protected_data_repository_info
