from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.certificate_export_type import CertificateExportType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, File, Response


def _get_kwargs(
    *,
    export_type: CertificateExportType,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_export_type = export_type.value
    params["exportType"] = json_export_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2.3/certificates/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[File, ProblemDetails]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.text))

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
) -> Response[Union[File, ProblemDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: CertificateExportType,
) -> Response[Union[File, ProblemDetails]]:
    """Export Certificates

     Exports certificates into a file with the specified format.

    Args:
        export_type (CertificateExportType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: CertificateExportType,
) -> Optional[Union[File, ProblemDetails]]:
    """Export Certificates

     Exports certificates into a file with the specified format.

    Args:
        export_type (CertificateExportType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, ProblemDetails]
    """

    return sync_detailed(
        client=client,
        export_type=export_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: CertificateExportType,
) -> Response[Union[File, ProblemDetails]]:
    """Export Certificates

     Exports certificates into a file with the specified format.

    Args:
        export_type (CertificateExportType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        export_type=export_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    export_type: CertificateExportType,
) -> Optional[Union[File, ProblemDetails]]:
    """Export Certificates

     Exports certificates into a file with the specified format.

    Args:
        export_type (CertificateExportType):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[File, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            export_type=export_type,
        )
    ).parsed
