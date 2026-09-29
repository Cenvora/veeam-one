"""A client library for accessing Veeam ONE REST API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
