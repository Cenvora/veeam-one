from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.guest_assign_type import GuestAssignType
from ..models.host_assign_type import HostAssignType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guest_settings_info import GuestSettingsInfo


T = TypeVar("T", bound="GuestAssignInfo")


@_attrs_define
class GuestAssignInfo:
    """
    Attributes:
        object_id (int | Unset): ID assigned to a host.
        object_name (None | str | Unset): Name of a host.
        object_type (HostAssignType | Unset):
        guest_assign (GuestAssignType | Unset):
        settings_info (GuestSettingsInfo | None | Unset): Guest OS settings.
    """

    object_id: int | Unset = UNSET
    object_name: None | str | Unset = UNSET
    object_type: HostAssignType | Unset = UNSET
    guest_assign: GuestAssignType | Unset = UNSET
    settings_info: GuestSettingsInfo | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.guest_settings_info import GuestSettingsInfo  # noqa: PLC0415

        object_id = self.object_id

        object_name: None | str | Unset
        if isinstance(self.object_name, Unset):
            object_name = UNSET
        else:
            object_name = self.object_name

        object_type: str | Unset = UNSET
        if not isinstance(self.object_type, Unset):
            object_type = self.object_type.value

        guest_assign: str | Unset = UNSET
        if not isinstance(self.guest_assign, Unset):
            guest_assign = self.guest_assign.value

        settings_info: dict[str, Any] | None | Unset
        if isinstance(self.settings_info, Unset):
            settings_info = UNSET
        elif isinstance(self.settings_info, GuestSettingsInfo):
            settings_info = self.settings_info.to_dict()
        else:
            settings_info = self.settings_info

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if object_name is not UNSET:
            field_dict["objectName"] = object_name
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if guest_assign is not UNSET:
            field_dict["guestAssign"] = guest_assign
        if settings_info is not UNSET:
            field_dict["settingsInfo"] = settings_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guest_settings_info import GuestSettingsInfo  # noqa: PLC0415

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
        object_type: HostAssignType | Unset
        if isinstance(_object_type, Unset):
            object_type = UNSET
        else:
            object_type = HostAssignType(_object_type)

        _guest_assign = d.pop("guestAssign", UNSET)
        guest_assign: GuestAssignType | Unset
        if isinstance(_guest_assign, Unset):
            guest_assign = UNSET
        else:
            guest_assign = GuestAssignType(_guest_assign)

        def _parse_settings_info(data: object) -> GuestSettingsInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_info_type_1 = GuestSettingsInfo.from_dict(data)

                return settings_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GuestSettingsInfo | None | Unset, data)

        settings_info = _parse_settings_info(d.pop("settingsInfo", UNSET))

        guest_assign_info = cls(
            object_id=object_id,
            object_name=object_name,
            object_type=object_type,
            guest_assign=guest_assign,
            settings_info=settings_info,
        )

        return guest_assign_info
