from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.guest_assign_type import GuestAssignType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.guest_settings_request import GuestSettingsRequest


T = TypeVar("T", bound="CredentialAssignGuestRequest")


@_attrs_define
class CredentialAssignGuestRequest:
    """
    Attributes:
        object_id (Union[Unset, int]): ID assigned to an object accessed using the credential set.
        propagate (Union[Unset, bool]): Indicates whether child objects are accessed using the same credential set.
        guest (Union[Unset, GuestAssignType]):
        guest_settings (Union['GuestSettingsRequest', None, Unset]): Guest OS settings.
    """

    object_id: Union[Unset, int] = UNSET
    propagate: Union[Unset, bool] = UNSET
    guest: Union[Unset, GuestAssignType] = UNSET
    guest_settings: Union["GuestSettingsRequest", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.guest_settings_request import GuestSettingsRequest

        object_id = self.object_id

        propagate = self.propagate

        guest: Union[Unset, str] = UNSET
        if not isinstance(self.guest, Unset):
            guest = self.guest.value

        guest_settings: Union[None, Unset, dict[str, Any]]
        if isinstance(self.guest_settings, Unset):
            guest_settings = UNSET
        elif isinstance(self.guest_settings, GuestSettingsRequest):
            guest_settings = self.guest_settings.to_dict()
        else:
            guest_settings = self.guest_settings

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_id is not UNSET:
            field_dict["objectId"] = object_id
        if propagate is not UNSET:
            field_dict["propagate"] = propagate
        if guest is not UNSET:
            field_dict["guest"] = guest
        if guest_settings is not UNSET:
            field_dict["guestSettings"] = guest_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.guest_settings_request import GuestSettingsRequest

        d = dict(src_dict)
        object_id = d.pop("objectId", UNSET)

        propagate = d.pop("propagate", UNSET)

        _guest = d.pop("guest", UNSET)
        guest: Union[Unset, GuestAssignType]
        if isinstance(_guest, Unset):
            guest = UNSET
        else:
            guest = GuestAssignType(_guest)

        def _parse_guest_settings(data: object) -> Union["GuestSettingsRequest", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                guest_settings_type_1 = GuestSettingsRequest.from_dict(data)

                return guest_settings_type_1
            except:  # noqa: E722
                pass
            return cast(Union["GuestSettingsRequest", None, Unset], data)

        guest_settings = _parse_guest_settings(d.pop("guestSettings", UNSET))

        credential_assign_guest_request = cls(
            object_id=object_id,
            propagate=propagate,
            guest=guest,
            guest_settings=guest_settings,
        )

        return credential_assign_guest_request
