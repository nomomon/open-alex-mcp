from fastmcp import FastMCP
from .works_tools import register_works_tools
from .authors_tools import register_authors_tools
from .institutions_tools import register_institutions_tools


def register_tools(mcp: FastMCP):
    """Register OpenAlex tools using pyalex."""
    register_works_tools(mcp)
    register_authors_tools(mcp)
    register_institutions_tools(mcp)


def _parse_filter(filter_str):
    # Very basic parser for key:value filter strings
    # e.g. "publication_year:2020" => {"publication_year": 2020}
    if not filter_str:
        return {}
    parts = filter_str.split(":", 1)
    if len(parts) == 2:
        key, value = parts
        try:
            value = int(value)
        except Exception:
            pass
        return {key: value}
    return {}


def _parse_sort(sort_str):
    # e.g. "publication_date:desc" => {"publication_date": "desc"}
    if not sort_str:
        return {}
    parts = sort_str.split(":", 1)
    if len(parts) == 2:
        key, value = parts
        return {key: value}
    return {}
