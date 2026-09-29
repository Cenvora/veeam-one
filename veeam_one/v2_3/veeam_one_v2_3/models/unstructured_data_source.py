from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnstructuredDataSource")


@_attrs_define
class UnstructuredDataSource:
    """
    Attributes:
        path (Union[None, Unset, str]): Path to a file or folder.
        inclusion_masks (Union[None, Unset, list[str]]): Names and name masks of files that must be included into a
            backup scope.
        exclusion_masks (Union[None, Unset, list[str]]): Names and name masks of files that must be excluded from a
            backup scope.
    """

    path: Union[None, Unset, str] = UNSET
    inclusion_masks: Union[None, Unset, list[str]] = UNSET
    exclusion_masks: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        inclusion_masks: Union[None, Unset, list[str]]
        if isinstance(self.inclusion_masks, Unset):
            inclusion_masks = UNSET
        elif isinstance(self.inclusion_masks, list):
            inclusion_masks = self.inclusion_masks

        else:
            inclusion_masks = self.inclusion_masks

        exclusion_masks: Union[None, Unset, list[str]]
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

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_inclusion_masks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inclusion_masks_type_0 = cast(list[str], data)

                return inclusion_masks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        inclusion_masks = _parse_inclusion_masks(d.pop("inclusionMasks", UNSET))

        def _parse_exclusion_masks(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclusion_masks_type_0 = cast(list[str], data)

                return exclusion_masks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        exclusion_masks = _parse_exclusion_masks(d.pop("exclusionMasks", UNSET))

        unstructured_data_source = cls(
            path=path,
            inclusion_masks=inclusion_masks,
            exclusion_masks=exclusion_masks,
        )

        return unstructured_data_source
