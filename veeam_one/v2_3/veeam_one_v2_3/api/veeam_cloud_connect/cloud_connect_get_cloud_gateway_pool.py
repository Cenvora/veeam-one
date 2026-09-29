from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_gateway_pool_info import CloudGatewayPoolInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    cloud_gateway_pool_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/cloudConnect/cloudGatewayPools/{cloud_gateway_pool_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = CloudGatewayPoolInfo.from_dict(response.json())

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
) -> Response[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_gateway_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    """Get Cloud Gateway Pool

     Returns a resource representation of a cloud gateway pool with the specified ID.

    Args:
        cloud_gateway_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CloudGatewayPoolInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        cloud_gateway_pool_id=cloud_gateway_pool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cloud_gateway_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    """Get Cloud Gateway Pool

     Returns a resource representation of a cloud gateway pool with the specified ID.

    Args:
        cloud_gateway_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CloudGatewayPoolInfo, ProblemDetails]
    """

    return sync_detailed(
        cloud_gateway_pool_id=cloud_gateway_pool_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_gateway_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    """Get Cloud Gateway Pool

     Returns a resource representation of a cloud gateway pool with the specified ID.

    Args:
        cloud_gateway_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CloudGatewayPoolInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        cloud_gateway_pool_id=cloud_gateway_pool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_gateway_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[CloudGatewayPoolInfo, ProblemDetails]]:
    """Get Cloud Gateway Pool

     Returns a resource representation of a cloud gateway pool with the specified ID.

    Args:
        cloud_gateway_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CloudGatewayPoolInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            cloud_gateway_pool_id=cloud_gateway_pool_id,
            client=client,
        )
    ).parsed
