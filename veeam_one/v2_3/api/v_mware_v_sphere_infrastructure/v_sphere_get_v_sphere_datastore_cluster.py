from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_datastore_cluster_info import VSphereDatastoreClusterInfo
from ...types import Response


def _get_kwargs(
    datastore_cluster_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/datastoreClusters/{datastore_cluster_id}".format(
            datastore_cluster_id=quote(str(datastore_cluster_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VSphereDatastoreClusterInfo | None:
    if response.status_code == 200:
        response_200 = VSphereDatastoreClusterInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VSphereDatastoreClusterInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    datastore_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereDatastoreClusterInfo]:
    """Get Datastore Cluster

     Returns a resource representation of a VMware vSphere datastore cluster with the specified ID.

    Args:
        datastore_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereDatastoreClusterInfo]
    """

    kwargs = _get_kwargs(
        datastore_cluster_id=datastore_cluster_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    datastore_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereDatastoreClusterInfo | None:
    """Get Datastore Cluster

     Returns a resource representation of a VMware vSphere datastore cluster with the specified ID.

    Args:
        datastore_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereDatastoreClusterInfo
    """

    return sync_detailed(
        datastore_cluster_id=datastore_cluster_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    datastore_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereDatastoreClusterInfo]:
    """Get Datastore Cluster

     Returns a resource representation of a VMware vSphere datastore cluster with the specified ID.

    Args:
        datastore_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereDatastoreClusterInfo]
    """

    kwargs = _get_kwargs(
        datastore_cluster_id=datastore_cluster_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    datastore_cluster_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereDatastoreClusterInfo | None:
    """Get Datastore Cluster

     Returns a resource representation of a VMware vSphere datastore cluster with the specified ID.

    Args:
        datastore_cluster_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereDatastoreClusterInfo
    """

    return (
        await asyncio_detailed(
            datastore_cluster_id=datastore_cluster_id,
            client=client,
        )
    ).parsed
