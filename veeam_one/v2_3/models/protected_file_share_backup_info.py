import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.file_share_backup_job_type import FileShareBackupJobType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo


T = TypeVar("T", bound="ProtectedFileShareBackupInfo")


@_attrs_define
class ProtectedFileShareBackupInfo:
    """
    Attributes:
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup chain.
        file_share_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected file share.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job.
        job_name (Union[None, Unset, str]): Name of a backup job.
        job_type (Union[Unset, FileShareBackupJobType]):
        backup_size (Union[None, Unset, int]): Size of a file backup, in bytes.
        archive_size (Union[None, Unset, int]): Size of an archived file backup, in bytes.
        restore_points (Union[Unset, int]): Number of restore points.
        last_protected_date (Union[None, Unset, datetime.datetime]): Time and date of the latest restore point creation.
        repository (Union['ProtectedDataRepositoryInfo', None, Unset]): Information on a target backup repository.
        archive_repository (Union['ProtectedDataRepositoryInfo', None, Unset]): Information on an archive repository.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup & Replication server.
        backup_server_name (Union[None, Unset, str]): Name of a Veeam Backup & Replication server.
    """

    backup_uid: Union[None, UUID, Unset] = UNSET
    file_share_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    job_type: Union[Unset, FileShareBackupJobType] = UNSET
    backup_size: Union[None, Unset, int] = UNSET
    archive_size: Union[None, Unset, int] = UNSET
    restore_points: Union[Unset, int] = UNSET
    last_protected_date: Union[None, Unset, datetime.datetime] = UNSET
    repository: Union["ProtectedDataRepositoryInfo", None, Unset] = UNSET
    archive_repository: Union["ProtectedDataRepositoryInfo", None, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    backup_server_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo

        backup_uid: Union[None, Unset, str]
        if isinstance(self.backup_uid, Unset):
            backup_uid = UNSET
        elif isinstance(self.backup_uid, UUID):
            backup_uid = str(self.backup_uid)
        else:
            backup_uid = self.backup_uid

        file_share_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.file_share_uid_in_vbr, Unset):
            file_share_uid_in_vbr = UNSET
        elif isinstance(self.file_share_uid_in_vbr, UUID):
            file_share_uid_in_vbr = str(self.file_share_uid_in_vbr)
        else:
            file_share_uid_in_vbr = self.file_share_uid_in_vbr

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

        backup_size: Union[None, Unset, int]
        if isinstance(self.backup_size, Unset):
            backup_size = UNSET
        else:
            backup_size = self.backup_size

        archive_size: Union[None, Unset, int]
        if isinstance(self.archive_size, Unset):
            archive_size = UNSET
        else:
            archive_size = self.archive_size

        restore_points = self.restore_points

        last_protected_date: Union[None, Unset, str]
        if isinstance(self.last_protected_date, Unset):
            last_protected_date = UNSET
        elif isinstance(self.last_protected_date, datetime.datetime):
            last_protected_date = self.last_protected_date.isoformat()
        else:
            last_protected_date = self.last_protected_date

        repository: Union[None, Unset, dict[str, Any]]
        if isinstance(self.repository, Unset):
            repository = UNSET
        elif isinstance(self.repository, ProtectedDataRepositoryInfo):
            repository = self.repository.to_dict()
        else:
            repository = self.repository

        archive_repository: Union[None, Unset, dict[str, Any]]
        if isinstance(self.archive_repository, Unset):
            archive_repository = UNSET
        elif isinstance(self.archive_repository, ProtectedDataRepositoryInfo):
            archive_repository = self.archive_repository.to_dict()
        else:
            archive_repository = self.archive_repository

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if file_share_uid_in_vbr is not UNSET:
            field_dict["fileShareUidInVbr"] = file_share_uid_in_vbr
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if backup_size is not UNSET:
            field_dict["backupSize"] = backup_size
        if archive_size is not UNSET:
            field_dict["archiveSize"] = archive_size
        if restore_points is not UNSET:
            field_dict["restorePoints"] = restore_points
        if last_protected_date is not UNSET:
            field_dict["lastProtectedDate"] = last_protected_date
        if repository is not UNSET:
            field_dict["repository"] = repository
        if archive_repository is not UNSET:
            field_dict["archiveRepository"] = archive_repository
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if backup_server_name is not UNSET:
            field_dict["backupServerName"] = backup_server_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protected_data_repository_info import ProtectedDataRepositoryInfo

        d = dict(src_dict)

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

        def _parse_file_share_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_share_uid_in_vbr_type_0 = UUID(data)

                return file_share_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        file_share_uid_in_vbr = _parse_file_share_uid_in_vbr(d.pop("fileShareUidInVbr", UNSET))

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
        job_type: Union[Unset, FileShareBackupJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = FileShareBackupJobType(_job_type)

        def _parse_backup_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_size = _parse_backup_size(d.pop("backupSize", UNSET))

        def _parse_archive_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        archive_size = _parse_archive_size(d.pop("archiveSize", UNSET))

        restore_points = d.pop("restorePoints", UNSET)

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

        def _parse_repository(data: object) -> Union["ProtectedDataRepositoryInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repository_type_1 = ProtectedDataRepositoryInfo.from_dict(data)

                return repository_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProtectedDataRepositoryInfo", None, Unset], data)

        repository = _parse_repository(d.pop("repository", UNSET))

        def _parse_archive_repository(data: object) -> Union["ProtectedDataRepositoryInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                archive_repository_type_1 = ProtectedDataRepositoryInfo.from_dict(data)

                return archive_repository_type_1
            except:  # noqa: E722
                pass
            return cast(Union["ProtectedDataRepositoryInfo", None, Unset], data)

        archive_repository = _parse_archive_repository(d.pop("archiveRepository", UNSET))

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

        protected_file_share_backup_info = cls(
            backup_uid=backup_uid,
            file_share_uid_in_vbr=file_share_uid_in_vbr,
            job_uid=job_uid,
            job_name=job_name,
            job_type=job_type,
            backup_size=backup_size,
            archive_size=archive_size,
            restore_points=restore_points,
            last_protected_date=last_protected_date,
            repository=repository,
            archive_repository=archive_repository,
            backup_server_id=backup_server_id,
            backup_server_name=backup_server_name,
        )

        return protected_file_share_backup_info
