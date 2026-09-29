from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataSource")


@_attrs_define
class UnstructuredDataSource:
    """
    Attributes:
        path (None | str | Unset): Path to a file or folder.
        inclusion_masks (list[str] | None | Unset): Names and name masks of files that must be included into a backup
            scope.
        exclusion_masks (list[str] | None | Unset): Names and name masks of files that must be excluded from a backup
            scope.
    """

    path: None | str | Unset = UNSET
    inclusion_masks: list[str] | None | Unset = UNSET
    exclusion_masks: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        inclusion_masks: list[str] | None | Unset
        if isinstance(self.inclusion_masks, Unset):
            inclusion_masks = UNSET
        elif isinstance(self.inclusion_masks, list):
            inclusion_masks = self.inclusion_masks

        else:
            inclusion_masks = self.inclusion_masks

        exclusion_masks: list[str] | None | Unset
        if isinstance(self.exclusion_masks, Unset):
            exclusion_masks = UNSET
        elif isinstance(self.exclusion_masks, list):
            exclusion_masks = self.exclusion_masks

        else:
            exclusion_masks = self.exclusion_masks

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if inclusion_masks is not UNSET:
            field_dict["inclusionMasks"] = inclusion_masks
        if exclusion_masks is not UNSET:
            field_dict["exclusionMasks"] = exclusion_masks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_inclusion_masks(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inclusion_masks_type_0 = cast(list[str], data)

                return inclusion_masks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        inclusion_masks = _parse_inclusion_masks(d.pop("inclusionMasks", UNSET))

        def _parse_exclusion_masks(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_masks_type_0 = cast(list[str], data)

                return exclusion_masks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclusion_masks = _parse_exclusion_masks(d.pop("exclusionMasks", UNSET))

        unstructured_data_source = cls(
            path=path,
            inclusion_masks=inclusion_masks,
            exclusion_masks=exclusion_masks,
        )

        return unstructured_data_source
