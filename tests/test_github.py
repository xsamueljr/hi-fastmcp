import pytest

from tests.setups import McpSetup


@pytest.mark.asyncio
async def test_server_returns_expected_user(mcp_setup: McpSetup):
    mcp_setup.github_service.name = "CoolDev"
    mcp_setup.github_service.repos_count = 42

    async with mcp_setup.client:
        response = await mcp_setup.mcp._mcp_call_tool("get_user_info", {"username": "CoolDev"})
        user_info = response[1]

        assert isinstance(user_info, dict)
        assert user_info["username"] == "CoolDev"
        assert user_info["repos_count"] == 42
