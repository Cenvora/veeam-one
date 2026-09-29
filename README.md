<h1 align="center">
<br>
<img src="https://raw.githubusercontent.com/Cenvora/veeam-one/main/media/Veeam_logo_2024_RGB_main_20.png"
     alt="Veeam Logo"
     height="100">
<br>
<br>
Veeam ONE Python API Wrapper
</h1>

<h4 align="center">
Python package for interacting with the Veeam ONE REST API
</h4>

<!-- Summary -->
This project is an independent, open source Python client for the Veeam ONE
<a href="https://helpcenter.veeam.com/docs/one/rest/reference/vone-rest.html">REST API</a>.
It is not affiliated with, endorsed by, or sponsored by Veeam Software.
<!-- Summary -->

## Supported Versions

| Veeam ONE Version | API Version | Supported |
| --- | --- | :---: |
| 13.1 | 2.3 | &#9989; |
| < 13.1 | < 2.3 | &#10060; |

The checked-in SDK is generated from the Veeam ONE REST API v2.3 OpenAPI specification
using openapi-python-client.

## How to support a new API version

1. Download the OpenAPI JSON specification into `openapi_schemas`.
2. Install the `openapi-python-client` package.
3. Run the fixer:
   `python fix_openapi.py .\openapi_schemas\veeam_one_rest_v2.3.json .\openapi_schemas\veeam_one_rest_v2.3_fixed.json`
4. Generate the SDK:
   `openapi-python-client generate --path ".\openapi_schemas\veeam_one_rest_v2.3_fixed.json" --config openapi-client-config.yaml --output-path ".\veeam_one\v2_3" --overwrite`
5. Move the generated package contents up one level so the versioned package is
   `veeam_one/v2_3`, then remove generated metadata that belongs to the repository root.
6. Fix any generator warnings/errors and verify the generated imports.
7. Add the API version to `versions.py`.
8. Add or update pytest coverage for the Smart Client and generated package.
9. If an older API has been deprecated, remove its versioned package and schema and
   update the supported versions table.

The repository workflow performs the same generation and normalizes the generated
folder layout automatically.

## Install

### From PyPI

`pip install veeam-one`

### From Source

Clone the repository and install dependencies:

```sh
git clone https://github.com/Cenvora/veeam-one.git
cd veeam-one
pip install -e .
```

## Usage

### Recommended Usage (Smart Client)

The `VeeamClient` handles:

- API version routing
- username/password authentication
- pre-existing bearer-token authentication
- refresh-token renewal
- async calls
- operation discovery
- SSL verification and request timeouts

Each packaged API version can also be called directly, but the Smart Client is the
recommended interface.

#### Create a client and connect

Using username/password authentication:

```python
import asyncio

from veeam_one.client import VeeamClient

async def main():
    async with VeeamClient(
        host="https://one.example:1239",
        username="administrator",
        password="SuperSecretPassword",
        api_version="2.3",
        verify_ssl=False,
    ) as one:
        result = await one.call(
            one.api("about").get_about
        )
        print(result)

asyncio.run(main())
```

You can also provide an existing bearer token:

```python
async with VeeamClient(
    host="https://one.example:1239",
    token="your-bearer-token",
    api_version="2.3",
) as one:
    result = await one.call(one.api("about").get_about)
```

`verify_ssl` accepts a boolean, an SSL context, or a CA bundle path.
`timeout` defaults to 30 seconds and can be set to `None` to disable the timeout.

#### Detect the API version and port

The REST API has no endpoint that reports its supported versions; the version is part of
every path. That path is also what makes detection possible: `/api/v{version}/about` exists
in every version and requires a token, so an anonymous probe gets 401 where the version is
served and 400 where it is not. `detect_api_version` returns the newest version that both
the server serves and this library can speak:

```python
from veeam_one.client import VeeamClient
from veeam_one.discovery import detect_api_version

base_url = "https://one.example:1239"
api_version = await detect_api_version(base_url, verify_ssl=False)
if api_version is None:
    # The server may be unreachable or behind a proxy — choose your own default
    api_version = "2.3"

one = VeeamClient(host=base_url, username="administrator", password="...", api_version=api_version)
```

Detection needs no credentials, and probes run concurrently, so it costs roughly one round
trip. If you don't know the port either, `detect_rest_api` finds both at once. Veeam ONE Web
Services listens on 1239 by default, but the port is set at install time, so pass your own
candidates when a deployment uses something else:

```python
from veeam_one.discovery import detect_rest_api

endpoint = await detect_rest_api("one.example", ports=(1239, 443), verify_ssl=False)
if endpoint:
    print(endpoint.port, endpoint.api_version)  # e.g. 1239 2.3
```

Both accept `client=` to reuse an existing `httpx.AsyncClient`.

#### Call an API endpoint

Operations map directly to the OpenAPI tag layout. For example:

```text
api/
└── about/
    └── about_get_about.py
```

Call it through the Smart Client:

```python
result = await one.call(
    one.api("about").get_about
)
```

Or address the operation explicitly:

```python
result = await one.call(
    one.api("about.about_get_about")
)
```

The generated package is also available directly:

```python
from veeam_one.v2_3 import AuthenticatedClient
from veeam_one.v2_3.api.about import about_get_about

client = AuthenticatedClient(
    base_url="https://one.example:1239",
    token="your-bearer-token",
)

async with client:
    about = await about_get_about.asyncio(client=client)
```

#### Pagination

Generated list endpoints expose their OpenAPI parameters directly. For example:

```python
result = await one.call(
    one.api("alarms").get_triggered_alarms,
    limit=50,
)
```

Use the generated endpoint signature for the exact parameters supported by each operation.

#### Errors

Authentication failures from the Smart Client raise `VeeamAuthenticationError`.
HTTP and transport errors from the generated client are left as their normal exception types.

```python
import httpx

from veeam_one.client import VeeamAuthenticationError

try:
    result = await one.call(one.api("about").get_about)
except VeeamAuthenticationError:
    ...  # credentials were rejected
except (httpx.HTTPError, OSError, TimeoutError):
    ...  # the server could not be reached
```

#### Close the client

```python
await one.close()
```

`async with` closes the underlying HTTP connection pool automatically.

## Contributing
Contributions are welcome! To contribute:
- Fork the repository
- Create a feature branch
- Make your changes and add tests
- Submit a pull request with a clear description

Please follow PEP8 style and include docstrings for new functions/classes.

## 🤝 Core Contributors
This project is made possible thanks to the efforts of our core contributors:

- [Jonah May](https://github.com/JonahMMay)  
- [Maurice Kevenaar](https://github.com/mkevenaar)  
