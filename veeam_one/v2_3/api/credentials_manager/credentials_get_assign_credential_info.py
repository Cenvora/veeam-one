from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.guest_assign_info_credential_assign_info import GuestAssignInfoCredentialAssignInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/credentials/assign/servicenow",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GuestAssignInfoCredentialAssignInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = GuestAssignInfoCredentialAssignInfo.from_dict(response.json())

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
) -> Response[GuestAssignInfoCredentialAssignInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GuestAssignInfoCredentialAssignInfo | ProblemDetails]:
    """Get ServiceNow Credentials

     Returns a resource representation of the ServiceNow credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GuestAssignInfoCredentialAssignInfo | ProblemDetails]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> GuestAssignInfoCredentialAssignInfo | ProblemDetails | None:
    """Get ServiceNow Credentials

     Returns a resource representation of the ServiceNow credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GuestAssignInfoCredentialAssignInfo | ProblemDetails
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[GuestAssignInfoCredentialAssignInfo | ProblemDetails]:
    """Get ServiceNow Credentials

     Returns a resource representation of the ServiceNow credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GuestAssignInfoCredentialAssignInfo | ProblemDetails]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> GuestAssignInfoCredentialAssignInfo | ProblemDetails | None:
    """Get ServiceNow Credentials

     Returns a resource representation of the ServiceNow credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GuestAssignInfoCredentialAssignInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
