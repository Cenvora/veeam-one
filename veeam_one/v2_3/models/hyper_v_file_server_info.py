from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.hyper_v_object_type import HyperVObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVFileServerInfo")


@_attrs_define
class HyperVFileServerInfo:
    """
    Attributes:
        file_server_id (Union[Unset, int]): ID assigned to a file server.
        name (Union[None, Unset, str]): Name of a file server.
        parent_id (Union[Unset, int]): ID assigned to a parent object.
        parent_type (Union[Unset, HyperVObjectType]):
    """

    file_server_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    parent_id: Union[Unset, int] = UNSET
    parent_type: Union[Unset, HyperVObjectType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        file_server_id = self.file_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        parent_id = self.parent_id

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if file_server_id is not UNSET:
            field_dict["fileServerId"] = file_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_server_id = d.pop("fileServerId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        parent_id = d.pop("parentId", UNSET)

        _parent_type = d.pop("parentType", UNSET)
        parent_type: Union[Unset, HyperVObjectType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = HyperVObjectType(_parent_type)

        hyper_v_file_server_info = cls(
            file_server_id=file_server_id,
            name=name,
            parent_id=parent_id,
            parent_type=parent_type,
        )

        return hyper_v_file_server_info
