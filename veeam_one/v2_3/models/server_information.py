from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerInformation")


@_attrs_define
class ServerInformation:
    """
    Attributes:
        name (None | str | Unset): Name of the service. Example: Veeam ONE Reporting Service.
        version (None | str | Unset): Veeam ONE version. Example: 11.0.0.1325.
        machine (None | str | Unset): Name of a machine that runs Veeam ONE Reporting Service. Example: one-srv.
        log_path (None | str | Unset): Path to a folder where log files are stored. Example:
            C:\\ProgramData\\Veeam\\Veeam ONE\\Logs\\Reporter.
    """

    name: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    machine: None | str | Unset = UNSET
    log_path: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        machine: None | str | Unset
        if isinstance(self.machine, Unset):
            machine = UNSET
        else:
            machine = self.machine

        log_path: None | str | Unset
        if isinstance(self.log_path, Unset):
            log_path = UNSET
        else:
            log_path = self.log_path

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if machine is not UNSET:
            field_dict["machine"] = machine
        if log_path is not UNSET:
            field_dict["logPath"] = log_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_machine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        machine = _parse_machine(d.pop("machine", UNSET))

        def _parse_log_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        log_path = _parse_log_path(d.pop("logPath", UNSET))

        server_information = cls(
            name=name,
            version=version,
            machine=machine,
            log_path=log_path,
        )

        return server_information
