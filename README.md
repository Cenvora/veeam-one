# veeam-one

Veeam ONE REST API wrapper for Python.

The generated v2.3 SDK is produced with openapi-python-client from the Veeam ONE REST API v2.3 OpenAPI specification. The v2.3 API is the current REST API documented for Veeam ONE 13.1.

## Usage

    import asyncio
    from veeam_one import VeeamClient

    async def main():
        async with VeeamClient(
            "https://one.example:1239",
            username="administrator",
            password="secret",
            verify_ssl=False,
        ) as one:
            result = await one.call(
                one.api("veeam_backup_replication_infrastructure").get_all_backup_repositories
            )
            print(result)

    asyncio.run(main())

The high-level client handles username/password authentication, refresh-token renewal, pre-existing bearer tokens, SSL verification, and version routing.

## Regenerating the SDK

The checked-in SDK is generated from the v2.3 OpenAPI schema with openapi-python-client. fix_openapi.py applies only the compatibility workaround required by the generator; the source schema is not modified.

Veeam ONE exposes Swagger UI at /swagger/index.html and the v2.3 specification at /swagger/v2.3/swagger.json on the Web Services endpoint. The documented default REST API port is 1239.
