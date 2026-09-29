from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    object_id: int,
    *,
    propagate: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["propagate"] = propagate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v2.3/credentials/object/{object_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProblemDetails]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    propagate: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
    propagate: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        object_id=object_id,
        client=client,
        propagate=propagate,
    ).parsed


async def asyncio_detailed(
    object_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    propagate: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, ProblemDetails]]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
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
    client: Union[AuthenticatedClient, Client],
    propagate: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, ProblemDetails]]:
    """Delete Credentials Assigned to Object

     Deletes credential set that is used to access an object with the specified ID.

    Args:
        object_id (int):
        propagate (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            object_id=object_id,
            client=client,
            propagate=propagate,
        )
    ).parsed
