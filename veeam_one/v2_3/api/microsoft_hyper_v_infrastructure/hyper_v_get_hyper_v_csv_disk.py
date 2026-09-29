from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_csv_info import HyperVCsvInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    csv_disk_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/hyperV/csvDisks/{csv_disk_id}".format(
            csv_disk_id=quote(str(csv_disk_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HyperVCsvInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = HyperVCsvInfo.from_dict(response.json())

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
) -> Response[HyperVCsvInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    csv_disk_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVCsvInfo | ProblemDetails]:
    """Get Microsoft Hyper-V CSV

     Returns a resource representation of a connected Microsoft Hyper-V CSV with the specified ID.

    Args:
        csv_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVCsvInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        csv_disk_id=csv_disk_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    csv_disk_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVCsvInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V CSV

     Returns a resource representation of a connected Microsoft Hyper-V CSV with the specified ID.

    Args:
        csv_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVCsvInfo | ProblemDetails
    """

    return sync_detailed(
        csv_disk_id=csv_disk_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    csv_disk_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[HyperVCsvInfo | ProblemDetails]:
    """Get Microsoft Hyper-V CSV

     Returns a resource representation of a connected Microsoft Hyper-V CSV with the specified ID.

    Args:
        csv_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HyperVCsvInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        csv_disk_id=csv_disk_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    csv_disk_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> HyperVCsvInfo | ProblemDetails | None:
    """Get Microsoft Hyper-V CSV

     Returns a resource representation of a connected Microsoft Hyper-V CSV with the specified ID.

    Args:
        csv_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HyperVCsvInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            csv_disk_id=csv_disk_id,
            client=client,
        )
    ).parsed
