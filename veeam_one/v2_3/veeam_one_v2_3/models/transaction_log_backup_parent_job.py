from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.transaction_log_backup_parent_job_type import TransactionLogBackupParentJobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionLogBackupParentJob")


@_attrs_define
class TransactionLogBackupParentJob:
    """
    Attributes:
        parent_job_uid (Union[Unset, UUID]): UID assigned to a parent job.
        parent_job_name (Union[None, Unset, str]): Name of a parent job.
        parent_job_type (Union[Unset, TransactionLogBackupParentJobType]):
    """

    parent_job_uid: Union[Unset, UUID] = UNSET
    parent_job_name: Union[None, Unset, str] = UNSET
    parent_job_type: Union[Unset, TransactionLogBackupParentJobType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        parent_job_uid: Union[Unset, str] = UNSET
        if not isinstance(self.parent_job_uid, Unset):
            parent_job_uid = str(self.parent_job_uid)

        parent_job_name: Union[None, Unset, str]
        if isinstance(self.parent_job_name, Unset):
            parent_job_name = UNSET
        else:
            parent_job_name = self.parent_job_name

        parent_job_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_job_type, Unset):
            parent_job_type = self.parent_job_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if parent_job_uid is not UNSET:
            field_dict["parentJobUid"] = parent_job_uid
        if parent_job_name is not UNSET:
            field_dict["parentJobName"] = parent_job_name
        if parent_job_type is not UNSET:
            field_dict["parentJobType"] = parent_job_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _parent_job_uid = d.pop("parentJobUid", UNSET)
        parent_job_uid: Union[Unset, UUID]
        if isinstance(_parent_job_uid, Unset):
            parent_job_uid = UNSET
        else:
            parent_job_uid = UUID(_parent_job_uid)

        def _parse_parent_job_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_job_name = _parse_parent_job_name(d.pop("parentJobName", UNSET))

        _parent_job_type = d.pop("parentJobType", UNSET)
        parent_job_type: Union[Unset, TransactionLogBackupParentJobType]
        if isinstance(_parent_job_type, Unset):
            parent_job_type = UNSET
        else:
            parent_job_type = TransactionLogBackupParentJobType(_parent_job_type)

        transaction_log_backup_parent_job = cls(
            parent_job_uid=parent_job_uid,
            parent_job_name=parent_job_name,
            parent_job_type=parent_job_type,
        )

        return transaction_log_backup_parent_job
