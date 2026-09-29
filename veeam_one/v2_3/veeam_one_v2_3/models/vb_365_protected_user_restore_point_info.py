import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.vb_365_job_type import Vb365JobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedUserRestorePointInfo")


@_attrs_define
class Vb365ProtectedUserRestorePointInfo:
    """
    Attributes:
        uid (Union[Unset, UUID]): UID assigned to a restore point.
        user_uid (Union[None, UUID, Unset]): UID assigned to a user.
        user_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a user in Veeam Backup for Microsoft 365.
        user_name (Union[None, Unset, str]): User name.
        is_mailbox_backedup (Union[Unset, bool]): Indicates whether a restore point includes the user mailbox backup.
        is_one_drive_backedup (Union[Unset, bool]): Indicates whether a restore point includes user OneDrive files
            backup.
        is_archive_backedup (Union[Unset, bool]): Indicates whether a restore point includes archive mailbox backup.
        is_site_backedup (Union[Unset, bool]): Indicates whether a restore point includes user site backup.
        organization_uid (Union[None, UUID, Unset]): UID assigned to a Microsoft organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft organization.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (Union[None, Unset, str]): Name of a Veeam Backup for Microsoft 365 server.
        repository_uid (Union[None, UUID, Unset]): UID assigned to a backup repository.
        repository_name (Union[None, Unset, str]): Name of a backup repository.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job.
        job_name (Union[None, Unset, str]): Name of a backup job.
        job_type (Union[Unset, Vb365JobType]):
        protection_date (Union[None, Unset, datetime.datetime]): Date and time when the restore point was created.
    """

    uid: Union[Unset, UUID] = UNSET
    user_uid: Union[None, UUID, Unset] = UNSET
    user_uid_in_vb_365: Union[None, Unset, str] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    is_mailbox_backedup: Union[Unset, bool] = UNSET
    is_one_drive_backedup: Union[Unset, bool] = UNSET
    is_archive_backedup: Union[Unset, bool] = UNSET
    is_site_backedup: Union[Unset, bool] = UNSET
    organization_uid: Union[None, UUID, Unset] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    vb_365_server_name: Union[None, Unset, str] = UNSET
    repository_uid: Union[None, UUID, Unset] = UNSET
    repository_name: Union[None, Unset, str] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    job_type: Union[Unset, Vb365JobType] = UNSET
    protection_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uid: Union[Unset, str] = UNSET
        if not isinstance(self.uid, Unset):
            uid = str(self.uid)

        user_uid: Union[None, Unset, str]
        if isinstance(self.user_uid, Unset):
            user_uid = UNSET
        elif isinstance(self.user_uid, UUID):
            user_uid = str(self.user_uid)
        else:
            user_uid = self.user_uid

        user_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.user_uid_in_vb_365, Unset):
            user_uid_in_vb_365 = UNSET
        else:
            user_uid_in_vb_365 = self.user_uid_in_vb_365

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        is_mailbox_backedup = self.is_mailbox_backedup

        is_one_drive_backedup = self.is_one_drive_backedup

        is_archive_backedup = self.is_archive_backedup

        is_site_backedup = self.is_site_backedup

        organization_uid: Union[None, Unset, str]
        if isinstance(self.organization_uid, Unset):
            organization_uid = UNSET
        elif isinstance(self.organization_uid, UUID):
            organization_uid = str(self.organization_uid)
        else:
            organization_uid = self.organization_uid

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        vb_365_server_id = self.vb_365_server_id

        vb_365_server_name: Union[None, Unset, str]
        if isinstance(self.vb_365_server_name, Unset):
            vb_365_server_name = UNSET
        else:
            vb_365_server_name = self.vb_365_server_name

        repository_uid: Union[None, Unset, str]
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        repository_name: Union[None, Unset, str]
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

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

        job_type: Union[Unset, str] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        protection_date: Union[None, Unset, str]
        if isinstance(self.protection_date, Unset):
            protection_date = UNSET
        elif isinstance(self.protection_date, datetime.datetime):
            protection_date = self.protection_date.isoformat()
        else:
            protection_date = self.protection_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uid is not UNSET:
            field_dict["uid"] = uid
        if user_uid is not UNSET:
            field_dict["userUid"] = user_uid
        if user_uid_in_vb_365 is not UNSET:
            field_dict["userUidInVb365"] = user_uid_in_vb_365
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if is_mailbox_backedup is not UNSET:
            field_dict["isMailboxBackedup"] = is_mailbox_backedup
        if is_one_drive_backedup is not UNSET:
            field_dict["isOneDriveBackedup"] = is_one_drive_backedup
        if is_archive_backedup is not UNSET:
            field_dict["isArchiveBackedup"] = is_archive_backedup
        if is_site_backedup is not UNSET:
            field_dict["isSiteBackedup"] = is_site_backedup
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if vb_365_server_name is not UNSET:
            field_dict["vb365ServerName"] = vb_365_server_name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if repository_name is not UNSET:
            field_dict["repositoryName"] = repository_name
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if protection_date is not UNSET:
            field_dict["protectionDate"] = protection_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _uid = d.pop("uid", UNSET)
        uid: Union[Unset, UUID]
        if isinstance(_uid, Unset):
            uid = UNSET
        else:
            uid = UUID(_uid)

        def _parse_user_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_uid_type_0 = UUID(data)

                return user_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        user_uid = _parse_user_uid(d.pop("userUid", UNSET))

        def _parse_user_uid_in_vb_365(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_uid_in_vb_365 = _parse_user_uid_in_vb_365(d.pop("userUidInVb365", UNSET))

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        is_mailbox_backedup = d.pop("isMailboxBackedup", UNSET)

        is_one_drive_backedup = d.pop("isOneDriveBackedup", UNSET)

        is_archive_backedup = d.pop("isArchiveBackedup", UNSET)

        is_site_backedup = d.pop("isSiteBackedup", UNSET)

        def _parse_organization_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_uid_type_0 = UUID(data)

                return organization_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        organization_uid = _parse_organization_uid(d.pop("organizationUid", UNSET))

        def _parse_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_vb_365_server_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vb_365_server_name = _parse_vb_365_server_name(d.pop("vb365ServerName", UNSET))

        def _parse_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_repository_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

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

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, Vb365JobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = Vb365JobType(_job_type)

        def _parse_protection_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protection_date_type_0 = isoparse(data)

                return protection_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        protection_date = _parse_protection_date(d.pop("protectionDate", UNSET))

        vb_365_protected_user_restore_point_info = cls(
            uid=uid,
            user_uid=user_uid,
            user_uid_in_vb_365=user_uid_in_vb_365,
            user_name=user_name,
            is_mailbox_backedup=is_mailbox_backedup,
            is_one_drive_backedup=is_one_drive_backedup,
            is_archive_backedup=is_archive_backedup,
            is_site_backedup=is_site_backedup,
            organization_uid=organization_uid,
            organization_name=organization_name,
            vb_365_server_id=vb_365_server_id,
            vb_365_server_name=vb_365_server_name,
            repository_uid=repository_uid,
            repository_name=repository_name,
            job_uid=job_uid,
            job_name=job_name,
            job_type=job_type,
            protection_date=protection_date,
        )

        return vb_365_protected_user_restore_point_info
