from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_physical_disk_info import HyperVPhysicalDiskInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    physical_disk_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/hyperV/physicalDisks/{physical_disk_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = HyperVPhysicalDiskInfo.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    physical_disk_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V Physical Disk

     Returns a resource representation of a Microsoft Hyper-V physical disk with the specified ID.

    Args:
        physical_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HyperVPhysicalDiskInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        physical_disk_id=physical_disk_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    physical_disk_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V Physical Disk

     Returns a resource representation of a Microsoft Hyper-V physical disk with the specified ID.

    Args:
        physical_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HyperVPhysicalDiskInfo, ProblemDetails]
    """

    return sync_detailed(
        physical_disk_id=physical_disk_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    physical_disk_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V Physical Disk

     Returns a resource representation of a Microsoft Hyper-V physical disk with the specified ID.

    Args:
        physical_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HyperVPhysicalDiskInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        physical_disk_id=physical_disk_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    physical_disk_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HyperVPhysicalDiskInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V Physical Disk

     Returns a resource representation of a Microsoft Hyper-V physical disk with the specified ID.

    Args:
        physical_disk_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HyperVPhysicalDiskInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            physical_disk_id=physical_disk_id,
            client=client,
        )
    ).parsed
