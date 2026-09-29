from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hyper_v_sc_vmm_server_info import HyperVScVmmServerInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    scvmm_server_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/hyperV/scVmmServers/{scvmm_server_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = HyperVScVmmServerInfo.from_dict(response.json())

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
) -> Response[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scvmm_server_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V SCVMM Server

     Returns a resource representation of a connected Microsoft Hyper-V SCVMM server with the specified
    ID.

    Args:
        scvmm_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HyperVScVmmServerInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        scvmm_server_id=scvmm_server_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scvmm_server_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V SCVMM Server

     Returns a resource representation of a connected Microsoft Hyper-V SCVMM server with the specified
    ID.

    Args:
        scvmm_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HyperVScVmmServerInfo, ProblemDetails]
    """

    return sync_detailed(
        scvmm_server_id=scvmm_server_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scvmm_server_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V SCVMM Server

     Returns a resource representation of a connected Microsoft Hyper-V SCVMM server with the specified
    ID.

    Args:
        scvmm_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HyperVScVmmServerInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        scvmm_server_id=scvmm_server_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scvmm_server_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HyperVScVmmServerInfo, ProblemDetails]]:
    """Get Microsoft Hyper-V SCVMM Server

     Returns a resource representation of a connected Microsoft Hyper-V SCVMM server with the specified
    ID.

    Args:
        scvmm_server_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HyperVScVmmServerInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            scvmm_server_id=scvmm_server_id,
            client=client,
        )
    ).parsed
