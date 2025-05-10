from fastmcp import FastMCP, Context
from typing import Any
from pyalex import Institutions
from .tools import _parse_filter, _parse_sort


def register_institutions_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_institution",
        description="Retrieve an institution's profile and metadata from OpenAlex by its ID.",
        tags={"institutions", "metadata", "openalex"},
        annotations={"title": "Get Institution by ID",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def get_institution(query: dict, ctx: Context) -> Any:
        institution_id = query["institution_id"]
        select = query.get("select")
        i = Institutions()
        if select:
            i = i.select(select)
        return i[institution_id]

    @mcp.tool(
        name="search_institutions",
        description="Search for institutions in OpenAlex using filters, search, sort, select, sample, group_by, and paging.",
        tags={"institutions", "search", "openalex"},
        annotations={"title": "Search Institutions",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def search_institutions(query: dict, ctx: Context) -> Any:
        filter_ = query.get("filter")
        search = query.get("search")
        sort = query.get("sort")
        select = query.get("select")
        per_page = query.get("per_page", 10)
        page = query.get("page", 1)
        sample = query.get("sample")
        group_by = query.get("group_by")
        i = Institutions()
        if filter_:
            i = i.filter(**_parse_filter(filter_))
        if search:
            i = i.search(search)
        if sort:
            i = i.sort(**_parse_sort(sort))
        if select:
            i = i.select(select)
        if sample:
            i = i.sample(sample)
        if group_by:
            i = i.group_by(group_by)
        return i.get(per_page=per_page, page=page)

    @mcp.tool(
        name="autocomplete_institutions",
        description="Autocomplete institutions by a query string, with optional filters.",
        tags={"institutions", "autocomplete", "openalex"},
        annotations={"title": "Autocomplete Institutions",
                     "readOnlyHint": True, "openWorldHint": True}
    )
    async def autocomplete_institutions(query: dict, ctx: Context) -> Any:
        text = query["text"]
        filter_ = query.get("filter")
        i = Institutions()
        if filter_:
            i = i.filter(**_parse_filter(filter_))
        return i.autocomplete(text)
