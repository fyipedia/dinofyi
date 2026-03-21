"""MCP server for dinofyi — AI assistant tools for dinofyi.com.

Run: uvx --from "dinofyi[mcp]" python -m dinofyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DinoFYI")


@mcp.tool()
def list_dinosaurs(limit: int = 20, offset: int = 0) -> str:
    """List dinosaurs from dinofyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from dinofyi.api import DinoFYI

    with DinoFYI() as api:
        data = api.list_dinosaurs(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No dinosaurs found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_dinosaur(slug: str) -> str:
    """Get detailed information about a specific dinosaur.

    Args:
        slug: URL slug identifier for the dinosaur.
    """
    from dinofyi.api import DinoFYI

    with DinoFYI() as api:
        data = api.get_dinosaur(slug)
        return str(data)


@mcp.tool()
def list_classifications(limit: int = 20, offset: int = 0) -> str:
    """List classifications from dinofyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from dinofyi.api import DinoFYI

    with DinoFYI() as api:
        data = api.list_classifications(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No classifications found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_dino(query: str) -> str:
    """Search dinofyi.com for dinosaurs, classifications, and geological periods.

    Args:
        query: Search query string.
    """
    from dinofyi.api import DinoFYI

    with DinoFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
