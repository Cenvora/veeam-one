from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.organization_vdc_info import OrganizationVdcInfo
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    organization_vdc_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2.3/cloudDirector/organizationVdcs/{organization_vdc_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[OrganizationVdcInfo, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = OrganizationVdcInfo.from_dict(response.json())

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
) -> Response[Union[OrganizationVdcInfo, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_vdc_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[OrganizationVdcInfo, ProblemDetails]]:
    """Get Organization VDC

     Returns a resource representation of an organization VDC with the specified ID.

    Args:
        organization_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganizationVdcInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        organization_vdc_id=organization_vdc_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_vdc_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[OrganizationVdcInfo, ProblemDetails]]:
    """Get Organization VDC

     Returns a resource representation of an organization VDC with the specified ID.

    Args:
        organization_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganizationVdcInfo, ProblemDetails]
    """

    return sync_detailed(
        organization_vdc_id=organization_vdc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_vdc_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[OrganizationVdcInfo, ProblemDetails]]:
    """Get Organization VDC

     Returns a resource representation of an organization VDC with the specified ID.

    Args:
        organization_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganizationVdcInfo, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        organization_vdc_id=organization_vdc_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_vdc_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[OrganizationVdcInfo, ProblemDetails]]:
    """Get Organization VDC

     Returns a resource representation of an organization VDC with the specified ID.

    Args:
        organization_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganizationVdcInfo, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            organization_vdc_id=organization_vdc_id,
            client=client,
        )
    ).parsed
