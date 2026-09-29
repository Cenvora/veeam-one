from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateIssuerInfo")


@_attrs_define
class CertificateIssuerInfo:
    """
    Attributes:
        issuer_name (Union[None, Unset, str]): Issuer name.
        organization (Union[None, Unset, str]): Name of an issuer organization.
        organizational_unit (Union[None, Unset, str]): Name of an issuer organizational unit.
        locality (Union[None, Unset, str]): City, town or municipality where the issuer organization is located.
        state_or_province (Union[None, Unset, str]): Major administrative region where the issuer organization is
            located.
        country (Union[None, Unset, str]): ISO of a country where the issuer organization is located.
        serial_number (Union[None, Unset, str]): Serial number.
        version (Union[Unset, int]): Version number.
    """

    issuer_name: Union[None, Unset, str] = UNSET
    organization: Union[None, Unset, str] = UNSET
    organizational_unit: Union[None, Unset, str] = UNSET
    locality: Union[None, Unset, str] = UNSET
    state_or_province: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    version: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        issuer_name: Union[None, Unset, str]
        if isinstance(self.issuer_name, Unset):
            issuer_name = UNSET
        else:
            issuer_name = self.issuer_name

        organization: Union[None, Unset, str]
        if isinstance(self.organization, Unset):
            organization = UNSET
        else:
            organization = self.organization

        organizational_unit: Union[None, Unset, str]
        if isinstance(self.organizational_unit, Unset):
            organizational_unit = UNSET
        else:
            organizational_unit = self.organizational_unit

        locality: Union[None, Unset, str]
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        state_or_province: Union[None, Unset, str]
        if isinstance(self.state_or_province, Unset):
            state_or_province = UNSET
        else:
            state_or_province = self.state_or_province

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if issuer_name is not UNSET:
            field_dict["issuerName"] = issuer_name
        if organization is not UNSET:
            field_dict["organization"] = organization
        if organizational_unit is not UNSET:
            field_dict["organizationalUnit"] = organizational_unit
        if locality is not UNSET:
            field_dict["locality"] = locality
        if state_or_province is not UNSET:
            field_dict["stateOrProvince"] = state_or_province
        if country is not UNSET:
            field_dict["country"] = country
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_issuer_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issuer_name = _parse_issuer_name(d.pop("issuerName", UNSET))

        def _parse_organization(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_organizational_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organizational_unit = _parse_organizational_unit(d.pop("organizationalUnit", UNSET))

        def _parse_locality(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_state_or_province(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state_or_province = _parse_state_or_province(d.pop("stateOrProvince", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serialNumber", UNSET))

        version = d.pop("version", UNSET)

        certificate_issuer_info = cls(
            issuer_name=issuer_name,
            organization=organization,
            organizational_unit=organizational_unit,
            locality=locality,
            state_or_province=state_or_province,
            country=country,
            serial_number=serial_number,
            version=version,
        )

        return certificate_issuer_info
