from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authentication_create_token_data_body import AuthenticationCreateTokenDataBody
from ...models.authentication_create_token_files_body import AuthenticationCreateTokenFilesBody
from ...models.problem_details import ProblemDetails
from ...models.token_response import TokenResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: AuthenticationCreateTokenDataBody | AuthenticationCreateTokenFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/token",
    }

    if isinstance(body, AuthenticationCreateTokenDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AuthenticationCreateTokenFilesBody):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | TokenResponse | None:
    if response.status_code == 200:
        response_200 = TokenResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ProblemDetails | TokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationCreateTokenDataBody | AuthenticationCreateTokenFilesBody | Unset = UNSET,
) -> Response[ProblemDetails | TokenResponse]:
    """Request Authorization Tokens

     Issues access and refresh JWT tokens.

    Args:
        body (AuthenticationCreateTokenDataBody | Unset):
        body (AuthenticationCreateTokenFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationCreateTokenDataBody | AuthenticationCreateTokenFilesBody | Unset = UNSET,
) -> ProblemDetails | TokenResponse | None:
    """Request Authorization Tokens

     Issues access and refresh JWT tokens.

    Args:
        body (AuthenticationCreateTokenDataBody | Unset):
        body (AuthenticationCreateTokenFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TokenResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationCreateTokenDataBody | AuthenticationCreateTokenFilesBody | Unset = UNSET,
) -> Response[ProblemDetails | TokenResponse]:
    """Request Authorization Tokens

     Issues access and refresh JWT tokens.

    Args:
        body (AuthenticationCreateTokenDataBody | Unset):
        body (AuthenticationCreateTokenFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | TokenResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AuthenticationCreateTokenDataBody | AuthenticationCreateTokenFilesBody | Unset = UNSET,
) -> ProblemDetails | TokenResponse | None:
    """Request Authorization Tokens

     Issues access and refresh JWT tokens.

    Args:
        body (AuthenticationCreateTokenDataBody | Unset):
        body (AuthenticationCreateTokenFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | TokenResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
