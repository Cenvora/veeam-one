from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.alarm_source_object_type import AlarmSourceObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlarmSource")


@_attrs_define
class AlarmSource:
    """
    Attributes:
        object_id (int | Unset): ID assigned to an object.
        object_name (None | str | Unset): Name of an object.
        object_type (AlarmSourceObjectType | Unset):
    """

    object_id: int | Unset = UNSET
    object_name: None | str | Unset = UNSET
    object_type: AlarmSourceObjectType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        object_name: None | str | Unset
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_id = d.pop("objectId", UNSET)

        def _parse_object_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_name = _parse_object_name(d.pop("objectName", UNSET))

        _object_type = d.pop("objectType", UNSET)
        object_type: AlarmSourceObjectType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = AlarmSourceObjectType(_object_type)

        alarm_source = cls(
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
        )

        return alarm_source
