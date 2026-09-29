from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_file_share_info import HyperVFileShareInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    file_share_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/hyperV/fileShares/{file_share_id}".format(
            file_share_id=quote(str(file_share_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HyperVFileShareInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = HyperVFileShareInfo.from_dict(response.json())

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
) -> Response[HyperVFileShareInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_share_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVFileShareInfo | ProblemDetails]:
    """Get Microsoft Hyper-V File Share

     Returns a resource representation of a connected Microsoft Hyper-V file share with the specified ID.

    Args:
        file_share_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVFileShareInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_share_id=file_share_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_share_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVFileShareInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V File Share

     Returns a resource representation of a connected Microsoft Hyper-V file share with the specified ID.

    Args:
        file_share_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVFileShareInfo | ProblemDetails
    """

    return sync_detailed(
        file_share_id=file_share_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_share_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVFileShareInfo | ProblemDetails]:
    """Get Microsoft Hyper-V File Share

     Returns a resource representation of a connected Microsoft Hyper-V file share with the specified ID.

    Args:
        file_share_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVFileShareInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_share_id=file_share_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_share_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVFileShareInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V File Share

     Returns a resource representation of a connected Microsoft Hyper-V file share with the specified ID.

    Args:
        file_share_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVFileShareInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            file_share_id=file_share_id,
            client=client,
        )
    ).parsed
