from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alarm_template_info import AlarmTemplateInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    alarm_template_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/alarms/templates/{alarm_template_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AlarmTemplateInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = AlarmTemplateInfo.from_dict(response.json())

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
) -> Response[Union[AlarmTemplateInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alarm_template_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AlarmTemplateInfo, ProblemDetails]]:
    """Get Alarm

     Returns a resource representation of an alarm with the specified ID.

    Args:
        alarm_template_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlarmTemplateInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        alarm_template_id=alarm_template_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alarm_template_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AlarmTemplateInfo, ProblemDetails]]:
    """Get Alarm

     Returns a resource representation of an alarm with the specified ID.

    Args:
        alarm_template_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlarmTemplateInfo, ProblemDetails]
    """

    return sync_detailed(
        alarm_template_id=alarm_template_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alarm_template_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[AlarmTemplateInfo, ProblemDetails]]:
    """Get Alarm

     Returns a resource representation of an alarm with the specified ID.

    Args:
        alarm_template_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AlarmTemplateInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        alarm_template_id=alarm_template_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alarm_template_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[AlarmTemplateInfo, ProblemDetails]]:
    """Get Alarm

     Returns a resource representation of an alarm with the specified ID.

    Args:
        alarm_template_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AlarmTemplateInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            alarm_template_id=alarm_template_id,
            client=client,
        )
    ).parsed
