from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.protected_application_info import ProtectedApplicationInfo
from ...types import Response


def _get_kwargs(
    application_uid_in_vbr: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/protectedData/applications/{application_uid_in_vbr}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, ProtectedApplicationInfo]]:
    if response.status_code == 200:
        response_200 = ProtectedApplicationInfo.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProblemDetails, ProtectedApplicationInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_uid_in_vbr: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, ProtectedApplicationInfo]]:
    """Get Protected Application

     Returns a resource representation of a protected application with the specified UID.

    Args:
        application_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, ProtectedApplicationInfo]]
    """

    kwargs = _get_kwargs(
        application_uid_in_vbr=application_uid_in_vbr,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    application_uid_in_vbr: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, ProtectedApplicationInfo]]:
    """Get Protected Application

     Returns a resource representation of a protected application with the specified UID.

    Args:
        application_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, ProtectedApplicationInfo]
    """

    return sync_detailed(
        application_uid_in_vbr=application_uid_in_vbr,
        client=client,
    ).parsed


async def asyncio_detailed(
    application_uid_in_vbr: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, ProtectedApplicationInfo]]:
    """Get Protected Application

     Returns a resource representation of a protected application with the specified UID.

    Args:
        application_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, ProtectedApplicationInfo]]
    """

    kwargs = _get_kwargs(
        application_uid_in_vbr=application_uid_in_vbr,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_uid_in_vbr: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, ProtectedApplicationInfo]]:
    """Get Protected Application

     Returns a resource representation of a protected application with the specified UID.

    Args:
        application_uid_in_vbr (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, ProtectedApplicationInfo]
    """

    return (
        await asyncio_detailed(
            application_uid_in_vbr=application_uid_in_vbr,
            client=client,
        )
    ).parsed
