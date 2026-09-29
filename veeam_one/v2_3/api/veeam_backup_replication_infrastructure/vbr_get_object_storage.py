from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.object_storage_info import ObjectStorageInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    object_storage_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/repositories/objectStorages/{object_storage_id}".format(
            object_storage_id=quote(str(object_storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ObjectStorageInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ObjectStorageInfo.from_dict(response.json())

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
) -> Response[ObjectStorageInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_storage_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorageInfo | ProblemDetails]:
    """Get Object Storage Repository

     Returns a resource representation of an object storage repository with the specified ID.

    Args:
        object_storage_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorageInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_storage_id=object_storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_storage_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorageInfo | ProblemDetails | None:
    """Get Object Storage Repository

     Returns a resource representation of an object storage repository with the specified ID.

    Args:
        object_storage_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorageInfo | ProblemDetails
    """

    return sync_detailed(
        object_storage_id=object_storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_storage_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ObjectStorageInfo | ProblemDetails]:
    """Get Object Storage Repository

     Returns a resource representation of an object storage repository with the specified ID.

    Args:
        object_storage_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ObjectStorageInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_storage_id=object_storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_storage_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ObjectStorageInfo | ProblemDetails | None:
    """Get Object Storage Repository

     Returns a resource representation of an object storage repository with the specified ID.

    Args:
        object_storage_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ObjectStorageInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            object_storage_id=object_storage_id,
            client=client,
        )
    ).parsed
