from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.scaleout_repository_info import ScaleoutRepositoryInfo
from ...types import Response


def _get_kwargs(
    scaleout_repository_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/scaleoutRepositories/{scaleout_repository_id}".format(
            scaleout_repository_id=quote(str(scaleout_repository_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | ScaleoutRepositoryInfo | None:
    if response.status_code == 200:
        response_200 = ScaleoutRepositoryInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | ScaleoutRepositoryInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    scaleout_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ScaleoutRepositoryInfo]:
    """Get Scale-Out Repository

     Returns a resource representation of a scale-out repository with the specified ID.

    Args:
        scaleout_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ScaleoutRepositoryInfo]
    """

    kwargs = _get_kwargs(
        scaleout_repository_id=scaleout_repository_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    scaleout_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ScaleoutRepositoryInfo | None:
    """Get Scale-Out Repository

     Returns a resource representation of a scale-out repository with the specified ID.

    Args:
        scaleout_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ScaleoutRepositoryInfo
    """

    return sync_detailed(
        scaleout_repository_id=scaleout_repository_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    scaleout_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ScaleoutRepositoryInfo]:
    """Get Scale-Out Repository

     Returns a resource representation of a scale-out repository with the specified ID.

    Args:
        scaleout_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ScaleoutRepositoryInfo]
    """

    kwargs = _get_kwargs(
        scaleout_repository_id=scaleout_repository_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    scaleout_repository_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ScaleoutRepositoryInfo | None:
    """Get Scale-Out Repository

     Returns a resource representation of a scale-out repository with the specified ID.

    Args:
        scaleout_repository_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ScaleoutRepositoryInfo
    """

    return (
        await asyncio_detailed(
            scaleout_repository_id=scaleout_repository_id,
            client=client,
        )
    ).parsed
