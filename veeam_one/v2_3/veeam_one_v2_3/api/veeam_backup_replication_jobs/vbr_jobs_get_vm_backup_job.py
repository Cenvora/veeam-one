from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.vm_backup_job_info import VmBackupJobInfo
from ...types import Response


def _get_kwargs(
    vm_backup_job_uid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vbrJobs/vmBackupJobs/{vm_backup_job_uid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, VmBackupJobInfo]]:
    if response.status_code == 200:
        response_200 = VmBackupJobInfo.from_dict(response.json())

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
) -> Response[Union[ProblemDetails, VmBackupJobInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    vm_backup_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VmBackupJobInfo]]:
    """Get VM Backup Job

     Returns a resource representation of a VM backup job with the specified UID.

    Args:
        vm_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VmBackupJobInfo]]
    """

    kwargs = _get_kwargs(
        vm_backup_job_uid=vm_backup_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    vm_backup_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VmBackupJobInfo]]:
    """Get VM Backup Job

     Returns a resource representation of a VM backup job with the specified UID.

    Args:
        vm_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VmBackupJobInfo]
    """

    return sync_detailed(
        vm_backup_job_uid=vm_backup_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    vm_backup_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VmBackupJobInfo]]:
    """Get VM Backup Job

     Returns a resource representation of a VM backup job with the specified UID.

    Args:
        vm_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VmBackupJobInfo]]
    """

    kwargs = _get_kwargs(
        vm_backup_job_uid=vm_backup_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    vm_backup_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VmBackupJobInfo]]:
    """Get VM Backup Job

     Returns a resource representation of a VM backup job with the specified UID.

    Args:
        vm_backup_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VmBackupJobInfo]
    """

    return (
        await asyncio_detailed(
            vm_backup_job_uid=vm_backup_job_uid,
            client=client,
        )
    ).parsed
