from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.business_view_group_type import BusinessViewGroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessViewGroupInfo")


@_attrs_define
class BusinessViewGroupInfo:
    """
    Attributes:
        group_id (int | Unset): ID assigned to a Business View group.
        name (None | str | Unset): Name of a Business View group.
        type_ (BusinessViewGroupType | Unset):
        category_id (int | Unset): ID assigned to a Business View category that includes the group.
    """

    group_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: BusinessViewGroupType | Unset = UNSET
    category_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        category_id = self.category_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_id = d.pop("groupId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: BusinessViewGroupType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BusinessViewGroupType(_type_)

        category_id = d.pop("categoryId", UNSET)

        business_view_group_info = cls(
            group_id=group_id,
            name=name,
            type_=type_,
            category_id=category_id,
        )

        return business_view_group_info
