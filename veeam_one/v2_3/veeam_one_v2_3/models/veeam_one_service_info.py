from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneServiceInfo")


@_attrs_define
class VeeamOneServiceInfo:
    """
    Attributes:
        product (Union[None, Unset, str]): Name of an installed product. Example: Veeam ONE.
        version (Union[None, Unset, str]): Version of an installed product. Example: 11.0.0.1325.
        installation_uid (Union[Unset, UUID]): UID assigned to product installation. Example:
            8a6626ad-16ce-482b-ae27-30c0966c1bd2.
    """

    product: Union[None, Unset, str] = UNSET
    version: Union[None, Unset, str] = UNSET
    installation_uid: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        product: Union[None, Unset, str]
        if isinstance(self.product, Unset):
            product = UNSET
        else:
            product = self.product

        version: Union[None, Unset, str]
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        installation_uid: Union[Unset, str] = UNSET
        if not isinstance(self.installation_uid, Unset):
            installation_uid = str(self.installation_uid)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if product is not UNSET:
            field_dict["product"] = product
        if version is not UNSET:
            field_dict["version"] = version
        if installation_uid is not UNSET:
            field_dict["installationUid"] = installation_uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_product(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        version = _parse_version(d.pop("version", UNSET))

        _installation_uid = d.pop("installationUid", UNSET)
        installation_uid: Union[Unset, UUID]
        if isinstance(_installation_uid, Unset):
            installation_uid = UNSET
        else:
            installation_uid = UUID(_installation_uid)

        veeam_one_service_info = cls(
            product=product,
            version=version,
            installation_uid=installation_uid,
        )

        return veeam_one_service_info
