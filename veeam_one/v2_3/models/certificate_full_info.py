from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_advanced_info import CertificateAdvancedInfo
    from ..models.certificate_issuer_info import CertificateIssuerInfo


T = TypeVar("T", bound="CertificateFullInfo")


@_attrs_define
class CertificateFullInfo:
    """
    Attributes:
        common_name (None | str | Unset): Common name of the certificate.
        issued_by (None | str | Unset): Certificate authority that issued the certificate.
        subject_alt_name (list[str] | None | Unset): Identities bound to the subject of the certificate.
        friendly_name (None | str | Unset): Friendly name.
        valid_from (datetime.datetime | Unset): Start date and time of the certificate validity period.
        expiration_date (datetime.datetime | Unset): End date and time of the certificate validity period.
        signature_algorithm (None | str | Unset): Identifier of the cryptographic algorithm utilized by a certificate
            authority to sign the certificate.
        thumbprint (None | str | Unset): Certificate thumbprint.
        organization (None | str | Unset): Organization name.
        organizational_unit (None | str | Unset): Organizational unit name.
        locality (None | str | Unset): City, town or municipality where the organization is located.
        state_or_province (None | str | Unset): Major administrative region where the organization is located.
        country (None | str | Unset): ISO of a country where the organization is located.
        issuer_info (CertificateIssuerInfo | None | Unset): Certificate issuer details.
        advanced_info (CertificateAdvancedInfo | None | Unset): Additional certificate information.
    """

    common_name: None | str | Unset = UNSET
    issued_by: None | str | Unset = UNSET
    subject_alt_name: list[str] | None | Unset = UNSET
    friendly_name: None | str | Unset = UNSET
    valid_from: datetime.datetime | Unset = UNSET
    expiration_date: datetime.datetime | Unset = UNSET
    signature_algorithm: None | str | Unset = UNSET
    thumbprint: None | str | Unset = UNSET
    organization: None | str | Unset = UNSET
    organizational_unit: None | str | Unset = UNSET
    locality: None | str | Unset = UNSET
    state_or_province: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    issuer_info: CertificateIssuerInfo | None | Unset = UNSET
    advanced_info: CertificateAdvancedInfo | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.certificate_advanced_info import CertificateAdvancedInfo  # noqa: PLC0415
        from ..models.certificate_issuer_info import CertificateIssuerInfo  # noqa: PLC0415

        common_name: None | str | Unset
        if isinstance(self.common_name, Unset):
            common_name = UNSET
        else:
            common_name = self.common_name

        issued_by: None | str | Unset
        if isinstance(self.issued_by, Unset):
            issued_by = UNSET
        else:
            issued_by = self.issued_by

        subject_alt_name: list[str] | None | Unset
        if isinstance(self.subject_alt_name, Unset):
            subject_alt_name = UNSET
        elif isinstance(self.subject_alt_name, list):
            subject_alt_name = self.subject_alt_name

        else:
            subject_alt_name = self.subject_alt_name

        friendly_name: None | str | Unset
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        valid_from: str | Unset = UNSET
        if not isinstance(self.valid_from, Unset):
            valid_from = self.valid_from.isoformat()

        expiration_date: str | Unset = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        signature_algorithm: None | str | Unset
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = self.signature_algorithm

        thumbprint: None | str | Unset
        if isinstance(self.thumbprint, Unset):
            thumbprint = UNSET
        else:
            thumbprint = self.thumbprint

        organization: None | str | Unset
        if isinstance(self.organization, Unset):
            organization = UNSET
        else:
            organization = self.organization

        organizational_unit: None | str | Unset
        if isinstance(self.organizational_unit, Unset):
            organizational_unit = UNSET
        else:
            organizational_unit = self.organizational_unit

        locality: None | str | Unset
        if isinstance(self.locality, Unset):
            locality = UNSET
        else:
            locality = self.locality

        state_or_province: None | str | Unset
        if isinstance(self.state_or_province, Unset):
            state_or_province = UNSET
        else:
            state_or_province = self.state_or_province

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        issuer_info: dict[str, Any] | None | Unset
        if isinstance(self.issuer_info, Unset):
            issuer_info = UNSET
        elif isinstance(self.issuer_info, CertificateIssuerInfo):
            issuer_info = self.issuer_info.to_dict()
        else:
            issuer_info = self.issuer_info

        advanced_info: dict[str, Any] | None | Unset
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
        from ..models.certificate_advanced_info import CertificateAdvancedInfo  # noqa: PLC0415
        from ..models.certificate_issuer_info import CertificateIssuerInfo  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_common_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        common_name = _parse_common_name(d.pop("commonName", UNSET))

        def _parse_issued_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issued_by = _parse_issued_by(d.pop("issuedBy", UNSET))

        def _parse_subject_alt_name(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                subject_alt_name_type_0 = cast(list[str], data)

                return subject_alt_name_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        subject_alt_name = _parse_subject_alt_name(d.pop("subjectAltName", UNSET))

        def _parse_friendly_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        friendly_name = _parse_friendly_name(d.pop("friendlyName", UNSET))

        _valid_from = d.pop("validFrom", UNSET)
        valid_from: datetime.datetime | Unset
        if isinstance(_valid_from, Unset):
            valid_from = UNSET
        else:
            valid_from = datetime.datetime.fromisoformat(_valid_from)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: datetime.datetime | Unset
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = datetime.datetime.fromisoformat(_expiration_date)

        def _parse_signature_algorithm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        signature_algorithm = _parse_signature_algorithm(d.pop("signatureAlgorithm", UNSET))

        def _parse_thumbprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbprint = _parse_thumbprint(d.pop("thumbprint", UNSET))

        def _parse_organization(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organization = _parse_organization(d.pop("organization", UNSET))

        def _parse_organizational_unit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        organizational_unit = _parse_organizational_unit(d.pop("organizationalUnit", UNSET))

        def _parse_locality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        locality = _parse_locality(d.pop("locality", UNSET))

        def _parse_state_or_province(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state_or_province = _parse_state_or_province(d.pop("stateOrProvince", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_issuer_info(data: object) -> CertificateIssuerInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                issuer_info_type_1 = CertificateIssuerInfo.from_dict(data)

                return issuer_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CertificateIssuerInfo | None | Unset, data)

        issuer_info = _parse_issuer_info(d.pop("issuerInfo", UNSET))

        def _parse_advanced_info(data: object) -> CertificateAdvancedInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                advanced_info_type_1 = CertificateAdvancedInfo.from_dict(data)

                return advanced_info_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CertificateAdvancedInfo | None | Unset, data)

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
