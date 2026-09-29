from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionGroup")


@_attrs_define
class ProtectionGroup:
    """
    Attributes:
        group_uid (Union[Unset, UUID]): UID assigned to a protection group in Veeam Backup & Replication.
        group_name (Union[None, Unset, str]): Name of a protection group.
    """

    group_uid: Union[Unset, UUID] = UNSET
    group_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_uid: Union[Unset, str] = UNSET
        if not isinstance(self.group_uid, Unset):
            group_uid = str(self.group_uid)

        group_name: Union[None, Unset, str]
        if isinstance(self.group_name, Unset):
            group_name = UNSET
        else:
            group_name = self.group_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_uid is not UNSET:
            field_dict["groupUid"] = group_uid
        if group_name is not UNSET:
            field_dict["groupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _group_uid = d.pop("groupUid", UNSET)
        group_uid: Union[Unset, UUID]
        if isinstance(_group_uid, Unset):
            group_uid = UNSET
        else:
            group_uid = UUID(_group_uid)

        def _parse_group_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_name = _parse_group_name(d.pop("groupName", UNSET))

        protection_group = cls(
            group_uid=group_uid,
            group_name=group_name,
        )

        return protection_group
