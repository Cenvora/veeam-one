from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.file_copy_job_info import FileCopyJobInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    file_copy_job_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbrJobs/fileCopyJobs/{file_copy_job_uid}".format(
            file_copy_job_uid=quote(str(file_copy_job_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FileCopyJobInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = FileCopyJobInfo.from_dict(response.json())

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
) -> Response[FileCopyJobInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileCopyJobInfo | ProblemDetails]:
    """Get File Copy Job

     Returns a resource representation of a file copy job with the specified UID.

    Args:
        file_copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileCopyJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_copy_job_uid=file_copy_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FileCopyJobInfo | ProblemDetails | None:
    """Get File Copy Job

     Returns a resource representation of a file copy job with the specified UID.

    Args:
        file_copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileCopyJobInfo | ProblemDetails
    """

    return sync_detailed(
        file_copy_job_uid=file_copy_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FileCopyJobInfo | ProblemDetails]:
    """Get File Copy Job

     Returns a resource representation of a file copy job with the specified UID.

    Args:
        file_copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FileCopyJobInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        file_copy_job_uid=file_copy_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FileCopyJobInfo | ProblemDetails | None:
    """Get File Copy Job

     Returns a resource representation of a file copy job with the specified UID.

    Args:
        file_copy_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FileCopyJobInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            file_copy_job_uid=file_copy_job_uid,
            client=client,
        )
    ).parsed
