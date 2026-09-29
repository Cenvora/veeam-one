from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.datastore_connection_state import DatastoreConnectionState
from ..models.v_sphere_datastore_type import VSphereDatastoreType
from ..models.v_sphere_object_type import VSphereObjectType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereDatastoreInfo")


@_attrs_define
class VSphereDatastoreInfo:
    """
    Attributes:
        datastore_id (int | Unset): ID assigned to a datastore.
        mo_ref (None | str | Unset): MoRef ID assigned to a datastore in VMware vSphere.
        parent_id (int | None | Unset): ID assigned to a parent object.
        parent_type (None | Unset | VSphereObjectType): Type of a parent object.
        name (None | str | Unset): Name of a datastore.
        type_ (VSphereDatastoreType | Unset):
        connection_state (DatastoreConnectionState | Unset):
        path (None | str | Unset): Location of a datastore.
        capacity_bytes (int | None | Unset): Storage capacity of a datastore, in bytes.
        free_space_bytes (int | None | Unset): Amount of available free space on a datastore, in bytes.
        vm_count (int | None | Unset): Number of VMs that reside on a datastore.
        host_count (int | None | Unset): Number of hosts that are connected to a datastore.
        business_view_group_ids (list[int] | None | Unset): Array of Business View groups.
    """

    datastore_id: int | Unset = UNSET
    mo_ref: None | str | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    parent_type: None | Unset | VSphereObjectType = UNSET
    name: None | str | Unset = UNSET
    type_: VSphereDatastoreType | Unset = UNSET
    connection_state: DatastoreConnectionState | Unset = UNSET
    path: None | str | Unset = UNSET
    capacity_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    vm_count: int | None | Unset = UNSET
    host_count: int | None | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        datastore_id = self.datastore_id

        mo_ref: None | str | Unset
        if isinstance(self.mo_ref, Unset):
            mo_ref = UNSET
        else:
            mo_ref = self.mo_ref

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        parent_type: None | str | Unset
        if isinstance(self.parent_type, Unset):
            parent_type = UNSET
        elif isinstance(self.parent_type, VSphereObjectType):
            parent_type = self.parent_type.value
        else:
            parent_type = self.parent_type

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        connection_state: str | Unset = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        capacity_bytes: int | None | Unset
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        vm_count: int | None | Unset
        if isinstance(self.vm_count, Unset):
            vm_count = UNSET
        else:
            vm_count = self.vm_count

        host_count: int | None | Unset
        if isinstance(self.host_count, Unset):
            host_count = UNSET
        else:
            host_count = self.host_count

        business_view_group_ids: list[int] | None | Unset
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if datastore_id is not UNSET:
            field_dict["datastoreId"] = datastore_id
        if mo_ref is not UNSET:
            field_dict["moRef"] = mo_ref
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if parent_type is not UNSET:
            field_dict["parentType"] = parent_type
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state
        if path is not UNSET:
            field_dict["path"] = path
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if vm_count is not UNSET:
            field_dict["vmCount"] = vm_count
        if host_count is not UNSET:
            field_dict["hostCount"] = host_count
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        datastore_id = d.pop("datastoreId", UNSET)

        def _parse_mo_ref(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mo_ref = _parse_mo_ref(d.pop("moRef", UNSET))

        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: VSphereDatastoreType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VSphereDatastoreType(_type_)

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: DatastoreConnectionState | Unset
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = DatastoreConnectionState(_connection_state)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_capacity_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_vm_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vm_count = _parse_vm_count(d.pop("vmCount", UNSET))

        def _parse_host_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        host_count = _parse_host_count(d.pop("hostCount", UNSET))

        def _parse_business_view_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        v_sphere_datastore_info = cls(
            datastore_id=datastore_id,
            mo_ref=mo_ref,
            parent_id=parent_id,
            parent_type=parent_type,
            name=name,
            type_=type_,
            connection_state=connection_state,
            path=path,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            vm_count=vm_count,
            host_count=host_count,
            business_view_group_ids=business_view_group_ids,
        )

        return v_sphere_datastore_info
