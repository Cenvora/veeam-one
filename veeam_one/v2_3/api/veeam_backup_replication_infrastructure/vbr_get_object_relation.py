from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vbr_object_relations_info import VbrObjectRelationsInfo
from ...types import Response


def _get_kwargs(
    object_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/objectRelations/{object_id}".format(
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VbrObjectRelationsInfo | None:
    if response.status_code == 200:
        response_200 = VbrObjectRelationsInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VbrObjectRelationsInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VbrObjectRelationsInfo]:
    """Get Relations of Infrastructure Object

     Returns a resource representation of a Veeam Backup & Replication infrastructure object with the
    specified ID and its relations.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VbrObjectRelationsInfo]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VbrObjectRelationsInfo | None:
    """Get Relations of Infrastructure Object

     Returns a resource representation of a Veeam Backup & Replication infrastructure object with the
    specified ID and its relations.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VbrObjectRelationsInfo
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VbrObjectRelationsInfo]:
    """Get Relations of Infrastructure Object

     Returns a resource representation of a Veeam Backup & Replication infrastructure object with the
    specified ID and its relations.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VbrObjectRelationsInfo]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VbrObjectRelationsInfo | None:
    """Get Relations of Infrastructure Object

     Returns a resource representation of a Veeam Backup & Replication infrastructure object with the
    specified ID and its relations.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VbrObjectRelationsInfo
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
        )
    ).parsed
