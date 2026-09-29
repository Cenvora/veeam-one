from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.triggered_alarm_info_2 import TriggeredAlarmInfo2


T = TypeVar("T", bound="TriggeredAlarmInfo2Page")


@_attrs_define
class TriggeredAlarmInfo2Page:
    """
    Attributes:
        items (list[TriggeredAlarmInfo2] | None | Unset):
        total_count (int | Unset):
    """

    items: list[TriggeredAlarmInfo2] | None | Unset = UNSET
    total_count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        items: list[dict[str, Any]] | None | Unset
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
        from ..models.triggered_alarm_info_2 import TriggeredAlarmInfo2  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_items(data: object) -> list[TriggeredAlarmInfo2] | None | Unset:
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
                    items_type_0_item = TriggeredAlarmInfo2.from_dict(items_type_0_item_data)

                    items_type_0.append(items_type_0_item)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TriggeredAlarmInfo2] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        total_count = d.pop("totalCount", UNSET)

        triggered_alarm_info_2_page = cls(
            items=items,
            total_count=total_count,
        )

        return triggered_alarm_info_2_page
