from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_file_server_info import HyperVFileServerInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    file_server_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/hyperV/fileServers/{file_server_id}".format(
            file_server_id=quote(str(file_server_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HyperVFileServerInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = HyperVFileServerInfo.from_dict(response.json())

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
) -> Response[HyperVFileServerInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVFileServerInfo | ProblemDetails]:
    """Get Microsoft Hyper-V File Server

     Returns a resource representation of a connected Microsoft Hyper-V file server with the specified
    ID.

    Args:
        file_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVFileServerInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_server_id=file_server_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVFileServerInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V File Server

     Returns a resource representation of a connected Microsoft Hyper-V file server with the specified
    ID.

    Args:
        file_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVFileServerInfo | ProblemDetails
    """

    return sync_detailed(
        file_server_id=file_server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVFileServerInfo | ProblemDetails]:
    """Get Microsoft Hyper-V File Server

     Returns a resource representation of a connected Microsoft Hyper-V file server with the specified
    ID.

    Args:
        file_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVFileServerInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_server_id=file_server_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_server_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVFileServerInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V File Server

     Returns a resource representation of a connected Microsoft Hyper-V file server with the specified
    ID.

    Args:
        file_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVFileServerInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            file_server_id=file_server_id,
            client=client,
        )
    ).parsed
