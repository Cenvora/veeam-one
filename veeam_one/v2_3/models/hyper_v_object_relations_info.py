from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.hyper_v_object_type import HyperVObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVObjectRelationsInfo")


@_attrs_define
class HyperVObjectRelationsInfo:
    """
    Attributes:
        object_id (Union[Unset, int]): ID assigned to an object.
        object_name (Union[None, Unset, str]): Name of an object.
        object_type (Union[Unset, HyperVObjectType]):
        parent_id (Union[None, Unset, int]): ID assigned to a parent object.
        parent_name (Union[None, Unset, str]): Name of a parent object.
        parent_type (Union[HyperVObjectType, None, Unset]): Type of a parent object.
    """

    object_id: Union[Unset, int] = UNSET
    object_name: Union[None, Unset, str] = UNSET
    object_type: Union[Unset, HyperVObjectType] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    parent_name: Union[None, Unset, str] = UNSET
    parent_type: Union[HyperVObjectType, None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_id = self.object_id

        object_name: Union[None, Unset, str]
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        object_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_name: Union[None, Unset, str]
        if isinstance(self.parent_name, Unset):
            parent_name = UNSET
        else:
            parent_name = self.parent_name

        parent_type: Union[None, Unset, str]
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, HyperVObjectType):
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

        def _parse_object_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_name = _parse_object_name(d.pop("objectName", UNSET))

        _object_type = d.pop("objectType", UNSET)
        object_type: Union[Unset, HyperVObjectType]
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = HyperVObjectType(_object_type)

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_name = _parse_parent_name(d.pop("parentName", UNSET))

        def _parse_parent_type(data: object) -> Union[HyperVObjectType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = HyperVObjectType(data)

                return parent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[HyperVObjectType, None, Unset], data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        hyper_v_object_relations_info = cls(
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            parent_id=parent_id,
            parent_name=parent_name,
            parent_type=parent_type,
        )

        return hyper_v_object_relations_info
