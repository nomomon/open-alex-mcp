# OpenAlex MCP

A minimal, production-like MCP server exposing the OpenAlex API as tools for LLMs and AI agents, using FastMCP.

## Features
- Exposes OpenAlex API endpoints (works, authors, institutions, etc.) as MCP tools
- Each tool has a clear, AI-friendly description and robust parameter validation
- Modular, extensible, and easy to test

## Project Structure

```
open-alex-mcp/
│
├── open-alex-mcp.py                  # Main entrypoint for the MCP server
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore
│
├── openalex/                  # App code (modularized)
│   ├── __init__.py
│   ├── authors_tools.py       # Author-related OpenAlex tools
│   ├── institutions_tools.py  # Institution-related OpenAlex tools
│   ├── works_tools.py         # Work-related OpenAlex tools
│   ├── tools.py               # Tool registration and shared logic
│   ├── utils.py               # Shared utility functions
│
├── tests/                     # Unit/integration tests
│   ├── __init__.py
│   └── test_tools.py
│
└── .github/
    └── documentation/
        └── open-alex.docs.md  # Reference documentation for OpenAlex API
```

## Quickstart

1. **Install dependencies:**

```sh
pip install -r requirements.txt
```

2. **Run the server:**

```sh
python open-alex-mcp.py
```

3. **Interact with the server:**

Use a FastMCP-compatible client, or see the [FastMCP Client documentation](.github/documentation/fastmcp.docs.md).

## Adding New Tools
- Define new tools in the appropriate file in `openalex/` (e.g., `authors_tools.py`, `works_tools.py`, etc.).
- Use clear docstrings and type annotations for each tool.
- For new OpenAlex endpoints, add a function and register it as a tool in the relevant module.

## Testing
- Place tests in `tests/`.
- Use `pytest` to run tests:

```sh
pytest
```

## References
- [OpenAlex API Docs](https://docs.openalex.org/)
- [FastMCP Documentation](https://gofastmcp.com/)

---

© 2025 OpenAlex MCP Example. MIT License.