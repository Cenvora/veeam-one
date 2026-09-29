import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.veeam_one_license_type import VeeamOneLicenseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLicenseInfo")


@_attrs_define
class VeeamOneLicenseInfo:
    """
    Attributes:
        type_ (Union[Unset, VeeamOneLicenseType]):
        expiration_date (Union[None, Unset, datetime.datetime]): Data and time of license expiration. Example:
            '2021-09-30T00:00:00Z'.
        support_expiration_date (Union[None, Unset, datetime.datetime]): Date and time of support service expiration.
            Example: '2021-09-30T00:00:00Z'.
        instances (Union[None, Unset, int]): Number of licensed instances. Example: 10000.
        sockets (Union[None, Unset, int]): Number of licensed sockets.
        package (Union[None, Unset, str]): Type of a license package. Example: Suite.
        company (Union[None, Unset, str]): Name of the user or company to which the license was issued. Example: Alpha
            Company.
        email (Union[None, Unset, str]): Contact e-mail address of the user or company to which the license was issued.
            Example: a.smith@alpha.com.
        support_id (Union[None, Unset, str]): License support ID. Example: 12345678.
        license_id (Union[None, UUID, Unset]): UID assigned to a license. Example: c44b3242-ce34-40c7-afcd-e8773deb7fd2.
    """

    type_: Union[Unset, VeeamOneLicenseType] = UNSET
    expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    support_expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    instances: Union[None, Unset, int] = UNSET
    sockets: Union[None, Unset, int] = UNSET
    package: Union[None, Unset, str] = UNSET
    company: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    support_id: Union[None, Unset, str] = UNSET
    license_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        expiration_date: Union[None, Unset, str]
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        support_expiration_date: Union[None, Unset, str]
        if isinstance(self.support_expiration_date, Unset):
            support_expiration_date = UNSET
        elif isinstance(self.support_expiration_date, datetime.datetime):
            support_expiration_date = self.support_expiration_date.isoformat()
        else:
            support_expiration_date = self.support_expiration_date

        instances: Union[None, Unset, int]
        if isinstance(self.instances, Unset):
            instances = UNSET
        else:
            instances = self.instances

        sockets: Union[None, Unset, int]
        if isinstance(self.sockets, Unset):
            sockets = UNSET
        else:
            sockets = self.sockets

        package: Union[None, Unset, str]
        if isinstance(self.package, Unset):
            package = UNSET
        else:
            package = self.package

        company: Union[None, Unset, str]
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        support_id: Union[None, Unset, str]
        if isinstance(self.support_id, Unset):
            support_id = UNSET
        else:
            support_id = self.support_id

        license_id: Union[None, Unset, str]
        if isinstance(self.license_id, Unset):
            license_id = UNSET
        elif isinstance(self.license_id, UUID):
            license_id = str(self.license_id)
        else:
            license_id = self.license_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if support_expiration_date is not UNSET:
            field_dict["supportExpirationDate"] = support_expiration_date
        if instances is not UNSET:
            field_dict["instances"] = instances
        if sockets is not UNSET:
            field_dict["sockets"] = sockets
        if package is not UNSET:
            field_dict["package"] = package
        if company is not UNSET:
            field_dict["company"] = company
        if email is not UNSET:
            field_dict["email"] = email
        if support_id is not UNSET:
            field_dict["supportId"] = support_id
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, VeeamOneLicenseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = VeeamOneLicenseType(_type_)

        def _parse_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        def _parse_support_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                support_expiration_date_type_0 = isoparse(data)

                return support_expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        support_expiration_date = _parse_support_expiration_date(d.pop("supportExpirationDate", UNSET))

        def _parse_instances(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        instances = _parse_instances(d.pop("instances", UNSET))

        def _parse_sockets(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sockets = _parse_sockets(d.pop("sockets", UNSET))

        def _parse_package(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        package = _parse_package(d.pop("package", UNSET))

        def _parse_company(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company = _parse_company(d.pop("company", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_support_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        support_id = _parse_support_id(d.pop("supportId", UNSET))

        def _parse_license_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                license_id_type_0 = UUID(data)

                return license_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        license_id = _parse_license_id(d.pop("licenseId", UNSET))

        veeam_one_license_info = cls(
            type_=type_,
            expiration_date=expiration_date,
            support_expiration_date=support_expiration_date,
            instances=instances,
            sockets=sockets,
            package=package,
            company=company,
            email=email,
            support_id=support_id,
            license_id=license_id,
        )

        return veeam_one_license_info
