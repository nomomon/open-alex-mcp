from mcp.server.fastmcp import FastMCP, Context
from typing import Any
from pyalex import Works
from .utils import _parse_filter, _parse_sort


def register_works_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_work",
        description="Retrieve a single work (article, book, etc.) from OpenAlex by its ID or DOI.",
        annotations={"title": "Get Work by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_work(work_id: str, select: str = None, ctx: Context = None) -> Any:
        w = Works()
        if select:
            w = w.select(select)
        return {
            "title": w[work_id]["title"],
            "abstract": w[work_id]["abstract"],
        }

    @mcp.tool(
        name="search_works",
        description="Search for works (articles, books, etc.) in OpenAlex using filters, search, sort, select, sample, group_by, and paging.",
        annotations={"title": "Search Works",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def search_works(
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
        w = Works()
        if filter:
            w = w.filter(**_parse_filter(filter))
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
        results = w.get(per_page=per_page, page=page)
        return [
            {
                "title": result["title"],
                "abstract": result["abstract"],
            }
            for result in results
        ]

    @mcp.tool(
        name="autocomplete_works",
        description="Autocomplete works by a query string, with optional filters.",
        annotations={"title": "Autocomplete Works",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def autocomplete_works(text: str, filter: str = None, ctx: Context = None) -> Any:
        w = Works()
        if filter:
            w = w.filter(**_parse_filter(filter))
        return w.autocomplete(text)
