from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereObjectRelationsInfo")


@_attrs_define
class VSphereObjectRelationsInfo:
    """
    Attributes:
        object_id (int | Unset): ID assigned to an object.
        object_name (None | str | Unset): Name of an object.
        object_type (VSphereObjectType | Unset):
        parent_id (int | None | Unset): ID assigned to a parent object.
        parent_name (None | str | Unset): Name of a parent object.
        parent_type (None | Unset | VSphereObjectType): Type of a parent object.
    """

    object_id: int | Unset = UNSET
    object_name: None | str | Unset = UNSET
    object_type: VSphereObjectType | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_name: None | str | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET

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

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_name: None | str | Unset
        if isinstance(self.parent_name, Unset):
            parent_name = UNSET
        else:
            parent_name = self.parent_name

        parent_type: None | str | Unset
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_name is not UNSET:
            field_dict["parentName"] = parent_name
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type

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
        object_type: VSphereObjectType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = VSphereObjectType(_object_type)

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_name = _parse_parent_name(d.pop("parentName", UNSET))

        def _parse_parent_type(data: object) -> None | Unset | VSphereObjectType:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VSphereObjectType, data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        v_sphere_object_relations_info = cls(
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            parent_id=parent_id,
            parent_name=parent_name,
            parent_type=parent_type,
        )

        return v_sphere_object_relations_info
