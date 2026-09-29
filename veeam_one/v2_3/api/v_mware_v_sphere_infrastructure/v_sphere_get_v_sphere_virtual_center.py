from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_center_server_info import VCenterServerInfo
from ...types import Response


def _get_kwargs(
    v_center_server_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/vCenterServers/{v_center_server_id}".format(
            v_center_server_id=quote(str(v_center_server_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VCenterServerInfo | None:
    if response.status_code == 200:
        response_200 = VCenterServerInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VCenterServerInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    v_center_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VCenterServerInfo]:
    """Get vCenter Server

     Returns a resource representation of a connected vCenter server with the specified ID.

    Args:
        v_center_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VCenterServerInfo]
    """

    kwargs = _get_kwargs(
        v_center_server_id=v_center_server_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    v_center_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VCenterServerInfo | None:
    """Get vCenter Server

     Returns a resource representation of a connected vCenter server with the specified ID.

    Args:
        v_center_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VCenterServerInfo
    """

    return sync_detailed(
        v_center_server_id=v_center_server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    v_center_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VCenterServerInfo]:
    """Get vCenter Server

     Returns a resource representation of a connected vCenter server with the specified ID.

    Args:
        v_center_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VCenterServerInfo]
    """

    kwargs = _get_kwargs(
        v_center_server_id=v_center_server_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    v_center_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VCenterServerInfo | None:
    """Get vCenter Server

     Returns a resource representation of a connected vCenter server with the specified ID.

    Args:
        v_center_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VCenterServerInfo
    """

    return (
        await asyncio_detailed(
            v_center_server_id=v_center_server_id,
            client=client,
        )
    ).parsed
