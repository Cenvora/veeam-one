from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.v_sphere_vm_info import VSphereVmInfo
from ...types import Response


def _get_kwargs(
    vm_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/vSphere/vms/{vm_id}".format(
            vm_id=quote(str(vm_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | VSphereVmInfo | None:
    if response.status_code == 200:
        response_200 = VSphereVmInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | VSphereVmInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vm_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereVmInfo]:
    """Get VMware vSphere VM

     Returns a resource representation of a VMware vSphere VM with the specified ID.

    Args:
        vm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereVmInfo]
    """

    kwargs = _get_kwargs(
        vm_id=vm_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vm_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereVmInfo | None:
    """Get VMware vSphere VM

     Returns a resource representation of a VMware vSphere VM with the specified ID.

    Args:
        vm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereVmInfo
    """

    return sync_detailed(
        vm_id=vm_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    vm_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | VSphereVmInfo]:
    """Get VMware vSphere VM

     Returns a resource representation of a VMware vSphere VM with the specified ID.

    Args:
        vm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | VSphereVmInfo]
    """

    kwargs = _get_kwargs(
        vm_id=vm_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vm_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | VSphereVmInfo | None:
    """Get VMware vSphere VM

     Returns a resource representation of a VMware vSphere VM with the specified ID.

    Args:
        vm_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | VSphereVmInfo
    """

    return (
        await asyncio_detailed(
            vm_id=vm_id,
            client=client,
        )
    ).parsed
