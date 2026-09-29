from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_cluster_info import BackupClusterInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    backup_cluster_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/backupClusters/{backup_cluster_id}".format(
            backup_cluster_id=quote(str(backup_cluster_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupClusterInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BackupClusterInfo.from_dict(response.json())

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
) -> Response[BackupClusterInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BackupClusterInfo | ProblemDetails]:
    """Get High Availability Cluster

     Returns a resource representation of a connected High Availability cluster with the specified ID.

    Args:
        backup_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupClusterInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        backup_cluster_id=backup_cluster_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BackupClusterInfo | ProblemDetails | None:
    """Get High Availability Cluster

     Returns a resource representation of a connected High Availability cluster with the specified ID.

    Args:
        backup_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupClusterInfo | ProblemDetails
    """

    return sync_detailed(
        backup_cluster_id=backup_cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    backup_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BackupClusterInfo | ProblemDetails]:
    """Get High Availability Cluster

     Returns a resource representation of a connected High Availability cluster with the specified ID.

    Args:
        backup_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupClusterInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        backup_cluster_id=backup_cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BackupClusterInfo | ProblemDetails | None:
    """Get High Availability Cluster

     Returns a resource representation of a connected High Availability cluster with the specified ID.

    Args:
        backup_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupClusterInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            backup_cluster_id=backup_cluster_id,
            client=client,
        )
    ).parsed
