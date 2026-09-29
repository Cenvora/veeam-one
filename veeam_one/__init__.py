"""Veeam ONE REST API wrapper for Python."""

from .client import VeeamAuthenticationError, VeeamClient

__all__ = ("VeeamClient", "VeeamAuthenticationError")
