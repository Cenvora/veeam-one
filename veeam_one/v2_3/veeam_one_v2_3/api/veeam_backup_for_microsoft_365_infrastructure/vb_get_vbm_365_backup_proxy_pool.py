from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vb_365_backup_proxy_pool_info import Vb365BackupProxyPoolInfo
from ...types import Response


def _get_kwargs(
    backup_proxy_pool_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vb365/backupProxyPools/{backup_proxy_pool_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    if response.status_code == 200:
        response_200 = Vb365BackupProxyPoolInfo.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_proxy_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Pool

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy pool with the
    specified ID.

    Args:
        backup_proxy_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]
    """

    kwargs = _get_kwargs(
        backup_proxy_pool_id=backup_proxy_pool_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_proxy_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Pool

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy pool with the
    specified ID.

    Args:
        backup_proxy_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, Vb365BackupProxyPoolInfo]
    """

    return sync_detailed(
        backup_proxy_pool_id=backup_proxy_pool_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    backup_proxy_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Pool

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy pool with the
    specified ID.

    Args:
        backup_proxy_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]
    """

    kwargs = _get_kwargs(
        backup_proxy_pool_id=backup_proxy_pool_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_proxy_pool_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, Vb365BackupProxyPoolInfo]]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Pool

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy pool with the
    specified ID.

    Args:
        backup_proxy_pool_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, Vb365BackupProxyPoolInfo]
    """

    return (
        await asyncio_detailed(
            backup_proxy_pool_id=backup_proxy_pool_id,
            client=client,
        )
    ).parsed
