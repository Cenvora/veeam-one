from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: int,
    *,
    propagate: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["propagate"] = propagate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v2.3/credentials/object/{object_id}".format(
            object_id=quote(str(object_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
    propagate: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        propagate=propagate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
    propagate: bool | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        propagate=propagate,
    ).parsed


async def asyncio_detailed(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
    propagate: bool | Unset = UNSET,
) -> Response[Any | ProblemDetails]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProblemDetails]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
        propagate=propagate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
    propagate: bool | Unset = UNSET,
) -> Any | ProblemDetails | None:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProblemDetails
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            propagate=propagate,
        )
    ).parsed
