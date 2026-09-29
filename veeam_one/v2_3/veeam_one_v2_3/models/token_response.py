from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.access_token_role import AccessTokenRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenResponse")


@_attrs_define
class TokenResponse:
    r"""
    Attributes:
        access_token (Union[None, Unset, str]): Access token. Example: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9LjthD9KEdtgfX
            IsBQWRnWOKmM19kCwgBP40K6TzHNpzqBhMEc3eyh9B0yqhrLgIhz4Xq0TYB4HHohOG2QoOrvk8yHQcoBxtWfmvDF347bQ1OVgE5_Ieh29cglNiT1
            mXQ5Z9S1a4KTwDkRhfS5tNMlVHLg0vUXQwZvFykKXIuck1cQFfZAHpJq9UhEySG9kx7Q-
            t09ZfDFFVf8IUT0OrNd9jJ2DQP9snvjNNXeHuHd3HE1Mer_bVg.
        refresh_token (Union[None, Unset, str]): Refresh token. Example: eyJhbGciOiJIUzI1Ni1BTcPnVzDIyOagiZNuEbPwbEBCe9u
            _m8l31biXWP1vOyh6_LdbKcDY6gzi6bUopTf02yV6ks4-hhEhhMsq4M6_hd3ZPZJmNLoHUEdDa8reXVBkHdsaLgr6NUGFArVeQ7cy1OdA.
        token_type (Union[None, Unset, str]): Type of the access token. Example: Bearer.
        expires_in (Union[Unset, int]): Time after which the access token expires, in seconds. Example: 899.
        user (Union[None, Unset, str]): User name in the DOMAIN\USERNAME format. Example: onesrv\administrator.
        user_role (Union[Unset, AccessTokenRole]):
    """

    access_token: Union[None, Unset, str] = UNSET
    refresh_token: Union[None, Unset, str] = UNSET
    token_type: Union[None, Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    user: Union[None, Unset, str] = UNSET
    user_role: Union[Unset, AccessTokenRole] = UNSET

    def to_dict(self) -> dict[str, Any]:
        access_token: Union[None, Unset, str]
        if isinstance(self.access_token, Unset):
            access_token = UNSET
        else:
            access_token = self.access_token

        refresh_token: Union[None, Unset, str]
        if isinstance(self.refresh_token, Unset):
            refresh_token = UNSET
        else:
            refresh_token = self.refresh_token

        token_type: Union[None, Unset, str]
        if isinstance(self.token_type, Unset):
            token_type = UNSET
        else:
            token_type = self.token_type

        expires_in = self.expires_in

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        user_role: Union[Unset, str] = UNSET
        if not isinstance(self.user_role, Unset):
            user_role = self.user_role.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if user is not UNSET:
            field_dict["user"] = user
        if user_role is not UNSET:
            field_dict["user_role"] = user_role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_access_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        access_token = _parse_access_token(d.pop("access_token", UNSET))

        def _parse_refresh_token(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refresh_token = _parse_refresh_token(d.pop("refresh_token", UNSET))

        def _parse_token_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        token_type = _parse_token_type(d.pop("token_type", UNSET))

        expires_in = d.pop("expires_in", UNSET)

        def _parse_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        _user_role = d.pop("user_role", UNSET)
        user_role: Union[Unset, AccessTokenRole]
        if isinstance(_user_role, Unset):
            user_role = UNSET
        else:
            user_role = AccessTokenRole(_user_role)

        token_response = cls(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type=token_type,
            expires_in=expires_in,
            user=user,
            user_role=user_role,
        )

        return token_response
