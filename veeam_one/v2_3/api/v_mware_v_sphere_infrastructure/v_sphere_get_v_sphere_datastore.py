from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_datastore_info import VSphereDatastoreInfo
from ...types import Response


def _get_kwargs(
    datastore_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/datastores/{datastore_id}".format(
            datastore_id=quote(str(datastore_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VSphereDatastoreInfo | None:
    if response.status_code == 200:
        response_200 = VSphereDatastoreInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VSphereDatastoreInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datastore_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereDatastoreInfo]:
    """Get VMware vSphere Datastore

     Returns a resource representation of a VMware vSphere datastore with the specified ID.

    Args:
        datastore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereDatastoreInfo]
    """

    kwargs = _get_kwargs(
        datastore_id=datastore_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datastore_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereDatastoreInfo | None:
    """Get VMware vSphere Datastore

     Returns a resource representation of a VMware vSphere datastore with the specified ID.

    Args:
        datastore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereDatastoreInfo
    """

    return sync_detailed(
        datastore_id=datastore_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    datastore_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereDatastoreInfo]:
    """Get VMware vSphere Datastore

     Returns a resource representation of a VMware vSphere datastore with the specified ID.

    Args:
        datastore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereDatastoreInfo]
    """

    kwargs = _get_kwargs(
        datastore_id=datastore_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datastore_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereDatastoreInfo | None:
    """Get VMware vSphere Datastore

     Returns a resource representation of a VMware vSphere datastore with the specified ID.

    Args:
        datastore_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereDatastoreInfo
    """

    return (
        await asyncio_detailed(
            datastore_id=datastore_id,
            client=client,
        )
    ).parsed
