from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereHostAndClusterFolderInfo")


@_attrs_define
class VSphereHostAndClusterFolderInfo:
    """
    Attributes:
        folder_id (Union[Unset, int]): ID assigned to a Host and Cluster folder.
        name (Union[None, Unset, str]): Name of a Host and Cluster folder.
        mo_ref (Union[None, Unset, str]): MoRef ID assigned to a Host and Cluster folder.
        parent_id (Union[None, Unset, int]): ID assigned to a parent object.
        parent_type (Union[None, Unset, VSphereObjectType]): Type of a parent object.
    """

    folder_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    mo_ref: Union[None, Unset, str] = UNSET
    parent_id: Union[None, Unset, int] = UNSET
    parent_type: Union[None, Unset, VSphereObjectType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        folder_id = self.folder_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        mo_ref: Union[None, Unset, str]
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        parent_id: Union[None, Unset, int]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: Union[None, Unset, str]
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if folder_id is not UNSET:
            field_dict["folderId"] = folder_id
        if name is not UNSET:
            field_dict["name"] = name
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        folder_id = d.pop("folderId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_mo_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_parent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

        def _parse_parent_type(data: object) -> Union[None, Unset, VSphereObjectType]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_type_type_1 = VSphereObjectType(data)

                return parent_type_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, VSphereObjectType], data)

        parent_type = _parse_parent_type(d.pop("parentType", UNSET))

        v_sphere_host_and_cluster_folder_info = cls(
            folder_id=folder_id,
            name=name,
            mo_ref=mo_ref,
            parent_id=parent_id,
            parent_type=parent_type,
        )

        return v_sphere_host_and_cluster_folder_info
