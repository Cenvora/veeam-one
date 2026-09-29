from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TapeServerInfo")


@_attrs_define
class TapeServerInfo:
    """
    Attributes:
        tape_server_id (int | Unset): ID assigned to a tape server.
        tape_server_uid_in_vbr (None | Unset | UUID): UID assigned to a tape server in Veeam Backup & Replication.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        name (None | str | Unset): Name of a tape server.
        version (None | str | Unset): Tape server version.
        upgrade_required (bool | None | Unset): Indicates whether a tape server must be updated.
    """

    tape_server_id: int | Unset = UNSET
    tape_server_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    upgrade_required: bool | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tape_server_id = self.tape_server_id

        tape_server_uid_in_vbr: None | str | Unset
        if isinstance(self.tape_server_uid_in_vbr, Unset):
            tape_server_uid_in_vbr = UNSET
        elif isinstance(self.tape_server_uid_in_vbr, UUID):
            tape_server_uid_in_vbr = str(self.tape_server_uid_in_vbr)
        else:
            tape_server_uid_in_vbr = self.tape_server_uid_in_vbr

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        upgrade_required: bool | None | Unset
        if isinstance(self.upgrade_required, Unset):
            upgrade_required = UNSET
        else:
            upgrade_required = self.upgrade_required

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tape_server_id is not UNSET:
            field_dict["tapeServerId"] = tape_server_id
        if tape_server_uid_in_vbr is not UNSET:
            field_dict["tapeServerUidInVbr"] = tape_server_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if upgrade_required is not UNSET:
            field_dict["upgradeRequired"] = upgrade_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tape_server_id = d.pop("tapeServerId", UNSET)

        def _parse_tape_server_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tape_server_uid_in_vbr_type_0 = UUID(data)

                return tape_server_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        tape_server_uid_in_vbr = _parse_tape_server_uid_in_vbr(d.pop("tapeServerUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_upgrade_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        upgrade_required = _parse_upgrade_required(d.pop("upgradeRequired", UNSET))

        tape_server_info = cls(
            tape_server_id=tape_server_id,
            tape_server_uid_in_vbr=tape_server_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            version=version,
            upgrade_required=upgrade_required,
        )

        return tape_server_info
