from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.business_view_category_info import BusinessViewCategoryInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    category_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/businessview/categories/{category_id}".format(
            category_id=quote(str(category_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> BusinessViewCategoryInfo | ProblemDetails | None:
    if response.status_code == 200:
        response_200 = BusinessViewCategoryInfo.from_dict(response.json())

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
) -> Response[BusinessViewCategoryInfo | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BusinessViewCategoryInfo | ProblemDetails]:
    """Get Business View Category

     Returns a collection resource representation of a Business View category with the specified ID.

    Args:
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessViewCategoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BusinessViewCategoryInfo | ProblemDetails | None:
    """Get Business View Category

     Returns a collection resource representation of a Business View category with the specified ID.

    Args:
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessViewCategoryInfo | ProblemDetails
    """

    return sync_detailed(
        category_id=category_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[BusinessViewCategoryInfo | ProblemDetails]:
    """Get Business View Category

     Returns a collection resource representation of a Business View category with the specified ID.

    Args:
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BusinessViewCategoryInfo | ProblemDetails]
    """

    kwargs = _get_kwargs(
        category_id=category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> BusinessViewCategoryInfo | ProblemDetails | None:
    """Get Business View Category

     Returns a collection resource representation of a Business View category with the specified ID.

    Args:
        category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BusinessViewCategoryInfo | ProblemDetails
    """

    return (
        await asyncio_detailed(
            category_id=category_id,
            client=client,
        )
    ).parsed
