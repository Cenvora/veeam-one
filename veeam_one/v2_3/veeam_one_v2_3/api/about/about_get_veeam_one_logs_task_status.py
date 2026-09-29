from http import HTTPStatus
from typing import Any, Optional, Union
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
        "url": f"/api/v2.3/about/logs/tasks/{task_id}/status",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AsyncTaskStatus, ProblemDetails]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AsyncTaskStatus, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AsyncTaskStatus, ProblemDetails]]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AsyncTaskStatus, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AsyncTaskStatus, ProblemDetails]]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AsyncTaskStatus, ProblemDetails]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    task_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AsyncTaskStatus, ProblemDetails]]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AsyncTaskStatus, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AsyncTaskStatus, ProblemDetails]]:
    """Get Log Archive Collection Task

     Returns a resource representation of status and result of a log archive collection task with the
    specified ID.

    Args:
        task_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AsyncTaskStatus, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
        )
    ).parsed
