from fastmcp import FastMCP

## more comments
# Initialize the MCP server with a name 
mcp = FastMCP("DemoServer")

# Example data source for our resource 
ARTICLES = {
"Claude": "Anthropic's Claude is an AI assistant with a 100K token context window and advanced reasoning abilities. - info by Santu",
"MCP": "MCP (Model Context Protocol) is a standard to connect AI models with external tools and data in a unified way. - - info by Santu",
"Planisware": "Planisware is a predictive forecasting and resourcing tool. - - info by Santu"
}

# Define a Resource (context unit) that provides an article's text by ID @mcp.resource("article://{article_id}")
@mcp.resource("article://{article_id}")
def get_article(article_id: str) -> str: 
    """Retrieve the content of an article by ID."""
    return ARTICLES.get(article_id, "Article not found.")

@mcp.tool()
def get_articleInfo(article_id: str) -> str:
    """Retrieve the content of an article by ID."""
    return ARTICLES.get(article_id, "Article not found.")

# Define a Tool (function) that the model can call @mcp.tool()
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result.""" 
    return a + b

# (Optional) Define a Prompt template for demonstration @mcp.prompt()
@mcp.prompt()
def how_to_use() -> str:
    """A prompt template that instructs the assistant on using this server."""
    return "You have access to a DemoServer with an 'article' resource and two tools - 'add' and 'get_articleInfo'. Always call get_articleInfo before answering any question about articles. If the tool returns nothing relevant, say so. You can call get_articleInfo with a relevant keyword of the article to get all article information."

if __name__ == "__main__":
# Run the server using standard I/O transport (suitable for local client connection)
    mcp.run(transport="stdio")