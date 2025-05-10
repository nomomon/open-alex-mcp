from fastmcp import FastMCP, Context
from typing import Any
from pyalex import Authors
from .utils import _parse_filter, _parse_sort


def register_authors_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_author",
        description="Retrieve an author's profile and metadata from OpenAlex by their ID.",
        tags={"authors", "metadata", "openalex"},
        annotations={"title": "Get Author by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_author(author_id: str, select: str = None, ctx: Context = None) -> Any:
        a = Authors()
        if select:
            a = a.select(select)
        return a[author_id]

    @mcp.tool(
        name="search_authors",
        description="Search for authors in OpenAlex using filters, search, sort, select, sample, group_by, and paging.",
        tags={"authors", "search", "openalex"},
        annotations={"title": "Search Authors",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def search_authors(
        filter: str = None,
        search: str = None,
        sort: str = None,
        select: str = None,
        per_page: int = 10,
        page: int = 1,
        sample: int = None,
        group_by: str = None,
        ctx: Context = None
    ) -> Any:
        a = Authors()
        if filter:
            a = a.filter(**_parse_filter(filter))
        if search:
            a = a.search(search)
        if sort:
            a = a.sort(**_parse_sort(sort))
        if select:
            a = a.select(select)
        if sample:
            a = a.sample(sample)
        if group_by:
            a = a.group_by(group_by)
        return a.get(per_page=per_page, page=page)

    @mcp.tool(
        name="autocomplete_authors",
        description="Autocomplete authors by a query string, with optional filters.",
        tags={"authors", "autocomplete", "openalex"},
        annotations={"title": "Autocomplete Authors",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def autocomplete_authors(text: str, filter: str = None, ctx: Context = None) -> Any:
        a = Authors()
        if filter:
            a = a.filter(**_parse_filter(filter))
        return a.autocomplete(text)
