from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.capacity_tier_extent_info import CapacityTierExtentInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    extent_uid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vbr/scaleoutRepositories/capacityTiers/{extent_uid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CapacityTierExtentInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = CapacityTierExtentInfo.from_dict(response.json())

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
) -> Response[Union[CapacityTierExtentInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extent_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CapacityTierExtentInfo, ProblemDetails]]:
    """Get Capacity Tier Extent

     Returns a resource representation of a capacity tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityTierExtentInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        extent_uid=extent_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extent_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CapacityTierExtentInfo, ProblemDetails]]:
    """Get Capacity Tier Extent

     Returns a resource representation of a capacity tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CapacityTierExtentInfo, ProblemDetails]
    """

    return sync_detailed(
        extent_uid=extent_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    extent_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CapacityTierExtentInfo, ProblemDetails]]:
    """Get Capacity Tier Extent

     Returns a resource representation of a capacity tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CapacityTierExtentInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        extent_uid=extent_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extent_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CapacityTierExtentInfo, ProblemDetails]]:
    """Get Capacity Tier Extent

     Returns a resource representation of a capacity tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CapacityTierExtentInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            extent_uid=extent_uid,
            client=client,
        )
    ).parsed
