import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.assign_type import AssignType
from ..models.credentials_type import CredentialsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityCredentialsInfo")


@_attrs_define
class EntityCredentialsInfo:
    """
    Attributes:
        credentials_id (Union[Unset, int]): ID assigned to a set of credentials.
        type_ (Union[Unset, CredentialsType]):
        user_name (Union[None, Unset, str]): User name.
        description (Union[None, Unset, str]): Description.
        last_modified (Union[Unset, datetime.datetime]): Date and time of the latest credentials modification.
        currently_assigned (Union[Unset, bool]): Indicates whether credentials are assigned to a user.
        is_propagated (Union[Unset, bool]): Indicates whether credentials of a parent object account are used.
        assign_type (Union[Unset, AssignType]):
    """

    credentials_id: Union[Unset, int] = UNSET
    type_: Union[Unset, CredentialsType] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    currently_assigned: Union[Unset, bool] = UNSET
    is_propagated: Union[Unset, bool] = UNSET
    assign_type: Union[Unset, AssignType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        credentials_id = self.credentials_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        currently_assigned = self.currently_assigned

        is_propagated = self.is_propagated

        assign_type: Union[Unset, str] = UNSET
        if not isinstance(self.assign_type, Unset):
            assign_type = self.assign_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if credentials_id is not UNSET:
            field_dict["credentialsId"] = credentials_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if description is not UNSET:
            field_dict["description"] = description
        if last_modified is not UNSET:
            field_dict["lastModified"] = last_modified
        if currently_assigned is not UNSET:
            field_dict["currentlyAssigned"] = currently_assigned
        if is_propagated is not UNSET:
            field_dict["isPropagated"] = is_propagated
        if assign_type is not UNSET:
            field_dict["assignType"] = assign_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credentials_id = d.pop("credentialsId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CredentialsType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CredentialsType(_type_)

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _last_modified = d.pop("lastModified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        currently_assigned = d.pop("currentlyAssigned", UNSET)

        is_propagated = d.pop("isPropagated", UNSET)

        _assign_type = d.pop("assignType", UNSET)
        assign_type: Union[Unset, AssignType]
        if isinstance(_assign_type, Unset):
            assign_type = UNSET
        else:
            assign_type = AssignType(_assign_type)

        entity_credentials_info = cls(
            credentials_id=credentials_id,
            type_=type_,
            user_name=user_name,
            description=description,
            last_modified=last_modified,
            currently_assigned=currently_assigned,
            is_propagated=is_propagated,
            assign_type=assign_type,
        )

        return entity_credentials_info
