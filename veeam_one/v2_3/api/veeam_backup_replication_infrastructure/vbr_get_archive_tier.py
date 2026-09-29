from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.archive_tier_extent_info import ArchiveTierExtentInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    extent_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/scaleoutRepositories/archiveTiers/{extent_uid}".format(
            extent_uid=quote(str(extent_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ArchiveTierExtentInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ArchiveTierExtentInfo.from_dict(response.json())

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
) -> Response[ArchiveTierExtentInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    extent_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ArchiveTierExtentInfo | ProblemDetails]:
    """Get Archive Tier Extent

     Returns a resource representation of an archive tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveTierExtentInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extent_uid=extent_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    extent_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ArchiveTierExtentInfo | ProblemDetails | None:
    """Get Archive Tier Extent

     Returns a resource representation of an archive tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveTierExtentInfo | ProblemDetails
    """

    return sync_detailed(
        extent_uid=extent_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    extent_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ArchiveTierExtentInfo | ProblemDetails]:
    """Get Archive Tier Extent

     Returns a resource representation of an archive tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ArchiveTierExtentInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        extent_uid=extent_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    extent_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> ArchiveTierExtentInfo | ProblemDetails | None:
    """Get Archive Tier Extent

     Returns a resource representation of an archive tier extent with the specified UID.

    Args:
        extent_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ArchiveTierExtentInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            extent_uid=extent_uid,
            client=client,
        )
    ).parsed
