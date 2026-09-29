import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_advanced_info import CertificateAdvancedInfo
    from ..models.certificate_issuer_info import CertificateIssuerInfo


T = TypeVar("T", bound="CertificateFullInfo")


@_attrs_define
class CertificateFullInfo:
    """
    Attributes:
        common_name (Union[None, Unset, str]): Common name of the certificate.
        issued_by (Union[None, Unset, str]): Certificate authority that issued the certificate.
        subject_alt_name (Union[None, Unset, list[str]]): Identities bound to the subject of the certificate.
        friendly_name (Union[None, Unset, str]): Friendly name.
        valid_from (Union[Unset, datetime.datetime]): Start date and time of the certificate validity period.
        expiration_date (Union[Unset, datetime.datetime]): End date and time of the certificate validity period.
        signature_algorithm (Union[None, Unset, str]): Identifier of the cryptographic algorithm utilized by a
            certificate authority to sign the certificate.
        thumbprint (Union[None, Unset, str]): Certificate thumbprint.
        organization (Union[None, Unset, str]): Organization name.
        organizational_unit (Union[None, Unset, str]): Organizational unit name.
        locality (Union[None, Unset, str]): City, town or municipality where the organization is located.
        state_or_province (Union[None, Unset, str]): Major administrative region where the organization is located.
        country (Union[None, Unset, str]): ISO of a country where the organization is located.
        issuer_info (Union['CertificateIssuerInfo', None, Unset]): Certificate issuer details.
        advanced_info (Union['CertificateAdvancedInfo', None, Unset]): Additional certificate information.
    """

    common_name: Union[None, Unset, str] = UNSET
    issued_by: Union[None, Unset, str] = UNSET
    subject_alt_name: Union[None, Unset, list[str]] = UNSET
    friendly_name: Union[None, Unset, str] = UNSET
    valid_from: Union[Unset, datetime.datetime] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    signature_algorithm: Union[None, Unset, str] = UNSET
    thumbprint: Union[None, Unset, str] = UNSET
    organization: Union[None, Unset, str] = UNSET
    organizational_unit: Union[None, Unset, str] = UNSET
    locality: Union[None, Unset, str] = UNSET
    state_or_province: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    issuer_info: Union["CertificateIssuerInfo", None, Unset] = UNSET
    advanced_info: Union["CertificateAdvancedInfo", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_advanced_info import CertificateAdvancedInfo
        from ..models.certificate_issuer_info import CertificateIssuerInfo

        common_name: Union[None, Unset, str]
        if isinstance(self.common_name, Unset):
            common_name = UNSET
        else:
            common_name = self.common_name

        issued_by: Union[None, Unset, str]
        if isinstance(self.issued_by, Unset):
            issued_by = UNSET
        else:
            issued_by = self.issued_by

        subject_alt_name: Union[None, Unset, list[str]]
        if isinstance(self.subject_alt_name, Unset):
            subject_alt_name = UNSET
        elif isinstance(self.subject_alt_name, list):
            subject_alt_name = self.subject_alt_name

        else:
            subject_alt_name = self.subject_alt_name

        friendly_name: Union[None, Unset, str]
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        valid_from: Union[Unset, str] = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        signature_algorithm: Union[None, Unset, str]
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = self.signature_algorithm

        thumbprint: Union[None, Unset, str]
        if isinstance(self.thumbprint, Unset):
            thumbprint = UNSET
        else:
            thumbprint = self.thumbprint

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

        issuer_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.issuer_info, Unset):
            issuer_info = UNSET
        elif isinstance(self.issuer_info, CertificateIssuerInfo):
            issuer_info = self.issuer_info.to_dict()
        else:
            issuer_info = self.issuer_info

        advanced_info: Union[None, Unset, dict[str, Any]]
        if isinstance(self.advanced_info, Unset):
            advanced_info = UNSET
        elif isinstance(self.advanced_info, CertificateAdvancedInfo):
            advanced_info = self.advanced_info.to_dict()
        else:
            advanced_info = self.advanced_info

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if issued_by is not UNSET:
            field_dict["issuedBy"] = issued_by
        if subject_alt_name is not UNSET:
            field_dict["subjectAltName"] = subject_alt_name
        if friendly_name is not UNSET:
            field_dict["friendlyName"] = friendly_name
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if signature_algorithm is not UNSET:
            field_dict["signatureAlgorithm"] = signature_algorithm
        if thumbprint is not UNSET:
            field_dict["thumbprint"] = thumbprint
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
        if issuer_info is not UNSET:
            field_dict["issuerInfo"] = issuer_info
        if advanced_info is not UNSET:
            field_dict["advancedInfo"] = advanced_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.certificate_advanced_info import CertificateAdvancedInfo
        from ..models.certificate_issuer_info import CertificateIssuerInfo

        d = dict(src_dict)

        def _parse_common_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        common_name = _parse_common_name(d.pop("commonName", UNSET))

        def _parse_issued_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        issued_by = _parse_issued_by(d.pop("issuedBy", UNSET))

        def _parse_subject_alt_name(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subject_alt_name_type_0 = cast(list[str], data)

                return subject_alt_name_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        subject_alt_name = _parse_subject_alt_name(d.pop("subjectAltName", UNSET))

        def _parse_friendly_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        friendly_name = _parse_friendly_name(d.pop("friendlyName", UNSET))

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: Union[Unset, datetime.datetime]
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = isoparse(_valid_from)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        def _parse_signature_algorithm(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        signature_algorithm = _parse_signature_algorithm(d.pop("signatureAlgorithm", UNSET))

        def _parse_thumbprint(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbprint = _parse_thumbprint(d.pop("thumbprint", UNSET))

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

        def _parse_issuer_info(data: object) -> Union["CertificateIssuerInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                issuer_info_type_1 = CertificateIssuerInfo.from_dict(data)

                return issuer_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CertificateIssuerInfo", None, Unset], data)

        issuer_info = _parse_issuer_info(d.pop("issuerInfo", UNSET))

        def _parse_advanced_info(data: object) -> Union["CertificateAdvancedInfo", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                advanced_info_type_1 = CertificateAdvancedInfo.from_dict(data)

                return advanced_info_type_1
            except:  # noqa: E722
                pass
            return cast(Union["CertificateAdvancedInfo", None, Unset], data)

        advanced_info = _parse_advanced_info(d.pop("advancedInfo", UNSET))

        certificate_full_info = cls(
            common_name=common_name,
            issued_by=issued_by,
            subject_alt_name=subject_alt_name,
            friendly_name=friendly_name,
            valid_from=valid_from,
            expiration_date=expiration_date,
            signature_algorithm=signature_algorithm,
            thumbprint=thumbprint,
            organization=organization,
            organizational_unit=organizational_unit,
            locality=locality,
            state_or_province=state_or_province,
            country=country,
            issuer_info=issuer_info,
            advanced_info=advanced_info,
        )

        return certificate_full_info
