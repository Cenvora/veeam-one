from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.v_sphere_host_sensor_state import VSphereHostSensorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereHostSensorInfo")


@_attrs_define
class VSphereHostSensorInfo:
    """
    Attributes:
        host_id (Union[Unset, int]): ID assigned to a host.
        name (Union[None, Unset, str]): Name of a hardware sensor.
        type_ (Union[None, Unset, str]): Type of a hardware sensor.
        state (Union[Unset, VSphereHostSensorState]):
        reading (Union[None, Unset, str]): Current reading of a sensor.
        details (Union[None, Unset, str]): Additional information on a hardware sensor.
    """

    host_id: Union[Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[None, Unset, str] = UNSET
    state: Union[Unset, VSphereHostSensorState] = UNSET
    reading: Union[None, Unset, str] = UNSET
    details: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_id = self.host_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[None, Unset, str]
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        reading: Union[None, Unset, str]
        if isinstance(self.reading, Unset):
            reading = UNSET
        else:
            reading = self.reading

        details: Union[None, Unset, str]
        if isinstance(self.details, Unset):
            details = UNSET
        else:
            details = self.details

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if state is not UNSET:
            field_dict["state"] = state
        if reading is not UNSET:
            field_dict["reading"] = reading
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        host_id = d.pop("hostId", UNSET)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        type_ = _parse_type_(d.pop("type", UNSET))

        _state = d.pop("state", UNSET)
        state: Union[Unset, VSphereHostSensorState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = VSphereHostSensorState(_state)

        def _parse_reading(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reading = _parse_reading(d.pop("reading", UNSET))

        def _parse_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        details = _parse_details(d.pop("details", UNSET))

        v_sphere_host_sensor_info = cls(
            host_id=host_id,
            name=name,
            type_=type_,
            state=state,
            reading=reading,
            details=details,
        )

        return v_sphere_host_sensor_info
