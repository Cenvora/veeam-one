from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.protected_application_platform import ProtectedApplicationPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_group import ProtectionGroup


T = TypeVar("T", bound="ProtectedApplicationInfo")


@_attrs_define
class ProtectedApplicationInfo:
    """
    Attributes:
        application_uid_in_vbr (None | Unset | UUID): UID assigned to an application in Veeam Backup & Replication.
        backup_server_id (int | None | Unset): ID assigned to the Veeam Backup & Replication server.
        backup_server_name (None | str | Unset): Name of a Veeam Backup & Replication server.
        name (None | str | Unset): Name of an application.
        is_cluster (bool | Unset): Indicates whether an application is a cluster.
        platform (ProtectedApplicationPlatform | Unset):
        processed_databases (int | Unset): Number of application databases processed by jobs.
        not_processed_databases (int | Unset): Number of application databases not processed by jobs.
        protection_groups (list[ProtectionGroup] | None | Unset): Array of protection groups that include the
            application.
        last_protected_date (datetime.datetime | None | Unset): Date and time when the latest successful job session
            finished.
    """

    application_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    backup_server_name: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    is_cluster: bool | Unset = UNSET
    platform: ProtectedApplicationPlatform | Unset = UNSET
    processed_databases: int | Unset = UNSET
    not_processed_databases: int | Unset = UNSET
    protection_groups: list[ProtectionGroup] | None | Unset = UNSET
    last_protected_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_uid_in_vbr: None | str | Unset
        if isinstance(self.application_uid_in_vbr, Unset):
            application_uid_in_vbr = UNSET
        elif isinstance(self.application_uid_in_vbr, UUID):
            application_uid_in_vbr = str(self.application_uid_in_vbr)
        else:
            application_uid_in_vbr = self.application_uid_in_vbr

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        backup_server_name: None | str | Unset
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_cluster = self.is_cluster

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        processed_databases = self.processed_databases

        not_processed_databases = self.not_processed_databases

        protection_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.protection_groups, Unset):
            protection_groups = UNSET
        elif isinstance(self.protection_groups, list):
            protection_groups = []
            for protection_groups_type_0_item_data in self.protection_groups:
                protection_groups_type_0_item = protection_groups_type_0_item_data.to_dict()
                protection_groups.append(protection_groups_type_0_item)

        else:
            protection_groups = self.protection_groups

        last_protected_date: None | str | Unset
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if application_uid_in_vbr is not UNSET:
            field_dict["applicationUidInVbr"] = application_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name
        if name is not UNSET:
            field_dict["name"] = name
        if is_cluster is not UNSET:
            field_dict["isCluster"] = is_cluster
        if platform is not UNSET:
            field_dict["platform"] = platform
        if processed_databases is not UNSET:
            field_dict["processedDatabases"] = processed_databases
        if not_processed_databases is not UNSET:
            field_dict["notProcessedDatabases"] = not_processed_databases
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_group import ProtectionGroup  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_application_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_uid_in_vbr_type_0 = UUID(data)

                return application_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_uid_in_vbr = _parse_application_uid_in_vbr(d.pop("applicationUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_backup_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        is_cluster = d.pop("isCluster", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: ProtectedApplicationPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProtectedApplicationPlatform(_platform)

        processed_databases = d.pop("processedDatabases", UNSET)

        not_processed_databases = d.pop("notProcessedDatabases", UNSET)

        def _parse_protection_groups(data: object) -> list[ProtectionGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_groups_type_0 = []
                _protection_groups_type_0 = data
                for protection_groups_type_0_item_data in _protection_groups_type_0:
                    protection_groups_type_0_item = ProtectionGroup.from_dict(protection_groups_type_0_item_data)

                    protection_groups_type_0.append(protection_groups_type_0_item)

                return protection_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionGroup] | None | Unset, data)

        protection_groups = _parse_protection_groups(d.pop("protectionGroups", UNSET))

        def _parse_last_protected_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_protected_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_protected_date = _parse_last_protected_date(d.pop("lastProtectedDate", UNSET))

        protected_application_info = cls(
            application_uid_in_vbr=application_uid_in_vbr,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
            name=name,
            is_cluster=is_cluster,
            platform=platform,
            processed_databases=processed_databases,
            not_processed_databases=not_processed_databases,
            protection_groups=protection_groups,
            last_protected_date=last_protected_date,
        )

        return protected_application_info
