from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchiveTierExtentInfo")


@_attrs_define
class ArchiveTierExtentInfo:
    """
    Attributes:
        extent_uid (Union[Unset, UUID]): UID assigned to an archive extent in Veeam Backup & Replication.
        scaleout_repository_id (Union[None, Unset, int]): ID assigned to a parent scale-out backup repository.
        underlying_repository_id (Union[Unset, int]): ID assigned to an archive extent.
        deep_archive (Union[None, Unset, bool]): Indicates whether the data is stored in a deep archive class storage.
        is_immutable (Union[None, Unset, bool]): Indicates whether immutability is enabled for an archive extent.
    """

    extent_uid: Union[Unset, UUID] = UNSET
    scaleout_repository_id: Union[None, Unset, int] = UNSET
    underlying_repository_id: Union[Unset, int] = UNSET
    deep_archive: Union[None, Unset, bool] = UNSET
    is_immutable: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        extent_uid: Union[Unset, str] = UNSET
        if not isinstance(self.extent_uid, Unset):
            extent_uid = str(self.extent_uid)

        scaleout_repository_id: Union[None, Unset, int]
        if isinstance(self.scaleout_repository_id, Unset):
            scaleout_repository_id = UNSET
        else:
            scaleout_repository_id = self.scaleout_repository_id

        underlying_repository_id = self.underlying_repository_id

        deep_archive: Union[None, Unset, bool]
        if isinstance(self.deep_archive, Unset):
            deep_archive = UNSET
        else:
            deep_archive = self.deep_archive

        is_immutable: Union[None, Unset, bool]
        if isinstance(self.is_immutable, Unset):
            is_immutable = UNSET
        else:
            is_immutable = self.is_immutable

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if extent_uid is not UNSET:
            field_dict["extentUid"] = extent_uid
        if scaleout_repository_id is not UNSET:
            field_dict["scaleoutRepositoryId"] = scaleout_repository_id
        if underlying_repository_id is not UNSET:
            field_dict["underlyingRepositoryId"] = underlying_repository_id
        if deep_archive is not UNSET:
            field_dict["deepArchive"] = deep_archive
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _extent_uid = d.pop("extentUid", UNSET)
        extent_uid: Union[Unset, UUID]
        if isinstance(_extent_uid, Unset):
            extent_uid = UNSET
        else:
            extent_uid = UUID(_extent_uid)

        def _parse_scaleout_repository_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        scaleout_repository_id = _parse_scaleout_repository_id(d.pop("scaleoutRepositoryId", UNSET))

        underlying_repository_id = d.pop("underlyingRepositoryId", UNSET)

        def _parse_deep_archive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        deep_archive = _parse_deep_archive(d.pop("deepArchive", UNSET))

        def _parse_is_immutable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_immutable = _parse_is_immutable(d.pop("isImmutable", UNSET))

        archive_tier_extent_info = cls(
            extent_uid=extent_uid,
            scaleout_repository_id=scaleout_repository_id,
            underlying_repository_id=underlying_repository_id,
            deep_archive=deep_archive,
            is_immutable=is_immutable,
        )

        return archive_tier_extent_info
