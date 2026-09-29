from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.best_practice_group import BestPracticeGroup
from ..models.best_practice_status import BestPracticeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BestPracticeInfo")


@_attrs_define
class BestPracticeInfo:
    """
    Attributes:
        best_practice_uid (UUID | Unset): ID assigned to a best practice.
        best_practice_name (None | str | Unset): Name of a best practice.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        recommendation (None | str | Unset): Implementation recommendations.
        status (BestPracticeStatus | Unset):
        group (BestPracticeGroup | Unset):
    """

    best_practice_uid: UUID | Unset = UNSET
    best_practice_name: None | str | Unset = UNSET
    backup_server_id: int | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    recommendation: None | str | Unset = UNSET
    status: BestPracticeStatus | Unset = UNSET
    group: BestPracticeGroup | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        best_practice_uid: str | Unset = UNSET
        if not isinstance(self.best_practice_uid, Unset):
            best_practice_uid = str(self.best_practice_uid)

        best_practice_name: None | str | Unset
        if isinstance(self.best_practice_name, Unset):
            best_practice_name = UNSET
        else:
            best_practice_name = self.best_practice_name

        backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        recommendation: None | str | Unset
        if isinstance(self.recommendation, Unset):
            recommendation = UNSET
        else:
            recommendation = self.recommendation

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        group: str | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if best_practice_uid is not UNSET:
            field_dict["bestPracticeUid"] = best_practice_uid
        if best_practice_name is not UNSET:
            field_dict["bestPracticeName"] = best_practice_name
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if status is not UNSET:
            field_dict["status"] = status
        if group is not UNSET:
            field_dict["group"] = group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _best_practice_uid = d.pop("bestPracticeUid", UNSET)
        best_practice_uid: UUID | Unset
        if isinstance(_best_practice_uid, Unset):
            best_practice_uid = UNSET
        else:
            best_practice_uid = UUID(_best_practice_uid)

        def _parse_best_practice_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        best_practice_name = _parse_best_practice_name(d.pop("bestPracticeName", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_recommendation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        recommendation = _parse_recommendation(d.pop("recommendation", UNSET))

        _status = d.pop("status", UNSET)
        status: BestPracticeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BestPracticeStatus(_status)

        _group = d.pop("group", UNSET)
        group: BestPracticeGroup | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = BestPracticeGroup(_group)

        best_practice_info = cls(
            best_practice_uid=best_practice_uid,
            best_practice_name=best_practice_name,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            recommendation=recommendation,
            status=status,
            group=group,
        )

        return best_practice_info
