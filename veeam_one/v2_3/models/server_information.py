from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerInformation")


@_attrs_define
class ServerInformation:
    r"""
    Attributes:
        name (Union[None, Unset, str]): Name of the service. Example: Veeam ONE Reporting Service.
        version (Union[None, Unset, str]): Veeam ONE version. Example: 11.0.0.1325.
        machine (Union[None, Unset, str]): Name of a machine that runs Veeam ONE Reporting Service. Example: one-srv.
        log_path (Union[None, Unset, str]): Path to a folder where log files are stored. Example:
            C:\ProgramData\Veeam\Veeam ONE\Logs\Reporter.
    """

    name: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    machine: Union[None, Unset, str] = UNSET
    log_path: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        machine: Union[None, Unset, str]
        if isinstance(self.machine, Unset):
            machine = UNSET
        else:
            machine = self.machine

        log_path: Union[None, Unset, str]
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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_machine(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        machine = _parse_machine(d.pop("machine", UNSET))

        def _parse_log_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        log_path = _parse_log_path(d.pop("logPath", UNSET))

        server_information = cls(
            name=name,
            version=version,
            machine=machine,
            log_path=log_path,
        )

        return server_information
