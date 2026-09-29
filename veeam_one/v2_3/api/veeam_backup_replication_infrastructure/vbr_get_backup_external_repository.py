from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.external_repository_info import ExternalRepositoryInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    external_repository_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/repositories/external/{external_repository_id}".format(
            external_repository_id=quote(str(external_repository_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExternalRepositoryInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ExternalRepositoryInfo.from_dict(response.json())

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
) -> Response[ExternalRepositoryInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExternalRepositoryInfo | ProblemDetails]:
    """Get External Backup Repository

     Returns a resource representation of an external backup repository with the specified ID.

    Args:
        external_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalRepositoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        external_repository_id=external_repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ExternalRepositoryInfo | ProblemDetails | None:
    """Get External Backup Repository

     Returns a resource representation of an external backup repository with the specified ID.

    Args:
        external_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalRepositoryInfo | ProblemDetails
    """

    return sync_detailed(
        external_repository_id=external_repository_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExternalRepositoryInfo | ProblemDetails]:
    """Get External Backup Repository

     Returns a resource representation of an external backup repository with the specified ID.

    Args:
        external_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExternalRepositoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        external_repository_id=external_repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ExternalRepositoryInfo | ProblemDetails | None:
    """Get External Backup Repository

     Returns a resource representation of an external backup repository with the specified ID.

    Args:
        external_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExternalRepositoryInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            external_repository_id=external_repository_id,
            client=client,
        )
    ).parsed
