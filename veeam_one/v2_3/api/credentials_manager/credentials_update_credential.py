from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.credential_info import CredentialInfo
from ...models.credential_save_request import CredentialSaveRequest
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    credential_id: int,
    *,
    body: CredentialSaveRequest | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2.3/credentials/{credential_id}".format(
            credential_id=quote(str(credential_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CredentialInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = CredentialInfo.from_dict(response.json())

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
) -> Response[CredentialInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credential_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialSaveRequest | Unset = UNSET,
) -> Response[CredentialInfo | ProblemDetails]:
    """Patch Credentials

     Modifies a credential set with the specified ID.

    Args:
        credential_id (int):
        body (CredentialSaveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    credential_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialSaveRequest | Unset = UNSET,
) -> CredentialInfo | ProblemDetails | None:
    """Patch Credentials

     Modifies a credential set with the specified ID.

    Args:
        credential_id (int):
        body (CredentialSaveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialInfo | ProblemDetails
    """

    return sync_detailed(
        credential_id=credential_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    credential_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialSaveRequest | Unset = UNSET,
) -> Response[CredentialInfo | ProblemDetails]:
    """Patch Credentials

     Modifies a credential set with the specified ID.

    Args:
        credential_id (int):
        body (CredentialSaveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CredentialInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        credential_id=credential_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    credential_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CredentialSaveRequest | Unset = UNSET,
) -> CredentialInfo | ProblemDetails | None:
    """Patch Credentials

     Modifies a credential set with the specified ID.

    Args:
        credential_id (int):
        body (CredentialSaveRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CredentialInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            credential_id=credential_id,
            client=client,
            body=body,
        )
    ).parsed
