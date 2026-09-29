from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vb_365_backup_proxy_info import Vb365BackupProxyInfo
from ...types import Response


def _get_kwargs(
    backup_proxy_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vb365/backupProxies/{backup_proxy_id}".format(
            backup_proxy_id=quote(str(backup_proxy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | Vb365BackupProxyInfo | None:
    if response.status_code == 200:
        response_200 = Vb365BackupProxyInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | Vb365BackupProxyInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_proxy_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365BackupProxyInfo]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Server

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy server with the
    specified ID.

    Args:
        backup_proxy_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365BackupProxyInfo]
    """

    kwargs = _get_kwargs(
        backup_proxy_id=backup_proxy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_proxy_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365BackupProxyInfo | None:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Server

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy server with the
    specified ID.

    Args:
        backup_proxy_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365BackupProxyInfo
    """

    return sync_detailed(
        backup_proxy_id=backup_proxy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    backup_proxy_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365BackupProxyInfo]:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Server

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy server with the
    specified ID.

    Args:
        backup_proxy_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365BackupProxyInfo]
    """

    kwargs = _get_kwargs(
        backup_proxy_id=backup_proxy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_proxy_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365BackupProxyInfo | None:
    """Get Veeam Backup for Microsoft 365 Backup Proxy Server

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup proxy server with the
    specified ID.

    Args:
        backup_proxy_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365BackupProxyInfo
    """

    return (
        await asyncio_detailed(
            backup_proxy_id=backup_proxy_id,
            client=client,
        )
    ).parsed
