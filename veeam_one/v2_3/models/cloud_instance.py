from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CloudInstance")


@_attrs_define
class CloudInstance:
    """
    Attributes:
        instance_id (Union[None, Unset, str]): ID assigned to a cloud instance.
        instance_name (Union[None, Unset, str]): Name of a cloud instance.
    """

    instance_id: Union[None, Unset, str] = UNSET
    instance_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        instance_id: Union[None, Unset, str]
        if isinstance(self.instance_id, Unset):
            instance_id = UNSET
        else:
            instance_id = self.instance_id

        instance_name: Union[None, Unset, str]
        if isinstance(self.instance_name, Unset):
            instance_name = UNSET
        else:
            instance_name = self.instance_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_instance_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance_id = _parse_instance_id(d.pop("instanceId", UNSET))

        def _parse_instance_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instance_name = _parse_instance_name(d.pop("instanceName", UNSET))

        cloud_instance = cls(
            instance_id=instance_id,
            instance_name=instance_name,
        )

        return cloud_instance
