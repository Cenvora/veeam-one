from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateAdvancedInfo")


@_attrs_define
class CertificateAdvancedInfo:
    """
    Attributes:
        public_key_algorithm (Union[None, Unset, str]): Public key algorithm.
        key_usage (Union[None, Unset, str]): Main purpose of the key.
        key_size_bits (Union[None, Unset, str]): Key size, in bits.
        curve (Union[None, Unset, str]): Curve used by the elliptic curve public key algorithm.
        extended_key_usage_oids (Union[None, Unset, list[str]]): Array of object identifiers assigned to the key
            additional purposes.
        extended_key_usage_names (Union[None, Unset, list[str]]): Array of the names of the key additional purposes.
    """

    public_key_algorithm: Union[None, Unset, str] = UNSET
    key_usage: Union[None, Unset, str] = UNSET
    key_size_bits: Union[None, Unset, str] = UNSET
    curve: Union[None, Unset, str] = UNSET
    extended_key_usage_oids: Union[None, Unset, list[str]] = UNSET
    extended_key_usage_names: Union[None, Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        public_key_algorithm: Union[None, Unset, str]
        if isinstance(self.public_key_algorithm, Unset):
            public_key_algorithm = UNSET
        else:
            public_key_algorithm = self.public_key_algorithm

        key_usage: Union[None, Unset, str]
        if isinstance(self.key_usage, Unset):
            key_usage = UNSET
        else:
            key_usage = self.key_usage

        key_size_bits: Union[None, Unset, str]
        if isinstance(self.key_size_bits, Unset):
            key_size_bits = UNSET
        else:
            key_size_bits = self.key_size_bits

        curve: Union[None, Unset, str]
        if isinstance(self.curve, Unset):
            curve = UNSET
        else:
            curve = self.curve

        extended_key_usage_oids: Union[None, Unset, list[str]]
        if isinstance(self.extended_key_usage_oids, Unset):
            extended_key_usage_oids = UNSET
        elif isinstance(self.extended_key_usage_oids, list):
            extended_key_usage_oids = self.extended_key_usage_oids

        else:
            extended_key_usage_oids = self.extended_key_usage_oids

        extended_key_usage_names: Union[None, Unset, list[str]]
        if isinstance(self.extended_key_usage_names, Unset):
            extended_key_usage_names = UNSET
        elif isinstance(self.extended_key_usage_names, list):
            extended_key_usage_names = self.extended_key_usage_names

        else:
            extended_key_usage_names = self.extended_key_usage_names

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if public_key_algorithm is not UNSET:
            field_dict["publicKeyAlgorithm"] = public_key_algorithm
        if key_usage is not UNSET:
            field_dict["keyUsage"] = key_usage
        if key_size_bits is not UNSET:
            field_dict["keySizeBits"] = key_size_bits
        if curve is not UNSET:
            field_dict["curve"] = curve
        if extended_key_usage_oids is not UNSET:
            field_dict["extendedKeyUsageOids"] = extended_key_usage_oids
        if extended_key_usage_names is not UNSET:
            field_dict["extendedKeyUsageNames"] = extended_key_usage_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_public_key_algorithm(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        public_key_algorithm = _parse_public_key_algorithm(d.pop("publicKeyAlgorithm", UNSET))

        def _parse_key_usage(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key_usage = _parse_key_usage(d.pop("keyUsage", UNSET))

        def _parse_key_size_bits(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key_size_bits = _parse_key_size_bits(d.pop("keySizeBits", UNSET))

        def _parse_curve(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        curve = _parse_curve(d.pop("curve", UNSET))

        def _parse_extended_key_usage_oids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extended_key_usage_oids_type_0 = cast(list[str], data)

                return extended_key_usage_oids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        extended_key_usage_oids = _parse_extended_key_usage_oids(d.pop("extendedKeyUsageOids", UNSET))

        def _parse_extended_key_usage_names(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                extended_key_usage_names_type_0 = cast(list[str], data)

                return extended_key_usage_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        extended_key_usage_names = _parse_extended_key_usage_names(d.pop("extendedKeyUsageNames", UNSET))

        certificate_advanced_info = cls(
            public_key_algorithm=public_key_algorithm,
            key_usage=key_usage,
            key_size_bits=key_size_bits,
            curve=curve,
            extended_key_usage_oids=extended_key_usage_oids,
            extended_key_usage_names=extended_key_usage_names,
        )

        return certificate_advanced_info
