from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.veeam_one_license_usage_report import VeeamOneLicenseUsageReport
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/license/usageReport",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    if response.status_code == 200:
        response_200 = VeeamOneLicenseUsageReport.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = ProblemDetails.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    """Get License Usage Report

     Returns a resource representation of a license usage report. Available only for Rental license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VeeamOneLicenseUsageReport]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    """Get License Usage Report

     Returns a resource representation of a license usage report. Available only for Rental license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VeeamOneLicenseUsageReport]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    """Get License Usage Report

     Returns a resource representation of a license usage report. Available only for Rental license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProblemDetails, VeeamOneLicenseUsageReport]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ProblemDetails, VeeamOneLicenseUsageReport]]:
    """Get License Usage Report

     Returns a resource representation of a license usage report. Available only for Rental license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProblemDetails, VeeamOneLicenseUsageReport]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
