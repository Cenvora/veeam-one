from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vb_365_organization_info import Vb365OrganizationInfo
from ...types import Response


def _get_kwargs(
    organization_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vb365/organizations/{organization_uid}".format(
            organization_uid=quote(str(organization_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | Vb365OrganizationInfo | None:
    if response.status_code == 200:
        response_200 = Vb365OrganizationInfo.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | Vb365OrganizationInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365OrganizationInfo]:
    """Get Microsoft Organization

     Returns a resource representation of a Microsoft organization with the specified UID.

    Args:
        organization_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365OrganizationInfo]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365OrganizationInfo | None:
    """Get Microsoft Organization

     Returns a resource representation of a Microsoft organization with the specified UID.

    Args:
        organization_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365OrganizationInfo
    """

    return sync_detailed(
        organization_uid=organization_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365OrganizationInfo]:
    """Get Microsoft Organization

     Returns a resource representation of a Microsoft organization with the specified UID.

    Args:
        organization_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365OrganizationInfo]
    """

    kwargs = _get_kwargs(
        organization_uid=organization_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365OrganizationInfo | None:
    """Get Microsoft Organization

     Returns a resource representation of a Microsoft organization with the specified UID.

    Args:
        organization_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365OrganizationInfo
    """

    return (
        await asyncio_detailed(
            organization_uid=organization_uid,
            client=client,
        )
    ).parsed
