from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.v_sphere_host_sensor_state import VSphereHostSensorState
from ..types import UNSET, Unset

T = TypeVar("T", bound="VSphereHostSensorInfo")


@_attrs_define
class VSphereHostSensorInfo:
    """
    Attributes:
        host_id (int | Unset): ID assigned to a host.
        name (None | str | Unset): Name of a hardware sensor.
        type_ (None | str | Unset): Type of a hardware sensor.
        state (VSphereHostSensorState | Unset):
        reading (None | str | Unset): Current reading of a sensor.
        details (None | str | Unset): Additional information on a hardware sensor.
    """

    host_id: int | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    state: VSphereHostSensorState | Unset = UNSET
    reading: None | str | Unset = UNSET
    details: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        host_id = self.host_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        reading: None | str | Unset
        if isinstance(self.reading, Unset):
            reading = UNSET
        else:
            reading = self.reading

        details: None | str | Unset
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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        _state = d.pop("state", UNSET)
        state: VSphereHostSensorState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = VSphereHostSensorState(_state)

        def _parse_reading(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reading = _parse_reading(d.pop("reading", UNSET))

        def _parse_details(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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
