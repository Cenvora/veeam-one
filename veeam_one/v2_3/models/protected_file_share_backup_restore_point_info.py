import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unstructured_data_source import UnstructuredDataSource


T = TypeVar("T", bound="ProtectedFileShareBackupRestorePointInfo")


@_attrs_define
class ProtectedFileShareBackupRestorePointInfo:
    """
    Attributes:
        restore_point_uid (Union[Unset, UUID]): UID assigned to a restore point.
        file_share_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a protected file share.
        backup_uid (Union[None, UUID, Unset]): UID assigned to a backup chain.
        job_uid (Union[None, UUID, Unset]): UID assigned to a backup job.
        job_name (Union[None, Unset, str]): Name of a backup job.
        repository_uid (Union[None, UUID, Unset]): UID assigned to a repository on which a restore point resides.
        archive_repository_uid (Union[None, UUID, Unset]): UID assigned to an archive repository on which a restore
            point resides.
        source_size_bytes (Union[None, Unset, int]): Size of protected data, in bytes.
        creation_date (Union[None, Unset, datetime.datetime]): Time and date when a restore point was created.
        immutable_till (Union[None, Unset, datetime.datetime]): Date and time till which a restore point remains
            immutable.
        is_long_term (Union[None, Unset, bool]): Indicates whether protected files are stored in archive repository.
        sources (Union[None, Unset, list['UnstructuredDataSource']]): Information on protected files and folders.
    """

    restore_point_uid: Union[Unset, UUID] = UNSET
    file_share_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_uid: Union[None, UUID, Unset] = UNSET
    job_uid: Union[None, UUID, Unset] = UNSET
    job_name: Union[None, Unset, str] = UNSET
    repository_uid: Union[None, UUID, Unset] = UNSET
    archive_repository_uid: Union[None, UUID, Unset] = UNSET
    source_size_bytes: Union[None, Unset, int] = UNSET
    creation_date: Union[None, Unset, datetime.datetime] = UNSET
    immutable_till: Union[None, Unset, datetime.datetime] = UNSET
    is_long_term: Union[None, Unset, bool] = UNSET
    sources: Union[None, Unset, list["UnstructuredDataSource"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        restore_point_uid: Union[Unset, str] = UNSET
        if not isinstance(self.restore_point_uid, Unset):
            restore_point_uid = str(self.restore_point_uid)

        file_share_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.file_share_uid_in_vbr, Unset):
            file_share_uid_in_vbr = UNSET
        elif isinstance(self.file_share_uid_in_vbr, UUID):
            file_share_uid_in_vbr = str(self.file_share_uid_in_vbr)
        else:
            file_share_uid_in_vbr = self.file_share_uid_in_vbr

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

        repository_uid: Union[None, Unset, str]
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        archive_repository_uid: Union[None, Unset, str]
        if isinstance(self.archive_repository_uid, Unset):
            archive_repository_uid = UNSET
        elif isinstance(self.archive_repository_uid, UUID):
            archive_repository_uid = str(self.archive_repository_uid)
        else:
            archive_repository_uid = self.archive_repository_uid

        source_size_bytes: Union[None, Unset, int]
        if isinstance(self.source_size_bytes, Unset):
            source_size_bytes = UNSET
        else:
            source_size_bytes = self.source_size_bytes

        creation_date: Union[None, Unset, str]
        if isinstance(self.creation_date, Unset):
            creation_date = UNSET
        elif isinstance(self.creation_date, datetime.datetime):
            creation_date = self.creation_date.isoformat()
        else:
            creation_date = self.creation_date

        immutable_till: Union[None, Unset, str]
        if isinstance(self.immutable_till, Unset):
            immutable_till = UNSET
        elif isinstance(self.immutable_till, datetime.datetime):
            immutable_till = self.immutable_till.isoformat()
        else:
            immutable_till = self.immutable_till

        is_long_term: Union[None, Unset, bool]
        if isinstance(self.is_long_term, Unset):
            is_long_term = UNSET
        else:
            is_long_term = self.is_long_term

        sources: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.sources, Unset):
            sources = UNSET
        elif isinstance(self.sources, list):
            sources = []
            for sources_type_0_item_data in self.sources:
                sources_type_0_item = sources_type_0_item_data.to_dict()
                sources.append(sources_type_0_item)

        else:
            sources = self.sources

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if restore_point_uid is not UNSET:
            field_dict["restorePointUid"] = restore_point_uid
        if file_share_uid_in_vbr is not UNSET:
            field_dict["fileShareUidInVbr"] = file_share_uid_in_vbr
        if backup_uid is not UNSET:
            field_dict["backupUid"] = backup_uid
        if job_uid is not UNSET:
            field_dict["jobUid"] = job_uid
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if repository_uid is not UNSET:
            field_dict["repositoryUid"] = repository_uid
        if archive_repository_uid is not UNSET:
            field_dict["archiveRepositoryUid"] = archive_repository_uid
        if source_size_bytes is not UNSET:
            field_dict["sourceSizeBytes"] = source_size_bytes
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if immutable_till is not UNSET:
            field_dict["immutableTill"] = immutable_till
        if is_long_term is not UNSET:
            field_dict["isLongTerm"] = is_long_term
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.unstructured_data_source import UnstructuredDataSource

        d = dict(src_dict)
        _restore_point_uid = d.pop("restorePointUid", UNSET)
        restore_point_uid: Union[Unset, UUID]
        if isinstance(_restore_point_uid, Unset):
            restore_point_uid = UNSET
        else:
            restore_point_uid = UUID(_restore_point_uid)

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

        def _parse_archive_repository_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archive_repository_uid_type_0 = UUID(data)

                return archive_repository_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        archive_repository_uid = _parse_archive_repository_uid(d.pop("archiveRepositoryUid", UNSET))

        def _parse_source_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        source_size_bytes = _parse_source_size_bytes(d.pop("sourceSizeBytes", UNSET))

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

        def _parse_immutable_till(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                immutable_till_type_0 = isoparse(data)

                return immutable_till_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        immutable_till = _parse_immutable_till(d.pop("immutableTill", UNSET))

        def _parse_is_long_term(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_long_term = _parse_is_long_term(d.pop("isLongTerm", UNSET))

        def _parse_sources(data: object) -> Union[None, Unset, list["UnstructuredDataSource"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sources_type_0 = []
                _sources_type_0 = data
                for sources_type_0_item_data in _sources_type_0:
                    sources_type_0_item = UnstructuredDataSource.from_dict(sources_type_0_item_data)

                    sources_type_0.append(sources_type_0_item)

                return sources_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["UnstructuredDataSource"]], data)

        sources = _parse_sources(d.pop("sources", UNSET))

        protected_file_share_backup_restore_point_info = cls(
            restore_point_uid=restore_point_uid,
            file_share_uid_in_vbr=file_share_uid_in_vbr,
            backup_uid=backup_uid,
            job_uid=job_uid,
            job_name=job_name,
            repository_uid=repository_uid,
            archive_repository_uid=archive_repository_uid,
            source_size_bytes=source_size_bytes,
            creation_date=creation_date,
            immutable_till=immutable_till,
            is_long_term=is_long_term,
            sources=sources,
        )

        return protected_file_share_backup_restore_point_info
