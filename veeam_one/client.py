import importlib
from datetime import datetime, timedelta, timezone
from typing import Any

from .versions import VERSION_TO_PACKAGE


class ApiNamespace:
    """Lazy namespace for openapi-python-client operation modules."""

    def __init__(self, client: "VeeamClient", base_module: str):
        self._client = client
        self._base = base_module

    def __getattr__(self, name: str):
        try:
            return importlib.import_module(f"{self._base}.{name}").asyncio
        except ModuleNotFoundError as exc:
            prefix = self._base.rsplit(".", 1)[-1]
            try:
                return importlib.import_module(f"{self._base}.{prefix}_{name}").asyncio
            except ModuleNotFoundError:
                raise exc


class VeeamAuthenticationError(PermissionError):
    """Raised when Veeam ONE rejects authentication."""


class VeeamClient:
    """Async high-level client for the versioned Veeam ONE REST SDK."""

    def __init__(
        self,
        host: str,
        api_version: str = "2.3",
        verify_ssl: bool = True,
        username: str | None = None,
        password: str | None = None,
        token: str | None = None,
        timeout: float | None = 30.0,
    ):
        if api_version not in VERSION_TO_PACKAGE:
            raise ValueError(f"Unsupported API version: {api_version}")
        if token:
            self.token = token
            self.username = self.password = None
        elif username and password:
            self.token = None
            self.username = username
            self.password = password
        else:
            raise ValueError("Must provide either 'token' or both 'username' and 'password'")

        self.host = host.rstrip("/")
        self.api_version = api_version
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.package = VERSION_TO_PACKAGE[api_version]
        self._client = None
        self._access_token = None
        self._refresh_token = None
        self._expires_at: datetime | None = None

    async def connect(self):
        Client = getattr(importlib.import_module(f"{self.package}.client"), "Client")
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )

        if self.token:
            self._access_token = self.token
            self._client = AuthenticatedClient(
                base_url=self.host,
                token=self._access_token,
                verify_ssl=self.verify_ssl,
                timeout=self.timeout,
            )
            return self

        self._client = Client(
            base_url=self.host,
            verify_ssl=self.verify_ssl,
            timeout=self.timeout,
        )
        await self._login(self.username, self.password)
        return self

    async def _request_token(
        self, *, grant_type, username=None, password=None, refresh_token=None
    ):
        module = importlib.import_module(
            f"{self.package}.api.authentication.authentication_create_token"
        )
        body_cls = getattr(
            importlib.import_module(
                f"{self.package}.models.authentication_create_token_data_body"
            ),
            "AuthenticationCreateTokenDataBody",
        )
        kwargs = {"grant_type": grant_type}
        if username is not None:
            kwargs["username"] = username
        if password is not None:
            kwargs["password"] = password
        if refresh_token is not None:
            kwargs["refresh_token"] = refresh_token
        body = body_cls(**kwargs)
        result = await module.asyncio(client=self._client, body=body)
        if not hasattr(result, "access_token") or not result.access_token:
            raise VeeamAuthenticationError("Veeam ONE authentication failed")
        return result

    async def _login(self, username: str, password: str):
        grant = getattr(
            importlib.import_module(
                f"{self.package}.models.authentication_create_token_data_body_grant_type"
            ),
            "AuthenticationCreateTokenDataBodyGrantType",
        )
        token = await self._request_token(
            grant_type=grant.PASSWORD,
            username=username,
            password=password,
        )
        self._store_token(token)

    def _store_token(self, token):
        AuthenticatedClient = getattr(
            importlib.import_module(f"{self.package}.client"), "AuthenticatedClient"
        )
        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        expires_in = token.expires_in if isinstance(token.expires_in, int) else 900
        self._expires_at = datetime.now(timezone.utc) + timedelta(
            seconds=max(1, expires_in - 30)
        )
        self._client = AuthenticatedClient(
            base_url=self.host,
            token=self._access_token,
            verify_ssl=self.verify_ssl,
            timeout=self.timeout,
        )

    async def _refresh_token_if_needed(self):
        if self.token:
            return
        if self._expires_at and datetime.now(timezone.utc) < self._expires_at:
            return

        grant = getattr(
            importlib.import_module(
                f"{self.package}.models.authentication_create_token_data_body_grant_type"
            ),
            "AuthenticationCreateTokenDataBodyGrantType",
        )
        try:
            token = await self._request_token(
                grant_type=grant.REFRESH_TOKEN,
                refresh_token=self._refresh_token,
            )
            self._store_token(token)
        except Exception:
            if not self.username or not self.password:
                raise
            await self._login(self.username, self.password)

    async def close(self):
        if self._client is not None:
            await self._client.get_async_httpx_client().aclose()
        self._client = None

    async def __aenter__(self):
        return await self.connect()

    async def __aexit__(self, *args):
        await self.close()

    def api(self, name: str) -> Any:
        if "." in name:
            return importlib.import_module(f"{self.package}.api.{name}").asyncio
        return ApiNamespace(self, f"{self.package}.api.{name}")

    async def call(self, fn, *args, **kwargs):
        await self._refresh_token_if_needed()
        return await fn(client=self._client, *args, **kwargs)
