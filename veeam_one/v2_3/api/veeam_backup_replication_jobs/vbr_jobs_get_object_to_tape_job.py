from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.object_to_tape_job_info import ObjectToTapeJobInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    object_to_tape_job_uid: UUID,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/vbrJobs/objectToTapeJobs/{object_to_tape_job_uid}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = ObjectToTapeJobInfo.from_dict(response.json())

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
) -> Response[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_to_tape_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    """Get Object to Tape Job

     Returns a resource representation of an object to tape job with the specified UID.

    Args:
        object_to_tape_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ObjectToTapeJobInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        object_to_tape_job_uid=object_to_tape_job_uid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_to_tape_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    """Get Object to Tape Job

     Returns a resource representation of an object to tape job with the specified UID.

    Args:
        object_to_tape_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ObjectToTapeJobInfo, ProblemDetails]
    """

    return sync_detailed(
        object_to_tape_job_uid=object_to_tape_job_uid,
        client=client,
    ).parsed


async def asyncio_detailed(
    object_to_tape_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    """Get Object to Tape Job

     Returns a resource representation of an object to tape job with the specified UID.

    Args:
        object_to_tape_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ObjectToTapeJobInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        object_to_tape_job_uid=object_to_tape_job_uid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_to_tape_job_uid: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ObjectToTapeJobInfo, ProblemDetails]]:
    """Get Object to Tape Job

     Returns a resource representation of an object to tape job with the specified UID.

    Args:
        object_to_tape_job_uid (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ObjectToTapeJobInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            object_to_tape_job_uid=object_to_tape_job_uid,
            client=client,
        )
    ).parsed
