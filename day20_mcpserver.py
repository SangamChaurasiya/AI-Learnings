from mcp.server.mcpserver import MCPServer


mcp = MCPServer("Sangam Calculator")


@mcp.tool()
def sangam_calc(a: int, b: int) -> int:
    """Add two numbers using the Sangam Calculator"""
    return a + b + 100 # deliberate bug: proves Claude is using our tool


if __name__ == "__main__":
    mcp.run()


# uv add "mcp[cli]"
