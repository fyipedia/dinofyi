"""MCP server for dinofyi."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from dinofyi.api import DinoFYI

mcp = FastMCP("dinofyi")


@mcp.tool()
def search_dinofyi(query: str) -> dict[str, Any]:
    """Search dinofyi.com for content matching the query."""
    with DinoFYI() as api:
        return api.search(query)
