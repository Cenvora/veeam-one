from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_director_info import CloudDirectorInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    cloud_director_server_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/cloudDirector/cloudDirectorServers/{cloud_director_server_id}".format(
            cloud_director_server_id=quote(str(cloud_director_server_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloudDirectorInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = CloudDirectorInfo.from_dict(response.json())

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
) -> Response[CloudDirectorInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_director_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CloudDirectorInfo | ProblemDetails]:
    """Get VMware Cloud Director Server

     Returns a resource representation of a VMware Cloud Director server with the specified ID.

    Args:
        cloud_director_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudDirectorInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        cloud_director_server_id=cloud_director_server_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cloud_director_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CloudDirectorInfo | ProblemDetails | None:
    """Get VMware Cloud Director Server

     Returns a resource representation of a VMware Cloud Director server with the specified ID.

    Args:
        cloud_director_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudDirectorInfo | ProblemDetails
    """

    return sync_detailed(
        cloud_director_server_id=cloud_director_server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_director_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CloudDirectorInfo | ProblemDetails]:
    """Get VMware Cloud Director Server

     Returns a resource representation of a VMware Cloud Director server with the specified ID.

    Args:
        cloud_director_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudDirectorInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        cloud_director_server_id=cloud_director_server_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_director_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CloudDirectorInfo | ProblemDetails | None:
    """Get VMware Cloud Director Server

     Returns a resource representation of a VMware Cloud Director server with the specified ID.

    Args:
        cloud_director_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudDirectorInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            cloud_director_server_id=cloud_director_server_id,
            client=client,
        )
    ).parsed
