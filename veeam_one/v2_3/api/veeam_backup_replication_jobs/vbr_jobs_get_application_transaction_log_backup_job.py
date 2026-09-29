from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_transaction_log_backup_job_info_page import ApplicationTransactionLogBackupJobInfoPage
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    application_job_uid: UUID,
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
        "url": "/api/v2.3/vbrJobs/applicationBackupJobs/{application_job_uid}/logJobs".format(
            application_job_uid=quote(str(application_job_uid), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplicationTransactionLogBackupJobInfoPage | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ApplicationTransactionLogBackupJobInfoPage.from_dict(response.json())

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
) -> Response[ApplicationTransactionLogBackupJobInfoPage | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[ApplicationTransactionLogBackupJobInfoPage | ProblemDetails]:
    """Get Application Transaction Log Backup Job

     Returns a resource representation of a transaction log backup job initiated by an application backup
    job with the specified UID.

    Args:
        application_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationTransactionLogBackupJobInfoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_job_uid=application_job_uid,
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
    application_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> ApplicationTransactionLogBackupJobInfoPage | ProblemDetails | None:
    """Get Application Transaction Log Backup Job

     Returns a resource representation of a transaction log backup job initiated by an application backup
    job with the specified UID.

    Args:
        application_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationTransactionLogBackupJobInfoPage | ProblemDetails
    """

    return sync_detailed(
        application_job_uid=application_job_uid,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    ).parsed


async def asyncio_detailed(
    application_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[ApplicationTransactionLogBackupJobInfoPage | ProblemDetails]:
    """Get Application Transaction Log Backup Job

     Returns a resource representation of a transaction log backup job initiated by an application backup
    job with the specified UID.

    Args:
        application_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationTransactionLogBackupJobInfoPage | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_job_uid=application_job_uid,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_job_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> ApplicationTransactionLogBackupJobInfoPage | ProblemDetails | None:
    """Get Application Transaction Log Backup Job

     Returns a resource representation of a transaction log backup job initiated by an application backup
    job with the specified UID.

    Args:
        application_job_uid (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationTransactionLogBackupJobInfoPage | ProblemDetails
    """

    return (
        await asyncio_detailed(
            application_job_uid=application_job_uid,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
            sort=sort,
            select=select,
        )
    ).parsed
