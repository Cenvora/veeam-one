from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.application_info import ApplicationInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    application_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/applications/{application_id}".format(
            application_id=quote(str(application_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApplicationInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = ApplicationInfo.from_dict(response.json())

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
) -> Response[ApplicationInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApplicationInfo | ProblemDetails]:
    """Get Connected Application

     Returns a resource representation of a connected application with the specified ID.

    Args:
        application_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ApplicationInfo | ProblemDetails | None:
    """Get Connected Application

     Returns a resource representation of a connected application with the specified ID.

    Args:
        application_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationInfo | ProblemDetails
    """

    return sync_detailed(
        application_id=application_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ApplicationInfo | ProblemDetails]:
    """Get Connected Application

     Returns a resource representation of a connected application with the specified ID.

    Args:
        application_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApplicationInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ApplicationInfo | ProblemDetails | None:
    """Get Connected Application

     Returns a resource representation of a connected application with the specified ID.

    Args:
        application_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApplicationInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            application_id=application_id,
            client=client,
        )
    ).parsed
