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
