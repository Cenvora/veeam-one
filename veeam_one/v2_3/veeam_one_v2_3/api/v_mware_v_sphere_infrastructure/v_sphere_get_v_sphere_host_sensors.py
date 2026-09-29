from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_host_sensor_info_page import VSphereHostSensorInfoPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    host_id: int,
    *,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
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
        "url": f"/api/v2.3/vSphere/hosts/{host_id}/sensors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    if response.status_code == 200:
        response_200 = VSphereHostSensorInfoPage.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    """Get Hardware Sensors of Host

     Returns a collection resource representation of all hardware sensors of a VMware vSphere host with
    the specified ID.

    Args:
        host_id (int):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VSphereHostSensorInfoPage]]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
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
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    """Get Hardware Sensors of Host

     Returns a collection resource representation of all hardware sensors of a VMware vSphere host with
    the specified ID.

    Args:
        host_id (int):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VSphereHostSensorInfoPage]
    """

    return sync_detailed(
        host_id=host_id,
        client=client,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    ).parsed


async def asyncio_detailed(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Response[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    """Get Hardware Sensors of Host

     Returns a collection resource representation of all hardware sensors of a VMware vSphere host with
    the specified ID.

    Args:
        host_id (int):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VSphereHostSensorInfoPage]]
    """

    kwargs = _get_kwargs(
        host_id=host_id,
        offset=offset,
        limit=limit,
        filter_=filter_,
        sort=sort,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    host_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    filter_: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    select: Union[Unset, str] = UNSET,
) -> Optional[Union[ProblemDetails, VSphereHostSensorInfoPage]]:
    """Get Hardware Sensors of Host

     Returns a collection resource representation of all hardware sensors of a VMware vSphere host with
    the specified ID.

    Args:
        host_id (int):
        offset (Union[Unset, int]):  Default: 0.
        limit (Union[Unset, int]):  Default: 100.
        filter_ (Union[Unset, str]):
        sort (Union[Unset, str]):
        select (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VSphereHostSensorInfoPage]
    """

    return (
        await asyncio_detailed(
            host_id=host_id,
            client=client,
            offset=offset,
            limit=limit,
            filter_=filter_,
            sort=sort,
            select=select,
        )
    ).parsed
