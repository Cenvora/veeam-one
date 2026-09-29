from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_job_type import Vb365JobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ProtectedTeamRestorePointInfo")


@_attrs_define
class Vb365ProtectedTeamRestorePointInfo:
    """
    Attributes:
        uid (UUID | Unset): UID assigned to a restore point.
        team_uid (UUID | Unset): UID assigned to a team.
        team_name (None | str | Unset): Name of a team.
        organization_uid (UUID | Unset): UID assigned to a Microsoft organization.
        organization_name (None | str | Unset): Name of a Microsoft organization.
        vb_365_server_id (int | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        vb_365_server_name (None | str | Unset): Name of a Veeam Backup for Microsoft 365 server.
        repository_uid (None | Unset | UUID): UID assigned to a backup repository.
        repository_name (None | str | Unset): Name of backup repository.
        job_uid (None | Unset | UUID): UID assigned to a backup job.
        job_name (None | str | Unset): Name of a backup job.
        job_type (Vb365JobType | Unset):
        protection_date (datetime.datetime | None | Unset): Date and time when the restore point was created.
    """

    uid: UUID | Unset = UNSET
    team_uid: UUID | Unset = UNSET
    team_name: None | str | Unset = UNSET
    organization_uid: UUID | Unset = UNSET
    organization_name: None | str | Unset = UNSET
    vb_365_server_id: int | Unset = UNSET
    vb_365_server_name: None | str | Unset = UNSET
    repository_uid: None | Unset | UUID = UNSET
    repository_name: None | str | Unset = UNSET
    job_uid: None | Unset | UUID = UNSET
    job_name: None | str | Unset = UNSET
    job_type: Vb365JobType | Unset = UNSET
    protection_date: datetime.datetime | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uid: str | Unset = UNSET
        if not isinstance(self.uid, Unset):
            uid = str(self.uid)

        team_uid: str | Unset = UNSET
        if not isinstance(self.team_uid, Unset):
            team_uid = str(self.team_uid)

        team_name: None | str | Unset
        if isinstance(self.team_name, Unset):
            team_name = UNSET
        else:
            team_name = self.team_name

        organization_uid: str | Unset = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: None | str | Unset
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        vb_365_server_id = self.vb_365_server_id

        vb_365_server_name: None | str | Unset
        if isinstance(self.vb_365_server_name, Unset):
            vb_365_server_name = UNSET
        else:
            vb_365_server_name = self.vb_365_server_name

        repository_uid: None | str | Unset
        if isinstance(self.repository_uid, Unset):
            repository_uid = UNSET
        elif isinstance(self.repository_uid, UUID):
            repository_uid = str(self.repository_uid)
        else:
            repository_uid = self.repository_uid

        repository_name: None | str | Unset
        if isinstance(self.repository_name, Unset):
            repository_name = UNSET
        else:
            repository_name = self.repository_name

        job_uid: None | str | Unset
        if isinstance(self.job_uid, Unset):
            job_uid = UNSET
        elif isinstance(self.job_uid, UUID):
            job_uid = str(self.job_uid)
        else:
            job_uid = self.job_uid

        job_name: None | str | Unset
        if isinstance(self.job_name, Unset):
            job_name = UNSET
        else:
            job_name = self.job_name

        job_type: str | Unset = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        protection_date: None | str | Unset
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
        if team_uid is not UNSET:
            field_dict["teamUid"] = team_uid
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
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
        uid: UUID | Unset
        if isinstance(_uid, Unset):
            uid = UNSET
        else:
            uid = UUID(_uid)

        _team_uid = d.pop("teamUid", UNSET)
        team_uid: UUID | Unset
        if isinstance(_team_uid, Unset):
            team_uid = UNSET
        else:
            team_uid = UUID(_team_uid)

        def _parse_team_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        team_name = _parse_team_name(d.pop("teamName", UNSET))

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: UUID | Unset
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_organization_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        def _parse_vb_365_server_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vb_365_server_name = _parse_vb_365_server_name(d.pop("vb365ServerName", UNSET))

        def _parse_repository_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                repository_uid_type_0 = UUID(data)

                return repository_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        repository_uid = _parse_repository_uid(d.pop("repositoryUid", UNSET))

        def _parse_repository_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repository_name = _parse_repository_name(d.pop("repositoryName", UNSET))

        def _parse_job_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_uid_type_0 = UUID(data)

                return job_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_uid = _parse_job_uid(d.pop("jobUid", UNSET))

        def _parse_job_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_name = _parse_job_name(d.pop("jobName", UNSET))

        _job_type = d.pop("jobType", UNSET)
        job_type: Vb365JobType | Unset
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = Vb365JobType(_job_type)

        def _parse_protection_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protection_date_type_0 = datetime.datetime.fromisoformat(data)

                return protection_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        protection_date = _parse_protection_date(d.pop("protectionDate", UNSET))

        vb_365_protected_team_restore_point_info = cls(
            uid=uid,
            team_uid=team_uid,
            team_name=team_name,
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

        return vb_365_protected_team_restore_point_info
