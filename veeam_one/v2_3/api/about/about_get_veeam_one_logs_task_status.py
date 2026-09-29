from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.async_task_status import AsyncTaskStatus
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    task_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2.3/about/logs/tasks/{task_id}/status".format(
            task_id=quote(str(task_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AsyncTaskStatus | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = AsyncTaskStatus.from_dict(response.json())

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
) -> Response[AsyncTaskStatus | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AsyncTaskStatus | ProblemDetails]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskStatus | ProblemDetails]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AsyncTaskStatus | ProblemDetails | None:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskStatus | ProblemDetails
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AsyncTaskStatus | ProblemDetails]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AsyncTaskStatus | ProblemDetails]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AsyncTaskStatus | ProblemDetails | None:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AsyncTaskStatus | ProblemDetails
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
        )
    ).parsed
