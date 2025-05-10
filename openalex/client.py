import httpx
from typing import Any, Dict, Optional

OPENALEX_BASE_URL = "https://api.openalex.org/"


class OpenAlexClient:
    """Minimal HTTP client for the OpenAlex API."""

    def __init__(self, base_url: str = OPENALEX_BASE_URL):
        self.base_url = base_url.rstrip("/") + "/"
        self.session = httpx.AsyncClient()

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        url = self.base_url + endpoint.lstrip("/")
        response = await self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    async def close(self):
        await self.session.aclose()
