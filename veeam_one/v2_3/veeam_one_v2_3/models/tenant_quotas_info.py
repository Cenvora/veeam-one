import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantQuotasInfo")


@_attrs_define
class TenantQuotasInfo:
    """
    Attributes:
        tenant_quota_id (Union[Unset, int]): ID assigned to a tenant quota.
        tenant_quota_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a tenant quota in Veeam Cloud Connect.
        tenant_id (Union[None, Unset, int]): ID assigned to a tenant.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Cloud Connect server.
        quota_mb (Union[None, Unset, int]): Cloud storage space allocated to a tenant, in MB.
        used_quota_mb (Union[None, Unset, int]): Cloud storage space consumed by a tenant.
        protected_vms_count (Union[None, Unset, int]): Number of VMs that are protected by tenant jobs.
        last_backup_activity_time (Union[None, Unset, datetime.datetime]): Date and time when the latest tenant job
            session finished.
        servers_count (Union[None, Unset, int]): Number of servers that are protected by tenant jobs.
        workstations_count (Union[None, Unset, int]): Number of workstations that are protected by tenant jobs.
    """

    tenant_quota_id: Union[Unset, int] = UNSET
    tenant_quota_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    tenant_id: Union[None, Unset, int] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    quota_mb: Union[None, Unset, int] = UNSET
    used_quota_mb: Union[None, Unset, int] = UNSET
    protected_vms_count: Union[None, Unset, int] = UNSET
    last_backup_activity_time: Union[None, Unset, datetime.datetime] = UNSET
    servers_count: Union[None, Unset, int] = UNSET
    workstations_count: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_quota_id = self.tenant_quota_id

        tenant_quota_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.tenant_quota_uid_in_vbr, Unset):
            tenant_quota_uid_in_vbr = UNSET
        elif isinstance(self.tenant_quota_uid_in_vbr, UUID):
            tenant_quota_uid_in_vbr = str(self.tenant_quota_uid_in_vbr)
        else:
            tenant_quota_uid_in_vbr = self.tenant_quota_uid_in_vbr

        tenant_id: Union[None, Unset, int]
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        quota_mb: Union[None, Unset, int]
        if isinstance(self.quota_mb, Unset):
            quota_mb = UNSET
        else:
            quota_mb = self.quota_mb

        used_quota_mb: Union[None, Unset, int]
        if isinstance(self.used_quota_mb, Unset):
            used_quota_mb = UNSET
        else:
            used_quota_mb = self.used_quota_mb

        protected_vms_count: Union[None, Unset, int]
        if isinstance(self.protected_vms_count, Unset):
            protected_vms_count = UNSET
        else:
            protected_vms_count = self.protected_vms_count

        last_backup_activity_time: Union[None, Unset, str]
        if isinstance(self.last_backup_activity_time, Unset):
            last_backup_activity_time = UNSET
        elif isinstance(self.last_backup_activity_time, datetime.datetime):
            last_backup_activity_time = self.last_backup_activity_time.isoformat()
        else:
            last_backup_activity_time = self.last_backup_activity_time

        servers_count: Union[None, Unset, int]
        if isinstance(self.servers_count, Unset):
            servers_count = UNSET
        else:
            servers_count = self.servers_count

        workstations_count: Union[None, Unset, int]
        if isinstance(self.workstations_count, Unset):
            workstations_count = UNSET
        else:
            workstations_count = self.workstations_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tenant_quota_id is not UNSET:
            field_dict["tenantQuotaId"] = tenant_quota_id
        if tenant_quota_uid_in_vbr is not UNSET:
            field_dict["tenantQuotaUidInVbr"] = tenant_quota_uid_in_vbr
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if quota_mb is not UNSET:
            field_dict["quotaMb"] = quota_mb
        if used_quota_mb is not UNSET:
            field_dict["usedQuotaMb"] = used_quota_mb
        if protected_vms_count is not UNSET:
            field_dict["protectedVmsCount"] = protected_vms_count
        if last_backup_activity_time is not UNSET:
            field_dict["lastBackupActivityTime"] = last_backup_activity_time
        if servers_count is not UNSET:
            field_dict["serversCount"] = servers_count
        if workstations_count is not UNSET:
            field_dict["workstationsCount"] = workstations_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_quota_id = d.pop("tenantQuotaId", UNSET)

        def _parse_tenant_quota_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_quota_uid_in_vbr_type_0 = UUID(data)

                return tenant_quota_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        tenant_quota_uid_in_vbr = _parse_tenant_quota_uid_in_vbr(d.pop("tenantQuotaUidInVbr", UNSET))

        def _parse_tenant_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_quota_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quota_mb = _parse_quota_mb(d.pop("quotaMb", UNSET))

        def _parse_used_quota_mb(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        used_quota_mb = _parse_used_quota_mb(d.pop("usedQuotaMb", UNSET))

        def _parse_protected_vms_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        protected_vms_count = _parse_protected_vms_count(d.pop("protectedVmsCount", UNSET))

        def _parse_last_backup_activity_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_backup_activity_time_type_0 = isoparse(data)

                return last_backup_activity_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_backup_activity_time = _parse_last_backup_activity_time(d.pop("lastBackupActivityTime", UNSET))

        def _parse_servers_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        servers_count = _parse_servers_count(d.pop("serversCount", UNSET))

        def _parse_workstations_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        workstations_count = _parse_workstations_count(d.pop("workstationsCount", UNSET))

        tenant_quotas_info = cls(
            tenant_quota_id=tenant_quota_id,
            tenant_quota_uid_in_vbr=tenant_quota_uid_in_vbr,
            tenant_id=tenant_id,
            backup_server_id=backup_server_id,
            quota_mb=quota_mb,
            used_quota_mb=used_quota_mb,
            protected_vms_count=protected_vms_count,
            last_backup_activity_time=last_backup_activity_time,
            servers_count=servers_count,
            workstations_count=workstations_count,
        )

        return tenant_quotas_info
