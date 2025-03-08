"""
FastMCP Echo Server
"""
from mcp.server.fastmcp import FastMCP

# 创建服务器
mcp = FastMCP("Echo Server")

# 添加 Echo 工具
@mcp.tool()
def echo(text: str) -> str:
    """Echo the input text"""
    return text
