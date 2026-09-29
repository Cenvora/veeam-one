from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_vdc import ProviderVdc


T = TypeVar("T", bound="CloudDirectorDatastoreInfo")


@_attrs_define
class CloudDirectorDatastoreInfo:
    """
    Attributes:
        datastore_id (int | Unset): ID assigned to a datastore.
        cloud_director_id (int | Unset): ID assigned to a VMware Cloud Director server.
        v_center_server_id (int | Unset): ID assigned to a vCenter server.
        href (None | str | Unset): Unique datastore identifier in the URL format. Identical to the `href` property in
            VMware Cloud Director API.
        name (None | str | Unset): Name of a datastore.
        type_ (None | str | Unset): Type of a datastore.
        capacity_bytes (int | Unset): Storage capacity of a datastore, in bytes.
        used_bytes (int | Unset): Amount of storage space consumed on a datastore, in bytes.
        provisioned_bytes (int | Unset): Amount of storage space allocated to a provider VDC, in bytes.
        requested_bytes (int | Unset): Amount of storage space consumed by a provider VDC, in bytes.
        provider_vdc_count (int | Unset): Number of provider VDCs to which a datastore provides resources.
        provider_vdcs (list[ProviderVdc] | None | Unset): Array of provider VDCs to which a datastore provides
            resources.
    """

    datastore_id: int | Unset = UNSET
    cloud_director_id: int | Unset = UNSET
    v_center_server_id: int | Unset = UNSET
    href: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    capacity_bytes: int | Unset = UNSET
    used_bytes: int | Unset = UNSET
    provisioned_bytes: int | Unset = UNSET
    requested_bytes: int | Unset = UNSET
    provider_vdc_count: int | Unset = UNSET
    provider_vdcs: list[ProviderVdc] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        datastore_id = self.datastore_id

        cloud_director_id = self.cloud_director_id

        v_center_server_id = self.v_center_server_id

        href: None | str | Unset
        if isinstance(self.href, Unset):
            href = UNSET
        else:
            href = self.href

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

        capacity_bytes = self.capacity_bytes

        used_bytes = self.used_bytes

        provisioned_bytes = self.provisioned_bytes

        requested_bytes = self.requested_bytes

        provider_vdc_count = self.provider_vdc_count

        provider_vdcs: list[dict[str, Any]] | None | Unset
        if isinstance(self.provider_vdcs, Unset):
            provider_vdcs = UNSET
        elif isinstance(self.provider_vdcs, list):
            provider_vdcs = []
            for provider_vdcs_type_0_item_data in self.provider_vdcs:
                provider_vdcs_type_0_item = provider_vdcs_type_0_item_data.to_dict()
                provider_vdcs.append(provider_vdcs_type_0_item)

        else:
            provider_vdcs = self.provider_vdcs

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if datastore_id is not UNSET:
            field_dict["datastoreId"] = datastore_id
        if cloud_director_id is not UNSET:
            field_dict["cloudDirectorId"] = cloud_director_id
        if v_center_server_id is not UNSET:
            field_dict["vCenterServerId"] = v_center_server_id
        if href is not UNSET:
            field_dict["href"] = href
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if used_bytes is not UNSET:
            field_dict["usedBytes"] = used_bytes
        if provisioned_bytes is not UNSET:
            field_dict["provisionedBytes"] = provisioned_bytes
        if requested_bytes is not UNSET:
            field_dict["requestedBytes"] = requested_bytes
        if provider_vdc_count is not UNSET:
            field_dict["providerVdcCount"] = provider_vdc_count
        if provider_vdcs is not UNSET:
            field_dict["providerVdcs"] = provider_vdcs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_vdc import ProviderVdc  # noqa: PLC0415

        d = dict(src_dict)
        datastore_id = d.pop("datastoreId", UNSET)

        cloud_director_id = d.pop("cloudDirectorId", UNSET)

        v_center_server_id = d.pop("vCenterServerId", UNSET)

        def _parse_href(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        href = _parse_href(d.pop("href", UNSET))

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

        capacity_bytes = d.pop("capacityBytes", UNSET)

        used_bytes = d.pop("usedBytes", UNSET)

        provisioned_bytes = d.pop("provisionedBytes", UNSET)

        requested_bytes = d.pop("requestedBytes", UNSET)

        provider_vdc_count = d.pop("providerVdcCount", UNSET)

        def _parse_provider_vdcs(data: object) -> list[ProviderVdc] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                provider_vdcs_type_0 = []
                _provider_vdcs_type_0 = data
                for provider_vdcs_type_0_item_data in _provider_vdcs_type_0:
                    provider_vdcs_type_0_item = ProviderVdc.from_dict(provider_vdcs_type_0_item_data)

                    provider_vdcs_type_0.append(provider_vdcs_type_0_item)

                return provider_vdcs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProviderVdc] | None | Unset, data)

        provider_vdcs = _parse_provider_vdcs(d.pop("providerVdcs", UNSET))

        cloud_director_datastore_info = cls(
            datastore_id=datastore_id,
            cloud_director_id=cloud_director_id,
            v_center_server_id=v_center_server_id,
            href=href,
            name=name,
            type_=type_,
            capacity_bytes=capacity_bytes,
            used_bytes=used_bytes,
            provisioned_bytes=provisioned_bytes,
            requested_bytes=requested_bytes,
            provider_vdc_count=provider_vdc_count,
            provider_vdcs=provider_vdcs,
        )

        return cloud_director_datastore_info
