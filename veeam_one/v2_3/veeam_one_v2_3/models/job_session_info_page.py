from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_session_info import JobSessionInfo


T = TypeVar("T", bound="JobSessionInfoPage")


@_attrs_define
class JobSessionInfoPage:
    """
    Attributes:
        items (Union[None, Unset, list['JobSessionInfo']]):
        total_count (Union[Unset, int]):
    """

    items: Union[None, Unset, list["JobSessionInfo"]] = UNSET
    total_count: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = []
            for items_type_0_item_data in self.items:
                items_type_0_item = items_type_0_item_data.to_dict()
                items.append(items_type_0_item)

        else:
            items = self.items

        total_count = self.total_count

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_session_info import JobSessionInfo

        d = dict(src_dict)

        def _parse_items(data: object) -> Union[None, Unset, list["JobSessionInfo"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = []
                _items_type_0 = data
                for items_type_0_item_data in _items_type_0:
                    items_type_0_item = JobSessionInfo.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["JobSessionInfo"]], data)

        items = _parse_items(d.pop("items", UNSET))

        total_count = d.pop("totalCount", UNSET)

        job_session_info_page = cls(
            items=items,
            total_count=total_count,
        )

        return job_session_info_page
