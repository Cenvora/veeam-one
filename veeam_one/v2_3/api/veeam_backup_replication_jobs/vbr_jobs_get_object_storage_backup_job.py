from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.object_storage_backup_job_info import ObjectStorageBackupJobInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    object_storage_job_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbrJobs/objectStorageBackupJobs/{object_storage_job_uid}".format(
            object_storage_job_uid=quote(str(object_storage_job_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorageBackupJobInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ObjectStorageBackupJobInfo.from_dict(response.json())

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
) -> Response[ObjectStorageBackupJobInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_storage_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorageBackupJobInfo | ProblemDetails]:
    """Get Object Storage Job

     Returns a resource representation of an object storage job with the specified UID.

    Args:
        object_storage_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorageBackupJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_storage_job_uid=object_storage_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_storage_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorageBackupJobInfo | ProblemDetails | None:
    """Get Object Storage Job

     Returns a resource representation of an object storage job with the specified UID.

    Args:
        object_storage_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorageBackupJobInfo | ProblemDetails
    """

    return sync_detailed(
        object_storage_job_uid=object_storage_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_storage_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorageBackupJobInfo | ProblemDetails]:
    """Get Object Storage Job

     Returns a resource representation of an object storage job with the specified UID.

    Args:
        object_storage_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorageBackupJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_storage_job_uid=object_storage_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_storage_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorageBackupJobInfo | ProblemDetails | None:
    """Get Object Storage Job

     Returns a resource representation of an object storage job with the specified UID.

    Args:
        object_storage_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorageBackupJobInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            object_storage_job_uid=object_storage_job_uid,
            client=client,
        )
    ).parsed
