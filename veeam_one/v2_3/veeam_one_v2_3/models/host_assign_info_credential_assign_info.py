from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_assign_info import HostAssignInfo


T = TypeVar("T", bound="HostAssignInfoCredentialAssignInfo")


@_attrs_define
class HostAssignInfoCredentialAssignInfo:
    """
    Attributes:
        credential_id (Union[Unset, int]): ID assigned to a credential set.
        user_name (Union[None, Unset, str]): User name.
        assigned_objects (Union[None, Unset, list['HostAssignInfo']]): Array of hosts that can be accessed using the
            credential set.
    """

    credential_id: Union[Unset, int] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    assigned_objects: Union[None, Unset, list["HostAssignInfo"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        assigned_objects: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.assigned_objects, Unset):
            assigned_objects = UNSET
        elif isinstance(self.assigned_objects, list):
            assigned_objects = []
            for assigned_objects_type_0_item_data in self.assigned_objects:
                assigned_objects_type_0_item = assigned_objects_type_0_item_data.to_dict()
                assigned_objects.append(assigned_objects_type_0_item)

        else:
            assigned_objects = self.assigned_objects

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credential_id is not UNSET:
            field_dict["credentialId"] = credential_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if assigned_objects is not UNSET:
            field_dict["assignedObjects"] = assigned_objects

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.host_assign_info import HostAssignInfo

        d = dict(src_dict)
        credential_id = d.pop("credentialId", UNSET)

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_assigned_objects(data: object) -> Union[None, Unset, list["HostAssignInfo"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                assigned_objects_type_0 = []
                _assigned_objects_type_0 = data
                for assigned_objects_type_0_item_data in _assigned_objects_type_0:
                    assigned_objects_type_0_item = HostAssignInfo.from_dict(assigned_objects_type_0_item_data)

                    assigned_objects_type_0.append(assigned_objects_type_0_item)

                return assigned_objects_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["HostAssignInfo"]], data)

        assigned_objects = _parse_assigned_objects(d.pop("assignedObjects", UNSET))

        host_assign_info_credential_assign_info = cls(
            credential_id=credential_id,
            user_name=user_name,
            assigned_objects=assigned_objects,
        )

        return host_assign_info_credential_assign_info
