import pytest

from veeam_one.client import VeeamClient
from veeam_one.versions import VERSION_TO_PACKAGE


def test_version_mapping():
    assert VERSION_TO_PACKAGE["2.3"] == "veeam_one.v2_3"


def test_requires_credentials():
    with pytest.raises(ValueError):
        VeeamClient("https://one.example")


def test_rejects_unknown_version():
    with pytest.raises(ValueError):
        VeeamClient("https://one.example", token="x", api_version="9.9")


def test_api_namespace():
    client = VeeamClient("https://one.example", token="x")
    operation = client.api("about").get_about
    assert operation.__name__ == "asyncio"


def test_accepts_an_ssl_context():
    import ssl

    context = ssl.create_default_context()
    client = VeeamClient("https://one.example", token="x", verify_ssl=context)
    assert client.verify_ssl is context
