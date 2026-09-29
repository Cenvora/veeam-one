from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vb_365_copy_job import Vb365CopyJob
from ...types import Response


def _get_kwargs(
    copy_job_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vb365Jobs/copyJobs/{copy_job_uid}".format(
            copy_job_uid=quote(str(copy_job_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | Vb365CopyJob | None:
    if response.status_code == 200:
        response_200 = Vb365CopyJob.from_dict(response.json())

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
) -> Response[ProblemDetails | Vb365CopyJob]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365CopyJob]:
    """Get Veeam Backup for Microsoft 365 Backup Copy Job

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup copy job with the
    specified UID.

    Args:
        copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365CopyJob]
    """

    kwargs = _get_kwargs(
        copy_job_uid=copy_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365CopyJob | None:
    """Get Veeam Backup for Microsoft 365 Backup Copy Job

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup copy job with the
    specified UID.

    Args:
        copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365CopyJob
    """

    return sync_detailed(
        copy_job_uid=copy_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | Vb365CopyJob]:
    """Get Veeam Backup for Microsoft 365 Backup Copy Job

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup copy job with the
    specified UID.

    Args:
        copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | Vb365CopyJob]
    """

    kwargs = _get_kwargs(
        copy_job_uid=copy_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | Vb365CopyJob | None:
    """Get Veeam Backup for Microsoft 365 Backup Copy Job

     Returns a resource representation of a Veeam Backup for Microsoft 365 backup copy job with the
    specified UID.

    Args:
        copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | Vb365CopyJob
    """

    return (
        await asyncio_detailed(
            copy_job_uid=copy_job_uid,
            client=client,
        )
    ).parsed
