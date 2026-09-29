from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_repository_info import BackupRepositoryInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    repository_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/repositories/{repository_id}".format(
            repository_id=quote(str(repository_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupRepositoryInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BackupRepositoryInfo.from_dict(response.json())

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
) -> Response[BackupRepositoryInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BackupRepositoryInfo | ProblemDetails]:
    """Get Backup Repository

     Returns a resource representation of a backup repository with the specified ID. Does not return
    object storage repositories.

    Args:
        repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupRepositoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BackupRepositoryInfo | ProblemDetails | None:
    """Get Backup Repository

     Returns a resource representation of a backup repository with the specified ID. Does not return
    object storage repositories.

    Args:
        repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupRepositoryInfo | ProblemDetails
    """

    return sync_detailed(
        repository_id=repository_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BackupRepositoryInfo | ProblemDetails]:
    """Get Backup Repository

     Returns a resource representation of a backup repository with the specified ID. Does not return
    object storage repositories.

    Args:
        repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupRepositoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        repository_id=repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BackupRepositoryInfo | ProblemDetails | None:
    """Get Backup Repository

     Returns a resource representation of a backup repository with the specified ID. Does not return
    object storage repositories.

    Args:
        repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupRepositoryInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            repository_id=repository_id,
            client=client,
        )
    ).parsed
