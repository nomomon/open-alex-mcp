import pytest
import asyncio
from fastmcp import FastMCP
from openalex.tools import register_tools
from openalex.schemas import WorkQuery


@pytest.mark.asyncio
async def test_get_work():
    mcp = FastMCP("TestServer")
    register_tools(mcp)
    client = mcp.client()
    async with client:
        # Use a known OpenAlex work ID for a real test, or mock OpenAlexClient for unit tests
        query = WorkQuery(work_id="W2741809807")
        result = await client.call_tool("get_work", {"work_id": query.work_id})
        # Should return a work object with an 'id' field
        assert "id" in result[0]
