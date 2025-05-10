from fastmcp import FastMCP, Context
from openalex.client import OpenAlexClient
from openalex.schemas import WorkQuery, WorksSearchQuery, AuthorQuery, InstitutionQuery
from typing import Any

# Register all OpenAlex tools to the MCP server


def register_tools(mcp: FastMCP):
    """Register OpenAlex API tools with clear descriptions."""

    @mcp.tool(
        name="get_work",
        description="Retrieve a single work (article, book, etc.) from OpenAlex by its ID or DOI. Use this to fetch detailed metadata about a publication.",
        tags={"works", "metadata", "openalex"},
        annotations={"title": "Get Work by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_work(query: WorkQuery, ctx: Context) -> Any:
        """Fetch a work from OpenAlex by its OpenAlex ID or DOI."""
        client = OpenAlexClient()
        try:
            result = await client.get(f"works/{query.work_id}")
        finally:
            await client.close()
        return result

    @mcp.tool(
        name="search_works",
        description="Search for works (articles, books, etc.) in OpenAlex using filters (e.g., by institution, year, etc.). Returns a list of matching works.",
        tags={"works", "search", "openalex"},
        annotations={"title": "Search Works",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def search_works(query: WorksSearchQuery, ctx: Context) -> Any:
        """Search for works in OpenAlex using filters and sorting."""
        client = OpenAlexClient()
        try:
            params = {}
            if query.filter:
                params["filter"] = query.filter
            if query.sort:
                params["sort"] = query.sort
            params["per-page"] = query.per_page or 10
            params["page"] = query.page or 1
            result = await client.get("works", params=params)
        finally:
            await client.close()
        return result

    @mcp.tool(
        name="get_author",
        description="Retrieve an author's profile and metadata from OpenAlex by their ID.",
        tags={"authors", "metadata", "openalex"},
        annotations={"title": "Get Author by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_author(query: AuthorQuery, ctx: Context) -> Any:
        """Fetch an author from OpenAlex by their OpenAlex ID."""
        client = OpenAlexClient()
        try:
            result = await client.get(f"authors/{query.author_id}")
        finally:
            await client.close()
        return result

    @mcp.tool(
        name="get_institution",
        description="Retrieve an institution's profile and metadata from OpenAlex by its ID.",
        tags={"institutions", "metadata", "openalex"},
        annotations={"title": "Get Institution by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_institution(query: InstitutionQuery, ctx: Context) -> Any:
        """Fetch an institution from OpenAlex by its OpenAlex ID."""
        client = OpenAlexClient()
        try:
            result = await client.get(f"institutions/{query.institution_id}")
        finally:
            await client.close()
        return result
