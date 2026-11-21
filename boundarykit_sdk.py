"""Utilities for building BoundaryKit API requests."""

from urllib.request import Request


class Workspace:
    """Identify the organization and credential used for a request."""

    def __init__(self, organization: str, api_key: str):
        self.organization = organization
        self.api_key = api_key

    def list_boundaries(self) -> Request:
        """Prepare a request for the first page of v2 boundaries."""
        return Request(
            "https://api.boundarykit.com/v2/boundaries",
            headers={"X-Organization-Id": self.organization, "X-API-Key": self.api_key},
        )
