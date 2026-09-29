from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.business_view_category_type import BusinessViewCategoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessViewCategoryInfo")


@_attrs_define
class BusinessViewCategoryInfo:
    """
    Attributes:
        category_id (Union[Unset, int]): ID assigned to a Business View category.
        name (Union[None, Unset, str]): Name of a Business View category.
        type_ (Union[Unset, BusinessViewCategoryType]):
        group_ids (Union[None, Unset, list[int]]): Array of IDs assigned to Business View groups included in the
            category.
    """

    category_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, BusinessViewCategoryType] = UNSET
    group_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        category_id = self.category_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        group_ids: Union[None, Unset, list[int]]
        if isinstance(self.group_ids, Unset):
            group_ids = UNSET
        elif isinstance(self.group_ids, list):
            group_ids = self.group_ids

        else:
            group_ids = self.group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category_id = d.pop("categoryId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BusinessViewCategoryType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BusinessViewCategoryType(_type_)

        def _parse_group_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                group_ids_type_0 = cast(list[int], data)

                return group_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        group_ids = _parse_group_ids(d.pop("groupIds", UNSET))

        business_view_category_info = cls(
            category_id=category_id,
            name=name,
            type_=type_,
            group_ids=group_ids,
        )

        return business_view_category_info
