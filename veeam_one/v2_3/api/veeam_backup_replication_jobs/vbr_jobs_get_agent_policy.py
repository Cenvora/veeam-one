from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_policy_info import AgentPolicyInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    agent_policy_uid: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vbrJobs/agentPolicies/{agent_policy_uid}".format(
            agent_policy_uid=quote(str(agent_policy_uid), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentPolicyInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = AgentPolicyInfo.from_dict(response.json())

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
) -> Response[AgentPolicyInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_policy_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AgentPolicyInfo | ProblemDetails]:
    """Get Veeam Backup Agent Policy

     Returns a resource representation of a Veeam backup agent policy with the specified UID.

    Args:
        agent_policy_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPolicyInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        agent_policy_uid=agent_policy_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_policy_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AgentPolicyInfo | ProblemDetails | None:
    """Get Veeam Backup Agent Policy

     Returns a resource representation of a Veeam backup agent policy with the specified UID.

    Args:
        agent_policy_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPolicyInfo | ProblemDetails
    """

    return sync_detailed(
        agent_policy_uid=agent_policy_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    agent_policy_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AgentPolicyInfo | ProblemDetails]:
    """Get Veeam Backup Agent Policy

     Returns a resource representation of a Veeam backup agent policy with the specified UID.

    Args:
        agent_policy_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPolicyInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        agent_policy_uid=agent_policy_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_policy_uid: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> AgentPolicyInfo | ProblemDetails | None:
    """Get Veeam Backup Agent Policy

     Returns a resource representation of a Veeam backup agent policy with the specified UID.

    Args:
        agent_policy_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPolicyInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            agent_policy_uid=agent_policy_uid,
            client=client,
        )
    ).parsed
