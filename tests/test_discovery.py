"""Tests for API version detection.

Served against httpx.MockTransport, so the probing behaviour is exercised for real rather
than mocked out.
"""

import httpx
import pytest

from veeam_one.discovery import (
    RestApiEndpoint,
    detect_api_version,
    detect_rest_api,
    newest_first,
    probe_url,
)
from veeam_one.versions import VERSION_TO_PACKAGE

BASE_URL = "https://one.example.com:1239"

# The package ships one version today; tests about choosing between versions supply their own
CANDIDATES = ["2.1", "2.2", "2.3"]


def make_client(served, status_for_unserved=400, served_status=401, fail_with=None):
    """An httpx client whose server routes only the given versions.

    A served version answers 401 by default, which is what an unauthenticated probe of a
    real server gets: the route exists and the bearer token is missing.
    """
    requested = []

    def handler(request):
        requested.append(str(request.url))
        if fail_with is not None:
            raise fail_with
        for version in served:
            if request.url.path == f"/api/v{version}/about":
                return httpx.Response(served_status)
        return httpx.Response(status_for_unserved)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


def test_probe_url_uses_the_versioned_path():
    assert probe_url(BASE_URL, "2.3") == f"{BASE_URL}/api/v2.3/about"


def test_probe_url_tolerates_a_trailing_slash():
    assert probe_url(BASE_URL + "/", "2.3").count("//") == 1


@pytest.mark.parametrize(
    "versions,expected",
    [
        (["2.1", "2.3", "2.2"], ["2.3", "2.2", "2.1"]),
        # Numeric ordering, which string sorting would get wrong
        (["2.3", "2.10"], ["2.10", "2.3"]),
        # Unrecognizable entries are dropped rather than ordered arbitrarily
        (["2.2", "nonsense", None, ""], ["2.2"]),
        ([], []),
    ],
)
def test_newest_first(versions, expected):
    assert newest_first(versions) == expected


@pytest.mark.asyncio
async def test_detects_the_newest_version_the_server_serves():
    client, _ = make_client(served=["2.1", "2.2"])

    detected = await detect_api_version(BASE_URL, client=client, versions=CANDIDATES)

    assert detected == "2.2", "an older server must not be handed a newer version"


@pytest.mark.asyncio
async def test_detects_the_newest_when_the_server_serves_everything():
    client, _ = make_client(served=list(VERSION_TO_PACKAGE))

    detected = await detect_api_version(BASE_URL, client=client)

    assert detected == newest_first(VERSION_TO_PACKAGE)[0]


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [200, 401, 403])
async def test_any_routed_status_counts_as_served(status):
    """The question is whether the path routes, not whether the probe was allowed."""
    client, _ = make_client(served=["2.3"], served_status=status)

    assert await detect_api_version(BASE_URL, client=client) == "2.3"


@pytest.mark.asyncio
async def test_older_versions_the_server_serves_are_not_chosen_over_supported_ones():
    """Veeam ONE 13 answers 401 for 2.1, 2.2 and 2.3; only 2.3 is usable."""
    client, _ = make_client(served=["2.1", "2.2", "2.3"])

    assert await detect_api_version(BASE_URL, client=client) == "2.3"


@pytest.mark.asyncio
@pytest.mark.parametrize("status", [400, 404])
async def test_unrouted_statuses_mean_not_served(status):
    """Veeam ONE answers 400 for an unknown version; a proxy in front may say 404."""
    client, _ = make_client(served=[], status_for_unserved=status)

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_probes_only_versions_this_package_supports():
    """Reporting a version the SDK cannot speak would be useless to the caller."""
    client, requested = make_client(served=list(VERSION_TO_PACKAGE))

    await detect_api_version(BASE_URL, client=client)

    probed = {url.rsplit("/", 2)[1].removeprefix("v") for url in requested}
    assert probed == set(VERSION_TO_PACKAGE)


@pytest.mark.asyncio
async def test_candidate_list_can_be_narrowed():
    client, requested = make_client(served=["2.2"])

    detected = await detect_api_version(BASE_URL, client=client, versions=["2.2"])

    assert detected == "2.2"
    assert len(requested) == 1


@pytest.mark.asyncio
async def test_returns_none_when_no_version_answers():
    """The caller then falls back to a version of its own choosing."""
    client, _ = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_server_is_unreachable():
    client, _ = make_client(served=[], fail_with=httpx.ConnectError("unreachable"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_a_probe_times_out():
    client, _ = make_client(served=[], fail_with=httpx.ReadTimeout("too slow"))

    assert await detect_api_version(BASE_URL, client=client) is None


@pytest.mark.asyncio
async def test_a_single_failing_probe_does_not_hide_the_others():
    """One version timing out must not lose a version that did answer."""
    calls = {"n": 0}

    def handler(request):
        if request.url.path == "/api/v2.3/about":
            raise httpx.ReadTimeout("too slow")
        if request.url.path == "/api/v2.2/about":
            calls["n"] += 1
            return httpx.Response(401)
        return httpx.Response(400)

    client = httpx.AsyncClient(transport=httpx.MockTransport(handler))

    detected = await detect_api_version(BASE_URL, client=client, versions=CANDIDATES)

    assert detected == "2.2"
    assert calls["n"] == 1


@pytest.mark.asyncio
async def test_empty_candidate_list_makes_no_requests():
    client, requested = make_client(served=[])

    assert await detect_api_version(BASE_URL, client=client, versions=[]) is None
    assert requested == []


@pytest.mark.asyncio
async def test_caller_supplied_client_is_left_open():
    """Reusing a caller's client must not close it out from under them."""
    client, _ = make_client(served=["2.2"])

    await detect_api_version(BASE_URL, client=client)

    assert not client.is_closed
    await client.aclose()


@pytest.mark.asyncio
async def test_detected_version_is_usable_with_veeam_client():
    """Detection is only useful if its result routes to a real SDK package."""
    from veeam_one.client import VeeamClient

    client, _ = make_client(served=list(VERSION_TO_PACKAGE))
    detected = await detect_api_version(BASE_URL, client=client)

    vc = VeeamClient(
        host=BASE_URL,
        username="administrator",
        password="pw",
        api_version=detected,
    )
    assert vc.package == VERSION_TO_PACKAGE[detected]


# ---------------------------------------------------------------------------
# Endpoint detection: which port, and which version on it
#
# Veeam ONE Web Services listens on 1239 out of the box, but the port is configurable, so a
# caller cannot assume it.
# ---------------------------------------------------------------------------


def make_endpoint_client(served, fail_with=None):
    """A client whose server routes only the given (port, version) pairs.

    httpx reports url.port as None for a scheme's default port, so an https URL written as
    ":443" arrives here with no port at all — hence the fallback. A real server still sees
    the TCP port it was reached on.
    """
    requested = []

    def port_of(request):
        return request.url.port or 443

    def handler(request):
        requested.append((port_of(request), str(request.url.path)))
        if fail_with is not None:
            raise fail_with
        for port, version in served:
            if port_of(request) == port and request.url.path == f"/api/v{version}/about":
                return httpx.Response(401)
        return httpx.Response(400)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler)), requested


@pytest.mark.asyncio
async def test_finds_the_default_port():
    client, _ = make_endpoint_client([(1239, "2.3")])

    endpoint = await detect_rest_api("one.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=1239, api_version="2.3")


@pytest.mark.asyncio
async def test_reports_the_newest_version_on_the_answering_port():
    client, _ = make_endpoint_client([(1239, "2.2"), (1239, "2.3")])

    endpoint = await detect_rest_api("one.example.com", client=client)

    assert endpoint == RestApiEndpoint(port=1239, api_version="2.3")


@pytest.mark.asyncio
async def test_port_order_is_the_callers_choice():
    """A caller running the service on a custom port can say so."""
    client, _ = make_endpoint_client([(1239, "2.3"), (1240, "2.3")])

    endpoint = await detect_rest_api("one.example.com", ports=(1240, 1239), client=client)

    assert endpoint.port == 1240


@pytest.mark.asyncio
async def test_probes_every_port_and_version_combination():
    client, requested = make_endpoint_client([])

    await detect_rest_api(
        "one.example.com", ports=(1239, 443), client=client, versions=["2.3", "2.2"]
    )

    assert sorted(requested) == sorted(
        [(port, f"/api/v{version}/about") for port in (1239, 443) for version in ("2.3", "2.2")]
    )


@pytest.mark.asyncio
async def test_returns_none_when_no_port_answers():
    """Caller keeps whatever the user configured rather than guessing."""
    client, _ = make_endpoint_client([])

    assert await detect_rest_api("one.example.com", client=client) is None


@pytest.mark.asyncio
async def test_returns_none_when_the_host_is_unreachable():
    client, _ = make_endpoint_client([], fail_with=httpx.ConnectError("no route"))

    assert await detect_rest_api("one.example.com", client=client) is None


@pytest.mark.asyncio
async def test_no_ports_means_no_requests():
    client, requested = make_endpoint_client([])

    assert await detect_rest_api("one.example.com", ports=(), client=client) is None
    assert requested == []


@pytest.mark.asyncio
async def test_detected_endpoint_builds_a_working_base_url():
    """The result should drop straight into a VeeamClient host argument."""
    from veeam_one.client import VeeamClient

    client, _ = make_endpoint_client([(1239, "2.3")])
    endpoint = await detect_rest_api("one.example.com", client=client)

    vc = VeeamClient(
        host=f"https://one.example.com{endpoint.base_url_suffix}",
        username="administrator",
        password="pw",
        api_version=endpoint.api_version,
    )
    assert vc.host == "https://one.example.com:1239"
    assert vc.package == VERSION_TO_PACKAGE[endpoint.api_version]
