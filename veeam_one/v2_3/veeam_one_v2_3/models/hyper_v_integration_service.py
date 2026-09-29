from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HyperVIntegrationService")


@_attrs_define
class HyperVIntegrationService:
    """
    Attributes:
        wmi_class_name (Union[None, Unset, str]): Name of a WMI Hyper-V class.
        name (Union[None, Unset, str]): Name of an integration service.
        is_launched (Union[Unset, bool]): Indicates whether an integration service is launched.
    """

    wmi_class_name: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    is_launched: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        wmi_class_name: Union[None, Unset, str]
        if isinstance(self.wmi_class_name, Unset):
            wmi_class_name = UNSET
        else:
            wmi_class_name = self.wmi_class_name

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_launched = self.is_launched

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if wmi_class_name is not UNSET:
            field_dict["wmiClassName"] = wmi_class_name
        if name is not UNSET:
            field_dict["name"] = name
        if is_launched is not UNSET:
            field_dict["isLaunched"] = is_launched

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_wmi_class_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        wmi_class_name = _parse_wmi_class_name(d.pop("wmiClassName", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        is_launched = d.pop("isLaunched", UNSET)

        hyper_v_integration_service = cls(
            wmi_class_name=wmi_class_name,
            name=name,
            is_launched=is_launched,
        )

        return hyper_v_integration_service
