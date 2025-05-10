import pytest
import asyncio
import json
from fastmcp import FastMCP, Client
from openalex.tools import register_tools
from openalex.schemas import WorkQuery, WorksSearchQuery, AuthorQuery, InstitutionQuery
from fastmcp.exceptions import ClientError


@pytest.mark.asyncio
async def test_get_work():
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = WorkQuery(work_id="W2741809807")
        result = await client.call_tool("get_work", {"query": query})
        work = json.loads(result[0].text)
        assert "id" in work


@pytest.mark.asyncio
async def test_search_works():
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = WorksSearchQuery(filter=None, page=1, per_page=1, sort=None)
        result = await client.call_tool("search_works", {"query": query})
        works = json.loads(result[0].text)
        assert "results" in works


@pytest.mark.asyncio
async def test_search_works_text_search():
    """Test search_works with a general text search (search parameter)."""
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = WorksSearchQuery(filter="search:microbiome", page=1, per_page=3, sort="publication_date:desc")
        result = await client.call_tool("search_works", {"query": query})
        works = json.loads(result[0].text)
        assert "results" in works
        assert len(works["results"]) > 0
        # Check that at least one result mentions 'microbiome' in title or abstract
        found = any(
            "microbiome" in (w.get("display_name", "") + json.dumps(w.get("abstract_inverted_index", {}))).lower()
            for w in works["results"]
        )
        assert found


@pytest.mark.asyncio
async def test_search_works_field_filter():
    """Test search_works with a field-specific filter (e.g., publication year)."""
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = WorksSearchQuery(filter="publication_year:2020", page=1, per_page=2, sort="publication_date:desc")
        result = await client.call_tool("search_works", {"query": query})
        works = json.loads(result[0].text)
        assert "results" in works
        assert len(works["results"]) > 0
        for w in works["results"]:
            assert w.get("publication_year") == 2020


@pytest.mark.asyncio
async def test_search_works_paging():
    """Test search_works paging returns different results for different pages."""
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query1 = WorksSearchQuery(filter=None, page=1, per_page=1)
        query2 = WorksSearchQuery(filter=None, page=2, per_page=1)
        result1 = await client.call_tool("search_works", {"query": query1})
        result2 = await client.call_tool("search_works", {"query": query2})
        works1 = json.loads(result1[0].text)
        works2 = json.loads(result2[0].text)
        assert works1["results"] != works2["results"]


@pytest.mark.asyncio
async def test_get_author():
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = AuthorQuery(author_id="A5023888391")
        result = await client.call_tool("get_author", {"query": query})
        author = json.loads(result[0].text)
        assert "id" in author


@pytest.mark.asyncio
async def test_get_institution():
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = Client(mcp)
    async with client:
        query = InstitutionQuery(institution_id="I97018004")
        result = await client.call_tool("get_institution", {"query": query})
        institution = json.loads(result[0].text)
        assert "id" in institution
