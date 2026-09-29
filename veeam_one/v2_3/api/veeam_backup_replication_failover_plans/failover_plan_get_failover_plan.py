from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.failover_plan_info import FailoverPlanInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    failover_plan_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbr/failoverPlans/{failover_plan_uid}".format(
            failover_plan_uid=quote(str(failover_plan_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> FailoverPlanInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = FailoverPlanInfo.from_dict(response.json())

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
) -> Response[FailoverPlanInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    failover_plan_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FailoverPlanInfo | ProblemDetails]:
    """Get Failover Plan

     Returns a resource representation of a failover plan with the specified UID.

    Args:
        failover_plan_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailoverPlanInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        failover_plan_uid=failover_plan_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    failover_plan_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FailoverPlanInfo | ProblemDetails | None:
    """Get Failover Plan

     Returns a resource representation of a failover plan with the specified UID.

    Args:
        failover_plan_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailoverPlanInfo | ProblemDetails
    """

    return sync_detailed(
        failover_plan_uid=failover_plan_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    failover_plan_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[FailoverPlanInfo | ProblemDetails]:
    """Get Failover Plan

     Returns a resource representation of a failover plan with the specified UID.

    Args:
        failover_plan_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FailoverPlanInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        failover_plan_uid=failover_plan_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    failover_plan_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> FailoverPlanInfo | ProblemDetails | None:
    """Get Failover Plan

     Returns a resource representation of a failover plan with the specified UID.

    Args:
        failover_plan_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FailoverPlanInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            failover_plan_uid=failover_plan_uid,
            client=client,
        )
    ).parsed
