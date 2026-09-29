from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vb_365_team_info_page import Vb365TeamInfoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_uid: UUID,
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    params["Filter"] = filter_

    params["Sort"] = sort

    params["Select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vb365/organizations/{organization_uid}/teams",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, Vb365TeamInfoPage]]:
    if response.status_code == 200:
        response_200 = Vb365TeamInfoPage.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProblemDetails, Vb365TeamInfoPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetails, Vb365TeamInfoPage]]:
    """Get All Teams of Microsoft Organization

     Returns a collection resource representation of all teams of a Microsoft 365 organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, Vb365TeamInfoPage]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetails, Vb365TeamInfoPage]]:
    """Get All Teams of Microsoft Organization

     Returns a collection resource representation of all teams of a Microsoft 365 organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, Vb365TeamInfoPage]
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetails, Vb365TeamInfoPage]]:
    """Get All Teams of Microsoft Organization

     Returns a collection resource representation of all teams of a Microsoft 365 organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, Vb365TeamInfoPage]]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetails, Vb365TeamInfoPage]]:
    """Get All Teams of Microsoft Organization

     Returns a collection resource representation of all teams of a Microsoft 365 organization with the
    specified UID.

    Args:
        organization_uid (UUID):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, Vb365TeamInfoPage]
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
            sort=sort,
            select=select,
        )
    ).parsed
