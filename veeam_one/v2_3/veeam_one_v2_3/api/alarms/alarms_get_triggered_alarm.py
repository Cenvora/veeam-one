from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.triggered_alarm_info_2 import TriggeredAlarmInfo2
from ...types import Response


def _get_kwargs(
    triggered_alarm_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/alarms/triggeredAlarms/{triggered_alarm_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    if response.status_code == 200:
        response_200 = TriggeredAlarmInfo2.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    triggered_alarm_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    """Get Triggered Alarm

     Returns a resource representation of a triggered alarm with the specified ID.

    Args:
        triggered_alarm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, TriggeredAlarmInfo2]]
    """

    kwargs = _get_kwargs(
        triggered_alarm_id=triggered_alarm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    triggered_alarm_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    """Get Triggered Alarm

     Returns a resource representation of a triggered alarm with the specified ID.

    Args:
        triggered_alarm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, TriggeredAlarmInfo2]
    """

    return sync_detailed(
        triggered_alarm_id=triggered_alarm_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    triggered_alarm_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    """Get Triggered Alarm

     Returns a resource representation of a triggered alarm with the specified ID.

    Args:
        triggered_alarm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, TriggeredAlarmInfo2]]
    """

    kwargs = _get_kwargs(
        triggered_alarm_id=triggered_alarm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    triggered_alarm_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, TriggeredAlarmInfo2]]:
    """Get Triggered Alarm

     Returns a resource representation of a triggered alarm with the specified ID.

    Args:
        triggered_alarm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, TriggeredAlarmInfo2]
    """

    return (
        await asyncio_detailed(
            triggered_alarm_id=triggered_alarm_id,
            client=client,
        )
    ).parsed
