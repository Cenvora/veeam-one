from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationInfo")


@_attrs_define
class OrganizationInfo:
    """
    Attributes:
        organization_id (Union[Unset, int]): ID assigned to an organization.
        href (Union[None, Unset, str]): Unique organization identifier in the URL format. Identical to the `href`
            property in VMware Cloud Director API.
        name (Union[None, Unset, str]): Name of an organization.
        is_enabled (Union[None, Unset, bool]): Indicates whether an organization is enabled.
        number_of_catalogs (Union[None, Unset, int]): Number of organization catalogs.
        cloud_director_id (Union[None, Unset, int]): ID assigned to a VMware Cloud Director server.
        organization_vdc_ids (Union[None, Unset, list[int]]): Array of IDs assigned to organization VDCs.
    """

    organization_id: Union[Unset, int] = UNSET
    href: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    is_enabled: Union[None, Unset, bool] = UNSET
    number_of_catalogs: Union[None, Unset, int] = UNSET
    cloud_director_id: Union[None, Unset, int] = UNSET
    organization_vdc_ids: Union[None, Unset, list[int]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        href: Union[None, Unset, str]
        if isinstance(self.href, Unset):
            href = UNSET
        else:
            href = self.href

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        is_enabled: Union[None, Unset, bool]
        if isinstance(self.is_enabled, Unset):
            is_enabled = UNSET
        else:
            is_enabled = self.is_enabled

        number_of_catalogs: Union[None, Unset, int]
        if isinstance(self.number_of_catalogs, Unset):
            number_of_catalogs = UNSET
        else:
            number_of_catalogs = self.number_of_catalogs

        cloud_director_id: Union[None, Unset, int]
        if isinstance(self.cloud_director_id, Unset):
            cloud_director_id = UNSET
        else:
            cloud_director_id = self.cloud_director_id

        organization_vdc_ids: Union[None, Unset, list[int]]
        if isinstance(self.organization_vdc_ids, Unset):
            organization_vdc_ids = UNSET
        elif isinstance(self.organization_vdc_ids, list):
            organization_vdc_ids = self.organization_vdc_ids

        else:
            organization_vdc_ids = self.organization_vdc_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if href is not UNSET:
            field_dict["href"] = href
        if name is not UNSET:
            field_dict["name"] = name
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if number_of_catalogs is not UNSET:
            field_dict["numberOfCatalogs"] = number_of_catalogs
        if cloud_director_id is not UNSET:
            field_dict["cloudDirectorId"] = cloud_director_id
        if organization_vdc_ids is not UNSET:
            field_dict["organizationVdcIds"] = organization_vdc_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        def _parse_href(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        href = _parse_href(d.pop("href", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_is_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_enabled = _parse_is_enabled(d.pop("isEnabled", UNSET))

        def _parse_number_of_catalogs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_catalogs = _parse_number_of_catalogs(d.pop("numberOfCatalogs", UNSET))

        def _parse_cloud_director_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cloud_director_id = _parse_cloud_director_id(d.pop("cloudDirectorId", UNSET))

        def _parse_organization_vdc_ids(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                organization_vdc_ids_type_0 = cast(list[int], data)

                return organization_vdc_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        organization_vdc_ids = _parse_organization_vdc_ids(d.pop("organizationVdcIds", UNSET))

        organization_info = cls(
            organization_id=organization_id,
            href=href,
            name=name,
            is_enabled=is_enabled,
            number_of_catalogs=number_of_catalogs,
            cloud_director_id=cloud_director_id,
            organization_vdc_ids=organization_vdc_ids,
        )

        return organization_info
