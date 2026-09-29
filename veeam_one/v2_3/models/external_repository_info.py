from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.external_repository_type import ExternalRepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalRepositoryInfo")


@_attrs_define
class ExternalRepositoryInfo:
    """
    Attributes:
        external_repository_id (int | Unset): ID assigned to an external repository.
        external_repository_uid_in_vbr (None | Unset | UUID): UID assigned to an external repository in Veeam Backup &
            Replication.
        backup_server_id (int | None | Unset): ID assigned to a Veeam Backup & Replication server.
        name (None | str | Unset): Name of an external repository.
        is_decryption_enabled (bool | None | Unset): Indicates whether backups located on an external repository are
            decrypted.
        region (None | str | Unset): Location type of an external repository.
        bucket (None | str | Unset): Name of a bucket or container.
        type_ (ExternalRepositoryType | Unset):
        description (None | str | Unset): Description of an external repository.
    """

    external_repository_id: int | Unset = UNSET
    external_repository_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    is_decryption_enabled: bool | None | Unset = UNSET
    region: None | str | Unset = UNSET
    bucket: None | str | Unset = UNSET
    type_: ExternalRepositoryType | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        external_repository_id = self.external_repository_id

        external_repository_uid_in_vbr: None | str | Unset
        if isinstance(self.external_repository_uid_in_vbr, Unset):
            external_repository_uid_in_vbr = UNSET
        elif isinstance(self.external_repository_uid_in_vbr, UUID):
            external_repository_uid_in_vbr = str(self.external_repository_uid_in_vbr)
        else:
            external_repository_uid_in_vbr = self.external_repository_uid_in_vbr

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

        is_decryption_enabled: bool | None | Unset
        if isinstance(self.is_decryption_enabled, Unset):
            is_decryption_enabled = UNSET
        else:
            is_decryption_enabled = self.is_decryption_enabled

        region: None | str | Unset
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        bucket: None | str | Unset
        if isinstance(self.bucket, Unset):
            bucket = UNSET
        else:
            bucket = self.bucket

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if external_repository_id is not UNSET:
            field_dict["externalRepositoryId"] = external_repository_id
        if external_repository_uid_in_vbr is not UNSET:
            field_dict["externalRepositoryUidInVbr"] = external_repository_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if is_decryption_enabled is not UNSET:
            field_dict["isDecryptionEnabled"] = is_decryption_enabled
        if region is not UNSET:
            field_dict["region"] = region
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if type_ is not UNSET:
            field_dict["type"] = type_
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_repository_id = d.pop("externalRepositoryId", UNSET)

        def _parse_external_repository_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                external_repository_uid_in_vbr_type_0 = UUID(data)

                return external_repository_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        external_repository_uid_in_vbr = _parse_external_repository_uid_in_vbr(
            d.pop("externalRepositoryUidInVbr", UNSET)
        )

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

        def _parse_is_decryption_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_decryption_enabled = _parse_is_decryption_enabled(d.pop("isDecryptionEnabled", UNSET))

        def _parse_region(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        region = _parse_region(d.pop("region", UNSET))

        def _parse_bucket(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket = _parse_bucket(d.pop("bucket", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: ExternalRepositoryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExternalRepositoryType(_type_)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        external_repository_info = cls(
            external_repository_id=external_repository_id,
            external_repository_uid_in_vbr=external_repository_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            is_decryption_enabled=is_decryption_enabled,
            region=region,
            bucket=bucket,
            type_=type_,
            description=description,
        )

        return external_repository_info
