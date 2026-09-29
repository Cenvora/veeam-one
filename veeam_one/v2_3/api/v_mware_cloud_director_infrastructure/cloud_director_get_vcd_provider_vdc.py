from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.provider_vdc_info import ProviderVdcInfo
from ...types import Response


def _get_kwargs(
    provider_vdc_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/cloudDirector/providerVdcs/{provider_vdc_id}".format(
            provider_vdc_id=quote(str(provider_vdc_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ProblemDetails | ProviderVdcInfo | None:
    if response.status_code == 200:
        response_200 = ProviderVdcInfo.from_dict(response.json())

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
) -> Response[ProblemDetails | ProviderVdcInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_vdc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProviderVdcInfo]:
    """Get Provider VDC

     Returns a resource representation of a provider VDC with the specified ID.

    Args:
        provider_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProviderVdcInfo]
    """

    kwargs = _get_kwargs(
        provider_vdc_id=provider_vdc_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_vdc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProviderVdcInfo | None:
    """Get Provider VDC

     Returns a resource representation of a provider VDC with the specified ID.

    Args:
        provider_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProviderVdcInfo
    """

    return sync_detailed(
        provider_vdc_id=provider_vdc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider_vdc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails | ProviderVdcInfo]:
    """Get Provider VDC

     Returns a resource representation of a provider VDC with the specified ID.

    Args:
        provider_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails | ProviderVdcInfo]
    """

    kwargs = _get_kwargs(
        provider_vdc_id=provider_vdc_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_vdc_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | ProviderVdcInfo | None:
    """Get Provider VDC

     Returns a resource representation of a provider VDC with the specified ID.

    Args:
        provider_vdc_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails | ProviderVdcInfo
    """

    return (
        await asyncio_detailed(
            provider_vdc_id=provider_vdc_id,
            client=client,
        )
    ).parsed
