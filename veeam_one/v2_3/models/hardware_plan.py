from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwarePlan")


@_attrs_define
class HardwarePlan:
    """
    Attributes:
        hardware_plan_uid (UUID | Unset): UID assigned to a hardware plan.
        name (None | str | Unset): Name of a hardware plan.
    """

    hardware_plan_uid: UUID | Unset = UNSET
    name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        hardware_plan_uid: str | Unset = UNSET
        if not isinstance(self.hardware_plan_uid, Unset):
            hardware_plan_uid = str(self.hardware_plan_uid)

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if hardware_plan_uid is not UNSET:
            field_dict["hardwarePlanUid"] = hardware_plan_uid
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _hardware_plan_uid = d.pop("hardwarePlanUid", UNSET)
        hardware_plan_uid: UUID | Unset
        if isinstance(_hardware_plan_uid, Unset):
            hardware_plan_uid = UNSET
        else:
            hardware_plan_uid = UUID(_hardware_plan_uid)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        hardware_plan = cls(
            hardware_plan_uid=hardware_plan_uid,
            name=name,
        )

        return hardware_plan
