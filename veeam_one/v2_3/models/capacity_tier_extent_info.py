from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CapacityTierExtentInfo")


@_attrs_define
class CapacityTierExtentInfo:
    """
    Attributes:
        extent_uid (UUID | Unset): UID assigned to a capacity extent in Veeam Backup & Replication.
        scaleout_repository_id (int | None | Unset): ID assigned to a parent scale-out backup repository.
        underlying_repository_id (int | Unset): ID assigned to a capacity extent.
        is_immutable (bool | None | Unset): Indicates whether immutability is enabled for a capacity extent.
        immutability_interval_days (int | None | Unset): Immutability period, in days.
    """

    extent_uid: UUID | Unset = UNSET
    scaleout_repository_id: int | None | Unset = UNSET
    underlying_repository_id: int | Unset = UNSET
    is_immutable: bool | None | Unset = UNSET
    immutability_interval_days: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        extent_uid: str | Unset = UNSET
        if not isinstance(self.extent_uid, Unset):
            extent_uid = str(self.extent_uid)

        scaleout_repository_id: int | None | Unset
        if isinstance(self.scaleout_repository_id, Unset):
            scaleout_repository_id = UNSET
        else:
            scaleout_repository_id = self.scaleout_repository_id

        underlying_repository_id = self.underlying_repository_id

        is_immutable: bool | None | Unset
        if isinstance(self.is_immutable, Unset):
            is_immutable = UNSET
        else:
            is_immutable = self.is_immutable

        immutability_interval_days: int | None | Unset
        if isinstance(self.immutability_interval_days, Unset):
            immutability_interval_days = UNSET
        else:
            immutability_interval_days = self.immutability_interval_days

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if extent_uid is not UNSET:
            field_dict["extentUid"] = extent_uid
        if scaleout_repository_id is not UNSET:
            field_dict["scaleoutRepositoryId"] = scaleout_repository_id
        if underlying_repository_id is not UNSET:
            field_dict["underlyingRepositoryId"] = underlying_repository_id
        if is_immutable is not UNSET:
            field_dict["isImmutable"] = is_immutable
        if immutability_interval_days is not UNSET:
            field_dict["immutabilityIntervalDays"] = immutability_interval_days

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _extent_uid = d.pop("extentUid", UNSET)
        extent_uid: UUID | Unset
        if isinstance(_extent_uid, Unset):
            extent_uid = UNSET
        else:
            extent_uid = UUID(_extent_uid)

        def _parse_scaleout_repository_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scaleout_repository_id = _parse_scaleout_repository_id(d.pop("scaleoutRepositoryId", UNSET))

        underlying_repository_id = d.pop("underlyingRepositoryId", UNSET)

        def _parse_is_immutable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_immutable = _parse_is_immutable(d.pop("isImmutable", UNSET))

        def _parse_immutability_interval_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        immutability_interval_days = _parse_immutability_interval_days(d.pop("immutabilityIntervalDays", UNSET))

        capacity_tier_extent_info = cls(
            extent_uid=extent_uid,
            scaleout_repository_id=scaleout_repository_id,
            underlying_repository_id=underlying_repository_id,
            is_immutable=is_immutable,
            immutability_interval_days=immutability_interval_days,
        )

        return capacity_tier_extent_info
