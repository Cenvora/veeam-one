from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_credentials_info import EntityCredentialsInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    object_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/credentials/object/{object_id}".format(
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | list[EntityCredentialsInfo] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EntityCredentialsInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ProblemDetails | list[EntityCredentialsInfo]]:
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
) -> Response[ProblemDetails | list[EntityCredentialsInfo]]:
    """Get Credentials Assigned to Object

     Returns a resource representation of credential set that is used to access an object with the
    specified ID.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[EntityCredentialsInfo]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | list[EntityCredentialsInfo] | None:
    """Get Credentials Assigned to Object

     Returns a resource representation of credential set that is used to access an object with the
    specified ID.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[EntityCredentialsInfo]
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | list[EntityCredentialsInfo]]:
    """Get Credentials Assigned to Object

     Returns a resource representation of credential set that is used to access an object with the
    specified ID.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | list[EntityCredentialsInfo]]
    """

    kwargs = _get_kwargs(
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | list[EntityCredentialsInfo] | None:
    """Get Credentials Assigned to Object

     Returns a resource representation of credential set that is used to access an object with the
    specified ID.

    Args:
        object_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | list[EntityCredentialsInfo]
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
        )
    ).parsed
