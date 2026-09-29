from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.backup_platform_type import BackupPlatformType
from ..models.backup_server_connection_state import BackupServerConnectionState
from ..models.best_practice_check_status import BestPracticeCheckStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupServerInfo")


@_attrs_define
class BackupServerInfo:
    """
    Attributes:
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        enterprise_manager_id (int | None | Unset): ID assigned to Veeam Backup Enterprise Manager.
        name (None | str | Unset): Veeam Backup & Replication server name.
        version (None | str | Unset): Version of Veeam Backup & Replication installed on the server.
        is_cluster (bool | Unset): Indicates whether a Veeam Backup & Replication server is a part of a High
            Availability cluster.
        cluster_name (None | str | Unset): Name of a High Availability cluster that includes a Veeam Backup &
            Replication server..
        connection_error (None | str | Unset): Details on Veeam Backup & Replication server connection failure.
        connection_state (BackupServerConnectionState | Unset):
        is_configuration_backup_enabled (bool | None | Unset): Indicates whether configuration backup is enabled.
        platform (BackupPlatformType | Unset):
        is_cloud_connect (bool | None | Unset): Indicates whether a Veeam Backup & Replication server acts as a Veeam
            Cloud Connect server.
        intelligent_diagnostics_enabled (bool | None | Unset): Indicates whether Veeam Intelligent Diagnostics is
            enabled for a Veeam Backup & Replication server.
        remediation_actions_enabled (bool | None | Unset): Indicates whether remediation actions for alarms are enabled
            for a Veeam Backup & Replication server.
        last_best_practice_check_date (datetime.datetime | None | Unset): Date and time of the latest best practices
            check.
        best_practice_check_status (BestPracticeCheckStatus | Unset):
    """

    backup_server_id: int | Unset = UNSET
    enterprise_manager_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    is_cluster: bool | Unset = UNSET
    cluster_name: None | str | Unset = UNSET
    connection_error: None | str | Unset = UNSET
    connection_state: BackupServerConnectionState | Unset = UNSET
    is_configuration_backup_enabled: bool | None | Unset = UNSET
    platform: BackupPlatformType | Unset = UNSET
    is_cloud_connect: bool | None | Unset = UNSET
    intelligent_diagnostics_enabled: bool | None | Unset = UNSET
    remediation_actions_enabled: bool | None | Unset = UNSET
    last_best_practice_check_date: datetime.datetime | None | Unset = UNSET
    best_practice_check_status: BestPracticeCheckStatus | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_server_id = self.backup_server_id

        enterprise_manager_id: int | None | Unset
        if isinstance(self.enterprise_manager_id, Unset):
            enterprise_manager_id = UNSET
        else:
            enterprise_manager_id = self.enterprise_manager_id

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

        is_cluster = self.is_cluster

        cluster_name: None | str | Unset
        if isinstance(self.cluster_name, Unset):
            cluster_name = UNSET
        else:
            cluster_name = self.cluster_name

        connection_error: None | str | Unset
        if isinstance(self.connection_error, Unset):
            connection_error = UNSET
        else:
            connection_error = self.connection_error

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        is_configuration_backup_enabled: bool | None | Unset
        if isinstance(self.is_configuration_backup_enabled, Unset):
            is_configuration_backup_enabled = UNSET
        else:
            is_configuration_backup_enabled = self.is_configuration_backup_enabled

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        is_cloud_connect: bool | None | Unset
        if isinstance(self.is_cloud_connect, Unset):
            is_cloud_connect = UNSET
        else:
            is_cloud_connect = self.is_cloud_connect

        intelligent_diagnostics_enabled: bool | None | Unset
        if isinstance(self.intelligent_diagnostics_enabled, Unset):
            intelligent_diagnostics_enabled = UNSET
        else:
            intelligent_diagnostics_enabled = self.intelligent_diagnostics_enabled

        remediation_actions_enabled: bool | None | Unset
        if isinstance(self.remediation_actions_enabled, Unset):
            remediation_actions_enabled = UNSET
        else:
            remediation_actions_enabled = self.remediation_actions_enabled

        last_best_practice_check_date: None | str | Unset
        if isinstance(self.last_best_practice_check_date, Unset):
            last_best_practice_check_date = UNSET
        elif isinstance(self.last_best_practice_check_date, datetime.datetime):
            last_best_practice_check_date = self.last_best_practice_check_date.isoformat()
        else:
            last_best_practice_check_date = self.last_best_practice_check_date

        best_practice_check_status: str | Unset = UNSET
        if not isinstance(self.best_practice_check_status, Unset):
            best_practice_check_status = self.best_practice_check_status.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if enterprise_manager_id is not UNSET:
            field_dict["enterpriseManagerId"] = enterprise_manager_id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if is_cluster is not UNSET:
            field_dict["isCluster"] = is_cluster
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if connection_error is not UNSET:
            field_dict["connectionError"] = connection_error
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if is_configuration_backup_enabled is not UNSET:
            field_dict["isConfigurationBackupEnabled"] = is_configuration_backup_enabled
        if platform is not UNSET:
            field_dict["platform"] = platform
        if is_cloud_connect is not UNSET:
            field_dict["isCloudConnect"] = is_cloud_connect
        if intelligent_diagnostics_enabled is not UNSET:
            field_dict["intelligentDiagnosticsEnabled"] = intelligent_diagnostics_enabled
        if remediation_actions_enabled is not UNSET:
            field_dict["remediationActionsEnabled"] = remediation_actions_enabled
        if last_best_practice_check_date is not UNSET:
            field_dict["lastBestPracticeCheckDate"] = last_best_practice_check_date
        if best_practice_check_status is not UNSET:
            field_dict["bestPracticeCheckStatus"] = best_practice_check_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_server_id = d.pop("backupServerId", UNSET)

        def _parse_enterprise_manager_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        enterprise_manager_id = _parse_enterprise_manager_id(d.pop("enterpriseManagerId", UNSET))

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

        is_cluster = d.pop("isCluster", UNSET)

        def _parse_cluster_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_name = _parse_cluster_name(d.pop("clusterName", UNSET))

        def _parse_connection_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_error = _parse_connection_error(d.pop("connectionError", UNSET))

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: BackupServerConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = BackupServerConnectionState(_connection_state)

        def _parse_is_configuration_backup_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_configuration_backup_enabled = _parse_is_configuration_backup_enabled(
            d.pop("isConfigurationBackupEnabled", UNSET)
        )

        _platform = d.pop("platform", UNSET)
        platform: BackupPlatformType | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = BackupPlatformType(_platform)

        def _parse_is_cloud_connect(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_cloud_connect = _parse_is_cloud_connect(d.pop("isCloudConnect", UNSET))

        def _parse_intelligent_diagnostics_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        intelligent_diagnostics_enabled = _parse_intelligent_diagnostics_enabled(
            d.pop("intelligentDiagnosticsEnabled", UNSET)
        )

        def _parse_remediation_actions_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        remediation_actions_enabled = _parse_remediation_actions_enabled(d.pop("remediationActionsEnabled", UNSET))

        def _parse_last_best_practice_check_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_best_practice_check_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_best_practice_check_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_best_practice_check_date = _parse_last_best_practice_check_date(d.pop("lastBestPracticeCheckDate", UNSET))

        _best_practice_check_status = d.pop("bestPracticeCheckStatus", UNSET)
        best_practice_check_status: BestPracticeCheckStatus | Unset
        if isinstance(_best_practice_check_status, Unset):
            best_practice_check_status = UNSET
        else:
            best_practice_check_status = BestPracticeCheckStatus(_best_practice_check_status)

        backup_server_info = cls(
            backup_server_id=backup_server_id,
            enterprise_manager_id=enterprise_manager_id,
            name=name,
            version=version,
            is_cluster=is_cluster,
            cluster_name=cluster_name,
            connection_error=connection_error,
            connection_state=connection_state,
            is_configuration_backup_enabled=is_configuration_backup_enabled,
            platform=platform,
            is_cloud_connect=is_cloud_connect,
            intelligent_diagnostics_enabled=intelligent_diagnostics_enabled,
            remediation_actions_enabled=remediation_actions_enabled,
            last_best_practice_check_date=last_best_practice_check_date,
            best_practice_check_status=best_practice_check_status,
        )

        return backup_server_info
