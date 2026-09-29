from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_host_info import HyperVHostInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    host_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/hyperV/hosts/{host_id}".format(
            host_id=quote(str(host_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HyperVHostInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = HyperVHostInfo.from_dict(response.json())

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
) -> Response[HyperVHostInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVHostInfo | ProblemDetails]:
    """Get Microsoft Hyper-V Host

     Returns a resource representation of a connected Microsoft Hyper-V host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVHostInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    host_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVHostInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V Host

     Returns a resource representation of a connected Microsoft Hyper-V host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVHostInfo | ProblemDetails
    """

    return sync_detailed(
        host_id=host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    host_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVHostInfo | ProblemDetails]:
    """Get Microsoft Hyper-V Host

     Returns a resource representation of a connected Microsoft Hyper-V host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVHostInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVHostInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V Host

     Returns a resource representation of a connected Microsoft Hyper-V host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVHostInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            host_id=host_id,
            client=client,
        )
    ).parsed
