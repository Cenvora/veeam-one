from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cloud_gateway_info import CloudGatewayInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    cloud_gateway_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/cloudConnect/cloudGateways/{cloud_gateway_id}".format(
            cloud_gateway_id=quote(str(cloud_gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CloudGatewayInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = CloudGatewayInfo.from_dict(response.json())

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
) -> Response[CloudGatewayInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_gateway_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CloudGatewayInfo | ProblemDetails]:
    """Get Cloud Gateway

     Returns a resource representation of a cloud gateway with the specified ID.

    Args:
        cloud_gateway_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudGatewayInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        cloud_gateway_id=cloud_gateway_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cloud_gateway_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CloudGatewayInfo | ProblemDetails | None:
    """Get Cloud Gateway

     Returns a resource representation of a cloud gateway with the specified ID.

    Args:
        cloud_gateway_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudGatewayInfo | ProblemDetails
    """

    return sync_detailed(
        cloud_gateway_id=cloud_gateway_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    cloud_gateway_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[CloudGatewayInfo | ProblemDetails]:
    """Get Cloud Gateway

     Returns a resource representation of a cloud gateway with the specified ID.

    Args:
        cloud_gateway_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CloudGatewayInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        cloud_gateway_id=cloud_gateway_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_gateway_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> CloudGatewayInfo | ProblemDetails | None:
    """Get Cloud Gateway

     Returns a resource representation of a cloud gateway with the specified ID.

    Args:
        cloud_gateway_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CloudGatewayInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            cloud_gateway_id=cloud_gateway_id,
            client=client,
        )
    ).parsed
