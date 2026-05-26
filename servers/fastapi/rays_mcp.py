import asyncio
import httpx
from fastmcp import FastMCP

mcp = FastMCP(name="RAYS_MCP")
BASE = "http://127.0.0.1:8000"


@mcp.tool(
    name="Generate presentation",
    description="Generate presentation and return the file path",
)
async def generate_ppt(
    topic: str,
    n_slides: int = 5,
    template: str = "general",
    tone: str = "default",
    export_as: str = "pptx",
    language: str = "English",
    verbosity: str = "standard",
    instructions: str | None = None,
) -> dict:
    pass
