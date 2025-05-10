# server.py
from mcp.server.fastmcp import FastMCP
from openalex.tools import register_tools

mcp = FastMCP("OpenAlex MCP Server")
register_tools(mcp)

if __name__ == "__main__":
    mcp.run()
