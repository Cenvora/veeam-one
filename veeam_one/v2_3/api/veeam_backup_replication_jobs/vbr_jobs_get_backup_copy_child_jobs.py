from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.backup_copy_child_job_info_page import BackupCopyChildJobInfoPage
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    backup_copy_job_uid: UUID,
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["Offset"] = offset

    params["Limit"] = limit

    params["Filter"] = filter_

    params["Sort"] = sort

    params["Select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbrJobs/backupCopyJobs/{backup_copy_job_uid}/childJobs".format(
            backup_copy_job_uid=quote(str(backup_copy_job_uid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BackupCopyChildJobInfoPage | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BackupCopyChildJobInfoPage.from_dict(response.json())

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
) -> Response[BackupCopyChildJobInfoPage | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    backup_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[BackupCopyChildJobInfoPage | ProblemDetails]:
    """Get All Child Jobs of Backup Copy Job

     Returns a collection resource representation of all child jobs of a backup copy job with the
    specified UID.

    Args:
        backup_copy_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupCopyChildJobInfoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        backup_copy_job_uid=backup_copy_job_uid,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    backup_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> BackupCopyChildJobInfoPage | ProblemDetails | None:
    """Get All Child Jobs of Backup Copy Job

     Returns a collection resource representation of all child jobs of a backup copy job with the
    specified UID.

    Args:
        backup_copy_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupCopyChildJobInfoPage | ProblemDetails
    """

    return sync_detailed(
        backup_copy_job_uid=backup_copy_job_uid,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    ).parsed


async def asyncio_detailed(
    backup_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[BackupCopyChildJobInfoPage | ProblemDetails]:
    """Get All Child Jobs of Backup Copy Job

     Returns a collection resource representation of all child jobs of a backup copy job with the
    specified UID.

    Args:
        backup_copy_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BackupCopyChildJobInfoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        backup_copy_job_uid=backup_copy_job_uid,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    backup_copy_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> BackupCopyChildJobInfoPage | ProblemDetails | None:
    """Get All Child Jobs of Backup Copy Job

     Returns a collection resource representation of all child jobs of a backup copy job with the
    specified UID.

    Args:
        backup_copy_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BackupCopyChildJobInfoPage | ProblemDetails
    """

    return (
        await asyncio_detailed(
            backup_copy_job_uid=backup_copy_job_uid,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
            sort=sort,
            select=select,
        )
    ).parsed
