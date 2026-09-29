from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.wan_accelerator_info import WanAcceleratorInfo
from ...types import Response


def _get_kwargs(
    wan_accelerator_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vbr/wanAccelerators/{wan_accelerator_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, WanAcceleratorInfo]]:
    if response.status_code == 200:
        response_200 = WanAcceleratorInfo.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, WanAcceleratorInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    wan_accelerator_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, WanAcceleratorInfo]]:
    """Get WAN Accelerator

     Returns a resource representation of a connected WAN accelerator with the specified ID.

    Args:
        wan_accelerator_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, WanAcceleratorInfo]]
    """

    kwargs = _get_kwargs(
        wan_accelerator_id=wan_accelerator_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    wan_accelerator_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, WanAcceleratorInfo]]:
    """Get WAN Accelerator

     Returns a resource representation of a connected WAN accelerator with the specified ID.

    Args:
        wan_accelerator_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, WanAcceleratorInfo]
    """

    return sync_detailed(
        wan_accelerator_id=wan_accelerator_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    wan_accelerator_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, WanAcceleratorInfo]]:
    """Get WAN Accelerator

     Returns a resource representation of a connected WAN accelerator with the specified ID.

    Args:
        wan_accelerator_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, WanAcceleratorInfo]]
    """

    kwargs = _get_kwargs(
        wan_accelerator_id=wan_accelerator_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    wan_accelerator_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, WanAcceleratorInfo]]:
    """Get WAN Accelerator

     Returns a resource representation of a connected WAN accelerator with the specified ID.

    Args:
        wan_accelerator_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, WanAcceleratorInfo]
    """

    return (
        await asyncio_detailed(
            wan_accelerator_id=wan_accelerator_id,
            client=client,
        )
    ).parsed
