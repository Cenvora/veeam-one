from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authentication_revoke_token_data_body import AuthenticationRevokeTokenDataBody
from ...models.authentication_revoke_token_files_body import AuthenticationRevokeTokenFilesBody
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        AuthenticationRevokeTokenDataBody,
        AuthenticationRevokeTokenFilesBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/revoke",
    }

    if isinstance(body, AuthenticationRevokeTokenDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, AuthenticationRevokeTokenFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ProblemDetails.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AuthenticationRevokeTokenDataBody,
        AuthenticationRevokeTokenFilesBody,
    ],
) -> Response[Union[Any, ProblemDetails]]:
    """Revoke Authorization Tokens

     Revokes the specified access JWT token or performs logout operation for the specified user.

    Args:
        body (AuthenticationRevokeTokenDataBody):
        body (AuthenticationRevokeTokenFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AuthenticationRevokeTokenDataBody,
        AuthenticationRevokeTokenFilesBody,
    ],
) -> Optional[Union[Any, ProblemDetails]]:
    """Revoke Authorization Tokens

     Revokes the specified access JWT token or performs logout operation for the specified user.

    Args:
        body (AuthenticationRevokeTokenDataBody):
        body (AuthenticationRevokeTokenFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AuthenticationRevokeTokenDataBody,
        AuthenticationRevokeTokenFilesBody,
    ],
) -> Response[Union[Any, ProblemDetails]]:
    """Revoke Authorization Tokens

     Revokes the specified access JWT token or performs logout operation for the specified user.

    Args:
        body (AuthenticationRevokeTokenDataBody):
        body (AuthenticationRevokeTokenFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AuthenticationRevokeTokenDataBody,
        AuthenticationRevokeTokenFilesBody,
    ],
) -> Optional[Union[Any, ProblemDetails]]:
    """Revoke Authorization Tokens

     Revokes the specified access JWT token or performs logout operation for the specified user.

    Args:
        body (AuthenticationRevokeTokenDataBody):
        body (AuthenticationRevokeTokenFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
