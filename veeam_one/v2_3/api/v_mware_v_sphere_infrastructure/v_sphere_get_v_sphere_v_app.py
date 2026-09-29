from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_v_app_info import VSphereVAppInfo
from ...types import Response


def _get_kwargs(
    v_app_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/vApps/{v_app_id}".format(
            v_app_id=quote(str(v_app_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VSphereVAppInfo | None:
    if response.status_code == 200:
        response_200 = VSphereVAppInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VSphereVAppInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    v_app_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereVAppInfo]:
    """Get vApp

     Returns a resource representation of a vApp with the specified ID.

    Args:
        v_app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereVAppInfo]
    """

    kwargs = _get_kwargs(
        v_app_id=v_app_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    v_app_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereVAppInfo | None:
    """Get vApp

     Returns a resource representation of a vApp with the specified ID.

    Args:
        v_app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereVAppInfo
    """

    return sync_detailed(
        v_app_id=v_app_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    v_app_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereVAppInfo]:
    """Get vApp

     Returns a resource representation of a vApp with the specified ID.

    Args:
        v_app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereVAppInfo]
    """

    kwargs = _get_kwargs(
        v_app_id=v_app_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    v_app_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereVAppInfo | None:
    """Get vApp

     Returns a resource representation of a vApp with the specified ID.

    Args:
        v_app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereVAppInfo
    """

    return (
        await asyncio_detailed(
            v_app_id=v_app_id,
            client=client,
        )
    ).parsed
