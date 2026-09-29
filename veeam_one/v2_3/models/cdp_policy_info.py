from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.cdp_policy_status import CdpPolicyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CdpPolicyInfo")


@_attrs_define
class CdpPolicyInfo:
    """
    Attributes:
        cdp_policy_uid (None | Unset | UUID): UID assigned to a job in Veeam Backup & Replication.
        backup_server_id (int | Unset): ID assigned to a Veeam Backup & Replication server.
        status (CdpPolicyStatus | Unset):
        name (None | str | Unset): Name of a job.
        description (None | str | Unset): Job description.
        rpo_sec (int | Unset): Recovery point objective, in seconds.
        short_term_retention_sec (int | Unset): Short-term retention, in seconds.
        long_term_retention_sec (int | Unset): Long-term retention, in seconds.
        keep_restore_points_in_days (int | Unset): Period for which the long-term restore points must be retained, in
            days.
        cluster_reference (None | str | Unset): Cluster where replicas must be stored.
        host_reference (None | str | Unset): Host where replicas must be stored.
        replica_name_suffix (None | str | Unset): Suffix that is added to names of replicas.
        source_proxy_auto_detect (bool | Unset): Indicates whether Veeam Backup & Replication selects source VMware CDP
            proxy automatically.
        target_proxy_auto_detect (bool | Unset): Indicates whether Veeam Backup & Replication selects target VMware CDP
            proxy automatically.
        is_application_aware_enabled (bool | Unset): Indicates whether application-aware processing is enabled.
    """

    cdp_policy_uid: None | Unset | UUID = UNSET
    backup_server_id: int | Unset = UNSET
    status: CdpPolicyStatus | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    rpo_sec: int | Unset = UNSET
    short_term_retention_sec: int | Unset = UNSET
    long_term_retention_sec: int | Unset = UNSET
    keep_restore_points_in_days: int | Unset = UNSET
    cluster_reference: None | str | Unset = UNSET
    host_reference: None | str | Unset = UNSET
    replica_name_suffix: None | str | Unset = UNSET
    source_proxy_auto_detect: bool | Unset = UNSET
    target_proxy_auto_detect: bool | Unset = UNSET
    is_application_aware_enabled: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cdp_policy_uid: None | str | Unset
        if isinstance(self.cdp_policy_uid, Unset):
            cdp_policy_uid = UNSET
        elif isinstance(self.cdp_policy_uid, UUID):
            cdp_policy_uid = str(self.cdp_policy_uid)
        else:
            cdp_policy_uid = self.cdp_policy_uid

        backup_server_id = self.backup_server_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        rpo_sec = self.rpo_sec

        short_term_retention_sec = self.short_term_retention_sec

        long_term_retention_sec = self.long_term_retention_sec

        keep_restore_points_in_days = self.keep_restore_points_in_days

        cluster_reference: None | str | Unset
        if isinstance(self.cluster_reference, Unset):
            cluster_reference = UNSET
        else:
            cluster_reference = self.cluster_reference

        host_reference: None | str | Unset
        if isinstance(self.host_reference, Unset):
            host_reference = UNSET
        else:
            host_reference = self.host_reference

        replica_name_suffix: None | str | Unset
        if isinstance(self.replica_name_suffix, Unset):
            replica_name_suffix = UNSET
        else:
            replica_name_suffix = self.replica_name_suffix

        source_proxy_auto_detect = self.source_proxy_auto_detect

        target_proxy_auto_detect = self.target_proxy_auto_detect

        is_application_aware_enabled = self.is_application_aware_enabled

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cdp_policy_uid is not UNSET:
            field_dict["cdpPolicyUid"] = cdp_policy_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if rpo_sec is not UNSET:
            field_dict["rpoSec"] = rpo_sec
        if short_term_retention_sec is not UNSET:
            field_dict["shortTermRetentionSec"] = short_term_retention_sec
        if long_term_retention_sec is not UNSET:
            field_dict["longTermRetentionSec"] = long_term_retention_sec
        if keep_restore_points_in_days is not UNSET:
            field_dict["keepRestorePointsInDays"] = keep_restore_points_in_days
        if cluster_reference is not UNSET:
            field_dict["clusterReference"] = cluster_reference
        if host_reference is not UNSET:
            field_dict["hostReference"] = host_reference
        if replica_name_suffix is not UNSET:
            field_dict["replicaNameSuffix"] = replica_name_suffix
        if source_proxy_auto_detect is not UNSET:
            field_dict["sourceProxyAutoDetect"] = source_proxy_auto_detect
        if target_proxy_auto_detect is not UNSET:
            field_dict["targetProxyAutoDetect"] = target_proxy_auto_detect
        if is_application_aware_enabled is not UNSET:
            field_dict["isApplicationAwareEnabled"] = is_application_aware_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cdp_policy_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cdp_policy_uid_type_0 = UUID(data)

                return cdp_policy_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cdp_policy_uid = _parse_cdp_policy_uid(d.pop("cdpPolicyUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: CdpPolicyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CdpPolicyStatus(_status)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        rpo_sec = d.pop("rpoSec", UNSET)

        short_term_retention_sec = d.pop("shortTermRetentionSec", UNSET)

        long_term_retention_sec = d.pop("longTermRetentionSec", UNSET)

        keep_restore_points_in_days = d.pop("keepRestorePointsInDays", UNSET)

        def _parse_cluster_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cluster_reference = _parse_cluster_reference(d.pop("clusterReference", UNSET))

        def _parse_host_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_reference = _parse_host_reference(d.pop("hostReference", UNSET))

        def _parse_replica_name_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replica_name_suffix = _parse_replica_name_suffix(d.pop("replicaNameSuffix", UNSET))

        source_proxy_auto_detect = d.pop("sourceProxyAutoDetect", UNSET)

        target_proxy_auto_detect = d.pop("targetProxyAutoDetect", UNSET)

        is_application_aware_enabled = d.pop("isApplicationAwareEnabled", UNSET)

        cdp_policy_info = cls(
            cdp_policy_uid=cdp_policy_uid,
            backup_server_id=backup_server_id,
            status=status,
            name=name,
            description=description,
            rpo_sec=rpo_sec,
            short_term_retention_sec=short_term_retention_sec,
            long_term_retention_sec=long_term_retention_sec,
            keep_restore_points_in_days=keep_restore_points_in_days,
            cluster_reference=cluster_reference,
            host_reference=host_reference,
            replica_name_suffix=replica_name_suffix,
            source_proxy_auto_detect=source_proxy_auto_detect,
            target_proxy_auto_detect=target_proxy_auto_detect,
            is_application_aware_enabled=is_application_aware_enabled,
        )

        return cdp_policy_info
