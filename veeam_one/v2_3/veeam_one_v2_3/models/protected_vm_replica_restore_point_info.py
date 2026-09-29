import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hardware_plan import HardwarePlan


T = TypeVar("T", bound="ProtectedVmReplicaRestorePointInfo")


@_attrs_define
class ProtectedVmReplicaRestorePointInfo:
    """
    Attributes:
        replica_restore_point_uid (Union[Unset, UUID]): UID assigned to a replication restore point.
        vm_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected VM.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a replication chain.
        job_uid (Union[None, UUID, Unset]): UID assigned to a replication job.
        job_name (Union[None, Unset, str]): Name of a replication job.
        hardware_plan (Union['HardwarePlan', None, Unset]): Hardware plan.
        creation_date (Union[None, Unset, datetime.datetime]): Time and date when a restore point was created.
    """

    replica_restore_point_uid: Union[Unset, UUID] = UNSET
    vm_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    hardware_plan: Union["HardwarePlan", None, Unset] = UNSET
    creation_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.hardware_plan import HardwarePlan

        replica_restore_point_uid: Union[Unset, str] = UNSET
        if not isinstance(self.replica_restore_point_uid, Unset):
            replica_restore_point_uid = str(self.replica_restore_point_uid)

        vm_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.vm_uid_in_vbr, Unset):
            vm_uid_in_vbr = UNSET
        elif isinstance(self.vm_uid_in_vbr, UUID):
            vm_uid_in_vbr = str(self.vm_uid_in_vbr)
        else:
            vm_uid_in_vbr = self.vm_uid_in_vbr

        backup_uid: Union[None, Unset, str]
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        job_uid: Union[None, Unset, str]
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        job_name: Union[None, Unset, str]
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        hardware_plan: Union[None, Unset, dict[str, Any]]
        if isinstance(self.hardware_plan, Unset):
            hardware_plan = UNSET
        elif isinstance(self.hardware_plan, HardwarePlan):
            hardware_plan = self.hardware_plan.to_dict()
        else:
            hardware_plan = self.hardware_plan

        creation_date: Union[None, Unset, str]
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if replica_restore_point_uid is not UNSET:
            field_dict["replicaRestorePointUid"] = replica_restore_point_uid
        if vm_uid_in_vbr is not UNSET:
            field_dict["vmUidInVbr"] = vm_uid_in_vbr
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if hardware_plan is not UNSET:
            field_dict["hardwarePlan"] = hardware_plan
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hardware_plan import HardwarePlan

        d = dict(src_dict)
        _replica_restore_point_uid = d.pop("replicaRestorePointUid", UNSET)
        replica_restore_point_uid: Union[Unset, UUID]
        if isinstance(_replica_restore_point_uid, Unset):
            replica_restore_point_uid = UNSET
        else:
            replica_restore_point_uid = UUID(_replica_restore_point_uid)

        def _parse_vm_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                vm_uid_in_vbr_type_0 = UUID(data)

                return vm_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        vm_uid_in_vbr = _parse_vm_uid_in_vbr(d.pop("vmUidInVbr", UNSET))

        def _parse_backup_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_uid_type_0 = UUID(data)

                return backup_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_uid = _parse_backup_uid(d.pop("backupUid", UNSET))

        def _parse_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_job_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        def _parse_hardware_plan(data: object) -> Union["HardwarePlan", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hardware_plan_type_1 = HardwarePlan.from_dict(data)

                return hardware_plan_type_1
            except:  # noqa: E722
                pass
            return cast(Union["HardwarePlan", None, Unset], data)

        hardware_plan = _parse_hardware_plan(d.pop("hardwarePlan", UNSET))

        def _parse_creation_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                creation_date_type_0 = isoparse(data)

                return creation_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        creation_date = _parse_creation_date(d.pop("creationDate", UNSET))

        protected_vm_replica_restore_point_info = cls(
            replica_restore_point_uid=replica_restore_point_uid,
            vm_uid_in_vbr=vm_uid_in_vbr,
            backup_uid=backup_uid,
            job_uid=job_uid,
            job_name=job_name,
            hardware_plan=hardware_plan,
            creation_date=creation_date,
        )

        return protected_vm_replica_restore_point_info
