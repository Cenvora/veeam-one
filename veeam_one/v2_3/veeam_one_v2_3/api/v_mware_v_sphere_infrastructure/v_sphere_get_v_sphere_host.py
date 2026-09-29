from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_host_info import VSphereHostInfo
from ...types import Response


def _get_kwargs(
    host_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vSphere/hosts/{host_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, VSphereHostInfo]]:
    if response.status_code == 200:
        response_200 = VSphereHostInfo.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, VSphereHostInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VSphereHostInfo]]:
    """Get VMware vSphere Host

     Returns a resource representation of a VMware vSphere host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VSphereHostInfo]]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VSphereHostInfo]]:
    """Get VMware vSphere Host

     Returns a resource representation of a VMware vSphere host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VSphereHostInfo]
    """

    return sync_detailed(
        host_id=host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VSphereHostInfo]]:
    """Get VMware vSphere Host

     Returns a resource representation of a VMware vSphere host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VSphereHostInfo]]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VSphereHostInfo]]:
    """Get VMware vSphere Host

     Returns a resource representation of a VMware vSphere host with the specified ID.

    Args:
        host_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VSphereHostInfo]
    """

    return (
        await asyncio_detailed(
            host_id=host_id,
            client=client,
        )
    ).parsed
