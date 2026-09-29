import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.protected_application_platform import ProtectedApplicationPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_group import ProtectionGroup


T = TypeVar("T", bound="ProtectedApplicationInfo")


@_attrs_define
class ProtectedApplicationInfo:
    """
    Attributes:
        application_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to an application in Veeam Backup & Replication.
        backup_server_id (Union[None, Unset, int]): ID assigned to the Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
        name (Union[None, Unset, str]): Name of an application.
        is_cluster (Union[Unset, bool]): Indicates whether an application is a cluster.
        platform (Union[Unset, ProtectedApplicationPlatform]):
        processed_databases (Union[Unset, int]): Number of application databases processed by jobs.
        not_processed_databases (Union[Unset, int]): Number of application databases not processed by jobs.
        protection_groups (Union[None, Unset, list['ProtectionGroup']]): Array of protection groups that include the
            application.
        last_protected_date (Union[None, Unset, datetime.datetime]): Date and time when the latest successful job
            session finished.
    """

    application_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    is_cluster: Union[Unset, bool] = UNSET
    platform: Union[Unset, ProtectedApplicationPlatform] = UNSET
    processed_databases: Union[Unset, int] = UNSET
    not_processed_databases: Union[Unset, int] = UNSET
    protection_groups: Union[None, Unset, list["ProtectionGroup"]] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.application_uid_in_vbr, Unset):
            application_uid_in_vbr = UNSET
        elif isinstance(self.application_uid_in_vbr, UUID):
            application_uid_in_vbr = str(self.application_uid_in_vbr)
        else:
            application_uid_in_vbr = self.application_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        backup_server_name: Union[None, Unset, str]
        if isinstance(self.backup_server_name, Unset):
            backup_server_name = UNSET
        else:
            backup_server_name = self.backup_server_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_cluster = self.is_cluster

        platform: Union[Unset, str] = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        processed_databases = self.processed_databases

        not_processed_databases = self.not_processed_databases

        protection_groups: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.protection_groups, Unset):
            protection_groups = UNSET
        elif isinstance(self.protection_groups, list):
            protection_groups = []
            for protection_groups_type_0_item_data in self.protection_groups:
                protection_groups_type_0_item = protection_groups_type_0_item_data.to_dict()
                protection_groups.append(protection_groups_type_0_item)

        else:
            protection_groups = self.protection_groups

        last_protected_date: Union[None, Unset, str]
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
        from ..models.protection_group import ProtectionGroup

        d = dict(src_dict)

        def _parse_application_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_uid_in_vbr_type_0 = UUID(data)

                return application_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        application_uid_in_vbr = _parse_application_uid_in_vbr(d.pop("applicationUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_backup_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        backup_server_name = _parse_backup_server_name(d.pop("backupServerName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        is_cluster = d.pop("isCluster", UNSET)

        _platform = d.pop("platform", UNSET)
        platform: Union[Unset, ProtectedApplicationPlatform]
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ProtectedApplicationPlatform(_platform)

        processed_databases = d.pop("processedDatabases", UNSET)

        not_processed_databases = d.pop("notProcessedDatabases", UNSET)

        def _parse_protection_groups(data: object) -> Union[None, Unset, list["ProtectionGroup"]]:
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
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ProtectionGroup"]], data)

        protection_groups = _parse_protection_groups(d.pop("protectionGroups", UNSET))

        def _parse_last_protected_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_protected_date_type_0 = isoparse(data)

                return last_protected_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

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
