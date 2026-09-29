from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.host_assign_info import HostAssignInfo


T = TypeVar("T", bound="HostAssignInfoCredentialAssignInfo")


@_attrs_define
class HostAssignInfoCredentialAssignInfo:
    """
    Attributes:
        credential_id (int | Unset): ID assigned to a credential set.
        user_name (None | str | Unset): User name.
        assigned_objects (list[HostAssignInfo] | None | Unset): Array of hosts that can be accessed using the credential
            set.
    """

    credential_id: int | Unset = UNSET
    user_name: None | str | Unset = UNSET
    assigned_objects: list[HostAssignInfo] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        assigned_objects: list[dict[str, Any]] | None | Unset
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
        from ..models.host_assign_info import HostAssignInfo  # noqa: PLC0415

        d = dict(src_dict)
        credential_id = d.pop("credentialId", UNSET)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_assigned_objects(data: object) -> list[HostAssignInfo] | None | Unset:
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
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[HostAssignInfo] | None | Unset, data)

        assigned_objects = _parse_assigned_objects(d.pop("assignedObjects", UNSET))

        host_assign_info_credential_assign_info = cls(
            credential_id=credential_id,
            user_name=user_name,
            assigned_objects=assigned_objects,
        )

        return host_assign_info_credential_assign_info
