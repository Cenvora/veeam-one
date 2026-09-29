from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.protected_cloud_network_backup_info_page import ProtectedCloudNetworkBackupInfoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    cloud_network_uid_in_vbr: UUID,
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
        "url": "/api/v2.3/protectedData/publicCloud/networks/{cloud_network_uid_in_vbr}/backups".format(
            cloud_network_uid_in_vbr=quote(str(cloud_network_uid_in_vbr), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | ProtectedCloudNetworkBackupInfoPage | None:
    if response.status_code == 200:
        response_200 = ProtectedCloudNetworkBackupInfoPage.from_dict(response.json())

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
) -> Response[ProblemDetails | ProtectedCloudNetworkBackupInfoPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cloud_network_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[ProblemDetails | ProtectedCloudNetworkBackupInfoPage]:
    """Get Backups of Cloud Network

     Returns a collection resource representation of all backups of a protected cloud network with the
    specified UID.

    Args:
        cloud_network_uid_in_vbr (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedCloudNetworkBackupInfoPage]
    """

    kwargs = _get_kwargs(
        cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
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
    cloud_network_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> ProblemDetails | ProtectedCloudNetworkBackupInfoPage | None:
    """Get Backups of Cloud Network

     Returns a collection resource representation of all backups of a protected cloud network with the
    specified UID.

    Args:
        cloud_network_uid_in_vbr (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedCloudNetworkBackupInfoPage
    """

    return sync_detailed(
        cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    ).parsed


async def asyncio_detailed(
    cloud_network_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> Response[ProblemDetails | ProtectedCloudNetworkBackupInfoPage]:
    """Get Backups of Cloud Network

     Returns a collection resource representation of all backups of a protected cloud network with the
    specified UID.

    Args:
        cloud_network_uid_in_vbr (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedCloudNetworkBackupInfoPage]
    """

    kwargs = _get_kwargs(
        cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cloud_network_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
    offset: int | Unset = 0,
    limit: int | Unset = 100,
    filter_: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    select: str | Unset = UNSET,
) -> ProblemDetails | ProtectedCloudNetworkBackupInfoPage | None:
    """Get Backups of Cloud Network

     Returns a collection resource representation of all backups of a protected cloud network with the
    specified UID.

    Args:
        cloud_network_uid_in_vbr (UUID):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 100.
        filter_ (str | Unset):
        sort (str | Unset):
        select (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedCloudNetworkBackupInfoPage
    """

    return (
        await asyncio_detailed(
            cloud_network_uid_in_vbr=cloud_network_uid_in_vbr,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
            sort=sort,
            select=select,
        )
    ).parsed
