from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_info import OrganizationInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    organization_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/cloudDirector/organizations/{organization_id}".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OrganizationInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = OrganizationInfo.from_dict(response.json())

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
) -> Response[OrganizationInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OrganizationInfo | ProblemDetails]:
    """Get Organization

     Returns a resource representation of a VMware Cloud Director organization with the specified ID.

    Args:
        organization_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> OrganizationInfo | ProblemDetails | None:
    """Get Organization

     Returns a resource representation of a VMware Cloud Director organization with the specified ID.

    Args:
        organization_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationInfo | ProblemDetails
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[OrganizationInfo | ProblemDetails]:
    """Get Organization

     Returns a resource representation of a VMware Cloud Director organization with the specified ID.

    Args:
        organization_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OrganizationInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> OrganizationInfo | ProblemDetails | None:
    """Get Organization

     Returns a resource representation of a VMware Cloud Director organization with the specified ID.

    Args:
        organization_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OrganizationInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
        )
    ).parsed
