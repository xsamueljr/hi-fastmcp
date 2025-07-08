from tests.mocks import MockGitHubService


from fastmcp import Client, FastMCP


from dataclasses import dataclass


@dataclass
class McpSetup:
    mcp: FastMCP
    client: Client
    github_service: MockGitHubService