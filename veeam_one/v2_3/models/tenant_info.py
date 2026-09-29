import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.tenant_type import TenantType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TenantInfo")


@_attrs_define
class TenantInfo:
    """
    Attributes:
        tenant_id (Union[Unset, int]): ID assigned to a tenant.
        tenant_uid_in_vbr (Union[None, UUID, Unset]): UID assigned to a tenant in Veeam Cloud Connect.
        backup_server_id (Union[None, Unset, int]): ID assigned to a Veeam Cloud Connect server.
        name (Union[None, Unset, str]): Name of a tenant.
        type_ (Union[Unset, TenantType]):
        tenant_contract_expiration_date (Union[None, Unset, datetime.datetime]): Date and time when the lease period for
            a tenant expires.
    """

    tenant_id: Union[Unset, int] = UNSET
    tenant_uid_in_vbr: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    type_: Union[Unset, TenantType] = UNSET
    tenant_contract_expiration_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        tenant_id = self.tenant_id

        tenant_uid_in_vbr: Union[None, Unset, str]
        if isinstance(self.tenant_uid_in_vbr, Unset):
            tenant_uid_in_vbr = UNSET
        elif isinstance(self.tenant_uid_in_vbr, UUID):
            tenant_uid_in_vbr = str(self.tenant_uid_in_vbr)
        else:
            tenant_uid_in_vbr = self.tenant_uid_in_vbr

        backup_server_id: Union[None, Unset, int]
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        tenant_contract_expiration_date: Union[None, Unset, str]
        if isinstance(self.tenant_contract_expiration_date, Unset):
            tenant_contract_expiration_date = UNSET
        elif isinstance(self.tenant_contract_expiration_date, datetime.datetime):
            tenant_contract_expiration_date = self.tenant_contract_expiration_date.isoformat()
        else:
            tenant_contract_expiration_date = self.tenant_contract_expiration_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if tenant_uid_in_vbr is not UNSET:
            field_dict["tenantUidInVbr"] = tenant_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if tenant_contract_expiration_date is not UNSET:
            field_dict["tenantContractExpirationDate"] = tenant_contract_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tenant_id = d.pop("tenantId", UNSET)

        def _parse_tenant_uid_in_vbr(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_uid_in_vbr_type_0 = UUID(data)

                return tenant_uid_in_vbr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        tenant_uid_in_vbr = _parse_tenant_uid_in_vbr(d.pop("tenantUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TenantType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = TenantType(_type_)

        def _parse_tenant_contract_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tenant_contract_expiration_date_type_0 = isoparse(data)

                return tenant_contract_expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        tenant_contract_expiration_date = _parse_tenant_contract_expiration_date(
            d.pop("tenantContractExpirationDate", UNSET)
        )

        tenant_info = cls(
            tenant_id=tenant_id,
            tenant_uid_in_vbr=tenant_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            type_=type_,
            tenant_contract_expiration_date=tenant_contract_expiration_date,
        )

        return tenant_info
