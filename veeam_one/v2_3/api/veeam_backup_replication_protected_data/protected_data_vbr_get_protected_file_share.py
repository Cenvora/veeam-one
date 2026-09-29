from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.protected_file_share_info import ProtectedFileShareInfo
from ...types import Response


def _get_kwargs(
    file_share_uid_in_vbr: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/protectedData/unstructuredData/fileShares/{file_share_uid_in_vbr}".format(
            file_share_uid_in_vbr=quote(str(file_share_uid_in_vbr), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | ProtectedFileShareInfo | None:
    if response.status_code == 200:
        response_200 = ProtectedFileShareInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | ProtectedFileShareInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_share_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProtectedFileShareInfo]:
    """Get Protected File Share

     Returns a resource representation of a protected file share with the specified UID.

    Args:
        file_share_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedFileShareInfo]
    """

    kwargs = _get_kwargs(
        file_share_uid_in_vbr=file_share_uid_in_vbr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_share_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProtectedFileShareInfo | None:
    """Get Protected File Share

     Returns a resource representation of a protected file share with the specified UID.

    Args:
        file_share_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedFileShareInfo
    """

    return sync_detailed(
        file_share_uid_in_vbr=file_share_uid_in_vbr,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_share_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProtectedFileShareInfo]:
    """Get Protected File Share

     Returns a resource representation of a protected file share with the specified UID.

    Args:
        file_share_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedFileShareInfo]
    """

    kwargs = _get_kwargs(
        file_share_uid_in_vbr=file_share_uid_in_vbr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_share_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProtectedFileShareInfo | None:
    """Get Protected File Share

     Returns a resource representation of a protected file share with the specified UID.

    Args:
        file_share_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedFileShareInfo
    """

    return (
        await asyncio_detailed(
            file_share_uid_in_vbr=file_share_uid_in_vbr,
            client=client,
        )
    ).parsed
