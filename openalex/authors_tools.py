from fastmcp import FastMCP, Context
from typing import Any
from pyalex import Authors
from .tools import _parse_filter, _parse_sort


def register_authors_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_author",
        description="Retrieve an author's profile and metadata from OpenAlex by their ID.",
        tags={"authors", "metadata", "openalex"},
        annotations={"title": "Get Author by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_author(query: dict, ctx: Context) -> Any:
        author_id = query["author_id"]
        select = query.get("select")
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
    async def search_authors(query: dict, ctx: Context) -> Any:
        filter_ = query.get("filter")
        search = query.get("search")
        sort = query.get("sort")
        select = query.get("select")
        per_page = query.get("per_page", 10)
        page = query.get("page", 1)
        sample = query.get("sample")
        group_by = query.get("group_by")
        a = Authors()
        if filter_:
            a = a.filter(**_parse_filter(filter_))
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
    async def autocomplete_authors(query: dict, ctx: Context) -> Any:
        text = query["text"]
        filter_ = query.get("filter")
        a = Authors()
        if filter_:
            a = a.filter(**_parse_filter(filter_))
        return a.autocomplete(text)
