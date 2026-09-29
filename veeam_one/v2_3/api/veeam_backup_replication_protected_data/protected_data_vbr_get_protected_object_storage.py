from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.protected_object_storage_info import ProtectedObjectStorageInfo
from ...types import Response


def _get_kwargs(
    object_storage_uid_in_vbr: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/protectedData/unstructuredData/objectStorages/{object_storage_uid_in_vbr}".format(
            object_storage_uid_in_vbr=quote(str(object_storage_uid_in_vbr), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | ProtectedObjectStorageInfo | None:
    if response.status_code == 200:
        response_200 = ProtectedObjectStorageInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | ProtectedObjectStorageInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_storage_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProtectedObjectStorageInfo]:
    """Get Protected Object Storage

     Returns a resource representation of a protected object storage with the specified UID.

    Args:
        object_storage_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedObjectStorageInfo]
    """

    kwargs = _get_kwargs(
        object_storage_uid_in_vbr=object_storage_uid_in_vbr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_storage_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProtectedObjectStorageInfo | None:
    """Get Protected Object Storage

     Returns a resource representation of a protected object storage with the specified UID.

    Args:
        object_storage_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedObjectStorageInfo
    """

    return sync_detailed(
        object_storage_uid_in_vbr=object_storage_uid_in_vbr,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_storage_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProtectedObjectStorageInfo]:
    """Get Protected Object Storage

     Returns a resource representation of a protected object storage with the specified UID.

    Args:
        object_storage_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProtectedObjectStorageInfo]
    """

    kwargs = _get_kwargs(
        object_storage_uid_in_vbr=object_storage_uid_in_vbr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_storage_uid_in_vbr: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProtectedObjectStorageInfo | None:
    """Get Protected Object Storage

     Returns a resource representation of a protected object storage with the specified UID.

    Args:
        object_storage_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProtectedObjectStorageInfo
    """

    return (
        await asyncio_detailed(
            object_storage_uid_in_vbr=object_storage_uid_in_vbr,
            client=client,
        )
    ).parsed
