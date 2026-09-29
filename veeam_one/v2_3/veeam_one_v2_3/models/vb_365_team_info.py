from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365TeamInfo")


@_attrs_define
class Vb365TeamInfo:
    """
    Attributes:
        team_uid (Union[Unset, UUID]): UID assigned to a team.
        name (Union[None, Unset, str]): Name of a team.
        description (Union[None, Unset, str]): Description of a team.
        mail (Union[None, Unset, str]): Email address of a team.
        vb_365_server_id (Union[Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        organization_uid (Union[Unset, UUID]): UID assigned to a Microsoft 365 organization.
        organization_name (Union[None, Unset, str]): Name of a Microsoft 365 organization.
    """

    team_uid: Union[Unset, UUID] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    mail: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[Unset, int] = UNSET
    organization_uid: Union[Unset, UUID] = UNSET
    organization_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        team_uid: Union[Unset, str] = UNSET
        if not isinstance(self.team_uid, Unset):
            team_uid = str(self.team_uid)

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        mail: Union[None, Unset, str]
        if isinstance(self.mail, Unset):
            mail = UNSET
        else:
            mail = self.mail

        vb_365_server_id = self.vb_365_server_id

        organization_uid: Union[Unset, str] = UNSET
        if not isinstance(self.organization_uid, Unset):
            organization_uid = str(self.organization_uid)

        organization_name: Union[None, Unset, str]
        if isinstance(self.organization_name, Unset):
            organization_name = UNSET
        else:
            organization_name = self.organization_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if team_uid is not UNSET:
            field_dict["teamUid"] = team_uid
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if mail is not UNSET:
            field_dict["mail"] = mail
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if organization_uid is not UNSET:
            field_dict["organizationUid"] = organization_uid
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _team_uid = d.pop("teamUid", UNSET)
        team_uid: Union[Unset, UUID]
        if isinstance(_team_uid, Unset):
            team_uid = UNSET
        else:
            team_uid = UUID(_team_uid)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_mail(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mail = _parse_mail(d.pop("mail", UNSET))

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

        vb_365_team_info = cls(
            team_uid=team_uid,
            name=name,
            description=description,
            mail=mail,
            vb_365_server_id=vb_365_server_id,
            organization_uid=organization_uid,
            organization_name=organization_name,
        )

        return vb_365_team_info
