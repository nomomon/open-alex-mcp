import os
import pyalex
from mcp.server.fastmcp import FastMCP
from .works_tools import register_works_tools
from .authors_tools import register_authors_tools
from .institutions_tools import register_institutions_tools


def register_tools(mcp: FastMCP):
    """Register OpenAlex tools using pyalex."""
    pyalex.config.email = os.environ.get("PYalex_EMAIL")
    register_works_tools(mcp)
    register_authors_tools(mcp)
    register_institutions_tools(mcp)
