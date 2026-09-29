from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.tenant_info import TenantInfo
from ...types import Response


def _get_kwargs(
    tenant_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/cloudConnect/tenants/{tenant_id}".format(
            tenant_id=quote(str(tenant_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | TenantInfo | None:
    if response.status_code == 200:
        response_200 = TenantInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | TenantInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tenant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | TenantInfo]:
    """Get Tenant

     Returns a resource representation of a Veeam Cloud Connect tenant with the specified ID.

    Args:
        tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TenantInfo]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tenant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | TenantInfo | None:
    """Get Tenant

     Returns a resource representation of a Veeam Cloud Connect tenant with the specified ID.

    Args:
        tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TenantInfo
    """

    return sync_detailed(
        tenant_id=tenant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    tenant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | TenantInfo]:
    """Get Tenant

     Returns a resource representation of a Veeam Cloud Connect tenant with the specified ID.

    Args:
        tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TenantInfo]
    """

    kwargs = _get_kwargs(
        tenant_id=tenant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tenant_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | TenantInfo | None:
    """Get Tenant

     Returns a resource representation of a Veeam Cloud Connect tenant with the specified ID.

    Args:
        tenant_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TenantInfo
    """

    return (
        await asyncio_detailed(
            tenant_id=tenant_id,
            client=client,
        )
    ).parsed
