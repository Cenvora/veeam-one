from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_backup_job_info import ApplicationBackupJobInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    application_backup_job_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbrJobs/applicationBackupJobs/{application_backup_job_uid}".format(
            application_backup_job_uid=quote(str(application_backup_job_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplicationBackupJobInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ApplicationBackupJobInfo.from_dict(response.json())

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
) -> Response[ApplicationBackupJobInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_backup_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApplicationBackupJobInfo | ProblemDetails]:
    """Get Application Backup Job

     Returns a resource representation of an application backup job with the specified UID.

    Args:
        application_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationBackupJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_backup_job_uid=application_backup_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_backup_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApplicationBackupJobInfo | ProblemDetails | None:
    """Get Application Backup Job

     Returns a resource representation of an application backup job with the specified UID.

    Args:
        application_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationBackupJobInfo | ProblemDetails
    """

    return sync_detailed(
        application_backup_job_uid=application_backup_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_backup_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApplicationBackupJobInfo | ProblemDetails]:
    """Get Application Backup Job

     Returns a resource representation of an application backup job with the specified UID.

    Args:
        application_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationBackupJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_backup_job_uid=application_backup_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_backup_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ApplicationBackupJobInfo | ProblemDetails | None:
    """Get Application Backup Job

     Returns a resource representation of an application backup job with the specified UID.

    Args:
        application_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationBackupJobInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            application_backup_job_uid=application_backup_job_uid,
            client=client,
        )
    ).parsed
