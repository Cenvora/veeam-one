from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.remediation_mode import RemediationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="Remediation")


@_attrs_define
class Remediation:
    """
    Attributes:
        description (Union[None, Unset, str]): Description of a remediation action.
        mode (Union[Unset, RemediationMode]):
    """

    description: Union[None, Unset, str] = UNSET
    mode: Union[Unset, RemediationMode] = UNSET

    def to_dict(self) -> dict[str, Any]:
        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, RemediationMode]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = RemediationMode(_mode)

        remediation = cls(
            description=description,
            mode=mode,
        )

        return remediation
