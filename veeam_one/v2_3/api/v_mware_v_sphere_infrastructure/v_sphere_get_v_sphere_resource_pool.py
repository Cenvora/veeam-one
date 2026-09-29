from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_resource_pool_info import VSphereResourcePoolInfo
from ...types import Response


def _get_kwargs(
    resource_pool_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/resourcePools/{resource_pool_id}".format(
            resource_pool_id=quote(str(resource_pool_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VSphereResourcePoolInfo | None:
    if response.status_code == 200:
        response_200 = VSphereResourcePoolInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VSphereResourcePoolInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_pool_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereResourcePoolInfo]:
    """Get Resource Pool

     Returns a resource representation of a VMware vSphere resource pool with the specified ID.

    Args:
        resource_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereResourcePoolInfo]
    """

    kwargs = _get_kwargs(
        resource_pool_id=resource_pool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_pool_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereResourcePoolInfo | None:
    """Get Resource Pool

     Returns a resource representation of a VMware vSphere resource pool with the specified ID.

    Args:
        resource_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereResourcePoolInfo
    """

    return sync_detailed(
        resource_pool_id=resource_pool_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    resource_pool_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereResourcePoolInfo]:
    """Get Resource Pool

     Returns a resource representation of a VMware vSphere resource pool with the specified ID.

    Args:
        resource_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereResourcePoolInfo]
    """

    kwargs = _get_kwargs(
        resource_pool_id=resource_pool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_pool_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereResourcePoolInfo | None:
    """Get Resource Pool

     Returns a resource representation of a VMware vSphere resource pool with the specified ID.

    Args:
        resource_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereResourcePoolInfo
    """

    return (
        await asyncio_detailed(
            resource_pool_id=resource_pool_id,
            client=client,
        )
    ).parsed
