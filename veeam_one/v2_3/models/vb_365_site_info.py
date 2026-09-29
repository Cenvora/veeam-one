from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365SiteInfo")


@_attrs_define
class Vb365SiteInfo:
    """
    Attributes:
        site_uid (Union[Unset, UUID]): UID assigned to a SharePoint site.
        site_uid_in_vb_365 (Union[None, Unset, str]): UID assigned to a SharePoint site in Veeam Backup for Microsoft
            365.
        name (Union[None, Unset, str]): Name of a Microsoft SharePoint site.
        url (Union[None, Unset, str]): URL of a Microsoft SharePoint site.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft 365 organization.
        is_cloud (Union[Unset, bool]): Indicates whether a Microsoft SharePoint site is cloud-based.
        is_personal (Union[Unset, bool]): Indicates whether a Microsoft SharePoint site is personal.
        is_available (Union[Unset, bool]): Indicates whether a Microsoft SharePoint site is available.
    """

    site_uid: Union[Unset, UUID] = UNSET
    site_uid_in_vb_365: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    url: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET
    is_cloud: Union[Unset, bool] = UNSET
    is_personal: Union[Unset, bool] = UNSET
    is_available: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        site_uid: Union[Unset, str] = UNSET
        if not isinstance(self.site_uid, Unset):
            site_uid = str(self.site_uid)

        site_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.site_uid_in_vb_365, Unset):
            site_uid_in_vb_365 = UNSET
        else:
            site_uid_in_vb_365 = self.site_uid_in_vb_365

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        vb_365_server_id = self.vb_365_server_id

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        is_cloud = self.is_cloud

        is_personal = self.is_personal

        is_available = self.is_available

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if site_uid is not UNSET:
            field_dict["siteUid"] = site_uid
        if site_uid_in_vb_365 is not UNSET:
            field_dict["siteUidInVb365"] = site_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if is_cloud is not UNSET:
            field_dict["isCloud"] = is_cloud
        if is_personal is not UNSET:
            field_dict["isPersonal"] = is_personal
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _site_uid = d.pop("siteUid", UNSET)
        site_uid: Union[Unset, UUID]
        if isinstance(_site_uid, Unset):
            site_uid = UNSET
        else:
            site_uid = UUID(_site_uid)

        def _parse_site_uid_in_vb_365(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        site_uid_in_vb_365 = _parse_site_uid_in_vb_365(d.pop("siteUidInVb365", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        vb_365_server_id = d.pop("vb365ServerId", UNSET)

        _organization_uid = d.pop("organizationUid", UNSET)
        organization_uid: Union[Unset, UUID]
        if isinstance(_organization_uid, Unset):
            organization_uid = UNSET
        else:
            organization_uid = UUID(_organization_uid)

        def _parse_organization_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_name = _parse_organization_name(d.pop("organizationName", UNSET))

        is_cloud = d.pop("isCloud", UNSET)

        is_personal = d.pop("isPersonal", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        vb_365_site_info = cls(
            site_uid=site_uid,
            site_uid_in_vb_365=site_uid_in_vb_365,
            name=name,
            url=url,
            vb_365_server_id=vb_365_server_id,
            organization_uid=organization_uid,
            organization_name=organization_name,
            is_cloud=is_cloud,
            is_personal=is_personal,
            is_available=is_available,
        )

        return vb_365_site_info
