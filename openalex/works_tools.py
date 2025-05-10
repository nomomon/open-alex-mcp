from fastmcp import FastMCP, Context
from typing import Any
from pyalex import Works
from .tools import _parse_filter, _parse_sort


def register_works_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_work",
        description="Retrieve a single work (article, book, etc.) from OpenAlex by its ID or DOI.",
        tags={"works", "metadata", "openalex"},
        annotations={"title": "Get Work by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_work(query: dict, ctx: Context) -> Any:
        work_id = query["work_id"]
        select = query.get("select")
        w = Works()
        if select:
            w = w.select(select)
        return w[work_id]

    @mcp.tool(
        name="search_works",
        description="Search for works (articles, books, etc.) in OpenAlex using filters, search, sort, select, sample, group_by, and paging.",
        tags={"works", "search", "openalex"},
        annotations={"title": "Search Works",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def search_works(query: dict, ctx: Context) -> Any:
        filter_ = query.get("filter")
        search = query.get("search")
        sort = query.get("sort")
        select = query.get("select")
        per_page = query.get("per_page", 10)
        page = query.get("page", 1)
        sample = query.get("sample")
        group_by = query.get("group_by")
        w = Works()
        if filter_:
            w = w.filter(**_parse_filter(filter_))
        if search:
            w = w.search(search)
        if sort:
            w = w.sort(**_parse_sort(sort))
        if select:
            w = w.select(select)
        if sample:
            w = w.sample(sample)
        if group_by:
            w = w.group_by(group_by)
        return w.get(per_page=per_page, page=page)

    @mcp.tool(
        name="autocomplete_works",
        description="Autocomplete works by a query string, with optional filters.",
        tags={"works", "autocomplete", "openalex"},
        annotations={"title": "Autocomplete Works",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def autocomplete_works(query: dict, ctx: Context) -> Any:
        text = query["text"]
        filter_ = query.get("filter")
        w = Works()
        if filter_:
            w = w.filter(**_parse_filter(filter_))
        return w.autocomplete(text)
